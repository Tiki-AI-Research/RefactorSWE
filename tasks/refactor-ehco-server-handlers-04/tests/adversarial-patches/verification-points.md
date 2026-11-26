# Adversarial patches and verification points

Task: refactor-ehco-server-handlers-04
Base commit: 7fe290e7fc72c5ef548949608272e7613c7800c2

This package contains 26 patches. Expected outcomes describe test intent. Recorded results are stored in the separate audit directory.

See README.md for replay instructions. An invalid run cannot establish a successful rejection. The original task tests and scoring rules apply.

## P-0001

[patch](patches/P-0001-0b306607ceee.patch)
SHA-256: 0b306607ceeeaa35745be83276575e3270b8b8cd06c63615aa355cfc75c6b546

### VP-0001: Targeted regression: Actual parameter name start_ts/end_ts

- **requirement**: Use start_ts and end_ts. Default to [now-60,now], use Num=1 for latest=true and -1 otherwise, and forward a positive step. Retain defaults on parse failure. Success returns 200 with total/data, and query failure returns 500.
- **mutation**: Targeted regression: Actual parameter name start_ts/end_ts (changed files: internal/web/handler_api.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0002

[patch](patches/P-0002-0de0231730a9.patch)
SHA-256: 0de0231730a9953e23970e842669853f6d334d72853cafaa1dcf0334072b4062

### VP-0002: Targeted regression: Stateless source omitted xray instead of null

- **requirement**: Stateful source omits xray instead of null; when there is a source, retains the XraySnapshot field and its value.
- **mutation**: Targeted regression: Stateless source omitted xray instead of null (changed files: internal/web/handler_api.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0003

[patch](patches/P-0003-0fc3d0f06405.patch)
SHA-256: 0fc3d0f064058c48da1e8e8c215b170f152c20c79299119606fdaa35c9fd1147

### VP-0003: Targeted regression: Pass the label to HealthCheck and provide the request context.

- **requirement**: Pass the tag to HealthCheck and provide the request context; success 200/0/connect success/actual latency; check failed 400/-1/error message/zero latency
- **mutation**: Targeted regression: Pass the label to HealthCheck and provide the request context. (changed files: internal/web/handler_api.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0006

[patch](patches/P-0006-21bdd59be63c.patch)
SHA-256: 21bdd59be63c171c1ce3170709b197f4fbf9e6e338771d9dc0bbf2df1512bd48

### VP-0006: Targeted regression: Return 400 invalid parameter: time range before calling the query source.

- **requirement**: Return 400 invalid parameter: time range before calling the query source.
- **mutation**: Targeted regression: Return 400 invalid parameter: time range before calling the query source. (changed files: internal/web/handler_api.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0007

[patch](patches/P-0007-235b78138acd.patch)
SHA-256: 235b78138acd0dbb6a44206aea1d76c7bd33d5ab869988a83536ae53217c615c

### VP-0007: Targeted regression: When authRequired is false, protected routes can enter the processor without authentication.

- **requirement**: When authRequired is false, protected routes can enter the processor without authentication.
- **mutation**: Targeted regression: When authRequired is false, protected routes can enter the processor without authentication. (changed files: internal/web/auth.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0010

[patch](patches/P-0010-284d10a9d987.patch)
SHA-256: 284d10a9d98785792768a08932131bd0b8c34fb057e7fc58ab0057872679a199

### VP-0010: Targeted regression: 200 authenticated:true

- **requirement**: 200 authenticated:true; eHco_sid cookie issued, with Path=/, HttpOnly, Strict SameSite, Secure based on TLS settings, and existing expiration time
- **mutation**: Targeted regression: 200 authenticated:true (changed files: internal/web/auth.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0013

[patch](patches/P-0013-376815d8f518.patch)
SHA-256: 376815d8f518d8ca2445d35096637d5ea6fdd65b79f923e4dc105297e1605e9d

### VP-0013: Targeted regression: The conversation TTL is still 7 days. The expired SID is deleted and the authorization is lost.

- **requirement**: The conversation TTL is still 7 days. The expired SID is deleted and the authorization is lost. If the verification is successful, the expiration will be pushed to now + TTL. The protected request will continue to be resent with a renewed cookie.
- **mutation**: Targeted regression: The conversation TTL is still 7 days. The expired SID is deleted and the authorization is lost. (changed files: internal/web/auth.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0014

[patch](patches/P-0014-3bdfb49bd36e.patch)
SHA-256: 3bdfb49bd36e27ae3d4bdab799fafbb59cb211898d373a53190fb211e263c723

### VP-0014: Targeted regression: Start() error: Failed to start HTTP with the configured host/port, and an Echo start error occurred.

- **requirement**: Start() error: Failed to start HTTP with the configured host/port, and an Echo start error occurred.
- **mutation**: Targeted regression: Start() error: Failed to start HTTP with the configured host/port, and an Echo start error occurred. (changed files: internal/web/server.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0015

[patch](patches/P-0015-3fd471ceda19.patch)
SHA-256: 3fd471ceda194389cdda2bc44bb22c450ff61a61a13556455f7829ae8ae21edf

### VP-0015: Targeted regression: After successfully upgrading GET /ws/logs, call AddWebSocketConn. Call Remove and Close when the connection closes or a read failure ends the loop.

- **requirement**: After successfully upgrading GET /ws/logs, call AddWebSocketConn. Call Remove and Close when the connection closes or a read failure ends the loop. Preserve upgrade error behavior. If a broadcast write fails for one connection, remove and close that connection and continue sending frames to the others.
- **mutation**: Targeted regression: After successfully upgrading GET /ws/logs, call AddWebSocketConn. Call Remove and Close when the connection closes or a read failure ends the loop. (changed files: internal/web/handlers_ws.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0026

[patch](patches/P-0026-758c0fe27a9c.patch)
SHA-256: 758c0fe27a9ce96f80422118d54f9ec93529e293f687487ed4b89fb1c513c41d

### VP-0026: Targeted regression: When X-Ehco-Token is equal to the configured ApiToken, it is allowed.

- **requirement**: X-Ehco-Token is allowed when configured to be equal to ApiToken; a 401 error is returned for incorrect tokens.
- **mutation**: Targeted regression: When X-Ehco-Token is equal to the configured ApiToken, it is allowed. (changed files: internal/web/auth.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0029

[patch](patches/P-0029-7c9c050cd997.patch)
SHA-256: 7c9c050cd997df673bb15764a6c760239f94d4d5b5cedeb4366c29ec8bbaa8b2

### VP-0029: Targeted regression: Success verification will advance the expiration date to now+TTL.

- **requirement**: The successful verification will advance the expiration date to now+TTL; the protected request will continue to be resent with the renewal cookie.
- **mutation**: Targeted regression: Success verification will advance the expiration date to now+TTL. (changed files: internal/web/auth.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0030

[patch](patches/P-0030-7ef89d9a0fc5.patch)
SHA-256: 7ef89d9a0fc5bf8540d7e8b5840d9f4cbf2c242008aa94f46079e602dee95eec

### VP-0030: Targeted regression: When an error is returned from the upstream, the HTTP status is 502, and the message is retained.

- **requirement**: When an error is returned from the upstream, the HTTP status is 502 with the message retained; 400 is returned before the application execution for non-Linux systems; the channel/force/restart remains; the default is auto; when the background Apply block occurs, the HTTP status is still 202 with an empty body; the background context is separated from the request lifetime; the background calls relay.Reload(true) and optionally xray.Reload(true) in the original order; error is logged; HTTP status is set to reload success without waiting for the background to complete; the 400 failure status is retained.
- **mutation**: Targeted regression: When an error is returned from the upstream, the HTTP status is 502, and the message is retained. (changed files: internal/web/handler_update.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0032

[patch](patches/P-0032-85d229bc6a68.patch)
SHA-256: 85d229bc6a687e3c2e390f8b62fde3d3466239a46e63eb6bd96ebd87e2f30915

### VP-0032: Targeted regression: The API paths /api/, /ws/, /metrics/, and /debug/ return 404 when reaching SPA fallback, and no HTML is returned.

- **requirement**: The /api/, /ws/, /metrics/, and /debug/ paths reaching SPA fallback return 404 without returning HTML; some endpoints still return a 401 error after authentication interception; the /assets/ path returns 404 for missing files and missing file handlers for the existing favicon asset processor; existing files are served by the FileServer service; the /, /index.html, and accessible SPA client routes return shell, 200, text/html; no-store
- **mutation**: Targeted regression: The API paths /api/, /ws/, /metrics/, and /debug/ return 404 when reaching SPA fallback, and no HTML is returned. (changed files: internal/web/webui_embed.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0033

[patch](patches/P-0033-8cdceea654c3.patch)
SHA-256: 8cdceea654c38aa214ca839c6516d9af90622828125033228ff3511da52f51c3

### VP-0033: Targeted regression: A successful 200 response returns the original maintenance payload.

- **requirement**: A successful 200 response returns the original maintenance payload.
- **mutation**: Targeted regression: A successful 200 response returns the original maintenance payload. (changed files: internal/web/handler_api.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0034

[patch](patches/P-0034-93ceb1817bc1.patch)
SHA-256: 93ceb1817bc15bc7c3ed259e7e8c0c1d8224b852fa5a55658bf9c2f64e990921

### VP-0034: Targeted regression: NewEchoServer() *echo.Echo can still be called at the transport layer.

- **requirement**: Preserve NewEchoServer() *echo.Echo for transport-layer callers, with Debug, HidePort, and HideBanner true. NginxLogMiddleware(logger) echo.MiddlewareFunc must call the next handler, return its error, and log the IP, request, status, and elapsed time. MakeIndexF() http.HandlerFunc must still log the request and return "access from remote ip: <RemoteAddr>" with the original newline.
- **mutation**: Targeted regression: NewEchoServer() *echo.Echo can still be called at the transport layer. (changed files: internal/web/utils.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0040

[patch](patches/P-0040-ad3854b36441.patch)
SHA-256: ad3854b36441f5508661467027781520a7d2c858a29ae37d774c3e66df1228f3

### VP-0040: Targeted regression: Preserve NewServer(cfg, relayReloader, healthChecker, connMgr) (*Server,error).

- **requirement**: NewServer(cfg, relayReloader, healthChecker, connMgr) (*Server,error) Reserved; valid configuration assembled; WebPort <= 0 or > 65535 returns nil Server and invalid configuration error; no delay to Start verification; Start() error starts HTTP with configured host/port and returns Echo start error; Stop() error closes HTTP service, retains existing errors; after startup, sets/ replaces status source before next overview read of new snapshot; nil does not clear existing sources; after startup, sets/ replaces reloader before next reload call to new source; APIGroup() *echo.Group retains prefix; endpoints are accessible and processed by the same global middleware
- **mutation**: Targeted regression: Preserve NewServer(cfg, relayReloader, healthChecker, connMgr) (*Server,error). (changed files: internal/web/server.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0041

[patch](patches/P-0041-b860e37e2da8.patch)
SHA-256: b860e37e2da8773b6e3bea89eb9e052523566ed7b15a27a09d365a39fe3b8d21

### VP-0041: Targeted regression: Effective ehco_sid release

- **requirement**: A valid ehco_sid, a correct Authorization: Bearer <ApiToken>, or X-Ehco-Token equal to ApiToken grants access. Expired or unknown SIDs grant no access, and an incorrect token returns 401. When authRequired is false, protected routes reach their handlers without authentication. The public routes are /, /index.html, both favicon routes, robots, /assets/, and the three auth endpoints. Other routes requiring authentication return 401 authentication required. auth_required describes the configuration and authenticated describes the request. Handle the open and token-only branches first, as in the baseline. With a configured password, invalid JSON returns 400 invalid login body and a mismatched password in valid JSON returns 401 invalid password. With empty DashboardPass and nonempty ApiToken, return 403 dashboard login not configured and issue no session. A successful password login returns 200 authenticated:true and sets ehco_sid with Path=/, HttpOnly, Strict SameSite, Secure according to TLS, and the existing expiry. With both credentials empty, return authenticated:true without parsing the password or issuing a new session via Set-Cookie. Logout revokes a supplied session and clears the cookie even if the session is missing. The old session then becomes invalid. Preserve the seven-day TTL, delete expired SIDs and deny them access, extend stored expiry to now+TTL after successful validation, and resend the renewed cookie on protected requests.
- **mutation**: Targeted regression: Effective ehco_sid release (changed files: internal/web/auth.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0043

[patch](patches/P-0043-c3e8be05e9ac.patch)
SHA-256: c3e8be05e9aca2911ea5a12dfec33e36a8a846723c51a75ea77e7e85ac30662e

### VP-0043: Targeted regression: NginxLogMiddleware(logger) echo.MiddlewareFunc continues to call downstream components, returns their errors, and records the IP, request, status, etc.

- **requirement**: NginxLogMiddleware(logger) echo.MiddlewareFunc continues to call downstream components, returns their errors, and records the IP, request, status, and duration.
- **mutation**: Targeted regression: NginxLogMiddleware(logger) echo.MiddlewareFunc continues to call downstream components, returns their errors, and records the IP, request, status, and duration. (changed files: internal/web/mw.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0045

[patch](patches/P-0045-d231ed2d1565.patch)
SHA-256: d231ed2d1565e820186ec6dddac255e7d2f1cad4e2e1bab6ece142aa879dabd5

### VP-0045: Targeted regression: The Stop() function closes the HTTP service, retaining all existing error messages.

- **requirement**: The Stop() function closes the HTTP service, retaining all existing error messages.
- **mutation**: Targeted regression: The Stop() function closes the HTTP service, retaining all existing error messages. (changed files: internal/web/server.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0047

[patch](patches/P-0047-dd982675edeb.patch)
SHA-256: dd982675edebac84a1762bb128caa91a9beea4201f5ab1e659519b938c866696

### VP-0047: Targeted regression: When errors.Is of each db endpoint matches cmgr.ErrMetricsDisabled, a 503 error is reported, along with the error message.

- **requirement**: When errors.Is of each db endpoint matches cmgr.ErrMetricsDisabled, a 503 error is reported, along with the error message.
- **mutation**: Targeted regression: When errors.Is of each db endpoint matches cmgr.ErrMetricsDisabled, a 503 error is reported, along with the error message. (changed files: internal/web/handler_api.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0050

[patch](patches/P-0050-e22504b11c07.patch)
SHA-256: e22504b11c07032c352bcdd0bafe60f136e6546bff2e3f2e56e0ff25cdf05d4a

### VP-0050: Targeted regression: /, /index.html, two favicon types, robots, /assets/, and three auth endpoints are exposed.

- **requirement**: /, /index.html, two favicon types, robots, /assets/, and three auth endpoints are public; all others require 401 authentication.
- **mutation**: Targeted regression: /, /index.html, two favicon types, robots, /assets/, and three auth endpoints are exposed. (changed files: internal/web/webui_embed.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0052

[patch](patches/P-0052-e6db10bf8638.patch)
SHA-256: e6db10bf86385f95a0d3c5251af0bf81ee54bfe1b5766a63a8c5fa85e5516d37

### VP-0052: Targeted regression: Each maintenance entry returns 500 if it encounters an error in non-special areas. The original error message is retained.

- **requirement**: Each maintenance entry returns 500 if it encounters an error in non-special areas. The original error message is retained.
- **mutation**: Targeted regression: Each maintenance entry returns 500 if it encounters an error in non-special areas. The original error message is retained. (changed files: internal/web/handler_api.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0057

[patch](patches/P-0057-f67034b45373.patch)
SHA-256: f67034b453733f39be58a43d7c0d3e7de9f4eeaaa5c3e79e1dcf2bd3da00faf1

### VP-0057: Targeted regression: When errors.Is matches ms.ErrTruncateNotConfirmed, a 400 error is reported, along with the error message.

- **requirement**: When errors.Is matches ms.ErrTruncateNotConfirmed, a 400 error is reported, along with the error message.
- **mutation**: Targeted regression: When errors.Is matches ms.ErrTruncateNotConfirmed, a 400 error is reported, along with the error message. (changed files: internal/web/handler_api.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0058

[patch](patches/P-0058-f703fa0224f9.patch)
SHA-256: f703fa0224f92d702c0850e113a2cf92457535fe3b570035b6fbd0cd170f4501

### VP-0058: Targeted regression: /assets/missing files and missing file responses for the existing favicon asset processor return 404

- **requirement**: /assets/missing files and missing file responses for the existing favicon asset processor return 404
- **mutation**: Targeted regression: /assets/missing files and missing file responses for the existing favicon asset processor return 404 (changed files: internal/web/webui_embed.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0059

[patch](patches/P-0059-f78f4482976d.patch)
SHA-256: f78f4482976de43c0663dc194d95ff82769f23b37de9333363980fa6d3e502f7

### VP-0059: Targeted regression: MakeIndexF() http.HandlerFunc continues to respond to access from the remote IP: <RemoteAddr> and continues with the original process.

- **requirement**: MakeIndexF() http.HandlerFunc continues to respond to access from remote IP: <RemoteAddr> and records the log, maintaining the original line breaks.
- **mutation**: Targeted regression: MakeIndexF() http.HandlerFunc continues to respond to access from remote IP: <RemoteAddr> and records the log, maintaining the original line breaks. (changed files: internal/web/utils.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

## P-0060

[patch](patches/P-0060-f8178f44c213.patch)
SHA-256: f8178f44c2139322e3fdad94bcad8b91ca682fd6aebfea0c5c728dc4afc1460a

### VP-0060: Targeted regression: Existing files are stored on the FileServer service.

- **requirement**: Existing files are served by the FileServer service; /, /index.html, and accessible SPA client routes return shell, 200, text/html; no-store
- **mutation**: Targeted regression: Existing files are stored on the FileServer service. (changed files: internal/web/webui_embed.go)
- **setup**: Apply this patch to the clean baseline at 7fe290e7fc72, then run the official grader with tests/test.sh.
- **application**: clean_base
- **expected_relation**: reject
- **expected_result**: The task grader should reject the candidate because at least one assertion for this behavior fails. Acceptance indicates that the tests missed this specific defect.
- **prerequisites**: None (clean baseline)
- **invalid_if**: The patch does not apply to the task baseline (APPLY_FAILED). The task image fails to build or the container environment fails (ENV_ERROR). The tests produce no case-level report, fail to finish, or time out. Not actually read the target assertion or there is infrastructure confusion

