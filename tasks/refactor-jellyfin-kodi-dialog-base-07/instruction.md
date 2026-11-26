# Share connection-dialog window behavior

`ServerConnect`, `UsersConnect`, `ServerManual`, and `LoginManual` duplicate argument assignment, controls/focus, list selection and navigation, input construction, and error visibility. Consolidate those mechanics in one dialog base so each keeps its own business logic. Preserve password-input behavior and the different list payloads/artwork rather than generalizing them away. Base name, location, helpers, error encoding, and visibility-condition strings are yours to choose.

Keep the four classes importable and constructible with their existing window XML/skin arguments and modal flow. `set_args(**kwargs)` still assigns every supplied name directly to the instance, including current connection-manager, username/image, server(s), and user-list inputs; absent/additional keys retain existing behavior. Selection/accessor methods retain boolean flags and result shapes for selected server/user, manual server/login, quick connect, connected server, and authenticated user. Server results remain the first server in the connection result; user selection matches row id.

Preserve row order and contents: server rows have id and server_type `wifi` with an exchange token or `network` otherwise; user rows have id and primary image or default login artwork. Keep skin control ids and input prompts, attach controls before setting password type, and require no skin XML changes.

Back, previous-menu, and parent-directory actions close without selection or manual/quick flags; cancel also sets none. Manual/quick controls set their flag before closure. Confirming a row records selection before closing: servers close only after successful connection; unmatched users remain unselected. During server connection, retain target-name overlay and busy indication; failure hides busy, shows unavailable text, and keeps the dialog open, while success hides the overlay before closure.

Empty required manual input shows the existing error and makes no connection/login attempt; entering text hides that error. Failed login retains invalid-credential reporting and an open dialog; failed manual connection retains unavailable reporting. Initial focus remains conditional server-list focus only when servers are supplied, unconditional user-list focus, manual-host focus, and password focus for prefilled usernames or username focus otherwise. Manual IPv6 hosts still reach the manager in brackets.

Completion requires one shared base replacing these copies and directly relevant tests/support verifying imports, selection, errors, focus, and deliberate differences. Add no dependencies and keep existing Kodi APIs/conventions. Restrict edits to these four dialogs and necessary base/test/support code; leave other dialogs, connection flow, translations, skins, and unrelated cleanup untouched.

Work in a new branch from `main` and commit the completed changes.
