# Adversarial patches and verification points

Task: `lute-DOM-TextMark-parse-AST-Protyle-Vditor-01`

Base commit: `8928f1866da3269aed613288afb3554985df94e1`

These 59 patches and 112 verification points were selected from the archived run of 2026-10-22. Only candidates recorded as REJECTED with reward=0 were retained. The source refers to renumbering.json for old/new IDs and result hashes, but that file was not supplied. The patches were selected and renumbered without rerunning tests; target assertion coverage is still unconfirmed.

The current runner is bound to the task supplied on 2026-10-23: 2,953 P2P and 18 F2P checks. The source also refers to task-binding.json, which was not supplied. Historical results from the older verifier do not establish results under this version; replay is required.

Replay all patches:

```bash
bash ./run.sh /path/to/submitted-task
```

Use an existing matching task image:

```bash
bash ./run.sh /path/to/submitted-task --image your-task-verifier-image
```

Requires Python 3.9 or later and Docker. Without `--image`, the runner builds or reuses an image from the supplied task's `tests/Dockerfile`. Each patch runs in a separate clean container. Task materials are read-only; results go to a new directory beside the package by default. The runner invokes the official task grader without adding an independent judge. Grading acceptance or rejection does not certify that the intended assertion was reached.

Exit codes: 0 = expectations matched; 1 = expectation mismatch; 2 = incomplete execution or evidence; 130 = interrupted. Use `--check-only` to check materials without running tests, or `--patch P-0001` to select one patch.

| Patch | Verification points | Subject |
| --- | --- | --- |
| [P-0001](patches/P-0001-05b0e3d43248.patch) | VP-0001, VP-0002 | Accept nil options on branches that do not use them |
| [P-0002](patches/P-0002-0d69ef1e2ca0.patch) | VP-0003, VP-0004 | Preserve style-string normalization |
| [P-0003](patches/P-0003-12dcd72ea894.patch) | VP-0005, VP-0006 | Preserve Markdown export mode |
| [P-0004](patches/P-0004-1339f3d42c9b.patch) | VP-0007, VP-0008 | Preserve Markdown export mode |
| [P-0005](patches/P-0005-1a4995607358.patch) | VP-0009, VP-0010 | Preserve ordinary Markdown rendering |
| [P-0006](patches/P-0006-1c04704db46b.patch) | VP-0011 | Preserve safe fallback for unclosed inline HTML |
| [P-0007](patches/P-0007-1cc42787703d.patch) | VP-0012, VP-0013 | Match complete TextMark types |
| [P-0008](patches/P-0008-1cdeee0a5092.patch) | VP-0014, VP-0015 | Preserve the AST produced by editor DOM import |
| [P-0009](patches/P-0009-24b26e889c06.patch) | VP-0016, VP-0017 | Preserve AST and mode semantics in regular flattening |
| [P-0010](patches/P-0010-2635069ef593.patch) | VP-0018, VP-0019 | Preserve fields in DOM-to-TextMark conversion |
| [P-0011](patches/P-0011-2746c0187b66.patch) | VP-0020, VP-0021 | Keep equivalent inputs independent of earlier calls |
| [P-0012](patches/P-0012-2c78d2998994.patch) | VP-0022, VP-0023 | Preserve safe fallback for unclosed inline HTML |
| [P-0013](patches/P-0013-30b322b07c7a.patch) | VP-0024, VP-0025 | Preserve safe fallback for unclosed inline HTML |
| [P-0014](patches/P-0014-376a6aba0ff4.patch) | VP-0026, VP-0027 | Preserve Markdown-to-editor-DOM conversion |
| [P-0015](patches/P-0015-3c6cdd788eab.patch) | VP-0028, VP-0029 | Preserve AST and mode semantics in regular flattening |
| [P-0016](patches/P-0016-3df88bce25be.patch) | VP-0030, VP-0031 | Preserve the AST produced by editor DOM import |
| [P-0017](patches/P-0017-3e0d0ccc87d8.patch) | VP-0032, VP-0033 | Preserve the distinct semantics of hybrid flattening |
| [P-0018](patches/P-0018-494b691547de.patch) | VP-0034, VP-0035 | Preserve the distinct semantics of hybrid flattening |
| [P-0019](patches/P-0019-54e718a0313a.patch) | VP-0036, VP-0037 | Use context from the current DOM conversion call |
| [P-0020](patches/P-0020-5a48363b2f75.patch) | VP-0038, VP-0039 | Keep attributes and IAL nodes in sync |
| [P-0021](patches/P-0021-5bd4c6928cdd.patch) | VP-0040, VP-0041 | Keep equivalent inputs independent of earlier calls |
| [P-0022](patches/P-0022-5eab06bd7a8c.patch) | VP-0042, VP-0043 | Preserve fields in DOM-to-TextMark conversion |
| [P-0023](patches/P-0023-64ad4408959d.patch) | VP-0044 | Preserve preview HTML |
| [P-0024](patches/P-0024-66a4211b7c0d.patch) | VP-0045, VP-0046 | Preserve HTML export |
| [P-0025](patches/P-0025-680acec5c6a8.patch) | VP-0047, VP-0048 | Leave unrelated documents unchanged |
| [P-0026](patches/P-0026-70b4766c38da.patch) | VP-0049, VP-0050 | Accept nil options on branches that do not use them |
| [P-0027](patches/P-0027-70ec12c5c528.patch) | VP-0051, VP-0052 | Preserve editor-DOM-to-Markdown conversion |
| [P-0028](patches/P-0028-7256490957f7.patch) | VP-0053, VP-0054 | Preserve inline-Markdown-to-editor-DOM conversion |
| [P-0029](patches/P-0029-73b775a30e8f.patch) | VP-0055 | Preserve safe fallback for unclosed inline HTML |
| [P-0030](patches/P-0030-7ab2d4100d58.patch) | VP-0056, VP-0057 | Preserve inline-Markdown-to-editor-DOM conversion |
| [P-0031](patches/P-0031-7b0e70924c90.patch) | VP-0058, VP-0059 | Match complete TextMark types |
| [P-0032](patches/P-0032-86a917dbc75d.patch) | VP-0060, VP-0061 | Use the current tree's options during reverse conversion |
| [P-0033](patches/P-0033-9244e6fe58b0.patch) | VP-0062 | Preserve ordinary Markdown rendering |
| [P-0034](patches/P-0034-929bca56fae6.patch) | VP-0063, VP-0064 | Preserve AST and mode semantics in regular flattening |
| [P-0035](patches/P-0035-930ebf760502.patch) | VP-0065, VP-0066 | Preserve TextMark-to-inline conversion |
| [P-0036](patches/P-0036-a13b5ec8aea6.patch) | VP-0067, VP-0068 | Match complete TextMark types |
| [P-0037](patches/P-0037-a9441b736f09.patch) | VP-0069, VP-0070 | Preserve editor DOM spin conversion |
| [P-0038](patches/P-0038-aa05bf73cb74.patch) | VP-0071, VP-0072 | Preserve Markdown-to-editor-DOM conversion |
| [P-0039](patches/P-0039-aade6a232a3b.patch) | VP-0073, VP-0074 | Preserve safe fallback for unclosed inline HTML |
| [P-0040](patches/P-0040-b2f1addef1a1.patch) | VP-0075, VP-0076 | Preserve ordinary Markdown rendering |
| [P-0041](patches/P-0041-b5966f6a10ef.patch) | VP-0077, VP-0078 | Accept nil options on branches that do not use them |
| [P-0042](patches/P-0042-b6f269933bfa.patch) | VP-0079, VP-0080 | Preserve the distinct semantics of hybrid flattening |
| [P-0043](patches/P-0043-b7054a45b71a.patch) | VP-0081, VP-0082 | Use context from the current DOM conversion call |
| [P-0044](patches/P-0044-bcf1133e45c1.patch) | VP-0083, VP-0084 | Keep attributes and IAL nodes in sync |
| [P-0045](patches/P-0045-ca3c2a7b7e36.patch) | VP-0085, VP-0086 | Leave unrelated documents unchanged |
| [P-0046](patches/P-0046-d74c448821a4.patch) | VP-0087, VP-0088 | Preserve Markdown-to-editor-DOM conversion |
| [P-0047](patches/P-0047-d91fd0004952.patch) | VP-0089, VP-0090 | Preserve TextMark-to-inline conversion |
| [P-0048](patches/P-0048-d946beba1822.patch) | VP-0091, VP-0092 | Keep equivalent inputs independent of earlier calls |
| [P-0049](patches/P-0049-d97c7f3de188.patch) | VP-0093, VP-0094 | Keep inline HTML conversion options effective |
| [P-0050](patches/P-0050-d9ca7b58b805.patch) | VP-0095, VP-0096 | Preserve TextMark-to-inline conversion |
| [P-0051](patches/P-0051-e1c13f9c27d0.patch) | VP-0097 | Preserve safe fallback for unclosed inline HTML |
| [P-0052](patches/P-0052-e50cbb94ac15.patch) | VP-0098 | Preserve Markdown-to-editor-DOM conversion |
| [P-0053](patches/P-0053-e80ac3b460de.patch) | VP-0099, VP-0100 | Preserve fields in DOM-to-TextMark conversion |
| [P-0054](patches/P-0054-e94bb6ebba28.patch) | VP-0101, VP-0102 | Preserve style-string normalization |
| [P-0055](patches/P-0055-eb649b4e27a2.patch) | VP-0103, VP-0104 | Preserve Markdown export mode |
| [P-0056](patches/P-0056-f354b00a1973.patch) | VP-0105, VP-0106 | Preserve preview HTML |
| [P-0057](patches/P-0057-f4843e63ae75.patch) | VP-0107, VP-0108 | Leave unrelated documents unchanged |
| [P-0058](patches/P-0058-f5493c9580e0.patch) | VP-0109, VP-0110 | Keep attributes and IAL nodes in sync |
| [P-0059](patches/P-0059-f7fd57578e3e.patch) | VP-0111, VP-0112 | Preserve style-string normalization |

## P-0001

[Patch file](patches/P-0001-05b0e3d43248.patch)

SHA-256: `1281b4e2f86d78b5f4b2e1fd54e9abd7de0cef0e1334639e5a7da774a2a46f85`

### VP-0001: Accept nil options on branches that do not use them

**Requirement:** TextMark branches that do not use options must continue to accept nil options.

**Change:** Read options.KeepEscaped early in the parse.SetTextMarkNode compatibility entry point, making the text/a branches panic on nil options even though they previously did not read options.

**Setup:** Call parse.SetTextMarkNode with a non-nil node and text, a, or the original scenario's inline-math DOM, with options set to nil.

**Expected result:** Branches that do not need options must still produce the original TextMark types and fields without panicking; the compatibility entry point must not read KeepEscaped early. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0002: Accept nil options on branches that do not use them

**Requirement:** TextMark branches that do not use options must continue to accept nil options.

**Change:** Read options.KeepEscaped early in the parse.SetTextMarkNode compatibility entry point, making the text/a branches panic on nil options even though they previously did not read options.

**Setup:** Call parse.SetTextMarkNode with a non-nil node and text, a, or the original scenario's inline-math DOM, with options set to nil.

**Expected result:** Branches that do not need options must still produce the original TextMark types and fields without panicking; the compatibility entry point must not read KeepEscaped early. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0002

[Patch file](patches/P-0002-0d69ef1e2ca0.patch)

SHA-256: `16f78557e4357a05b047d9c037ea2976225017a18a191fb1d7ae4cb9481d5ee3`

### VP-0003: Preserve style-string normalization

**Requirement:** Style normalization must return the same strings as before.

**Change:** Return the raw input string directly from the editor component's StyleValue, skipping whitespace and newline normalization.

**Setup:** Call parse.StyleValue with leading/trailing whitespace, repeated whitespace, newlines, or tabs; include the empty string.

**Expected result:** Return values must follow the baseline's normalization order; returning the unprocessed input or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0004: Preserve style-string normalization

**Requirement:** Style normalization must return the same strings as before.

**Change:** Return the raw input string directly from the editor component's StyleValue, skipping whitespace and newline normalization.

**Setup:** Call parse.StyleValue with leading/trailing whitespace, repeated whitespace, newlines, or tabs; include the empty string.

**Expected result:** Return values must follow the baseline's normalization order; returning the unprocessed input or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0003

[Patch file](patches/P-0003-12dcd72ea894.patch)

SHA-256: `65e4d83af613e882d5d3b5f9cd988772b9b2df07b136fb20456c620e6f552586`

### VP-0005: Preserve Markdown export mode

**Requirement:** Export mode must preserve the existing serialized output.

**Change:** Return early from Lute.BlockDOM2StdMd, producing empty exported Markdown.

**Setup:** Use InlineMd2BlockDOM to generate editor DOM containing strong, then export Markdown with Lute.BlockDOM2StdMd. Also check HTML export as specified in the original scenario.

**Expected result:** Exported Markdown must preserve baseline text, escaping, and attribute protocols. Non-export output, skipped export flattening, empty output, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0006: Preserve Markdown export mode

**Requirement:** Export mode must preserve the existing serialized output.

**Change:** Return early from Lute.BlockDOM2StdMd, producing empty exported Markdown.

**Setup:** Use InlineMd2BlockDOM to generate editor DOM containing strong, then export Markdown with Lute.BlockDOM2StdMd. Also check HTML export as specified in the original scenario.

**Expected result:** Exported Markdown must preserve baseline text, escaping, and attribute protocols. Non-export output, skipped export flattening, empty output, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0004

[Patch file](patches/P-0004-1339f3d42c9b.patch)

SHA-256: `1339f3d42c9bf4db9276a9936ef7a5612f209d33f58291049f7ccfa09440399d`

### VP-0007: Preserve Markdown export mode

**Requirement:** Preserve Markdown export mode. Exported text, escaping, and attribute protocols must match the public baseline; non-export-mode output is not a substitute.

**Change:** Make NewProtyleExportMdRenderer panic on a valid non-nil tree with a non-nil Root.

**Setup:** Use the original scenario's valid tree or editor DOM to enter the Markdown export path through NewProtyleExportMdRenderer, ProtyleExportMdNodeSync, or BlockDOM2StdMd, as applicable.

**Expected result:** Exported Markdown must preserve baseline text, escaping, and attribute protocols. Non-export output, skipped export flattening, empty output, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0008: Preserve Markdown export mode

**Requirement:** Preserve Markdown export mode. Exported text, escaping, and attribute protocols must match the public baseline; non-export-mode output is not a substitute.

**Change:** Make NewProtyleExportMdRenderer panic on a valid non-nil tree with a non-nil Root.

**Setup:** Use the original scenario's valid tree or editor DOM to enter the Markdown export path through NewProtyleExportMdRenderer, ProtyleExportMdNodeSync, or BlockDOM2StdMd, as applicable.

**Expected result:** Exported Markdown must preserve baseline text, escaping, and attribute protocols. Non-export output, skipped export flattening, empty output, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0005

[Patch file](patches/P-0005-1a4995607358.patch)

SHA-256: `da1bf9cbc3c6520e99498051530dd6d7575bf68a9b640c376e671ac66e6ac1a8`

### VP-0009: Preserve ordinary Markdown rendering

**Requirement:** Ordinary Markdown rendering must preserve its existing output.

**Change:** Replace the HTML returned by Lute.MarkdownStr with an empty string after the original rendering runs.

**Setup:** Render Markdown containing strong through Lute.MarkdownStr and compare it with the original scenario's ordinary HTML output.

**Expected result:** Produce the expected nonempty HTML with baseline text, escaping, and rendering options. Empty output or new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0010: Preserve ordinary Markdown rendering

**Requirement:** Ordinary Markdown rendering must preserve its existing output.

**Change:** Replace the HTML returned by Lute.MarkdownStr with an empty string after the original rendering runs.

**Setup:** Render Markdown containing strong through Lute.MarkdownStr and compare it with the original scenario's ordinary HTML output.

**Expected result:** Produce the expected nonempty HTML with baseline text, escaping, and rendering options. Empty output or new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0006

[Patch file](patches/P-0006-1c04704db46b.patch)

SHA-256: `1b988ce8ca23999d3bf0b523f08af77f4d082907df1db2ecc55f244de8589898`

### VP-0011: Preserve safe fallback for unclosed inline HTML

**Requirement:** Preserve the parser's fallback for incomplete inline HTML. When missing closing tags or existing nesting rules trigger fallback, retain the corresponding raw InlineHTML/text and parser position. The migration must not introduce panics or partially converted TextMarks.

**Change:** Make parseInlineHTML panic when the input contains <span but no </span>.

**Setup:** With HTMLTag2TextMark and editor options enabled as in the original scenario, use parse.Inline or parse.Parse on span or strong input with a missing closing tag.

**Expected result:** Retain the original InlineHTML/text fallback, valid text content, and parser position, without partially converted TextMarks or new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests. This version limits the added panic to input with a span opening tag and no span closing tag.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0007

[Patch file](patches/P-0007-1cc42787703d.patch)

SHA-256: `066be43a0c2ad34c167ec8a8e885799c0a18ce6ab03456753c1cb276f2b95627`

### VP-0012: Match complete TextMark types

**Requirement:** Boolean results for matches, misses, and an empty candidate list must match the baseline.

**Change:** Return false from parse.ContainTextMark for every non-nil node.

**Setup:** Call parse.ContainTextMark on a non-nil node whose TextMarkType is strong em. Query a matching type, a partial type, a nonmatching type, and an empty candidate list.

**Expected result:** Return true for a matching complete type and false for partial or nonmatching types; the empty candidate list must follow the baseline. Always returning false, matching substrings, or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0013: Match complete TextMark types

**Requirement:** Boolean results for matches, misses, and an empty candidate list must match the baseline.

**Change:** Return false from parse.ContainTextMark for every non-nil node.

**Setup:** Call parse.ContainTextMark on a non-nil node whose TextMarkType is strong em. Query a matching type, a partial type, a nonmatching type, and an empty candidate list.

**Expected result:** Return true for a matching complete type and false for partial or nonmatching types; the empty candidate list must follow the baseline. Always returning false, matching substrings, or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0008

[Patch file](patches/P-0008-1cdeee0a5092.patch)

SHA-256: `1cdeee0a5092c396379043edca3491c00bc5219be0bb9231f424b97f6bdf03bc`

### VP-0014: Preserve the AST produced by editor DOM import

**Requirement:** Preserve the AST produced by editor DOM import, including TextMarks, attributes, protocol metadata, and tree links.

**Change:** Add an unconditional panic at the Lute.BlockDOM2Tree entry point.

**Setup:** Import paragraph DOM containing TextMarks and link attributes through Lute.BlockDOM2Tree; compare tree fields, tokens, IAL, and links.

**Expected result:** Imported node types, content, and protocol metadata must match the baseline, without new panics or extra changes to tokens or IAL. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0015: Preserve the AST produced by editor DOM import

**Requirement:** Preserve the AST produced by editor DOM import, including TextMarks, attributes, protocol metadata, and tree links.

**Change:** Add an unconditional panic at the Lute.BlockDOM2Tree entry point.

**Setup:** Import paragraph DOM containing TextMarks and link attributes through Lute.BlockDOM2Tree; compare tree fields, tokens, IAL, and links.

**Expected result:** Imported node types, content, and protocol metadata must match the baseline, without new panics or extra changes to tokens or IAL. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0009

[Patch file](patches/P-0009-24b26e889c06.patch)

SHA-256: `24b26e889c061006a95c9fa51eb7aeadb80ea42b3a194186f6d395f30c17f234`

### VP-0016: Preserve AST and mode semantics in regular flattening

**Requirement:** Regular flattening must preserve AST results and escaping/export semantics. Node types, text/math/link/reference fields, IAL, and parent/child/sibling links must match the baseline, including ordinary escaping and isExportMd differences.

**Change:** Add an unconditional panic at the parse.NestedInlines2FlattedSpans entry point.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpans. Set isExportMd as in the original scenario and compare node types, text, IAL, and tree links.

**Expected result:** Convert nested strong nodes into TextMarks with the same content, preserving ordinary escaping and export-mode differences. Early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0017: Preserve AST and mode semantics in regular flattening

**Requirement:** Regular flattening must preserve AST results and escaping/export semantics. Node types, text/math/link/reference fields, IAL, and parent/child/sibling links must match the baseline, including ordinary escaping and isExportMd differences.

**Change:** Add an unconditional panic at the parse.NestedInlines2FlattedSpans entry point.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpans. Set isExportMd as in the original scenario and compare node types, text, IAL, and tree links.

**Expected result:** Convert nested strong nodes into TextMarks with the same content, preserving ordinary escaping and export-mode differences. Early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0010

[Patch file](patches/P-0010-2635069ef593.patch)

SHA-256: `30f04ae61efc395807c178a761d70c3ca7c6a95c38568903e745c6c03ee5fbad`

### VP-0018: Preserve fields in DOM-to-TextMark conversion

**Requirement:** DOM-to-TextMark conversion must preserve fields, whitespace, entities, and the effect of options.

**Change:** Return from the editor component's SetTextMarkNode before converting fields.

**Setup:** Call parse.SetTextMarkNode on a valid AST with the original scenario's strong or link DOM and current options; compare TextMark fields, text, leading/trailing whitespace, and adjacent nodes.

**Expected result:** Convert the node into the corresponding TextMark without losing content or protocol fields. Preserve whitespace, entities, and option handling; early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0019: Preserve fields in DOM-to-TextMark conversion

**Requirement:** DOM-to-TextMark conversion must preserve fields, whitespace, entities, and the effect of options.

**Change:** Return from the editor component's SetTextMarkNode before converting fields.

**Setup:** Call parse.SetTextMarkNode on a valid AST with the original scenario's strong or link DOM and current options; compare TextMark fields, text, leading/trailing whitespace, and adjacent nodes.

**Expected result:** Convert the node into the corresponding TextMark without losing content or protocol fields. Preserve whitespace, entities, and option handling; early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0011

[Patch file](patches/P-0011-2746c0187b66.patch)

SHA-256: `e15b1bc8c23379b944ff8bc8c9625ca69da16f6265256456290d8e71f6359845`

### VP-0020: Keep equivalent inputs independent of earlier calls

**Requirement:** Equivalent inputs must produce the same conversion results regardless of earlier calls.

**Change:** Keep a global call counter in the editor's regular-flattening implementation and append changed to TextMark text on later calls.

**Setup:** In one process, create a fresh equivalent tree for each call and compare results after interleaving other trees or modes. Do not infer idempotence by reusing an already modified tree. This candidate changes the editor's regular-flattening implementation.

**Expected result:** The same initial structure, options, and mode must produce the same ordered nodes and fields. Global call counts must not affect later results. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0021: Keep equivalent inputs independent of earlier calls

**Requirement:** Equivalent inputs must produce the same conversion results regardless of earlier calls.

**Change:** Keep a global call counter in the editor's regular-flattening implementation and append changed to TextMark text on later calls.

**Setup:** In one process, create a fresh equivalent tree for each call and compare results after interleaving other trees or modes. Do not infer idempotence by reusing an already modified tree. This candidate changes the editor's regular-flattening implementation.

**Expected result:** The same initial structure, options, and mode must produce the same ordered nodes and fields. Global call counts must not affect later results. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0012

[Patch file](patches/P-0012-2c78d2998994.patch)

SHA-256: `5b973453f9443d3a87cb638cc0b8c78bde1bc31a4f34b9b0f91dac5b5a1e13e3`

### VP-0022: Preserve safe fallback for unclosed inline HTML

**Requirement:** Previously safe cases, such as missing closing tags, must retain their text/InlineHTML fallback without new panics or premature TextMark conversion.

**Change:** Make the editor component's ProcessSpanTag panic when the remaining input has no closing tag.

**Setup:** With HTMLTag2TextMark and editor options enabled as in the original scenario, use parse.Inline or parse.Parse on span or strong input with a missing closing tag.

**Expected result:** Retain the original InlineHTML/text fallback, valid text content, and parser position, without partially converted TextMarks or new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0023: Preserve safe fallback for unclosed inline HTML

**Requirement:** Previously safe cases, such as missing closing tags, must retain their text/InlineHTML fallback without new panics or premature TextMark conversion.

**Change:** Make the editor component's ProcessSpanTag panic when the remaining input has no closing tag.

**Setup:** With HTMLTag2TextMark and editor options enabled as in the original scenario, use parse.Inline or parse.Parse on span or strong input with a missing closing tag.

**Expected result:** Retain the original InlineHTML/text fallback, valid text content, and parser position, without partially converted TextMarks or new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0013

[Patch file](patches/P-0013-30b322b07c7a.patch)

SHA-256: `30b322b07c7aa988b7c1736006be3e04450bbb993aed7391982ff0b47c9c5fbe`

### VP-0024: Preserve safe fallback for unclosed inline HTML

**Requirement:** Preserve the parser's fallback for incomplete inline HTML. When missing closing tags or existing nesting rules trigger fallback, retain the corresponding raw InlineHTML/text and parser position. The migration must not introduce panics or partially converted TextMarks.

**Change:** Add a conditional panic in parseInlineHTML for unclosed span input.

**Setup:** With HTMLTag2TextMark and editor options enabled as in the original scenario, use parse.Inline or parse.Parse on span or strong input with a missing closing tag.

**Expected result:** Retain the original InlineHTML/text fallback, valid text content, and parser position, without partially converted TextMarks or new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests. This version limits the added panic to input with a span opening tag and no span closing tag.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0025: Preserve safe fallback for unclosed inline HTML

**Requirement:** Preserve the parser's fallback for incomplete inline HTML. When missing closing tags or existing nesting rules trigger fallback, retain the corresponding raw InlineHTML/text and parser position. The migration must not introduce panics or partially converted TextMarks.

**Change:** Add a conditional panic in parseInlineHTML for unclosed span input.

**Setup:** With HTMLTag2TextMark and editor options enabled as in the original scenario, use parse.Inline or parse.Parse on span or strong input with a missing closing tag.

**Expected result:** Retain the original InlineHTML/text fallback, valid text content, and parser position, without partially converted TextMarks or new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests. This version limits the added panic to input with a span opening tag and no span closing tag.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0014

[Patch file](patches/P-0014-376a6aba0ff4.patch)

SHA-256: `5175afd51ee0a0d8880aa666cf32a5e957e0522f9dca7a69df9f608b2f8a2113`

### VP-0026: Preserve Markdown-to-editor-DOM conversion

**Requirement:** Preserve the returned AST and DOM string. reserveEmptyParagraph and custom renderer protocols must remain effective.

**Change:** Keep the real parse tree but replace the DOM string with CORRUPT when Md2BlockDOMTree returns.

**Setup:** Process Markdown containing strong through Lute.Md2BlockDOMTree and compare the returned tree and DOM. Keep the original scenario's reserveEmptyParagraph and renderer callback settings.

**Expected result:** The returned tree must contain the correct strong TextMark, and the DOM must retain its type, content, and configuration effects. Missing hybrid-conversion wiring, fabricated strings, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0027: Preserve Markdown-to-editor-DOM conversion

**Requirement:** Preserve the returned AST and DOM string. reserveEmptyParagraph and custom renderer protocols must remain effective.

**Change:** Keep the real parse tree but replace the DOM string with CORRUPT when Md2BlockDOMTree returns.

**Setup:** Process Markdown containing strong through Lute.Md2BlockDOMTree and compare the returned tree and DOM. Keep the original scenario's reserveEmptyParagraph and renderer callback settings.

**Expected result:** The returned tree must contain the correct strong TextMark, and the DOM must retain its type, content, and configuration effects. Missing hybrid-conversion wiring, fabricated strings, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0015

[Patch file](patches/P-0015-3c6cdd788eab.patch)

SHA-256: `48426b4a6a3f4f6a0d2e6250be27b6786799b703302ef457a89f8470ec14c413`

### VP-0028: Preserve AST and mode semantics in regular flattening

**Requirement:** Regular flattening must preserve in-place AST conversion and isExportMd semantics.

**Change:** Return early from the editor component's regular-flattening function, leaving nested strong input unchanged.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpans. Set isExportMd as in the original scenario and compare node types, text, IAL, and tree links.

**Expected result:** Convert nested strong nodes into TextMarks with the same content, preserving ordinary escaping and export-mode differences. Early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0029: Preserve AST and mode semantics in regular flattening

**Requirement:** Regular flattening must preserve in-place AST conversion and isExportMd semantics.

**Change:** Return early from the editor component's regular-flattening function, leaving nested strong input unchanged.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpans. Set isExportMd as in the original scenario and compare node types, text, IAL, and tree links.

**Expected result:** Convert nested strong nodes into TextMarks with the same content, preserving ordinary escaping and export-mode differences. Early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0016

[Patch file](patches/P-0016-3df88bce25be.patch)

SHA-256: `f844e00b61b2708b08d25d7fa28645807369ad8451bac8e4313eda0d8b65cbad`

### VP-0030: Preserve the AST produced by editor DOM import

**Requirement:** Imported TextMark fields, content, IAL, and node links must follow the existing editor DOM protocol.

**Change:** When BlockDOM2Tree returns, overwrite the first node's tokens and add an attribute with the value CORRUPT.

**Setup:** Import paragraph DOM containing TextMarks and link attributes through Lute.BlockDOM2Tree; compare tree fields, tokens, IAL, and links.

**Expected result:** Imported node types, content, and protocol metadata must match the baseline, without new panics or extra changes to tokens or IAL. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0031: Preserve the AST produced by editor DOM import

**Requirement:** Imported TextMark fields, content, IAL, and node links must follow the existing editor DOM protocol.

**Change:** When BlockDOM2Tree returns, overwrite the first node's tokens and add an attribute with the value CORRUPT.

**Setup:** Import paragraph DOM containing TextMarks and link attributes through Lute.BlockDOM2Tree; compare tree fields, tokens, IAL, and links.

**Expected result:** Imported node types, content, and protocol metadata must match the baseline, without new panics or extra changes to tokens or IAL. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0017

[Patch file](patches/P-0017-3e0d0ccc87d8.patch)

SHA-256: `ac527c9abca65711850472ee7872c4b3a7dad3bc5c8398012bf8392fdd62191b`

### VP-0032: Preserve the distinct semantics of hybrid flattening

**Requirement:** Hybrid flattening must retain its own handling of mixed nesting and escaping.

**Change:** Return early from the editor component's hybrid-flattening function, omitting TextMark conversion.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpansHybrid. Compare hybrid-mode TextMarks, escaping, and node links as specified in the original scenario.

**Expected result:** Hybrid flattening must produce the corresponding TextMark while preserving its distinct escaping, quotation, and nesting behavior. Early returns, new panics, and substitution with regular-flattening results are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0033: Preserve the distinct semantics of hybrid flattening

**Requirement:** Hybrid flattening must retain its own handling of mixed nesting and escaping.

**Change:** Return early from the editor component's hybrid-flattening function, omitting TextMark conversion.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpansHybrid. Compare hybrid-mode TextMarks, escaping, and node links as specified in the original scenario.

**Expected result:** Hybrid flattening must produce the corresponding TextMark while preserving its distinct escaping, quotation, and nesting behavior. Early returns, new panics, and substitution with regular-flattening results are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0018

[Patch file](patches/P-0018-494b691547de.patch)

SHA-256: `0f383e9434176a5786e9e80688f82b0ecde7f5792e7bf52ba93433bb03476f6f`

### VP-0034: Preserve the distinct semantics of hybrid flattening

**Requirement:** The in-place AST, text, and metadata must match the hybrid-mode baseline rather than the result of regular flattening.

**Change:** Return immediately from the parse.NestedInlines2FlattedSpansHybrid compatibility entry point.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpansHybrid. Compare hybrid-mode TextMarks, escaping, and node links as specified in the original scenario.

**Expected result:** Hybrid flattening must produce the corresponding TextMark while preserving its distinct escaping, quotation, and nesting behavior. Early returns, new panics, and substitution with regular-flattening results are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0035: Preserve the distinct semantics of hybrid flattening

**Requirement:** The in-place AST, text, and metadata must match the hybrid-mode baseline rather than the result of regular flattening.

**Change:** Return immediately from the parse.NestedInlines2FlattedSpansHybrid compatibility entry point.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpansHybrid. Compare hybrid-mode TextMarks, escaping, and node links as specified in the original scenario.

**Expected result:** Hybrid flattening must produce the corresponding TextMark while preserving its distinct escaping, quotation, and nesting behavior. Early returns, new panics, and substitution with regular-flattening results are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0019

[Patch file](patches/P-0019-54e718a0313a.patch)

SHA-256: `2d5371d1af0daecbd758a05090059cdb0b8c2cf7623456d3d162a42ed52079d9`

### VP-0036: Use context from the current DOM conversion call

**Requirement:** Each call must receive its options and required parsing capabilities explicitly.

**Change:** Save each call's options in a mutable package global and make KeepEscaped and Inline callbacks read that global.

**Setup:** Pass different KeepEscaped options and strong DOM containing entities to parse.SetTextMarkNode. Inspect where the options and Inline callback arguments come from.

**Expected result:** Each conversion must explicitly use the current call's options and reparsing capabilities. Mutable global pointers or reuse of the first call's options are not allowed. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0037: Use context from the current DOM conversion call

**Requirement:** Each call must receive its options and required parsing capabilities explicitly.

**Change:** Save each call's options in a mutable package global and make KeepEscaped and Inline callbacks read that global.

**Setup:** Pass different KeepEscaped options and strong DOM containing entities to parse.SetTextMarkNode. Inspect where the options and Inline callback arguments come from.

**Expected result:** Each conversion must explicitly use the current call's options and reparsing capabilities. Mutable global pointers or reuse of the first call's options are not allowed. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0020

[Patch file](patches/P-0020-5a48363b2f75.patch)

SHA-256: `2241b005845dcc354ea531c770587cad1e0dd04075556c728f4ec1fbc5d84e1f`

### VP-0038: Keep attributes and IAL nodes in sync

**Requirement:** Converting DOM attributes to span IAL must preserve attribute values, tokens, and insertion positions.

**Change:** Return from the editor component's SetSpanIAL before processing attributes.

**Setup:** Call parse.SetSpanIAL on a node in a valid tree with DOM containing style or custom attributes; compare KramdownIAL, IAL tokens, and node insertion positions.

**Expected result:** Normalize attribute values as in the baseline and synchronize them to the target node and IAL tokens while preserving adjacency. Omitting attribute conversion or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0039: Keep attributes and IAL nodes in sync

**Requirement:** Converting DOM attributes to span IAL must preserve attribute values, tokens, and insertion positions.

**Change:** Return from the editor component's SetSpanIAL before processing attributes.

**Setup:** Call parse.SetSpanIAL on a node in a valid tree with DOM containing style or custom attributes; compare KramdownIAL, IAL tokens, and node insertion positions.

**Expected result:** Normalize attribute values as in the baseline and synchronize them to the target node and IAL tokens while preserving adjacency. Omitting attribute conversion or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0021

[Patch file](patches/P-0021-5bd4c6928cdd.patch)

SHA-256: `c9721841dce49ac83a384f7e62976bcec9c2e7e0171ac9413ef0ca6e5d50d02a`

### VP-0040: Keep equivalent inputs independent of earlier calls

**Requirement:** After interleaved processing of other trees or options, a fresh equivalent tree must produce the same fields and output. Repeatedly modifying the same tree does not establish an idempotence requirement.

**Change:** Keep a global call counter in the hybrid-flattening compatibility entry point and replace root tokens with CORRUPT on later calls.

**Setup:** In one process, create a fresh equivalent tree for each call and compare results after interleaving other trees or modes. Do not infer idempotence by reusing an already modified tree. This candidate is triggered through parse.NestedInlines2FlattedSpansHybrid.

**Expected result:** The same initial structure, options, and mode must produce the same ordered nodes and fields. Global call counts must not affect later results. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0041: Keep equivalent inputs independent of earlier calls

**Requirement:** After interleaved processing of other trees or options, a fresh equivalent tree must produce the same fields and output. Repeatedly modifying the same tree does not establish an idempotence requirement.

**Change:** Keep a global call counter in the hybrid-flattening compatibility entry point and replace root tokens with CORRUPT on later calls.

**Setup:** In one process, create a fresh equivalent tree for each call and compare results after interleaving other trees or modes. Do not infer idempotence by reusing an already modified tree. This candidate is triggered through parse.NestedInlines2FlattedSpansHybrid.

**Expected result:** The same initial structure, options, and mode must produce the same ordered nodes and fields. Global call counts must not affect later results. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0022

[Patch file](patches/P-0022-5eab06bd7a8c.patch)

SHA-256: `66154054b438b853b50e52c47ca7a4d5311c4c278c88e094ece1894729a0ab6c`

### VP-0042: Preserve fields in DOM-to-TextMark conversion

**Requirement:** The target node's TextMark fields, tokens, adjacent whitespace text, and attached IAL must match the corresponding baseline branch.

**Change:** Return immediately from the parse.SetTextMarkNode compatibility entry point without converting the target node.

**Setup:** Call parse.SetTextMarkNode on a valid AST with the original scenario's strong or link DOM and current options; compare TextMark fields, text, leading/trailing whitespace, and adjacent nodes.

**Expected result:** Convert the node into the corresponding TextMark without losing content or protocol fields. Preserve whitespace, entities, and option handling; early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0043: Preserve fields in DOM-to-TextMark conversion

**Requirement:** The target node's TextMark fields, tokens, adjacent whitespace text, and attached IAL must match the corresponding baseline branch.

**Change:** Return immediately from the parse.SetTextMarkNode compatibility entry point without converting the target node.

**Setup:** Call parse.SetTextMarkNode on a valid AST with the original scenario's strong or link DOM and current options; compare TextMark fields, text, leading/trailing whitespace, and adjacent nodes.

**Expected result:** Convert the node into the corresponding TextMark without losing content or protocol fields. Preserve whitespace, entities, and option handling; early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0023

[Patch file](patches/P-0023-64ad4408959d.patch)

SHA-256: `61cc0c61d0f4d8c8950cfc4af7973a9c4b244844e9d1f317ac13920a3496c201`

### VP-0044: Preserve preview HTML

**Requirement:** Preserve preview HTML. It must match the baseline and continue to omit editor occlusion IDs that were previously excluded.

**Change:** Add an unconditional panic at the Lute.ProtylePreview entry point.

**Setup:** Call Lute.ProtylePreview with a valid tree and matching options, retaining the original scenario's ProtylePreviewStr or editor DOM input settings.

**Expected result:** Preview HTML must match the baseline and omit occlusion IDs that were previously excluded. Valid input must not cause new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0024

[Patch file](patches/P-0024-66a4211b7c0d.patch)

SHA-256: `66a4211b7c0de4a13d8234dbe932439b7315b64db61f48db23aaf431ad7db732`

### VP-0045: Preserve HTML export

**Requirement:** Preserve HTML export. Output must match the baseline, including existing rules for special TextMarks and editor metadata.

**Change:** Add an unconditional panic at the NewProtyleExportRenderer entry point.

**Setup:** Enter render.NewProtyleExportRenderer with the original scenario's valid tree and options, then render.

**Expected result:** Exported HTML must preserve existing output rules for TextMarks, content, and metadata. Valid input must not cause new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0046: Preserve HTML export

**Requirement:** Preserve HTML export. Output must match the baseline, including existing rules for special TextMarks and editor metadata.

**Change:** Add an unconditional panic at the NewProtyleExportRenderer entry point.

**Setup:** Enter render.NewProtyleExportRenderer with the original scenario's valid tree and options, then render.

**Expected result:** Exported HTML must preserve existing output rules for TextMarks, content, and metadata. Valid input must not cause new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0025

[Patch file](patches/P-0025-680acec5c6a8.patch)

SHA-256: `dff7cfe8c3cd9d64699220d06685b1fd406033a1ff622096a4a6512fc395229e`

### VP-0047: Leave unrelated documents unchanged

**Requirement:** Conversion must not change unrelated document structures.

**Change:** Retain the previous root pointer in regular flattening, then overwrite the previous document's TextMark content with corrupted on later calls.

**Setup:** Prepare two trees with no shared nodes. Convert the first and save a snapshot, then convert the second and inspect the first tree's content, attributes, and links. This candidate changes the editor's regular-flattening implementation.

**Expected result:** The independent document's snapshot must stay unchanged. Retained global tree or node pointers must not modify a previously processed document. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0048: Leave unrelated documents unchanged

**Requirement:** Conversion must not change unrelated document structures.

**Change:** Retain the previous root pointer in regular flattening, then overwrite the previous document's TextMark content with corrupted on later calls.

**Setup:** Prepare two trees with no shared nodes. Convert the first and save a snapshot, then convert the second and inspect the first tree's content, attributes, and links. This candidate changes the editor's regular-flattening implementation.

**Expected result:** The independent document's snapshot must stay unchanged. Retained global tree or node pointers must not modify a previously processed document. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0026

[Patch file](patches/P-0026-70b4766c38da.patch)

SHA-256: `70b4766c38dae64ab68f2ffe50fbcb580ec4cf6f52649f04b2886f4bf96967ee`

### VP-0049: Accept nil options on branches that do not use them

**Requirement:** Conversion branches that do not need options must continue to accept nil options. Paths that do not read options in the public baseline must return the same results without new partial mutations or panics. This does not cover branches that actually need Inline or KeepEscaped.

**Change:** Make parse.SetTextMarkNode panic immediately on nil options, rejecting previously safe branches.

**Setup:** Call parse.SetTextMarkNode with a non-nil node and text, a, or the original scenario's inline-math DOM, with options set to nil.

**Expected result:** Branches that do not need options must still produce the original TextMark types and fields without panicking; the compatibility entry point must not read KeepEscaped early. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0050: Accept nil options on branches that do not use them

**Requirement:** Conversion branches that do not need options must continue to accept nil options. Paths that do not read options in the public baseline must return the same results without new partial mutations or panics. This does not cover branches that actually need Inline or KeepEscaped.

**Change:** Make parse.SetTextMarkNode panic immediately on nil options, rejecting previously safe branches.

**Setup:** Call parse.SetTextMarkNode with a non-nil node and text, a, or the original scenario's inline-math DOM, with options set to nil.

**Expected result:** Branches that do not need options must still produce the original TextMark types and fields without panicking; the compatibility entry point must not read KeepEscaped early. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0027

[Patch file](patches/P-0027-70ec12c5c528.patch)

SHA-256: `70ec12c5c528c15b75f3ca0431c9bde5beec8b34414c5b666d7d0866167f58b4`

### VP-0051: Preserve editor-DOM-to-Markdown conversion

**Requirement:** Preserve editor-DOM-to-Markdown output, including TextMark, IAL, and occlusion-ID protocol metadata. Reimporting it through the original path must preserve its meaning.

**Change:** Add an unconditional panic at the Lute.BlockDOM2Md entry point.

**Setup:** Convert the original scenario's paragraph DOM through Lute.BlockDOM2Md. Compare the returned Markdown and its meaning after reparsing through the original path.

**Expected result:** Preserve returned text and TextMark, IAL, and occlusion-ID protocol metadata without new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0052: Preserve editor-DOM-to-Markdown conversion

**Requirement:** Preserve editor-DOM-to-Markdown output, including TextMark, IAL, and occlusion-ID protocol metadata. Reimporting it through the original path must preserve its meaning.

**Change:** Add an unconditional panic at the Lute.BlockDOM2Md entry point.

**Setup:** Convert the original scenario's paragraph DOM through Lute.BlockDOM2Md. Compare the returned Markdown and its meaning after reparsing through the original path.

**Expected result:** Preserve returned text and TextMark, IAL, and occlusion-ID protocol metadata without new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0028

[Patch file](patches/P-0028-7256490957f7.patch)

SHA-256: `957142dd0b55ea63a08d0241b6868884c9a6edc0606901b934a3fa20ab442d1f`

### VP-0053: Preserve inline-Markdown-to-editor-DOM conversion

**Requirement:** For the same input, inline DOM must match the baseline, and the relevant parser/renderer options must still be passed through.

**Change:** Replace the returned DOM string from InlineMd2BlockDOM with incorrect content.

**Setup:** Process inline Markdown containing strong and links through Lute.InlineMd2BlockDOM using the original scenario's parser and renderer options.

**Expected result:** Inline DOM types, text, and fields must match the baseline. Fabricated strings and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0054: Preserve inline-Markdown-to-editor-DOM conversion

**Requirement:** For the same input, inline DOM must match the baseline, and the relevant parser/renderer options must still be passed through.

**Change:** Replace the returned DOM string from InlineMd2BlockDOM with incorrect content.

**Setup:** Process inline Markdown containing strong and links through Lute.InlineMd2BlockDOM using the original scenario's parser and renderer options.

**Expected result:** Inline DOM types, text, and fields must match the baseline. Fabricated strings and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0029

[Patch file](patches/P-0029-73b775a30e8f.patch)

SHA-256: `73b775a30e8f1f147eea9f37aefdcbb82ed3c60f05542b281caafdd551d580f5`

### VP-0055: Preserve safe fallback for unclosed inline HTML

**Requirement:** Preserve the parser's fallback for incomplete inline HTML. When missing closing tags or existing nesting rules trigger fallback, retain the corresponding raw InlineHTML/text and parser position. The migration must not introduce panics or partially converted TextMarks.

**Change:** Make parseInlineHTML panic on nonempty input with a nonnegative parser position, including the unclosed-HTML fallback path.

**Setup:** With HTMLTag2TextMark and editor options enabled as in the original scenario, use parse.Inline or parse.Parse on span or strong input with a missing closing tag.

**Expected result:** Retain the original InlineHTML/text fallback, valid text content, and parser position, without partially converted TextMarks or new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests. The broader historical fault condition covers every nonempty input with a nonnegative parser position; it is not the narrower variant that affects only unclosed spans.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0030

[Patch file](patches/P-0030-7ab2d4100d58.patch)

SHA-256: `7ab2d4100d587fd62d9767eb0f3e1eb48b9e971b24ab0a6dbbca0caf6afa4d7d`

### VP-0056: Preserve inline-Markdown-to-editor-DOM conversion

**Requirement:** Preserve the inline-Markdown-to-editor-DOM entry point. DOM produced by inline parsing followed by hybrid flattening must match the baseline; block-level Md2BlockDOMTree output alone is not a substitute.

**Change:** Add an unconditional panic at the Lute.InlineMd2BlockDOM entry point.

**Setup:** Process inline Markdown containing strong and links through Lute.InlineMd2BlockDOM using the original scenario's parser and renderer options.

**Expected result:** Inline DOM types, text, and fields must match the baseline. Fabricated strings and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0057: Preserve inline-Markdown-to-editor-DOM conversion

**Requirement:** Preserve the inline-Markdown-to-editor-DOM entry point. DOM produced by inline parsing followed by hybrid flattening must match the baseline; block-level Md2BlockDOMTree output alone is not a substitute.

**Change:** Add an unconditional panic at the Lute.InlineMd2BlockDOM entry point.

**Setup:** Process inline Markdown containing strong and links through Lute.InlineMd2BlockDOM using the original scenario's parser and renderer options.

**Expected result:** Inline DOM types, text, and fields must match the baseline. Fabricated strings and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0031

[Patch file](patches/P-0031-7b0e70924c90.patch)

SHA-256: `381dbbcd4369a9cf2029311826ee69abaafdb2151742fb0254c0138f3400dc23`

### VP-0058: Match complete TextMark types

**Requirement:** TextMark queries on non-nil nodes must retain their existing matching results.

**Change:** Return false from the editor component's ContainTextMark on the non-nil branch.

**Setup:** Call parse.ContainTextMark on a non-nil node whose TextMarkType is strong em. Query a matching type, a partial type, a nonmatching type, and an empty candidate list.

**Expected result:** Return true for a matching complete type and false for partial or nonmatching types; the empty candidate list must follow the baseline. Always returning false, matching substrings, or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0059: Match complete TextMark types

**Requirement:** TextMark queries on non-nil nodes must retain their existing matching results.

**Change:** Return false from the editor component's ContainTextMark on the non-nil branch.

**Setup:** Call parse.ContainTextMark on a non-nil node whose TextMarkType is strong em. Query a matching type, a partial type, a nonmatching type, and an empty candidate list.

**Expected result:** Return true for a matching complete type and false for partial or nonmatching types; the empty candidate list must follow the baseline. Always returning false, matching substrings, or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0032

[Patch file](patches/P-0032-86a917dbc75d.patch)

SHA-256: `9eccb33b2d2af0aed784a7bb3adeeb9c43a3fc675f6aa5877facaaa1c69f87c5`

### VP-0060: Use the current tree's options during reverse conversion

**Requirement:** Inline re-entry must use the current tree/call's options and services, supplied without mutable globals or hidden execution context.

**Change:** Cache the first tree's options in TextMarks2Inlines and keep using them for Inline reparsing on later calls.

**Setup:** Call parse.TextMarks2Inlines on separate trees with Mark disabled and enabled, using ==payload== and nested marks. Also inspect the source of data supplied to the reparsing callback.

**Expected result:** Reparsing must use each tree's current options rather than caching the first options for later trees. Supported types, compound types, and occlusion nodes must retain their baseline behavior. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0061: Use the current tree's options during reverse conversion

**Requirement:** Inline re-entry must use the current tree/call's options and services, supplied without mutable globals or hidden execution context.

**Change:** Cache the first tree's options in TextMarks2Inlines and keep using them for Inline reparsing on later calls.

**Setup:** Call parse.TextMarks2Inlines on separate trees with Mark disabled and enabled, using ==payload== and nested marks. Also inspect the source of data supplied to the reparsing callback.

**Expected result:** Reparsing must use each tree's current options rather than caching the first options for later trees. Supported types, compound types, and occlusion nodes must retain their baseline behavior. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0033

[Patch file](patches/P-0033-9244e6fe58b0.patch)

SHA-256: `ea3f079929fd0b24b18fb1e98befe07edfb3ffc04ceabba658876f4b7a95ce12`

### VP-0062: Preserve ordinary Markdown rendering

**Requirement:** Preserve ordinary Markdown/HTML output. The same configuration and input must retain baseline HTML semantics, and existing renderer callbacks must remain connected.

**Change:** Add an unconditional panic at the Lute.MarkdownStr entry point.

**Setup:** Render Markdown containing strong through Lute.MarkdownStr and compare it with the original scenario's ordinary HTML output.

**Expected result:** Produce the expected nonempty HTML with baseline text, escaping, and rendering options. Empty output or new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0034

[Patch file](patches/P-0034-929bca56fae6.patch)

SHA-256: `2246d12ab4baa93a386900f3bed6065e171a898b5a7cf7e872db69c40b01f26f`

### VP-0063: Preserve AST and mode semantics in regular flattening

**Requirement:** Target-tree node types, order, tokens, TextMark metadata, and IAL must match the baseline; isExportMd must still control the existing differences.

**Change:** Return immediately from the parse.NestedInlines2FlattedSpans compatibility entry point.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpans. Set isExportMd as in the original scenario and compare node types, text, IAL, and tree links.

**Expected result:** Convert nested strong nodes into TextMarks with the same content, preserving ordinary escaping and export-mode differences. Early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0064: Preserve AST and mode semantics in regular flattening

**Requirement:** Target-tree node types, order, tokens, TextMark metadata, and IAL must match the baseline; isExportMd must still control the existing differences.

**Change:** Return immediately from the parse.NestedInlines2FlattedSpans compatibility entry point.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpans. Set isExportMd as in the original scenario and compare node types, text, IAL, and tree links.

**Expected result:** Convert nested strong nodes into TextMarks with the same content, preserving ordinary escaping and export-mode differences. Early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0035

[Patch file](patches/P-0035-930ebf760502.patch)

SHA-256: `36eca4055ef0bbc4798898d1ae2b9febd5b12314e0cc9551c0098fe0e30712a3`

### VP-0065: Preserve TextMark-to-inline conversion

**Requirement:** Supported single types must become the corresponding inline nodes with marker children. Compound types and occlusion nodes stay unchanged; reparsed subtrees must use the current options.

**Change:** Return immediately from the parse.TextMarks2Inlines compatibility entry point.

**Setup:** Place a strong TextMark under a paragraph in a valid tree and call parse.TextMarks2Inlines with the current parse options.

**Expected result:** Restore strong inline nodes, opening/closing markers, content, and reparsed results. Supported targets must not remain TextMarks or trigger new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0066: Preserve TextMark-to-inline conversion

**Requirement:** Supported single types must become the corresponding inline nodes with marker children. Compound types and occlusion nodes stay unchanged; reparsed subtrees must use the current options.

**Change:** Return immediately from the parse.TextMarks2Inlines compatibility entry point.

**Setup:** Place a strong TextMark under a paragraph in a valid tree and call parse.TextMarks2Inlines with the current parse options.

**Expected result:** Restore strong inline nodes, opening/closing markers, content, and reparsed results. Supported targets must not remain TextMarks or trigger new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0036

[Patch file](patches/P-0036-a13b5ec8aea6.patch)

SHA-256: `a13b5ec8aea610c1ebb7fd61f804c8fbc07cde76ea67c463125a5f55625b1f60`

### VP-0067: Match complete TextMark types

**Requirement:** TextMark membership queries on non-nil nodes must retain exact-match boolean results for hits, misses, and the existing empty variadic argument case. Substring matching is not allowed.

**Change:** Add an unconditional panic at the parse.ContainTextMark entry point.

**Setup:** Call parse.ContainTextMark on a non-nil node whose TextMarkType is strong em. Query a matching type, a partial type, a nonmatching type, and an empty candidate list.

**Expected result:** Return true for a matching complete type and false for partial or nonmatching types; the empty candidate list must follow the baseline. Always returning false, matching substrings, or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0068: Match complete TextMark types

**Requirement:** TextMark membership queries on non-nil nodes must retain exact-match boolean results for hits, misses, and the existing empty variadic argument case. Substring matching is not allowed.

**Change:** Add an unconditional panic at the parse.ContainTextMark entry point.

**Setup:** Call parse.ContainTextMark on a non-nil node whose TextMarkType is strong em. Query a matching type, a partial type, a nonmatching type, and an empty candidate list.

**Expected result:** Return true for a matching complete type and false for partial or nonmatching types; the empty candidate list must follow the baseline. Always returning false, matching substrings, or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0037

[Patch file](patches/P-0037-a9441b736f09.patch)

SHA-256: `a9441b736f092ab3401594e8309e15a31eedfa9769cf25b7286917fb23a6fa95`

### VP-0069: Preserve editor DOM spin conversion

**Requirement:** Preserve editor Spin conversion. DOM from hybrid inline spin must match the baseline, and temporary KeepEscaped changes must be restored after the call.

**Change:** Add an unconditional panic at the Lute.SpinBlockDOM entry point.

**Setup:** Process the original scenario's editor paragraph DOM through Lute.SpinBlockDOM and compare KeepEscaped before and after the call.

**Expected result:** DOM produced by hybrid inline spin must match the baseline. Restore temporary KeepEscaped changes at the end; new panics and missing conversions are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0070: Preserve editor DOM spin conversion

**Requirement:** Preserve editor Spin conversion. DOM from hybrid inline spin must match the baseline, and temporary KeepEscaped changes must be restored after the call.

**Change:** Add an unconditional panic at the Lute.SpinBlockDOM entry point.

**Setup:** Process the original scenario's editor paragraph DOM through Lute.SpinBlockDOM and compare KeepEscaped before and after the call.

**Expected result:** DOM produced by hybrid inline spin must match the baseline. Restore temporary KeepEscaped changes at the end; new panics and missing conversions are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0038

[Patch file](patches/P-0038-aa05bf73cb74.patch)

SHA-256: `647a1b479743c9ccde9b0a9cda6724fe1d9f7dd595a98450e460232c131be4a6`

### VP-0071: Preserve Markdown-to-editor-DOM conversion

**Requirement:** The editor DOM pipeline must retain its existing editor representation.

**Change:** Remove only the hybrid-flattening call immediately after TextMarks2Inlines in Md2BlockDOMTree.

**Setup:** Process Markdown containing strong through Lute.Md2BlockDOMTree and compare the returned tree and DOM. Keep the original scenario's reserveEmptyParagraph and renderer callback settings.

**Expected result:** The returned tree must contain the correct strong TextMark, and the DOM must retain its type, content, and configuration effects. Missing hybrid-conversion wiring, fabricated strings, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests. The revised candidate explicitly changes hybrid-conversion wiring in Md2BlockDOMTree.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0072: Preserve Markdown-to-editor-DOM conversion

**Requirement:** The editor DOM pipeline must retain its existing editor representation.

**Change:** Remove only the hybrid-flattening call immediately after TextMarks2Inlines in Md2BlockDOMTree.

**Setup:** Process Markdown containing strong through Lute.Md2BlockDOMTree and compare the returned tree and DOM. Keep the original scenario's reserveEmptyParagraph and renderer callback settings.

**Expected result:** The returned tree must contain the correct strong TextMark, and the DOM must retain its type, content, and configuration effects. Missing hybrid-conversion wiring, fabricated strings, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests. The revised candidate explicitly changes hybrid-conversion wiring in Md2BlockDOMTree.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0039

[Patch file](patches/P-0039-aade6a232a3b.patch)

SHA-256: `8e6a3a6e8e611ea72f1bbec5c7529d6a66b5d729d46add1d7a8620d12b9fbc0c`

### VP-0073: Preserve safe fallback for unclosed inline HTML

**Requirement:** Preserve the existing safe fallback for incomplete inline HTML.

**Change:** Make ProcessSpanTag panic when it cannot find a closing tag, blocking the existing InlineHTML fallback.

**Setup:** With HTMLTag2TextMark and editor options enabled as in the original scenario, use parse.Inline or parse.Parse on span or strong input with a missing closing tag.

**Expected result:** Retain the original InlineHTML/text fallback, valid text content, and parser position, without partially converted TextMarks or new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0074: Preserve safe fallback for unclosed inline HTML

**Requirement:** Preserve the existing safe fallback for incomplete inline HTML.

**Change:** Make ProcessSpanTag panic when it cannot find a closing tag, blocking the existing InlineHTML fallback.

**Setup:** With HTMLTag2TextMark and editor options enabled as in the original scenario, use parse.Inline or parse.Parse on span or strong input with a missing closing tag.

**Expected result:** Retain the original InlineHTML/text fallback, valid text content, and parser position, without partially converted TextMarks or new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0040

[Patch file](patches/P-0040-b2f1addef1a1.patch)

SHA-256: `b2f1addef1a1168df4f709799c89a85c2f3c74dd57b0b801dc3bb5018688a686`

### VP-0075: Preserve ordinary Markdown rendering

**Requirement:** Preserve ordinary Markdown/HTML output. The same configuration and input must retain baseline HTML semantics, and existing renderer callbacks must remain connected.

**Change:** Add an unconditional panic at the Lute.MarkdownStr entry point.

**Setup:** Render Markdown containing strong through Lute.MarkdownStr and compare it with the original scenario's ordinary HTML output.

**Expected result:** Produce the expected nonempty HTML with baseline text, escaping, and rendering options. Empty output or new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0076: Preserve ordinary Markdown rendering

**Requirement:** Preserve ordinary Markdown/HTML output. The same configuration and input must retain baseline HTML semantics, and existing renderer callbacks must remain connected.

**Change:** Add an unconditional panic at the Lute.MarkdownStr entry point.

**Setup:** Render Markdown containing strong through Lute.MarkdownStr and compare it with the original scenario's ordinary HTML output.

**Expected result:** Produce the expected nonempty HTML with baseline text, escaping, and rendering options. Empty output or new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0041

[Patch file](patches/P-0041-b5966f6a10ef.patch)

SHA-256: `bd30e25f660a736411f1c9c2900a2d5b0533075c3b8161db2dafe71601db20df`

### VP-0077: Accept nil options on branches that do not use them

**Requirement:** Valid a or inline-math DOM with nil options must still produce the original fields; compatibility wiring must not dereference options early.

**Change:** Read options.KeepEscaped unconditionally in the SetTextMarkNode compatibility entry point.

**Setup:** Call parse.SetTextMarkNode with a non-nil node and text, a, or the original scenario's inline-math DOM, with options set to nil.

**Expected result:** Branches that do not need options must still produce the original TextMark types and fields without panicking; the compatibility entry point must not read KeepEscaped early. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0078: Accept nil options on branches that do not use them

**Requirement:** Valid a or inline-math DOM with nil options must still produce the original fields; compatibility wiring must not dereference options early.

**Change:** Read options.KeepEscaped unconditionally in the SetTextMarkNode compatibility entry point.

**Setup:** Call parse.SetTextMarkNode with a non-nil node and text, a, or the original scenario's inline-math DOM, with options set to nil.

**Expected result:** Branches that do not need options must still produce the original TextMark types and fields without panicking; the compatibility entry point must not read KeepEscaped early. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0042

[Patch file](patches/P-0042-b6f269933bfa.patch)

SHA-256: `b6f269933bfa0af5fb7c7016d97f9282943f201d833c61fe6e2ee55cf7c9f6bb`

### VP-0079: Preserve the distinct semantics of hybrid flattening

**Requirement:** Hybrid flattening must preserve AST results and its own escaping and quotation rules. Mixed nested-type merging, text/metadata, IAL, and links must match the baseline, including link escaping and quote handling that differ from regular flattening.

**Change:** Add an unconditional panic at the parse.NestedInlines2FlattedSpansHybrid entry point.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpansHybrid. Compare hybrid-mode TextMarks, escaping, and node links as specified in the original scenario.

**Expected result:** Hybrid flattening must produce the corresponding TextMark while preserving its distinct escaping, quotation, and nesting behavior. Early returns, new panics, and substitution with regular-flattening results are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0080: Preserve the distinct semantics of hybrid flattening

**Requirement:** Hybrid flattening must preserve AST results and its own escaping and quotation rules. Mixed nested-type merging, text/metadata, IAL, and links must match the baseline, including link escaping and quote handling that differ from regular flattening.

**Change:** Add an unconditional panic at the parse.NestedInlines2FlattedSpansHybrid entry point.

**Setup:** Build an independent AST containing strong text and call parse.NestedInlines2FlattedSpansHybrid. Compare hybrid-mode TextMarks, escaping, and node links as specified in the original scenario.

**Expected result:** Hybrid flattening must produce the corresponding TextMark while preserving its distinct escaping, quotation, and nesting behavior. Early returns, new panics, and substitution with regular-flattening results are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0043

[Patch file](patches/P-0043-b7054a45b71a.patch)

SHA-256: `b7054a45b71a02f6ce998ffcdaafd13ad0f09d49e89b9629f7ccca46ae04f50a`

### VP-0081: Use context from the current DOM conversion call

**Requirement:** Pass context per call without mutable globals or hidden execution state. The source and call chain of options and reparsing capabilities must be traceable. There must be no global current tree/options/callback; each call uses its own context.

**Change:** Save the first options value in the global retainedOptions and reuse it on every later call.

**Setup:** Pass different KeepEscaped options and strong DOM containing entities to parse.SetTextMarkNode. Inspect where the options and Inline callback arguments come from.

**Expected result:** Each conversion must explicitly use the current call's options and reparsing capabilities. Mutable global pointers or reuse of the first call's options are not allowed. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0082: Use context from the current DOM conversion call

**Requirement:** Pass context per call without mutable globals or hidden execution state. The source and call chain of options and reparsing capabilities must be traceable. There must be no global current tree/options/callback; each call uses its own context.

**Change:** Save the first options value in the global retainedOptions and reuse it on every later call.

**Setup:** Pass different KeepEscaped options and strong DOM containing entities to parse.SetTextMarkNode. Inspect where the options and Inline callback arguments come from.

**Expected result:** Each conversion must explicitly use the current call's options and reparsing capabilities. Mutable global pointers or reuse of the first call's options are not allowed. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0044

[Patch file](patches/P-0044-bcf1133e45c1.patch)

SHA-256: `bcf1133e45c143c1b5a4572190e3bd952828a712caa52881ef9f86a64bf00929`

### VP-0083: Keep attributes and IAL nodes in sync

**Requirement:** Span-attribute conversion must keep node attributes and IAL nodes in sync. KramdownIAL, IAL tokens, and insertion positions must match the baseline, including existing handling of cell attributes and styles on image parents.

**Change:** Add an unconditional panic at the parse.SetSpanIAL entry point.

**Setup:** Call parse.SetSpanIAL on a node in a valid tree with DOM containing style or custom attributes; compare KramdownIAL, IAL tokens, and node insertion positions.

**Expected result:** Normalize attribute values as in the baseline and synchronize them to the target node and IAL tokens while preserving adjacency. Omitting attribute conversion or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0084: Keep attributes and IAL nodes in sync

**Requirement:** Span-attribute conversion must keep node attributes and IAL nodes in sync. KramdownIAL, IAL tokens, and insertion positions must match the baseline, including existing handling of cell attributes and styles on image parents.

**Change:** Add an unconditional panic at the parse.SetSpanIAL entry point.

**Setup:** Call parse.SetSpanIAL on a node in a valid tree with DOM containing style or custom attributes; compare KramdownIAL, IAL tokens, and node insertion positions.

**Expected result:** Normalize attribute values as in the baseline and synchronize them to the target node and IAL tokens while preserving adjacency. Omitting attribute conversion or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0045

[Patch file](patches/P-0045-ca3c2a7b7e36.patch)

SHA-256: `ca3c2a7b7e3693cdc7102984e1304d8ce1b53a8bde16b78b4f5cf537f0771009`

### VP-0085: Leave unrelated documents unchanged

**Requirement:** Conversion must leave an independent document unchanged. Its structure, content, and configuration snapshot must be identical before and after conversion of the target tree.

**Change:** Keep a global previousRoot in regular flattening and overwrite the previous independent document's root tokens on later calls.

**Setup:** Prepare two trees with no shared nodes. Convert the first and save a snapshot, then convert the second and inspect the first tree's content, attributes, and links.

**Expected result:** The independent document's snapshot must stay unchanged. Retained global tree or node pointers must not modify a previously processed document. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0086: Leave unrelated documents unchanged

**Requirement:** Conversion must leave an independent document unchanged. Its structure, content, and configuration snapshot must be identical before and after conversion of the target tree.

**Change:** Keep a global previousRoot in regular flattening and overwrite the previous independent document's root tokens on later calls.

**Setup:** Prepare two trees with no shared nodes. Convert the first and save a snapshot, then convert the second and inspect the first tree's content, attributes, and links.

**Expected result:** The independent document's snapshot must stay unchanged. Retained global tree or node pointers must not modify a previously processed document. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0046

[Patch file](patches/P-0046-d74c448821a4.patch)

SHA-256: `d74c448821a469b88b47a4bf63f7eea4f9e52a857c88aa2631a32ec2bad19663`

### VP-0087: Preserve Markdown-to-editor-DOM conversion

**Requirement:** Preserve the Markdown-to-editor-DOM pipeline. The returned BlockDOM and tree must retain their types, content, attributes, and empty-paragraph option behavior. Existing configuration methods must still work.

**Change:** Add an unconditional panic at the Lute.Md2BlockDOMTree entry point.

**Setup:** Process Markdown containing strong through Lute.Md2BlockDOMTree and compare the returned tree and DOM. Keep the original scenario's reserveEmptyParagraph and renderer callback settings.

**Expected result:** The returned tree must contain the correct strong TextMark, and the DOM must retain its type, content, and configuration effects. Missing hybrid-conversion wiring, fabricated strings, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0088: Preserve Markdown-to-editor-DOM conversion

**Requirement:** Preserve the Markdown-to-editor-DOM pipeline. The returned BlockDOM and tree must retain their types, content, attributes, and empty-paragraph option behavior. Existing configuration methods must still work.

**Change:** Add an unconditional panic at the Lute.Md2BlockDOMTree entry point.

**Setup:** Process Markdown containing strong through Lute.Md2BlockDOMTree and compare the returned tree and DOM. Keep the original scenario's reserveEmptyParagraph and renderer callback settings.

**Expected result:** The returned tree must contain the correct strong TextMark, and the DOM must retain its type, content, and configuration effects. Missing hybrid-conversion wiring, fabricated strings, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0047

[Patch file](patches/P-0047-d91fd0004952.patch)

SHA-256: `d91fd0004952c487f3da4a6e39dfb020291d28e8658a49f680368c5d97c46fdb`

### VP-0089: Preserve TextMark-to-inline conversion

**Requirement:** Reverse TextMark conversion must restore supported inline nodes using the current options. Target node types, opening/closing markers, and reparsed content must match the baseline; non-target types and occlusion-ID nodes stay unchanged.

**Change:** Add an unconditional panic at the parse.TextMarks2Inlines entry point.

**Setup:** Place a strong TextMark under a paragraph in a valid tree and call parse.TextMarks2Inlines with the current parse options.

**Expected result:** Restore strong inline nodes, opening/closing markers, content, and reparsed results. Supported targets must not remain TextMarks or trigger new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0090: Preserve TextMark-to-inline conversion

**Requirement:** Reverse TextMark conversion must restore supported inline nodes using the current options. Target node types, opening/closing markers, and reparsed content must match the baseline; non-target types and occlusion-ID nodes stay unchanged.

**Change:** Add an unconditional panic at the parse.TextMarks2Inlines entry point.

**Setup:** Place a strong TextMark under a paragraph in a valid tree and call parse.TextMarks2Inlines with the current parse options.

**Expected result:** Restore strong inline nodes, opening/closing markers, content, and reparsed results. Supported targets must not remain TextMarks or trigger new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0048

[Patch file](patches/P-0048-d946beba1822.patch)

SHA-256: `d946beba1822375b6cc4bf96636c4cf185c7a978d87f49b6e5c6aace4940339d`

### VP-0091: Keep equivalent inputs independent of earlier calls

**Requirement:** Equivalent initial inputs must be independent of earlier calls. Fixed initial tree/DOM, options, and mode must produce identical fields and ordered structure, even when another input is processed between calls. This does not imply idempotence.

**Change:** Use a global call count in regular flattening to control changes to root tokens on later trees.

**Setup:** In one process, create a fresh equivalent tree for each call and compare results after interleaving other trees or modes. Do not infer idempotence by reusing an already modified tree.

**Expected result:** The same initial structure, options, and mode must produce the same ordered nodes and fields. Global call counts must not affect later results. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0092: Keep equivalent inputs independent of earlier calls

**Requirement:** Equivalent initial inputs must be independent of earlier calls. Fixed initial tree/DOM, options, and mode must produce identical fields and ordered structure, even when another input is processed between calls. This does not imply idempotence.

**Change:** Use a global call count in regular flattening to control changes to root tokens on later trees.

**Setup:** In one process, create a fresh equivalent tree for each call and compare results after interleaving other trees or modes. Do not infer idempotence by reusing an already modified tree.

**Expected result:** The same initial structure, options, and mode must produce the same ordered nodes and fields. Global call counts must not affect later results. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0049

[Patch file](patches/P-0049-d97c7f3de188.patch)

SHA-256: `bd90b654ef86e5cb51492e747bd35c08861cebe72d11f97c73e1d79e40afdb39`

### VP-0093: Keep inline HTML conversion options effective

**Requirement:** Options such as HTMLTag2TextMark must remain effective. Inline HTML AST types/fields and final HTML must match the baseline.

**Change:** Force HTMLTag2TextMark off in the editor's inline HTML parser, disabling the existing option.

**Setup:** With HTMLTag2TextMark disabled and enabled, process inline HTML containing strong or link spans through parse.Inline and Markdown rendering; compare the AST and final HTML.

**Expected result:** HTMLTag2TextMark must affect node types, fields, and output as in the baseline; it must not be forced off. The correct control must retain this effect, and the candidate must fail the corresponding assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0094: Keep inline HTML conversion options effective

**Requirement:** Options such as HTMLTag2TextMark must remain effective. Inline HTML AST types/fields and final HTML must match the baseline.

**Change:** Force HTMLTag2TextMark off in the editor's inline HTML parser, disabling the existing option.

**Setup:** With HTMLTag2TextMark disabled and enabled, process inline HTML containing strong or link spans through parse.Inline and Markdown rendering; compare the AST and final HTML.

**Expected result:** HTMLTag2TextMark must affect node types, fields, and output as in the baseline; it must not be forced off. The correct control must retain this effect, and the candidate must fail the corresponding assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0050

[Patch file](patches/P-0050-d9ca7b58b805.patch)

SHA-256: `465284ccad53648d1d6a520365fabca18b2106a38143b5043197222adca0f7eb`

### VP-0095: Preserve TextMark-to-inline conversion

**Requirement:** Reverse TextMark conversion must preserve supported inline structures and branches that were previously left unconverted.

**Change:** Return early from the editor component's TextMarks2Inlines, omitting supported reverse conversion.

**Setup:** Place a strong TextMark under a paragraph in a valid tree and call parse.TextMarks2Inlines with the current parse options.

**Expected result:** Restore strong inline nodes, opening/closing markers, content, and reparsed results. Supported targets must not remain TextMarks or trigger new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0096: Preserve TextMark-to-inline conversion

**Requirement:** Reverse TextMark conversion must preserve supported inline structures and branches that were previously left unconverted.

**Change:** Return early from the editor component's TextMarks2Inlines, omitting supported reverse conversion.

**Setup:** Place a strong TextMark under a paragraph in a valid tree and call parse.TextMarks2Inlines with the current parse options.

**Expected result:** Restore strong inline nodes, opening/closing markers, content, and reparsed results. Supported targets must not remain TextMarks or trigger new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0051

[Patch file](patches/P-0051-e1c13f9c27d0.patch)

SHA-256: `e62884b63539dac8922bcbaefce24a384f775bb075fb4dd076da2fb908735cd6`

### VP-0097: Preserve safe fallback for unclosed inline HTML

**Requirement:** Preserve the parser's fallback for incomplete inline HTML. When missing closing tags or existing nesting rules trigger fallback, retain the corresponding raw InlineHTML/text and parser position. The migration must not introduce panics or partially converted TextMarks.

**Change:** Make parseInlineHTML panic on nonempty input with a nonnegative parser position, blocking the existing fallback.

**Setup:** With HTMLTag2TextMark and editor options enabled as in the original scenario, use parse.Inline or parse.Parse on span or strong input with a missing closing tag.

**Expected result:** Retain the original InlineHTML/text fallback, valid text content, and parser position, without partially converted TextMarks or new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests. The broader historical fault condition covers every nonempty input with a nonnegative parser position; it is not the narrower variant that affects only unclosed spans.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0052

[Patch file](patches/P-0052-e50cbb94ac15.patch)

SHA-256: `b822219b8d9cec5032e4650626b7be59e3302ec238deec0ccf95f4f19b07bf9e`

### VP-0098: Preserve Markdown-to-editor-DOM conversion

**Requirement:** The Markdown-to-editor-DOM pipeline must retain its existing hybrid-flattening semantics.

**Change:** Remove hybrid-flattening wiring from SpinBlockDOM, although the original recorded trigger calls Md2BlockDOMTree.

**Setup:** Process Markdown containing strong through Lute.Md2BlockDOMTree and compare the returned tree and DOM. Keep the original scenario's reserveEmptyParagraph and renderer callback settings.

**Expected result:** The original intent was to reject an editor DOM pipeline that omitted hybrid flattening. This patch changes SpinBlockDOM, so the recorded Md2BlockDOMTree input does not establish that the fault takes effect. Identify and exercise the changed path before deciding whether it should be rejected. This package does not invent a replacement input or execution result.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests. This historical version has an ineffective trigger: it changes SpinBlockDOM, but the recorded input calls Md2BlockDOMTree and therefore does not establish that the hybrid-wiring variant was detected.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.
- Execution still enters only through Md2BlockDOMTree without reaching the changed SpinBlockDOM.

## P-0053

[Patch file](patches/P-0053-e80ac3b460de.patch)

SHA-256: `e80ac3b460deba636e9f86ce6fd8e0f3b78ff00993353274ca04a55d10a2b760`

### VP-0099: Preserve fields in DOM-to-TextMark conversion

**Requirement:** DOM-to-TextMark conversion must preserve types, content, and metadata. TextMark fields, escaping, leading/trailing whitespace adjustments, table code, and underline reparsing must match the baseline without losing existing protocol fields.

**Change:** Add an unconditional panic at the parse.SetTextMarkNode entry point.

**Setup:** Call parse.SetTextMarkNode on a valid AST with the original scenario's strong or link DOM and current options; compare TextMark fields, text, leading/trailing whitespace, and adjacent nodes.

**Expected result:** Convert the node into the corresponding TextMark without losing content or protocol fields. Preserve whitespace, entities, and option handling; early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0100: Preserve fields in DOM-to-TextMark conversion

**Requirement:** DOM-to-TextMark conversion must preserve types, content, and metadata. TextMark fields, escaping, leading/trailing whitespace adjustments, table code, and underline reparsing must match the baseline without losing existing protocol fields.

**Change:** Add an unconditional panic at the parse.SetTextMarkNode entry point.

**Setup:** Call parse.SetTextMarkNode on a valid AST with the original scenario's strong or link DOM and current options; compare TextMark fields, text, leading/trailing whitespace, and adjacent nodes.

**Expected result:** Convert the node into the corresponding TextMark without losing content or protocol fields. Preserve whitespace, entities, and option handling; early returns and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0054

[Patch file](patches/P-0054-e94bb6ebba28.patch)

SHA-256: `e94bb6ebba28df42380bca1a4ff88a2d4bc8d91ff70bacddbd25e9dd25965919`

### VP-0101: Preserve style-string normalization

**Requirement:** Style-string normalization must return the same values as the baseline for newlines, tabs, repeated whitespace, and the empty string.

**Change:** Add an unconditional panic at the parse.StyleValue entry point.

**Setup:** Call parse.StyleValue with leading/trailing whitespace, repeated whitespace, newlines, or tabs; include the empty string.

**Expected result:** Return values must follow the baseline's normalization order; returning the unprocessed input or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0102: Preserve style-string normalization

**Requirement:** Style-string normalization must return the same values as the baseline for newlines, tabs, repeated whitespace, and the empty string.

**Change:** Add an unconditional panic at the parse.StyleValue entry point.

**Setup:** Call parse.StyleValue with leading/trailing whitespace, repeated whitespace, newlines, or tabs; include the empty string.

**Expected result:** Return values must follow the baseline's normalization order; returning the unprocessed input or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0055

[Patch file](patches/P-0055-eb649b4e27a2.patch)

SHA-256: `514ffbf99cc67030bd3e34df3980d5c979810215bc39eb788ae105f8cb9bd9fa`

### VP-0103: Preserve Markdown export mode

**Requirement:** Exported Markdown for existing marks, table math/code, and links must match the baseline strings.

**Change:** Return early from regular flattening when isExportMd=true, skipping conversion required by export mode.

**Setup:** Use the original scenario's valid tree or editor DOM to enter the Markdown export path through NewProtyleExportMdRenderer, ProtyleExportMdNodeSync, or BlockDOM2StdMd, as applicable.

**Expected result:** Exported Markdown must preserve baseline text, escaping, and attribute protocols. Non-export output, skipped export flattening, empty output, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0104: Preserve Markdown export mode

**Requirement:** Exported Markdown for existing marks, table math/code, and links must match the baseline strings.

**Change:** Return early from regular flattening when isExportMd=true, skipping conversion required by export mode.

**Setup:** Use the original scenario's valid tree or editor DOM to enter the Markdown export path through NewProtyleExportMdRenderer, ProtyleExportMdNodeSync, or BlockDOM2StdMd, as applicable.

**Expected result:** Exported Markdown must preserve baseline text, escaping, and attribute protocols. Non-export output, skipped export flattening, empty output, and new panics are incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0056

[Patch file](patches/P-0056-f354b00a1973.patch)

SHA-256: `f354b00a1973e8b891cb05df9cac61f8239eb35deef24b52a9fb126a619e2ab0`

### VP-0105: Preserve preview HTML

**Requirement:** Preserve preview HTML. It must match the baseline and continue to omit editor occlusion IDs that were previously excluded.

**Change:** Add an unconditional panic at the Lute.ProtylePreview entry point.

**Setup:** Call Lute.ProtylePreview with a valid tree and matching options, retaining the original scenario's ProtylePreviewStr or editor DOM input settings.

**Expected result:** Preview HTML must match the baseline and omit occlusion IDs that were previously excluded. Valid input must not cause new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0106: Preserve preview HTML

**Requirement:** Preserve preview HTML. It must match the baseline and continue to omit editor occlusion IDs that were previously excluded.

**Change:** Add an unconditional panic at the Lute.ProtylePreview entry point.

**Setup:** Call Lute.ProtylePreview with a valid tree and matching options, retaining the original scenario's ProtylePreviewStr or editor DOM input settings.

**Expected result:** Preview HTML must match the baseline and omit occlusion IDs that were previously excluded. Valid input must not cause new panics. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Base with the matching reference solution applied.

**Prerequisites:** Apply the matching reference implementation to the listed base first, then apply this incremental patch. Required reference-patch SHA-256: 069bd00153dbc8342e1b55f74a88bcb861fb3b314e0577bf108ba86a0e48c440. The reference patch is a control dependency and is not copied into this package. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0057

[Patch file](patches/P-0057-f4843e63ae75.patch)

SHA-256: `191be4b0a7a124a094d4f3086aefd3d9505de51243232ccc2d19adef2ddbb69d`

### VP-0107: Leave unrelated documents unchanged

**Requirement:** Converting A must leave B's fields, tokens, attributes, and parent/child/sibling links unchanged.

**Change:** Retain the previous Tree pointer in TextMarks2Inlines and replace the previous document's root tokens with CORRUPT while processing a new tree.

**Setup:** Create separate trees B and A containing strong TextMarks, with no shared nodes. Call parse.TextMarks2Inlines(B), save a snapshot, then call parse.TextMarks2Inlines(A) and compare B's fields and links.

**Expected result:** The independent document's snapshot must stay unchanged. Retained global tree or node pointers must not modify a previously processed document. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0108: Leave unrelated documents unchanged

**Requirement:** Converting A must leave B's fields, tokens, attributes, and parent/child/sibling links unchanged.

**Change:** Retain the previous Tree pointer in TextMarks2Inlines and replace the previous document's root tokens with CORRUPT while processing a new tree.

**Setup:** Create separate trees B and A containing strong TextMarks, with no shared nodes. Call parse.TextMarks2Inlines(B), save a snapshot, then call parse.TextMarks2Inlines(A) and compare B's fields and links.

**Expected result:** The independent document's snapshot must stay unchanged. Retained global tree or node pointers must not modify a previously processed document. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0058

[Patch file](patches/P-0058-f5493c9580e0.patch)

SHA-256: `d1ea4c15324673bbfbfbab18f3d75c0c876cf722a0e39f48810f291e96e06535`

### VP-0109: Keep attributes and IAL nodes in sync

**Requirement:** Styles, custom attributes, cell attributes, and image-ancestor attributes must still be merged into the correct node positions, without additional rewriting of the source DOM.

**Change:** Return immediately from the parse.SetSpanIAL compatibility entry point, omitting attribute and IAL conversion.

**Setup:** Call parse.SetSpanIAL on a node in a valid tree with DOM containing style or custom attributes; compare KramdownIAL, IAL tokens, and node insertion positions.

**Expected result:** Normalize attribute values as in the baseline and synchronize them to the target node and IAL tokens while preserving adjacency. Omitting attribute conversion or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0110: Keep attributes and IAL nodes in sync

**Requirement:** Styles, custom attributes, cell attributes, and image-ancestor attributes must still be merged into the correct node positions, without additional rewriting of the source DOM.

**Change:** Return immediately from the parse.SetSpanIAL compatibility entry point, omitting attribute and IAL conversion.

**Setup:** Call parse.SetSpanIAL on a node in a valid tree with DOM containing style or custom attributes; compare KramdownIAL, IAL tokens, and node insertion positions.

**Expected result:** Normalize attribute values as in the baseline and synchronize them to the target node and IAL tokens while preserving adjacency. Omitting attribute conversion or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

## P-0059

[Patch file](patches/P-0059-f7fd57578e3e.patch)

SHA-256: `1b25587f1637fbc29ea04af42a862ad00c870cdd7ebd39c7e4b47fd0d4d27992`

### VP-0111: Preserve style-string normalization

**Requirement:** Leading/trailing whitespace, repeated internal whitespace, and newlines must produce the same strings in the same processing order; an empty style must return an empty string.

**Change:** Return the raw style string directly from the parse.StyleValue compatibility entry point.

**Setup:** Call parse.StyleValue with leading/trailing whitespace, repeated whitespace, newlines, or tabs; include the empty string.

**Expected result:** Return values must follow the baseline's normalization order; returning the unprocessed input or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.

### VP-0112: Preserve style-string normalization

**Requirement:** Leading/trailing whitespace, repeated internal whitespace, and newlines must produce the same strings in the same processing order; an empty style must return an empty string.

**Change:** Return the raw style string directly from the parse.StyleValue compatibility entry point.

**Setup:** Call parse.StyleValue with leading/trailing whitespace, repeated whitespace, newlines, or tabs; include the empty string.

**Expected result:** Return values must follow the baseline's normalization order; returning the unprocessed input or introducing a panic is incorrect. The correct control must pass, and the faulty candidate must fail the relevant behavior or structural assertion.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** This file contains the complete candidate changes relative to the listed clean base; apply it in full. A matching Go environment, dependencies, and behavior or structural tests are also required. Test-installation patches and the runtime environment are not included in this package.

**Version note:** Archived candidate; verification validity is still unconfirmed. This export records the intended check and original patch without rerunning tests.

**The check is not established if:**

- The patch is not applied in full to the stated prerequisite state.
- The correct control on the matching baseline fails with the same entry point and input.
- The input does not reach the changed function or branch, or the target return value, structure, or side effects are not checked.
- An unrelated compilation, test-collection, or environment error stops the behavior case before the target assertion.
