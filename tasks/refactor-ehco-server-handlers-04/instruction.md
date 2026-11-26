# Separate admin handlers from server lifecycle

The admin server owns HTTP lifecycle and six handler families: authentication, configuration, database maintenance, self-update, log streaming, and SPA/static serving. Move those families out of the server, giving each only its actual dependencies. Aggregating handlers must use narrow purpose-specific contracts and be verifiable without assembling the full server. The remaining server owns lifecycle, middleware, and routing. Make absent optional hooks explicit and harmless while retaining late wiring; internal types and layout are yours to choose.

Preserve exported construction/start/stop capabilities, rejecting invalid configuration during construction. Status/reload setters stay callable after start, ignore nil inputs, and affect subsequent overview/reload behavior without recreation. Keep the exported `/api/v1` routing-group accessor so other components can mount endpoints after start under the same authentication/logging stack, plus the exported engine constructor, request-log middleware, and remote-IP index handler.

All routes retain methods, paths, middleware order, headers, inputs, payloads, and status codes: metrics, pprof, auth info/login/logout, configuration and reload, health/node metrics, overview/version, update check/apply, database maintenance, `/ws/logs`, assets, favicon, index, and SPA fallback. Sessions, Bearer authorization, and `X-Ehco-Token` remain accepted. With neither password nor API token the dashboard stays open. Index/index.html, favicons, robots, assets, and all three auth endpoints remain public; other unauthenticated requests return 401. `/api/`, `/ws/`, `/metrics/`, and `/debug/` paths must not receive the SPA shell, nor may missing assets: those return 404.

Keep these distinctions:

- Health check requires `relay_label` or returns 400, and retains `error_code`, `msg`, and `latency`. Node metrics keeps start/end/latest/step inputs, default 60-second window ending now, and 400 when start is at or after end.
- Overview retains configured rule count and `last_reload_at`, includes `xray` only with a status snapshot and `host` only with a recent metrics sample, and omits absent sources rather than returning null. Version fields stay unchanged.
- Auth info retains `auth_required` and `authenticated`; login/logout retain boolean `authenticated`. Login reads JSON `password`: malformed body 400, wrong password 401, API-token-only setup 403. Correct password issues a session. With no credentials, return 200/true without issuing one. Logout revokes sessions, clears the cookie, and returns 200 even when already unauthenticated; retain session expiry and sliding renewal.
- Database cleanup reads `older_than_days`, truncate reads `confirm`; disabled metrics maps to 503, unconfirmed truncate to 400, other failures to 500. Reset retains 204 with an empty body.
- Update check defaults optional `channel` to auto, forwards compiled version/git revision, and maps upstream failure to 502. Apply keeps `channel`, `force`, and `restart`, rejects non-Linux platforms with 400, and returns 202 without waiting. Reload returns `reload success`, requests relay and any wired subsystem reload asynchronously, or returns 400 without panic when no reloader exists.
- Log WebSockets register with the broadcaster while open and unregister on close; one failing client must not interrupt others.

Completion requires handler ownership/dependency separation and tests supporting equivalent behavior. Retain interface-based boundaries without concrete relay/xray/storage dependencies or recreated import cycles. Do not reinterpret validation, metrics registration, session lifetime, update/reload, or error policy. Limit edits to web-admin production code, tests, and required call sites; leave unrelated packages, embedded assets, dependencies, and formatting untouched.

Work in a new branch from `main` and commit the completed changes.
