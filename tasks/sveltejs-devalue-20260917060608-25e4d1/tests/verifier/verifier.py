#!/usr/bin/env python3
"""Run hydration tests and project their results onto configured F2P/P2P nodes."""
# Keep execution metadata here; the task description belongs only at the task root.
PLAN = {'schema_version': 'grader-verifier-plan:v2',
 'test_paths': ['test/test_hydration_contract.py'],
 'command': ['/opt/harbor-agent/bin/python3',
             '-m',
             'pytest',
              '--rootdir=.',
              '-q',
              'test/test_hydration_contract.py',
              '--junitxml={report}'],
 'timeout_seconds': 600,
 'gates': [{'id': 'P2P-API',
            'kind': 'P2P',
            'tests': ['test_public_api_and_standard_values']},
           {'id': 'P2P-BUILTINS',
            'kind': 'P2P',
            'tests': ['test_boxed_primitives_and_views']},
           {'id': 'P2P-GRAPHS',
            'kind': 'P2P',
            'tests': ['test_container_topology']},
           {'id': 'P2P-REVIVERS',
            'kind': 'P2P',
            'tests': ['test_reviver_raw_reference_and_cycles']},
           {'id': 'P2P-LIFETIME',
            'kind': 'P2P',
            'tests': ['test_reentrant_state_and_cache_order']},
           {'id': 'P2P-OPERATIONS',
            'kind': 'P2P',
            'tests': ['test_operations_order_and_opaque_handles']},
           {'id': 'P2P-SPARSE',
            'kind': 'P2P',
            'tests': ['test_sparse_limits_and_common_rejections']},
           {'id': 'P2P-ERRORS',
            'kind': 'P2P',
            'tests': ['test_preserved_boxed_null_error',
                      'test_preserved_callback_buffer_error',
                      'test_preserved_callback_view_error',
                      'test_unchanged_error_messages[circular]',
                      'test_preserved_native_view_error',
                      'test_unchanged_error_messages[unknown]']},
           {'id': 'F2P-SAFETY-PROTO',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[proto]']},
           {'id': 'F2P-SAFETY-NULL-PROTO',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[null_proto]']},
            {'id': 'F2P-SAFETY-VIEW',
             'kind': 'F2P',
             'tests': ['test_required_uniform_safety_errors[view]',
                       'test_view_buffer_typed_array_reference']},
           {'id': 'F2P-SAFETY-BUFFER',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[buffer]']},
           {'id': 'F2P-SAFETY-NESTED-PROTO',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[nested_proto]']},
            {'id': 'F2P-SAFETY-VIEW-SELF',
             'kind': 'F2P',
             'tests': ['test_required_uniform_safety_errors[view_self]',
                       'test_view_self_uint8_parse',
                       'test_view_self_dataview_parse',
                       'test_view_self_float64_unflatten']},
           {'id': 'F2P-SAFETY-VIEW-MISSING',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[view_missing]']},
           {'id': 'F2P-SAFETY-VIEW-NULL',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[view_null]']},
           {'id': 'F2P-SAFETY-BUFFER-MISSING',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[buffer_missing]']},
           {'id': 'F2P-SAFETY-BUFFER-NULL',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[buffer_null]']},
           {'id': 'F2P-SAFETY-BUFFER-ARRAY',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[buffer_array]']},
           {'id': 'F2P-SAFETY-DATA-VIEW-WRONG',
            'kind': 'F2P',
            'tests': ['test_required_uniform_safety_errors[data_view_wrong]']},
            {'id': 'P2P-SAFETY-REVIVER-SPARSE',
             'kind': 'P2P',
             'tests': ['test_reviver_mutation_cannot_bypass_sparse_bounds']},
           {'id': 'F2P-MALFORMED-FRACTIONAL',
            'kind': 'F2P',
            'tests': ['test_malformed_fractional_index']},
           {'id': 'F2P-MALFORMED-NEGATIVE',
            'kind': 'F2P',
            'tests': ['test_malformed_negative_index']},
           {'id': 'F2P-MALFORMED-NAN',
            'kind': 'F2P',
            'tests': ['test_malformed_nan_index']},
            {'id': 'P2P-MALFORMED-POSITIVE-INFINITY',
             'kind': 'P2P',
             'tests': ['test_malformed_positive_infinity_index']},
           {'id': 'F2P-MALFORMED-NEGATIVE-INFINITY',
            'kind': 'F2P',
            'tests': ['test_malformed_negative_infinity_index']},
            {'id': 'P2P-MALFORMED-NULL',
             'kind': 'P2P',
             'tests': ['test_malformed_null_index']},
            {'id': 'P2P-MALFORMED-BOOLEAN',
             'kind': 'P2P',
             'tests': ['test_malformed_boolean_index']},
            {'id': 'P2P-MALFORMED-STRING',
             'kind': 'P2P',
             'tests': ['test_malformed_string_reference']},
            {'id': 'P2P-MALFORMED-CONSTRUCTOR',
             'kind': 'P2P',
             'tests': ['test_malformed_inherited_constructor_reference']},
            {'id': 'P2P-MALFORMED-LENGTH',
             'kind': 'P2P',
             'tests': ['test_malformed_inherited_length_reference']},
           {'id': 'F2P-MALFORMED-VIEW-RANGE',
            'kind': 'F2P',
            'tests': ['test_malformed_typed_array_out_of_range_reference']},
           {'id': 'F2P-MALFORMED-VIEW-NEGATIVE',
            'kind': 'F2P',
            'tests': ['test_malformed_typed_array_negative_reference']},
            {'id': 'F2P-REVIVER-TABLE-SHRINK',
             'kind': 'F2P',
             'tests': ['test_reviver_table_shrink_keeps_unresolved_reference_invalid',
                       'test_reviver_shrinking_declared_length_is_rejected',
                       'test_reviver_string_declared_length_is_rejected',
                       'test_reviver_fractional_declared_length_is_rejected']},
            {'id': 'F2P-REVIVER-LATE-SPARSE-INDEX',
             'kind': 'F2P',
             'tests': ['test_later_reviver_cannot_mutate_processed_sparse_index',
                       'test_later_reviver_fractional_processed_sparse_index_is_rejected',
                       'test_later_reviver_string_processed_sparse_index_is_rejected']},
            {'id': 'F2P-REVIVER-LATE-SPARSE-LENGTH',
             'kind': 'F2P',
             'tests': ['test_later_reviver_infinite_sparse_length_is_rejected',
                       'test_later_reviver_negative_sparse_length_is_rejected']},
           {'id': 'F2P-BOUNDARY-OBJECT-FRACTIONAL',
            'kind': 'F2P',
            'tests': ['test_boundary_object_fractional_reference']},
            {'id': 'P2P-BOUNDARY-OBJECT-STRING',
             'kind': 'P2P',
             'tests': ['test_boundary_object_string_reference']},
            {'id': 'P2P-BOUNDARY-NESTED-PROTO',
             'kind': 'P2P',
             'tests': ['test_boundary_nested_proto_reference']},
            {'id': 'P2P-BOUNDARY-SPARSE-RANGE',
             'kind': 'P2P',
             'tests': ['test_boundary_sparse_large_index']},
            {'id': 'F2P-STRUCTURE-STATE-OWNER',
             'kind': 'F2P',
             'tests': ['test_structure_state_owner_is_scored']},
            {'id': 'F2P-STRUCTURE-DISPATCH-SEAMS',
             'kind': 'F2P',
             'tests': ['test_structure_dispatch_seams_are_scored']},
            {'id': 'F2P-STRUCTURE-SCOPE',
             'kind': 'F2P',
             'tests': ['test_structure_scope_is_scored']},
           ]}
TEST_SHA256 = 'bcf8563e4dfbc35240770f9367d13497c23522a46f67c0c6bce590c1b0bcfa23'
# Size of the frozen upstream uvu selection; `load_upstream_selection` enforces the same value.
UPSTREAM_SELECTION_SIZE = 798
import hashlib
import argparse
import json
import os
from decimal import Decimal, InvalidOperation
from pathlib import Path
import re
import subprocess
import sys
import time
import uuid
import xml.etree.ElementTree as ET
from urllib.parse import unquote

SELECTION_SHA256 = '27037e37b37fda79f8afeefe0e4a61f2a543b1847fb4fddfba7bd4d94ebe9ec1'


def load_upstream_gates():
    """Bind each trusted uvu case to exactly one independently scored P2P node."""
    data = Path(__file__).resolve().with_name('p2p_select.txt').read_bytes()
    if hashlib.sha256(data).hexdigest() != SELECTION_SHA256:
        raise ValueError('P2P selection digest mismatch')
    nodes = data.decode('utf-8').splitlines()
    if len(nodes) != 798 or len(set(nodes)) != 798:
        raise ValueError('Expected 798 unique upstream P2P nodes')
    gates = []
    for nodeid in nodes:
        source, suite, name, occurrence = nodeid.split('::')
        if source not in {
            'src/base64.test.js', 'src/utils.test.js', 'test/index.test.js',
            'test/operations.test.js', 'test/parse-operations.test.js',
        } or not occurrence.isdigit():
            raise ValueError('Malformed upstream node identity')
        readable = re.sub(r'[^A-Za-z0-9]+', '_', nodeid).strip('_').lower()[:160]
        gate_id = 'unit_js_' + readable + '_' + hashlib.sha256(nodeid.encode()).hexdigest()[:10]
        gates.append({
            'id': gate_id, 'kind': 'P2P', 'tests': [f'test_upstream_case[{gate_id}]'],
            'nodeid': nodeid, 'source': source, 'suite': unquote(suite),
            'test_name': unquote(name), 'occurrence': int(occurrence),
        })
    if len({g['id'] for g in gates}) != len(gates):
        raise ValueError('Upstream P2P ID collision')
    return gates


PLAN['gates'].extend(load_upstream_gates())

STATUSES = ('PASS', 'FAIL', 'INCONCLUSIVE', 'INFRA_ERROR')
BASE_COMMIT = 'a3d30d94c8fd9cfca4b774814ff9d5bfade5010c'
REVIEW_ITEMS = [
    {
        'id': 'STRUCTURE-DECOUPLING', 'replaces': ['F2P-DECOUPLE'],
        'question': 'Are per-call state management and supported-value handling independently understandable?',
    },
    {
        'id': 'STRUCTURE-STATE-ISOLATION', 'replaces': ['P2P-ISOLATION'],
        'question': 'Does the design avoid shared mutable deserialization state and ambient call contexts?',
    },
    {
        'id': 'INTEGRITY-CHANGE-SCOPE', 'replaces': ['P2P-SCOPE'],
        'question': 'Are changes relevant to deserialization and its tests without unrelated production changes?',
    },
]
REVIEW_OUTPUT = '/logs/verifier/structure-review.json'


class EvaluationFailure(RuntimeError):
    """Keep actual testcase observations when run integrity prevents a valid score."""

    def __init__(self, message, result):
        super().__init__(message)
        self.result = result


def validate_config_contract(config):
    """Validate fixed release-contract fields before writing CTRF reward inputs."""
    hard_gate = config.get('hard_gate')
    if not isinstance(hard_gate, dict) or hard_gate.get('p2p_requires_all') is not True:
        raise ValueError('Unsupported hard_gate.p2p_requires_all; release contract requires true')

    for key in ('missing_is_failure', 'skip_is_failure', 'duplicate_is_failure'):
        if config.get(key) is not True:
            raise ValueError(f'Unsupported {key}; release contract requires true')

    if config.get('reward_policy') != 'deterministic_verifier_only':
        raise ValueError('Unsupported reward_policy')
    
    evaluation_scope = config.get('evaluation_scope')
    if evaluation_scope not in ('behavior_and_structure', 'behavior_only'):
        raise ValueError('Unsupported evaluation_scope')

    f2p_ids = {
        gate['id'] for gate in PLAN['gates']
        if gate['kind'].lower() == 'f2p'
    }
    annotations = config.get('upstream_exception_annotations')
    if not isinstance(annotations, dict) or not annotations:
        raise ValueError('Missing upstream_exception_annotations')
    for label, entry in annotations.items():
        if (
            not isinstance(entry, dict)
            or entry.get('rule') not in f2p_ids
            or not isinstance(entry.get('reason'), str)
            or not entry['reason'].strip()
        ):
            raise ValueError(f'Invalid upstream exception annotation: {label}')

    # Auditable registration of the P2P selection so that
    # `baseline universe == selected + exceptions` is checkable without reading code.
    # Support both v2 (no p2p_selection field) and v3 (with p2p_selection) schemas.
    selection = config.get('p2p_selection')
    selected = config.get('p2p')
    
    # Count handwritten P2P gates (those without 'nodeid' field)
    handwritten_p2p = [
        gate for gate in PLAN['gates']
        if gate['kind'].lower() == 'p2p' and 'nodeid' not in gate
    ]
    
    if selection is None:
        # v2 schema: infer p2p_selection from the config
        exceptions = len(annotations)
        upstream_selected = UPSTREAM_SELECTION_SIZE
        universe = upstream_selected + exceptions
        
        # Validate that the P2P list matches expectations
        if not isinstance(selected, list):
            raise ValueError('p2p must be a list')
        expected_p2p_count = upstream_selected + len(handwritten_p2p)
        if len(selected) != expected_p2p_count:
            raise ValueError(f'Config p2p count {len(selected)} does not match expected {expected_p2p_count} (upstream={upstream_selected} + handwritten={len(handwritten_p2p)})')
    else:
        # v3 schema: validate explicit p2p_selection field
        if not isinstance(selection, dict):
            raise ValueError('p2p_selection must be a dict')
        if selection.get('exceptions_are_selection_exclusions') is not True:
            raise ValueError('p2p_selection.exceptions_are_selection_exclusions must be true')
        universe = selection.get('baseline_universe')
        exceptions = selection.get('exceptions')
        upstream_selected = selection.get('upstream_selected')
        if not isinstance(universe, int) or not isinstance(exceptions, int) or not isinstance(upstream_selected, int):
            raise ValueError('p2p_selection counts must be integers')
        if exceptions != len(annotations):
            raise ValueError('p2p_selection.exceptions differs from upstream_exception_annotations')
        if upstream_selected != UPSTREAM_SELECTION_SIZE:
            raise ValueError('p2p_selection.upstream_selected differs from the frozen selection size')
        if universe != upstream_selected + exceptions:
            raise ValueError('p2p_selection baseline universe does not equal selected + exceptions')
        if not isinstance(selected, list) or len(selected) != upstream_selected + len(handwritten_p2p):
            raise ValueError('p2p_selection.upstream_selected does not match the configured P2P membership')
        declared_sha = selection.get('upstream_selection_sha256')
        if declared_sha != SELECTION_SHA256:
            raise ValueError('p2p_selection.upstream_selection_sha256 differs from the frozen selection digest')

    review = config.get('structure_review')
    reports = config.get('reports')
    diagnostics = config.get('diagnostics')
    if not isinstance(review, dict) or not isinstance(reports, dict) or not isinstance(diagnostics, dict):
        raise ValueError('Missing structure review configuration')
    
    # Validate structure_review based on evaluation_scope
    if evaluation_scope == 'behavior_and_structure':
        # Legacy mode: structure review affects reward
        scored_structure_nodes = [
            'F2P-STRUCTURE-STATE-OWNER',
            'F2P-STRUCTURE-DISPATCH-SEAMS',
            'F2P-STRUCTURE-SCOPE',
        ]
        f2p_ids = {
            gate['id'] for gate in PLAN['gates']
            if gate['kind'].lower() == 'f2p'
        }
        # Platform reports/diagnostics have fixed keys. Declare this separate
        # evidence path only in structure_review, while keeping scored-node checks.
        if (
            review.get('mode') != 'scored_f2p'
            or review.get('affects_reward') is not True
            or review.get('automatic_approval') is not False
            or review.get('scored_nodes') != scored_structure_nodes
            or review.get('report') != REVIEW_OUTPUT
            or not set(scored_structure_nodes).issubset(f2p_ids)
        ):
            raise ValueError('Inconsistent structure_review configuration')
    elif evaluation_scope == 'behavior_only':
        # New mode: structure review is advisory only
        # In behavior_only mode, only review.report needs to be checked
        if (
            review.get('mode') != 'advisory'
            or review.get('affects_reward') is not False
            or review.get('automatic_approval') is not False
            or review.get('report') != REVIEW_OUTPUT
        ):
            raise ValueError('Inconsistent structure_review configuration for behavior_only scope')


def emit_structure_review(repo, output):
    """Persist structural evidence that explains the scored structure F2P nodes."""
    try:
        return structure_review(repo, output)
    except Exception as exc:
        target = Path(output)
        target.parent.mkdir(parents=True, exist_ok=True)
        report = {
            'schema_version': 'devalue-structure-review/v1',
            'status': 'UNAVAILABLE',
            'affects_reward': True,
            'automatic_approval': False,
            'scored_nodes': [
                'F2P-STRUCTURE-STATE-OWNER',
                'F2P-STRUCTURE-DISPATCH-SEAMS',
                'F2P-STRUCTURE-SCOPE',
            ],
            'error': type(exc).__name__ + ': ' + str(exc),
        }
        target.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        return report


def emit_unavailable_structure_review(output, reason):
    """Write an explicit non-applicable report when the candidate never applied."""
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    report = {
        'schema_version': 'devalue-structure-review/v1',
        'status': 'UNAVAILABLE',
        'affects_reward': True,
        'automatic_approval': False,
        'reason': reason,
        'scored_nodes': [
            'F2P-STRUCTURE-STATE-OWNER',
            'F2P-STRUCTURE-DISPATCH-SEAMS',
            'F2P-STRUCTURE-SCOPE',
        ],
    }
    target.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return report


def structure_review(root, output):
    """Collect non-executing review evidence for the scored structure F2P nodes."""
    root = Path(root).resolve(strict=True)
    target = Path(output)
    report = {
        'schema_version': 'devalue-structure-review/v1',
        'status': 'SCORED_BY_CTRF', 'affects_reward': True,
        'automatic_approval': False, 'candidate_root': str(root),
        'base_commit': BASE_COMMIT,
        'scored_nodes': [
            'F2P-STRUCTURE-STATE-OWNER',
            'F2P-STRUCTURE-DISPATCH-SEAMS',
            'F2P-STRUCTURE-SCOPE',
        ],
        'items': [dict(item, status='REVIEW_REQUIRED') for item in REVIEW_ITEMS],
        'limitations': [
            'This report records review evidence; the deterministic score is carried by the listed F2P structure nodes.',
            'No stack-owner, module-graph membership, or production-token hash rule is applied.',
            'Manual review may still inspect the attached diff for maintainability beyond the scored gates.',
        ],
    }
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        # Capture the implementation before pytest runs; exclude the trusted evaluator overlay.
        pathspec = ['.', ':(exclude)test/test_hydration_contract.py']
        def git(*args):
            result = subprocess.run(
                ['git', '--no-pager', '-C', str(root), *args],
                capture_output=True, timeout=20, check=True,
            )
            if len(result.stdout) > 10_000_000:
                raise ValueError('Review evidence exceeds size limit')
            return result.stdout
        diff = git('diff', '--no-ext-diff', '--no-textconv', '--binary',
                   BASE_COMMIT, '--', *pathspec)
        diff_path = target.parent / 'reports' / 'structure-candidate.diff'
        diff_path.parent.mkdir(parents=True, exist_ok=True)
        diff_path.write_bytes(diff)
        names = git('diff', '--no-ext-diff', '--no-textconv', '--name-only', '-z',
                    BASE_COMMIT, '--', *pathspec)
        report['evidence'] = {
            'candidate_head': git('rev-parse', 'HEAD').decode().strip(),
            'diff': str(diff_path),
            # Digest binds this report to the evidence, not to an allowed implementation.
            'diff_sha256': hashlib.sha256(diff).hexdigest(),
            'changed_files': [p.decode('utf-8', 'replace') for p in names.split(b'\0') if p],
            'numstat': git('diff', '--no-ext-diff', '--no-textconv', '--numstat',
                           BASE_COMMIT, '--', *pathspec).decode('utf-8', 'replace'),
            'untracked_files': [
                p.decode('utf-8', 'replace')
                for p in git('ls-files', '--others', '--exclude-standard', '-z',
                             '--', *pathspec).split(b'\0') if p
            ],
        }
        if report['evidence']['untracked_files']:
            report['limitations'].append('Untracked files are listed but not included in the tracked diff.')
    except Exception as exc:
        # Evidence-report failure does not mask the scored structure F2P observations.
        report.update(status='UNAVAILABLE', error=type(exc).__name__ + ': ' + str(exc))
        for item in report['items']:
            item['status'] = 'UNAVAILABLE'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return report


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def aggregate(statuses):
    return max(statuses, key=STATUSES.index) if statuses else 'INFRA_ERROR'


def unavailable(status='INFRA_ERROR'):
    return {'status': status, 'observations': [{'id':g['id'], 'typed_status':status} for g in PLAN['gates']]}


def project(report, returncode):
    """Use exact testcase membership, never broadcast an exit code to semantic gates."""
    try:
        if type(returncode) is not int:
            raise ValueError('Return code must be an integer')
        data = Path(report).read_bytes()
        if not data or len(data) > 20_000_000 or b'<!DOCTYPE' in data or b'<!ENTITY' in data:
            raise ValueError('Invalid XML document')
        root = ET.fromstring(data)
        if root.tag not in ('testsuites', 'testsuite'):
            raise ValueError('Not JUnit')
        expected = {n for g in PLAN['gates'] for n in g['tests']}
        seen = {}
        messages = {}
        durations = {}
        global_error = False
        for case in root.iter('testcase'):
            name = case.get('name')
            if name not in expected:
                global_error = True
                continue
            # Pytest JUnit records elapsed seconds; CTRF requires integer milliseconds.
            elapsed = Decimal(case.get('time', '0'))
            if not elapsed.is_finite() or elapsed < 0:
                raise ValueError('Invalid JUnit testcase duration')
            durations[name] = durations.get(name, Decimal(0)) + elapsed
            errors = list(case.findall('error'))
            failures = list(case.findall('failure'))
            skipped = list(case.findall('skipped'))
            details = '\n'.join(x.get('message','') for x in errors+failures+skipped)
            if details:
                messages.setdefault(name, []).append(details[:8000])
            if errors or 'INFRA_ERROR:' in details:
                status = 'INFRA_ERROR'
            elif skipped or 'INCONCLUSIVE:' in details:
                status = 'INCONCLUSIVE'
            elif failures:
                status = 'FAIL'
            else:
                status = 'PASS'
            if len(errors)+len(failures)+len(skipped)>1:
                status = 'INFRA_ERROR'
            seen.setdefault(name, []).append(status)
        observations = []
        for gate in PLAN['gates']:
            statuses = []
            for name in gate['tests']:
                values = seen.get(name, [])
                statuses.append(values[0] if len(values)==1 else 'INFRA_ERROR')
            observation = {
                'id': gate['id'], 'typed_status': aggregate(statuses),
                'duration': int(sum((durations.get(name, Decimal(0))
                                     for name in gate['tests']), Decimal(0)) * 1000),
            }
            evidence_messages = [text for name in gate['tests'] for text in messages.get(name, [])]
            if evidence_messages:
                observation['message'] = '\n'.join(evidence_messages)[:8000]
            observations.append(observation)
        status = aggregate([o['typed_status'] for o in observations])
        # Process/collection failures affect the run, not the independently observed node statuses.
        if global_error or returncode not in (0,1) or (returncode==0 and status=='FAIL') or (returncode==1 and status=='PASS'):
            status = 'INFRA_ERROR'
        return {'status':status, 'observations':observations}
    except (OSError, ValueError, ET.ParseError, TypeError, InvalidOperation):
        return unavailable()


def command(python, report):
    # Interpreter is supplied by the execution adapter; never bind a development path.
    return [str(python), *[a.replace('{report}', str(report)) for a in PLAN['command'][1:]]]


def write_ctrf(path, result, *, start, stop, config=None):
    """Convert verifier gate observations to the CTRF schema consumed by grader.py."""
    if type(start) is not int or type(stop) is not int or start < 0 or stop < start:
        raise ValueError('CTRF run times must be ordered Unix epoch milliseconds')
    tests = []
    for gate in PLAN['gates']:
        observation = next(
            (item for item in result['observations'] if item['id'] == gate['id']),
            {'typed_status': 'INFRA_ERROR'},
        )
        status = observation['typed_status']
        mapped = {
            'PASS': 'passed',
            'FAIL': 'failed',
            'INCONCLUSIVE': 'skipped',
            'INFRA_ERROR': 'other',
        }[status]
        tests.append({
                # grader.py indexes CTRF records by Gate ID, not pytest case names.
                'testId': gate['id'],
                'name': gate['id'],
                'status': mapped,
                # Zero denotes no measured execution for an unavailable observation.
                'duration': observation.get('duration', 0),
                'message': observation.get('message') or f'{gate.get("nodeid", gate["id"])}: {status}',
                'extra': {
                    # grader.py requires the configured group vocabulary: `F2P` / `P2P`.
                    'deepswe': {'group': gate['kind'], 'required': True},
                    **({'upstream': {key: gate[key] for key in
                       ('nodeid', 'source', 'suite', 'test_name', 'occurrence')}} if 'nodeid' in gate else {}),
                },
            })
    payload = {
        'reportFormat': 'CTRF',
        'specVersion': '0.0.0',
        'results': {
            'tool': {'name': 'deepswe-verifier'},
            'summary': {
                'tests': len(tests),
                'passed': sum(t['status'] == 'passed' for t in tests),
                'failed': sum(t['status'] == 'failed' for t in tests),
                'skipped': sum(t['status'] == 'skipped' for t in tests),
                'pending': 0,
                'other': sum(t['status'] == 'other' for t in tests),
                'start': start,
                'stop': stop,
            },
            'tests': tests,
        }
    }
    if config is not None:
        # Configuration uses snake_case; the platform CTRF extension uses camelCase.
        payload['results']['extra'] = {'deepswe': {
            report_key: config[config_key]
            for config_key, report_key in (
                ('task_id', 'taskId'),
                ('base_commit', 'baseCommit'),
                ('suite', 'suite'),
            )
            if config_key in config
        }}
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')


def run(ctrf_output=None, hard_gate_output=None, config=None):
    root = Path(os.environ['CANDIDATE_ROOT']).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Candidate root is not a directory')
    test = root/PLAN['test_paths'][0]
    if not test.exists():
        patch = Path(__file__).resolve().with_name('test.patch')
        # Overlay only the delivered evaluator test; never silently overwrite an existing test.
        subprocess.run(['git','apply','--check',str(patch)],cwd=root,check=True,capture_output=True)
        subprocess.run(['git','apply',str(patch)],cwd=root,check=True,capture_output=True)
    if test.is_symlink() or digest(test)!=TEST_SHA256:
        raise ValueError('Evaluator overlay hash mismatch')
    run_id = uuid.uuid4().hex
    # Store diagnostics outside the candidate tree so they are retained by Harbor.
    evidence = Path(ctrf_output).parent / 'reports' if ctrf_output else root
    evidence.mkdir(parents=True, exist_ok=True)
    report = evidence / ('verifier-'+run_id+'.xml')
    argv = command(sys.executable, report)
    # Retain upstream runner logs outside the candidate tree, alongside other reports.
    env = dict(os.environ, UPSTREAM_REPORT_DIR=str(evidence/('upstream-'+run_id)),
               UPSTREAM_SELECTION=str(Path(__file__).resolve().with_name('p2p_select.txt')))
    started_at = time.time_ns() // 1_000_000
    completed = subprocess.run(argv,cwd=root,env=env,capture_output=True,text=True,timeout=PLAN['timeout_seconds'])
    stopped_at = max(started_at, time.time_ns() // 1_000_000)
    (evidence/('verifier-'+run_id+'.log')).write_text(completed.stdout+completed.stderr)
    if not report.is_file():
        raise RuntimeError(f'Test runner exited {completed.returncode} without JUnit; see {evidence}')
    result = project(report,completed.returncode)
    receipt = {'schema_version':'verifier-run:v2','candidate_root':str(root),'run_id':run_id,
               'report':str(report),
               'report_sha256':'sha256:'+digest(report),'command':argv,
               'returncode':completed.returncode,'result':result}
    receipt_path = evidence/('verifier-'+run_id+'.receipt.json')
    receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
    if ctrf_output:
        write_ctrf(ctrf_output, result, start=started_at, stop=stopped_at, config=config)
    if hard_gate_output:
        Path(hard_gate_output).parent.mkdir(parents=True, exist_ok=True)
        # Integrity is independent of semantic PASS/FAIL; actually invoke the checker.
        checker = Path(__file__).resolve().with_name('hardgate.py')
        env = dict(os.environ, HARDGATE_EVIDENCE_RECEIPT=str(receipt_path))
        check = subprocess.run([sys.executable, str(checker)], env=env,
                               capture_output=True, text=True, timeout=30)
        (evidence/('verifier-'+run_id+'.hardgate.log')).write_text(check.stdout+check.stderr)
        integrity = json.loads(check.stdout)
        passed = check.returncode == 0 and integrity.get('status') == 'PASS'
        Path(hard_gate_output).write_text(json.dumps({
            'passed': passed, 'integrity': integrity, 'receipt': str(receipt_path),
        }, indent=2)+'\n', encoding='utf-8')
        if not passed:
            raise EvaluationFailure('Independent receipt validation failed; see hardgate log', result)
    if result['status'] in {'INFRA_ERROR', 'INCONCLUSIVE'}:
        raise EvaluationFailure(f'Verifier cannot issue a semantic score: {result["status"]}', result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config')
    parser.add_argument('--repo')
    parser.add_argument('--ctrf-output')
    parser.add_argument('--hard-gate-output')
    parser.add_argument('--structure-review-only', action='store_true')
    parser.add_argument('--review-output')
    parser.add_argument('--apply-failed', type=int, choices=(0, 1), default=0)
    args = parser.parse_args()
    if args.structure_review_only:
        if not args.repo or not args.review_output:
            parser.error('--structure-review-only requires --repo and --review-output')
        try:
            report = structure_review(args.repo, args.review_output)
            print(json.dumps({'structure_review': report['status'], 'affects_reward': True}))
            return 0
        except Exception as exc:
            print('Structure evidence report unavailable: ' + str(exc), file=sys.stderr)
            return 1
    started_at = time.time_ns() // 1_000_000
    config = None
    try:
        if args.repo:
            os.environ['CANDIDATE_ROOT'] = str(Path(args.repo).resolve(strict=True))
        if args.config:
            config = json.loads(Path(args.config).read_text())
            # Reject empty/mismatched memberships instead of silently scoring no gates.
            for group in ('p2p', 'f2p'):
                expected = {g['id'] for g in PLAN['gates'] if g['kind'].lower() == group}
                actual = config.get(group)
                if not isinstance(actual, list) or len(actual) != len(expected) or set(actual) != expected:
                    raise ValueError(f'Config {group} membership differs from verifier PLAN')
            validate_config_contract(config)
            if args.repo:
                # Get structure_review output path - use structure_review.report for behavior_only mode
                structure_review_path = config.get('structure_review', {}).get('report')
                if not structure_review_path:
                    # Fallback to reports.structure_review for behavior_and_structure mode
                    structure_review_path = config.get('reports', {}).get('structure_review')
                
                if structure_review_path:
                    if args.apply_failed:
                        emit_unavailable_structure_review(
                            structure_review_path,
                            'candidate_patch_apply_failed',
                        )
                    else:
                        emit_structure_review(
                            args.repo,
                            structure_review_path,
                        )
        if 'VERIFIER_JUNIT_REPORT' in os.environ:
            if args.hard_gate_output:
                raise ValueError('Standalone JUnit projection has no verified execution receipt')
            result = project(os.environ['VERIFIER_JUNIT_REPORT'],int(os.environ['VERIFIER_TEST_RETURNCODE']))
            if args.ctrf_output:
                # For standalone projection these bounds describe this verifier invocation.
                write_ctrf(args.ctrf_output, result, start=started_at,
                           stop=max(started_at, time.time_ns() // 1_000_000), config=config)
        else:
            result = run(args.ctrf_output, args.hard_gate_output, config=config)
    except Exception as exc:
        print(type(exc).__name__+': '+str(exc),file=sys.stderr)
        result = exc.result if isinstance(exc, EvaluationFailure) else unavailable()
        if args.ctrf_output:
            write_ctrf(args.ctrf_output, result, start=started_at,
                       stop=max(started_at, time.time_ns() // 1_000_000), config=config)
        if args.hard_gate_output:
            target = Path(args.hard_gate_output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps({'passed': False, 'error': str(exc)})+'\n')
        print(json.dumps(result,separators=(',',':')))
        return 2
    print(json.dumps(result,separators=(',',':')))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
