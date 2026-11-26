# Give request resources responsibility for their lifecycle

The request layer selects resource behavior through integer kind codes and long conditional chains. Plugins also inspect that private numeric state, including a hard-coded comparison. Opening resources, writing results back, and releasing handles or temporary files consequently depend on callers knowing what those codes mean.

Separate per-kind responsibility for opening, temporary-file creation, write-back, and closing from URI and mode parsing. Give plugins public, documented, read-only kind queries so they no longer need private numeric fields or hard-coded values. This changes responsibility, while preserving the observable behavior and legacy compatibility below. The private resource representation and lifecycle dispatch design are yours to choose.

## Request and plugin contracts

Keep the constructor signature:

```python
Request(uri, mode, *, extension=None, format_hint=None, **kwargs)
```

It accepts the same inputs with the same interpretation: HTTP(S), FTP(S), and `file://` URIs; standard `imageio:` images; special read and return-bytes URIs; local paths, including zip-member syntax; `bytes`; `memoryview`; `pathlib.Path`; and caller-provided file objects. Classification remains identical, including filename, extension, mode, and legacy numeric kind for each input class. Standard images continue to work with and without a zip member.

Preserve the names, types, and values of the request's raw URI, filename, extension, format hint, mode, keyword arguments, and header bytes. Plugins receive the request as before. Any added kind queries must reliably describe the resource without changing that handoff.

| Method | Preserved behavior |
| --- | --- |
| `get_file()` | No arguments; return the same expected read/write handle, or the current sentinel for a kind without a handle, with unchanged reuse semantics. |
| `get_local_filename()` | Return the existing local path or a temporary local path, as today. |
| `finish()` | Return `None`; flush results, release owned resources, and remove temporary files. |
| `get_result()` | Return the produced bytes for write-to-bytes requests and `None` otherwise. |

Keep `_uri_type` and the zip archive/member pair `_filename_zip` readable with their existing values. Numeric kind constants remain importable with unchanged values, and the shipped type declarations continue to describe the legacy surface. Existing third-party code can still read it even though resource lifecycle dispatch and the updated plugin call sites no longer depend on it.

## Ownership and existing edge behavior

Handles for local files, zip members, in-memory bytes, and caller-provided files read and write the same bytes as before. Finishing writes owned results back byte for byte to the original destination: the returned-bytes result, caller's file object, or zip member. Close only handles opened by the request and delete its temporary files. A caller-provided file object remains open after the request finishes.

For HTTP(S) reads, the video reader continues to pass the original raw URI to its backend rather than the generic handle. For `ftp://`, `get_file()` continues to return `None`; do not add a path that opens, downloads, or resolves FTP resources as part of this work. Retain the existing handling of other supported URIs as well.

Where the existing plugin-selection path rejects a directory, keep its error message and mode-specific type: `ValueError` in legacy mode and `IOError` otherwise. Preserve existing explicit-plugin handling of directories too. Read-only targets, including special read-only URIs, fail with the same error types as today.

Constructing a request adds no I/O, network access, temporary files, or other observable side effects beyond the current behavior. The responsibility move does not widen network access, environment-variable handling, or filesystem writes.

## Completion and scope

The per-kind lifecycle responsibilities remain separate from URI and mode parsing, and plugin call sites use semantic queries instead of private numeric state. Numeric codes remain a readable compatibility surface rather than the mechanism driving that lifecycle. Preserve all existing public names, signatures, attributes, constants, return shapes, and capabilities; the semantic queries are the only added capability.

Limit edits to core resource-kind machinery, the affected plugin call sites and type declarations, and tests for preserved behavior. Use existing runtime dependencies. Leave unrelated code and formatting alone, and report adjacent quirks such as the FTP handle path separately instead of fixing them in this refactor.

Work on a new branch from `main` and commit the completed changes.
