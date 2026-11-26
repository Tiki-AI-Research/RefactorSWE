# Adversarial patches and verification points

Task: `refactor-applemusic-like-lyrics-dom-02`

Base commit: `5c0959686d18ca185b81811added3cd31299569f`

This export contains 24 patches and 48 verification points selected at the task owner's request. Patches whose official grading results did not match expectations were excluded. The retained patches are renumbered P-0001–P-0024, with verification points VP-0001–VP-0048. The historical old/new ID mapping is not included in this package. Patch contents are unchanged, and tests were not rerun.

The export excludes 47 objects used as controls, auxiliary materials, or removed at the task owner's request. No objects remain unresolved, and no patchless control or historical-revision records are included. Expected results below describe the intended checks, not completed verification. Replay requires the matching task base, tests, and environment.

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
| [P-0001](patches/P-0001-071a059bdee3.patch) | VP-0001, VP-0002 | One source of truth for registration and ordering |
| [P-0002](patches/P-0002-1ae17fdf3676.patch) | VP-0003, VP-0004 | Reverse only the rebuild sort comparator |
| [P-0003](patches/P-0003-1c44059ddb82.patch) | VP-0005, VP-0006 | Bypass the shared ownership query in the mouse handler |
| [P-0004](patches/P-0004-2d58ec6550cd.patch) | VP-0007, VP-0008 | Change only the main-line event index |
| [P-0005](patches/P-0005-2eb8196da539.patch) | VP-0009, VP-0010 | Route background-lyric clicks to their main/background group |
| [P-0006](patches/P-0006-30bd35840052.patch) | VP-0011, VP-0012 | Use the same ownership source for events and measurements |
| [P-0007](patches/P-0007-3442184dccc4.patch) | VP-0013, VP-0014 | Update the correct group and current height on a main-group resize |
| [P-0008](patches/P-0008-34ac78e6966b.patch) | VP-0015, VP-0016 | Move subclass-group ownership registration back into the player rebuild path |
| [P-0009](patches/P-0009-3c57f56366bf.patch) | VP-0017, VP-0018 | Route main-lyric clicks to the correct group and main-line index |
| [P-0010](patches/P-0010-3dc8b70fd04a.patch) | VP-0019, VP-0020 | Update the owning group and its current layout height when the main wrapper resizes |
| [P-0011](patches/P-0011-3e8dda9ff660.patch) | VP-0021, VP-0022 | Provide ownership and line/group indexes from shared relationships to events, measurements, and remounting |
| [P-0012](patches/P-0012-54439ed104b0.patch) | VP-0023, VP-0024 | Ignore only clicks inside background lyrics |
| [P-0013](patches/P-0013-5e6880754cf8.patch) | VP-0025, VP-0026 | Maintain a separate ownership-removal path during group disposal |
| [P-0014](patches/P-0014-604f92423e35.patch) | VP-0027, VP-0028 | Support groups created directly by existing subclass build hooks |
| [P-0015](patches/P-0015-855fa6ca0d40.patch) | VP-0029, VP-0030 | Sort rebuilt groups stably by start time through the shared ordering mechanism |
| [P-0016](patches/P-0016-93cbcb1f167a.patch) | VP-0031, VP-0032 | Accept built-in and subclass-created or appended groups through the same registration mechanism |
| [P-0017](patches/P-0017-a79cfcb7ef9d.patch) | VP-0033, VP-0034 | Route main-element clicks to the owning group and the original main-line index |
| [P-0018](patches/P-0018-cf57e987552e.patch) | VP-0035, VP-0036 | Remove main-group ownership during hiding even though remounting still needs it |
| [P-0019](patches/P-0019-d08b1a87fb2b.patch) | VP-0037, VP-0038 | Distinguish hiding from disposal in shared relationship cleanup |
| [P-0020](patches/P-0020-dce36f00f271.patch) | VP-0039, VP-0040 | Remove only the main-group size notification, keeping cache and height updates |
| [P-0021](patches/P-0021-ef591fa63688.patch) | VP-0041, VP-0042 | Retain the original group, lines, and required relationships across hide/show |
| [P-0022](patches/P-0022-f37462f51368.patch) | VP-0043, VP-0044 | Move rebuild ordering back into the player |
| [P-0023](patches/P-0023-f717a41d24c2.patch) | VP-0045, VP-0046 | Sort rebuilt groups stably by start time |
| [P-0024](patches/P-0024-f9473dc6b991.patch) | VP-0047, VP-0048 | Keep the built-in DOM build path but remove discovery of external subclass groups |

## P-0001

[Patch file](patches/P-0001-071a059bdee3.patch)

SHA-256: `071a059bdee3af8eb75b11483c653e1b96a77afceaaf13a638a4a6b8146213c3`

### VP-0001: One source of truth for registration and ordering

**Requirement:** Move ordering, element mapping, and time/height registration back into the base class. DOM registration still calls the relationship object separately; runtime checks show that ordering no longer delegates to the same owner.

**Change:** One source of truth for registration and ordering: Move ordering, element mapping, and time/height registration back into the base class. DOM registration still calls the relationship object separately; runtime checks show that ordering no longer delegates to the same owner.

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Move ordering, element mapping, and time/height registration back into the base class. DOM registration still calls the relationship object separately; runtime checks show that ordering no longer delegates to the same owner. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0002: One source of truth for registration and ordering

**Requirement:** Move ordering, element mapping, and time/height registration back into the base class. DOM registration still calls the relationship object separately; runtime checks show that ordering no longer delegates to the same owner.

**Change:** One source of truth for registration and ordering: Move ordering, element mapping, and time/height registration back into the base class. DOM registration still calls the relationship object separately; runtime checks show that ordering no longer delegates to the same owner.

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Move ordering, element mapping, and time/height registration back into the base class. DOM registration still calls the relationship object separately; runtime checks show that ordering no longer delegates to the same owner. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0002

[Patch file](patches/P-0002-1ae17fdf3676.patch)

SHA-256: `1ae17fdf3676b836f785c10013ce7f9e5cbb34179e9030fcbb5a5f23d07e7a31`

### VP-0003: Reverse only the rebuild sort comparator

**Requirement:** After a rebuild, groups with different start times are ordered by ascending startTime, and their time boundaries follow that order.

**Change:** Reverse only the rebuild sort comparator

**Setup:** Build groups with different or equal start times, call rebuildLyricView, and advance time as specified. Check ordering, time boundaries, and active state.

**Expected result:** Expected condition: After a rebuild, groups with different start times are ordered by ascending startTime, and their time boundaries follow that order. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0004: Reverse only the rebuild sort comparator

**Requirement:** After a rebuild, groups with different start times are ordered by ascending startTime, and their time boundaries follow that order.

**Change:** Reverse only the rebuild sort comparator

**Setup:** Build groups with different or equal start times, call rebuildLyricView, and advance time as specified. Check ordering, time boundaries, and active state.

**Expected result:** Expected condition: After a rebuild, groups with different start times are ordered by ascending startTime, and their time boundaries follow that order. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0003

[Patch file](patches/P-0003-1c44059ddb82.patch)

SHA-256: `1c44059ddb8269315f0b88e1c5feafd12b93b4279142ba012135524c577647ec`

### VP-0005: Bypass the shared ownership query in the mouse handler

**Requirement:** Resolve main/background elements and the main-line index through one ownership relationship, rather than maintaining separate facts at different lifecycle stages.

**Change:** Bypass the shared ownership query in the mouse handler

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Resolve main/background elements and the main-line index through one ownership relationship, rather than maintaining separate facts at different lifecycle stages. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0006: Bypass the shared ownership query in the mouse handler

**Requirement:** Resolve main/background elements and the main-line index through one ownership relationship, rather than maintaining separate facts at different lifecycle stages.

**Change:** Bypass the shared ownership query in the mouse handler

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Resolve main/background elements and the main-line index through one ownership relationship, rather than maintaining separate facts at different lifecycle stages. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0004

[Patch file](patches/P-0004-2d58ec6550cd.patch)

SHA-256: `2d58ec6550cd53575934e7439a46ae390e1a63b7b8d53ae7772d82aa4bb97861`

### VP-0007: Change only the main-line event index

**Requirement:** The event lineIndex is the main line's index in processedLines; line and bgLine refer to the corresponding group.

**Change:** Change only the main-line event index

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: The event lineIndex is the main line's index in processedLines; line and bgLine refer to the corresponding group. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0008: Change only the main-line event index

**Requirement:** The event lineIndex is the main line's index in processedLines; line and bgLine refer to the corresponding group.

**Change:** Change only the main-line event index

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: The event lineIndex is the main line's index in processedLines; line and bgLine refer to the corresponding group. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0005

[Patch file](patches/P-0005-2eb8196da539.patch)

SHA-256: `2eb8196da539a0c2b72cd5af569fa80c7ef1500d04c47b7652d0ec17b63445a5`

### VP-0009: Route background-lyric clicks to their main/background group

**Requirement:** Route background-lyric clicks to their main/background group

**Change:** Route background-lyric clicks to their main/background group

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Route background-lyric clicks to their main/background group. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0010: Route background-lyric clicks to their main/background group

**Requirement:** Route background-lyric clicks to their main/background group

**Change:** Route background-lyric clicks to their main/background group

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Route background-lyric clicks to their main/background group. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0006

[Patch file](patches/P-0006-30bd35840052.patch)

SHA-256: `30bd35840052e9dab0b0b786527b17f32f961279dcd6c03e34fcdbeb366c6452`

### VP-0011: Use the same ownership source for events and measurements

**Requirement:** Events maintain a separate eventOwners snapshot while measurements keep the shared relationship query, creating two sources of truth. Trace both consumers at runtime.

**Change:** Use the same ownership source for events and measurements: Events maintain a separate eventOwners snapshot while measurements keep the shared relationship query, creating two sources of truth. Trace both consumers at runtime.

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Events maintain a separate eventOwners snapshot while measurements keep the shared relationship query, creating two sources of truth. Trace both consumers at runtime. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0012: Use the same ownership source for events and measurements

**Requirement:** Events maintain a separate eventOwners snapshot while measurements keep the shared relationship query, creating two sources of truth. Trace both consumers at runtime.

**Change:** Use the same ownership source for events and measurements: Events maintain a separate eventOwners snapshot while measurements keep the shared relationship query, creating two sources of truth. Trace both consumers at runtime.

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Events maintain a separate eventOwners snapshot while measurements keep the shared relationship query, creating two sources of truth. Trace both consumers at runtime. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0007

[Patch file](patches/P-0007-3442184dccc4.patch)

SHA-256: `3442184dccc4a2827f2d6e0b444298850f4eab99196da4406aed14976197bd9d`

### VP-0013: Update the correct group and current height on a main-group resize

**Requirement:** The correct main-group size is not written to the cache keyed by group identity.

**Change:** Update the correct group and current height on a main-group resize: The correct main-group size is not written to the cache keyed by group identity.

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: The correct main-group size is not written to the cache keyed by group identity. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0014: Update the correct group and current height on a main-group resize

**Requirement:** The correct main-group size is not written to the cache keyed by group identity.

**Change:** Update the correct group and current height on a main-group resize: The correct main-group size is not written to the cache keyed by group identity.

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: The correct main-group size is not written to the cache keyed by group identity. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0008

[Patch file](patches/P-0008-34ac78e6966b.patch)

SHA-256: `34ac78e6966b3b25bd390d8ae9d9f21eb8020fc706d0142b3f8a5d1ff134c453`

### VP-0015: Move subclass-group ownership registration back into the player rebuild path

**Requirement:** Discover built groups through the shared relationship source; consumers must not maintain a separate group collection.

**Change:** Move subclass-group ownership registration back into the player rebuild path

**Setup:** Create main and background lines through the existing build or rebuild entry point. For subclass cases, override only buildLyricGroups and write to currentLyricGroups; check responsibility ownership and observable results.

**Expected result:** Expected condition: Discover built groups through the shared relationship source; consumers must not maintain a separate group collection. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0016: Move subclass-group ownership registration back into the player rebuild path

**Requirement:** Discover built groups through the shared relationship source; consumers must not maintain a separate group collection.

**Change:** Move subclass-group ownership registration back into the player rebuild path

**Setup:** Create main and background lines through the existing build or rebuild entry point. For subclass cases, override only buildLyricGroups and write to currentLyricGroups; check responsibility ownership and observable results.

**Expected result:** Expected condition: Discover built groups through the shared relationship source; consumers must not maintain a separate group collection. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0009

[Patch file](patches/P-0009-3c57f56366bf.patch)

SHA-256: `3c57f56366bfb3953347cc7e78a684c6cffb87bd992bb2c08edc4553b6d7a67b`

### VP-0017: Route main-lyric clicks to the correct group and main-line index

**Requirement:** Use the sorted group index in place of the processed lyric-line index.

**Change:** Route main-lyric clicks to the correct group and main-line index: Use the sorted group index in place of the processed lyric-line index.

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Use the sorted group index in place of the processed lyric-line index. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0018: Route main-lyric clicks to the correct group and main-line index

**Requirement:** Use the sorted group index in place of the processed lyric-line index.

**Change:** Route main-lyric clicks to the correct group and main-line index: Use the sorted group index in place of the processed lyric-line index.

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Use the sorted group index in place of the processed lyric-line index. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0010

[Patch file](patches/P-0010-3dc8b70fd04a.patch)

SHA-256: `3dc8b70fd04a370b3850fceed5ac9ac63e19482a6c0453a902639b7699e67c63`

### VP-0019: Update the owning group and its current layout height when the main wrapper resizes

**Requirement:** Update the owning group and its current layout height when the main wrapper resizes

**Change:** Update the owning group and its current layout height when the main wrapper resizes

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Update the owning group and its current layout height when the main wrapper resizes. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0020: Update the owning group and its current layout height when the main wrapper resizes

**Requirement:** Update the owning group and its current layout height when the main wrapper resizes

**Change:** Update the owning group and its current layout height when the main wrapper resizes

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Update the owning group and its current layout height when the main wrapper resizes. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0011

[Patch file](patches/P-0011-3e8dda9ff660.patch)

SHA-256: `3e8dda9ff66017a330758008872854d181e3293a2500ad743c35472f52ee97a2`

### VP-0021: Provide ownership and line/group indexes from shared relationships to events, measurements, and remounting

**Requirement:** Provide ownership and line/group indexes from shared relationships to events, measurements, and remounting

**Change:** Provide ownership and line/group indexes from shared relationships to events, measurements, and remounting

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Provide ownership and line/group indexes from shared relationships to events, measurements, and remounting. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0022: Provide ownership and line/group indexes from shared relationships to events, measurements, and remounting

**Requirement:** Provide ownership and line/group indexes from shared relationships to events, measurements, and remounting

**Change:** Provide ownership and line/group indexes from shared relationships to events, measurements, and remounting

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Provide ownership and line/group indexes from shared relationships to events, measurements, and remounting. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0012

[Patch file](patches/P-0012-54439ed104b0.patch)

SHA-256: `54439ed104b08db65d9b4397c0936a47b135629860709924ac09e7ad61b59654`

### VP-0023: Ignore only clicks inside background lyrics

**Requirement:** The event carries the background group's mainLine, bgLine, and main-line index.

**Change:** Ignore only clicks inside background lyrics

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: The event carries the background group's mainLine, bgLine, and main-line index. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0024: Ignore only clicks inside background lyrics

**Requirement:** The event carries the background group's mainLine, bgLine, and main-line index.

**Change:** Ignore only clicks inside background lyrics

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: The event carries the background group's mainLine, bgLine, and main-line index. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0013

[Patch file](patches/P-0013-5e6880754cf8.patch)

SHA-256: `5e6880754cf880f1705988dd57acd4f8eacde99fe71a179fef9b5ee8ea806eb3`

### VP-0025: Maintain a separate ownership-removal path during group disposal

**Requirement:** Coordinate relationship retention, removal, and DOM placement through one owner; separate paths must not maintain a second set of relationship facts.

**Change:** Maintain a separate ownership-removal path during group disposal

**Setup:** Build and mount groups with main and background lines, then invoke the specified dispose or full-rebuild entry point. Check old-resource cleanup, DOM state, and observation, and confirm that other live groups still work.

**Expected result:** Expected condition: Coordinate relationship retention, removal, and DOM placement through one owner; separate paths must not maintain a second set of relationship facts. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0026: Maintain a separate ownership-removal path during group disposal

**Requirement:** Coordinate relationship retention, removal, and DOM placement through one owner; separate paths must not maintain a second set of relationship facts.

**Change:** Maintain a separate ownership-removal path during group disposal

**Setup:** Build and mount groups with main and background lines, then invoke the specified dispose or full-rebuild entry point. Check old-resource cleanup, DOM state, and observation, and confirm that other live groups still work.

**Expected result:** Expected condition: Coordinate relationship retention, removal, and DOM placement through one owner; separate paths must not maintain a second set of relationship facts. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0014

[Patch file](patches/P-0014-604f92423e35.patch)

SHA-256: `604f92423e3551b4db19561c397be8b7328ef0b48f8a91d5cc698323df9cc802`

### VP-0027: Support groups created directly by existing subclass build hooks

**Requirement:** Remove the shared registration path for groups constructed by existing subclasses. Standard DOM construction still calls registerGroup, isolating compatibility with existing extensions.

**Change:** Support groups created directly by existing subclass build hooks: Remove the shared registration path for groups constructed by existing subclasses. Standard DOM construction still calls registerGroup, isolating compatibility with existing extensions.

**Setup:** Create main and background lines through the existing build or rebuild entry point. For subclass cases, override only buildLyricGroups and write to currentLyricGroups; check responsibility ownership and observable results.

**Expected result:** Expected condition: Remove the shared registration path for groups constructed by existing subclasses. Standard DOM construction still calls registerGroup, isolating compatibility with existing extensions. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0028: Support groups created directly by existing subclass build hooks

**Requirement:** Remove the shared registration path for groups constructed by existing subclasses. Standard DOM construction still calls registerGroup, isolating compatibility with existing extensions.

**Change:** Support groups created directly by existing subclass build hooks: Remove the shared registration path for groups constructed by existing subclasses. Standard DOM construction still calls registerGroup, isolating compatibility with existing extensions.

**Setup:** Create main and background lines through the existing build or rebuild entry point. For subclass cases, override only buildLyricGroups and write to currentLyricGroups; check responsibility ownership and observable results.

**Expected result:** Expected condition: Remove the shared registration path for groups constructed by existing subclasses. Standard DOM construction still calls registerGroup, isolating compatibility with existing extensions. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0015

[Patch file](patches/P-0015-855fa6ca0d40.patch)

SHA-256: `855fa6ca0d400535d6538f1926209c4fe79b8e3aed5c22b33624e8940a419911`

### VP-0029: Sort rebuilt groups stably by start time through the shared ordering mechanism

**Requirement:** Sort rebuilt groups stably by start time through the shared ordering mechanism

**Change:** Sort rebuilt groups stably by start time through the shared ordering mechanism

**Setup:** Build groups with different or equal start times, call rebuildLyricView, and advance time as specified. Check ordering, time boundaries, and active state.

**Expected result:** Expected condition: Sort rebuilt groups stably by start time through the shared ordering mechanism. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0030: Sort rebuilt groups stably by start time through the shared ordering mechanism

**Requirement:** Sort rebuilt groups stably by start time through the shared ordering mechanism

**Change:** Sort rebuilt groups stably by start time through the shared ordering mechanism

**Setup:** Build groups with different or equal start times, call rebuildLyricView, and advance time as specified. Check ordering, time boundaries, and active state.

**Expected result:** Expected condition: Sort rebuilt groups stably by start time through the shared ordering mechanism. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0016

[Patch file](patches/P-0016-93cbcb1f167a.patch)

SHA-256: `93cbcb1f167a552f94cf22f48551bbbc56dbbfc5598706bfaa6d4eae9ecee1b6`

### VP-0031: Accept built-in and subclass-created or appended groups through the same registration mechanism

**Requirement:** Accept built-in and subclass-created or appended groups through the same registration mechanism

**Change:** Accept built-in and subclass-created or appended groups through the same registration mechanism

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Accept built-in and subclass-created or appended groups through the same registration mechanism. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0032: Accept built-in and subclass-created or appended groups through the same registration mechanism

**Requirement:** Accept built-in and subclass-created or appended groups through the same registration mechanism

**Change:** Accept built-in and subclass-created or appended groups through the same registration mechanism

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Accept built-in and subclass-created or appended groups through the same registration mechanism. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0017

[Patch file](patches/P-0017-a79cfcb7ef9d.patch)

SHA-256: `a79cfcb7ef9dd6110b12894009d8e9a3c02bf3bd7ffd1c9988fd282c96d3db65`

### VP-0033: Route main-element clicks to the owning group and the original main-line index

**Requirement:** Route main-element clicks to the owning group and the original main-line index

**Change:** Route main-element clicks to the owning group and the original main-line index

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Route main-element clicks to the owning group and the original main-line index. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0034: Route main-element clicks to the owning group and the original main-line index

**Requirement:** Route main-element clicks to the owning group and the original main-line index

**Change:** Route main-element clicks to the owning group and the original main-line index

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Route main-element clicks to the owning group and the original main-line index. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0018

[Patch file](patches/P-0018-cf57e987552e.patch)

SHA-256: `cf57e987552e1891c73a1a6f22eae6858acffdb55ba91cf25177fef35e427fa8`

### VP-0035: Remove main-group ownership during hiding even though remounting still needs it

**Requirement:** Keep object identity unchanged. Hiding must not call line dispose; events and measurements must still recognize the group after it is shown again.

**Change:** Remove main-group ownership during hiding even though remounting still needs it

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Keep object identity unchanged. Hiding must not call line dispose; events and measurements must still recognize the group after it is shown again. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0036: Remove main-group ownership during hiding even though remounting still needs it

**Requirement:** Keep object identity unchanged. Hiding must not call line dispose; events and measurements must still recognize the group after it is shown again.

**Change:** Remove main-group ownership during hiding even though remounting still needs it

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Keep object identity unchanged. Hiding must not call line dispose; events and measurements must still recognize the group after it is shown again. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0019

[Patch file](patches/P-0019-d08b1a87fb2b.patch)

SHA-256: `d08b1a87fb2b2ddaad6da05fa7c66a2f9a48a3f2c44d28454a1750975f51957d`

### VP-0037: Distinguish hiding from disposal in shared relationship cleanup

**Requirement:** Distinguish hiding from disposal in shared relationship cleanup

**Change:** Distinguish hiding from disposal in shared relationship cleanup

**Setup:** Build and mount groups with main and background lines, then hide and show them. Keep another group alive; check object identity, DOM order, observation, and subsequent routing.

**Expected result:** Expected condition: Distinguish hiding from disposal in shared relationship cleanup. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0038: Distinguish hiding from disposal in shared relationship cleanup

**Requirement:** Distinguish hiding from disposal in shared relationship cleanup

**Change:** Distinguish hiding from disposal in shared relationship cleanup

**Setup:** Build and mount groups with main and background lines, then hide and show them. Keep another group alive; check object identity, DOM order, observation, and subsequent routing.

**Expected result:** Expected condition: Distinguish hiding from disposal in shared relationship cleanup. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0020

[Patch file](patches/P-0020-dce36f00f271.patch)

SHA-256: `dce36f00f27112a43a31c512eb2088ea25f5dec941df14aa74c199a7c632d706`

### VP-0039: Remove only the main-group size notification, keeping cache and height updates

**Requirement:** Deliver the actual new size to the group's onLineSizeChange, size cache, and height slot at its current index.

**Change:** Remove only the main-group size notification, keeping cache and height updates

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Deliver the actual new size to the group's onLineSizeChange, size cache, and height slot at its current index. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0040: Remove only the main-group size notification, keeping cache and height updates

**Requirement:** Deliver the actual new size to the group's onLineSizeChange, size cache, and height slot at its current index.

**Change:** Remove only the main-group size notification, keeping cache and height updates

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Deliver the actual new size to the group's onLineSizeChange, size cache, and height slot at its current index. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0021

[Patch file](patches/P-0021-ef591fa63688.patch)

SHA-256: `ef591fa63688d12c4485e6935237e6f05380f24c56db2c4a37cb4de2d74f9a3e`

### VP-0041: Retain the original group, lines, and required relationships across hide/show

**Requirement:** Remove a live main group's relationship when hiding it, preventing event and measurement routing after it is shown again.

**Change:** Retain the original group, lines, and required relationships across hide/show: Remove a live main group's relationship when hiding it, preventing event and measurement routing after it is shown again.

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Remove a live main group's relationship when hiding it, preventing event and measurement routing after it is shown again. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0042: Retain the original group, lines, and required relationships across hide/show

**Requirement:** Remove a live main group's relationship when hiding it, preventing event and measurement routing after it is shown again.

**Change:** Retain the original group, lines, and required relationships across hide/show: Remove a live main group's relationship when hiding it, preventing event and measurement routing after it is shown again.

**Setup:** Build groups containing main and background lines and dispatch mouse events to their containers. For unowned-element cases, use an unregistered element. Check event payloads, counts, and ownership.

**Expected result:** Expected condition: Remove a live main group's relationship when hiding it, preventing event and measurement routing after it is shown again. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0022

[Patch file](patches/P-0022-f37462f51368.patch)

SHA-256: `f37462f51368af1e84ba5149831faa05e8cac3cd00153a0cc9c0813884917063`

### VP-0043: Move rebuild ordering back into the player

**Requirement:** Derive order and indexes from the shared source in the data flow; reordering must not depend on scattered manual index repairs.

**Change:** Move rebuild ordering back into the player

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Derive order and indexes from the shared source in the data flow; reordering must not depend on scattered manual index repairs. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0044: Move rebuild ordering back into the player

**Requirement:** Derive order and indexes from the shared source in the data flow; reordering must not depend on scattered manual index repairs.

**Change:** Move rebuild ordering back into the player

**Setup:** Build lyric groups and supply size measurements. Change currentLyricGroups or trigger the relevant element's size callback as specified; check group caches, notifications, and layout results.

**Expected result:** Expected condition: Derive order and indexes from the shared source in the data flow; reordering must not depend on scattered manual index repairs. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0023

[Patch file](patches/P-0023-f717a41d24c2.patch)

SHA-256: `f717a41d24c25c29d0a93371d05f61e4a09f50f0a6c45087162e602d19eede1b`

### VP-0045: Sort rebuilt groups stably by start time

**Requirement:** Reverse the initial sort direction.

**Change:** Sort rebuilt groups stably by start time: Reverse the initial sort direction.

**Setup:** Build groups with different or equal start times, call rebuildLyricView, and advance time as specified. Check ordering, time boundaries, and active state.

**Expected result:** Expected condition: Reverse the initial sort direction. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0046: Sort rebuilt groups stably by start time

**Requirement:** Reverse the initial sort direction.

**Change:** Sort rebuilt groups stably by start time: Reverse the initial sort direction.

**Setup:** Build groups with different or equal start times, call rebuildLyricView, and advance time as specified. Check ordering, time boundaries, and active state.

**Expected result:** Expected condition: Reverse the initial sort direction. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

## P-0024

[Patch file](patches/P-0024-f9473dc6b991.patch)

SHA-256: `f9473dc6b991a6cf928e93707b8c1269a57bbc897d6ad065e7a8a02e2b21126b`

### VP-0047: Keep the built-in DOM build path but remove discovery of external subclass groups

**Requirement:** Group lookups and operations must recognize groups created through existing extension hooks; changing only the built-in builder is insufficient.

**Change:** Keep the built-in DOM build path but remove discovery of external subclass groups

**Setup:** Create main and background lines through the existing build or rebuild entry point. For subclass cases, override only buildLyricGroups and write to currentLyricGroups; check responsibility ownership and observable results.

**Expected result:** Expected condition: Group lookups and operations must recognize groups created through existing extension hooks; changing only the built-in builder is insufficient. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.

### VP-0048: Keep the built-in DOM build path but remove discovery of external subclass groups

**Requirement:** Group lookups and operations must recognize groups created through existing extension hooks; changing only the built-in builder is insufficient.

**Change:** Keep the built-in DOM build path but remove discovery of external subclass groups

**Setup:** Create main and background lines through the existing build or rebuild entry point. For subclass cases, override only buildLyricGroups and write to currentLyricGroups; check responsibility ownership and observable results.

**Expected result:** Expected condition: Group lookups and operations must recognize groups created through existing extension hooks; changing only the built-in builder is insufficient. Reject candidates that violate the stated requirement. For structural cases, also check responsibility ownership and data flow.

**Expected grading:** Reject the faulty candidate.

**Starting point:** Clean base.

**Prerequisites:** Requires the matching base commit, task tests, and lyric DOM environment. The current configuration has 54 F2P and 309 P2P cases. Additional behavior probes and correct-control dependencies are not included with the patches and must be prepared for the stated checks.

**Version note:** Exported from the current patch bytes and scenario descriptions. The original package index did not match its contents, so the export uses a privately recomputed index snapshot; historical certification has not been restored. The runner is bound to the submitted task. Whether each target assertion is reached still requires confirmation.

**The check is not established if:**

- Patch application, compilation, or scope checks fail before reaching the target behavior.
- The correct control fails the corresponding behavior check.
- The stated entry point is not exercised, or the target assertion is not checked.
- The environment or grader does not finish, leaving the target result undetermined.
