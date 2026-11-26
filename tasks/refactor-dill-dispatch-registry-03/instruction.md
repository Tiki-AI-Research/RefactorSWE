# Give one registry ownership of serializer integration

Dill's extended pickler, registration functions, and standard-pickle integration share mutable dispatch state. Snapshotting, enabling integration, and restoring standard handlers are spread across those entry points. Put ownership of dill registrations, standard dispatch integration, and restoration behind one registry object while retaining the existing registration workflow.

The registry's storage, snapshot details, and delegation arrangement are internal. Callers continue using the current public APIs and mutable dispatch mapping.

## Public registration and dispatch

Keep these entry points, including keyword calls with the parameter names shown:

| API | Contract |
| --- | --- |
| `dill.register(t)` | Return a decorator that registers its serializer for type `t` and returns the original serializer function. |
| `dill.pickle(t, func)` | Register `func` for `t` in dill's dispatch and return `None`. |
| `dill.extend(use_dill=True)` | Keep the flag, default, and `None` return; enable or disable the standard integration as described below. |
| `dill.Pickler.dispatch` | Remain an accessible mutable mapping with compatible lookup, iteration, and assignment. |

A serializer added through either registration function is immediately usable by `dill.Pickler`. Direct changes to its dispatch continue governing dill serialization, and enabling standard integration uses the current registrations. Preserve serializer selection, serialized results, supported exception behavior, and all existing public signatures and return shapes.

## Integration and restoration

Importing dill still enables its default serializers automatically in the standard library's pure-Python `pickle._Pickler.dispatch` mapping.

`dill.extend(False)` removes dill's own handlers from that standard mapping and restores their pre-extension standard entries where those existed. It leaves externally defined handlers in place, whether introduced through public registration followed by enabling integration or through direct assignment. If an external handler replaced an existing standard handler, disabling integration must not overwrite that replacement with the earlier handler.

A later `dill.extend(True)` exposes the current dill registrations again. Neither toggle disables or erases serializers in dill's own dispatch; integration's dispatch changes are confined to the standard pure-Python pickler mapping. These restoration and external-handler rules remain the same through repeated enable/disable cycles.

## Completion and scope

One registry owns the registration and integration lifecycle, and the public paths delegate without retaining separate ownership of extension state. Existing direct dispatch access, import-time enabling, flags, capabilities, and serialized data formats remain compatible; users do not adopt a new registration API.

Add no runtime dependencies or unrelated package changes. Limit edits to necessary production code, relevant tests, and supporting adjustments required to implement and verify this contract.

Work on a new branch from `main` and commit the completed changes.
