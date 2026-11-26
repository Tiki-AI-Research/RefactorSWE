#!/usr/bin/env python3
"""Validate protected tests, report ownership, and independent Gate projection."""
import importlib.util
import json
import os
from pathlib import Path
import re
import sys

# Importing the sibling entrypoint must not create undeclared output artifacts.
sys.dont_write_bytecode = True


def load_verifier():
    path=Path(__file__).resolve().with_name('verifier.py')
    spec=importlib.util.spec_from_file_location('_trusted_verifier',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def no_duplicates(pairs):
    result={}
    for key,value in pairs:
        if key in result: raise ValueError('Duplicate JSON key')
        result[key]=value
    return result


def safe_file(path):
    path=Path(path).absolute()
    if any(p.is_symlink() for p in [path,*path.parents]): raise ValueError('Symlink in evidence path')
    resolved=path.resolve(strict=True)
    if not resolved.is_file(): raise ValueError('Expected regular evidence file')
    return resolved


def normalized_hash(value):
    if not isinstance(value,str): raise ValueError('Missing digest')
    value=value.removeprefix('sha256:')
    if not re.fullmatch('[0-9a-f]{64}',value): raise ValueError('Malformed digest')
    return value


def verify():
    v=load_verifier()
    root=Path(os.environ['CANDIDATE_ROOT']).resolve(strict=True)
    if not root.is_dir(): raise ValueError('Invalid candidate root')
    receipt_path=safe_file(os.environ['HARDGATE_EVIDENCE_RECEIPT'])
    receipt=json.loads(receipt_path.read_text(),object_pairs_hook=no_duplicates)
    if receipt.get('schema_version')!='verifier-run:v2': raise ValueError('Invalid receipt version')
    if not isinstance(receipt.get('candidate_root'),str) or Path(receipt['candidate_root']).resolve(strict=True)!=root:
        raise ValueError('Receipt belongs to a different candidate root')
    run_id=receipt.get('run_id')
    if not isinstance(run_id,str) or not run_id.strip() or any(c in run_id for c in '/\\\x00'):
        raise ValueError('Invalid run identity')
    # Validate executable node membership without duplicating the task description.
    tests=[];ids=[]
    if not v.PLAN['gates']: raise ValueError('Empty Gate plan')
    for gate in v.PLAN['gates']:
        if (gate['kind'] not in ('P2P','F2P')
                or not isinstance(gate['id'],str) or not gate['id']
                or not isinstance(gate['tests'],list) or not gate['tests']
                or not all(isinstance(name,str) and name for name in gate['tests'])):
            raise ValueError('Invalid Gate binding')
        tests.extend(gate['tests']);ids.append(gate['id'])
    if len(tests)!=len(set(tests)) or len(ids)!=len(set(ids)):
        raise ValueError('Gate membership is duplicated')
    overlay=safe_file(root/v.PLAN['test_paths'][0])
    if not overlay.is_relative_to(root) or v.digest(overlay)!=v.TEST_SHA256: raise ValueError('Test overlay mismatch')
    report_value=receipt.get('report')
    if not isinstance(report_value,str) or not report_value: raise ValueError('Missing report')
    report_path=Path(report_value)
    if '..' in report_path.parts: raise ValueError('Report path traversal')
    if not report_path.is_absolute(): report_path=receipt_path.parent/report_path
    report=safe_file(report_path)
    if not (report.is_relative_to(receipt_path.parent) or report.is_relative_to(root)):
        raise ValueError('Report is not owned by this receipt or candidate')
    expected_hash=receipt.get('report_sha256')
    if not isinstance(expected_hash,str) or not expected_hash.startswith('sha256:') or normalized_hash(expected_hash)!=v.digest(report):
        raise ValueError('JUnit digest mismatch')
    rc=receipt.get('returncode')
    if type(rc) is not int: raise ValueError('Invalid test returncode')
    argv=receipt.get('command')
    if not isinstance(argv,list) or not argv or not all(isinstance(a,str) for a in argv): raise ValueError('Invalid command')
    if not re.fullmatch(r'python(?:3(?:\.\d+)?)?',Path(argv[0]).name): raise ValueError('Unexpected test interpreter')
    if argv!=v.command(argv[0],report): raise ValueError('Command is not bound to declared tests and report')
    result=v.project(report,rc)
    if receipt.get('result')!=result: raise ValueError('Receipt result differs from actual JUnit projection')
    return {'status':'PASS','semantic_status':result['status']}


def main():
    try:
        print(json.dumps(verify(),separators=(',',':')))
        return 0
    except Exception as exc:
        print(type(exc).__name__+': '+str(exc),file=sys.stderr)
        print(json.dumps({'status':'FAIL','semantic_status':'INFRA_ERROR'},separators=(',',':')))
        return 1


if __name__=='__main__':
    raise SystemExit(main())
