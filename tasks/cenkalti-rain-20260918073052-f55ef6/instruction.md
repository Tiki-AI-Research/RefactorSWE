## Background

Rain is an embeddable BitTorrent client and library. Applications embed Rain's `Session` component to manage torrent downloads, seeding, peer communication, resume-data persistence, and optional RPC control. Long-running host processes, test suites, and dynamic services require dependable lifecycle semantics for session shutdown, background workload termination, and resource ownership release.

Inspection of the repository reveals lifecycle and resource ownership gaps during session teardown:
1. Calling `Session.Close()` more than once sequentially triggers an unhandled runtime panic due to duplicate channel closure, preventing safe sequential cleanup in teardown routines and deferred statements.
2. Concurrent calls to `Session.Close()` from multiple goroutines produce data races, uncoordinated channel closures, and runtime crashes.
3. Invoking `Session.Close()` while torrents are actively allocating disk storage or transferring data lacks verified completion boundaries, leaving background workers running and open file handles leaked.
4. In-flight RPC handlers and network listeners lack coordinated shutdown timeouts, allowing active handlers to hang or prevent `Session.Close()` from completing within bounded time.
5. Unbounded teardown can block indefinitely without error reporting or retain database ownership unpredictably.

Refactoring is required to establish consistent shutdown coordination and resource ownership release across session teardown without altering Rain's public API, core BitTorrent wire protocols, or on-disk data storage formats.

## Goal

Provide deterministic session shutdown coordination across all teardown paths:
- A successful shutdown returning `nil` MUST leave no session-owned network listeners, active client connections, active server-side RPC handlers, active torrent workloads, background worker routines, database ownership, or open file handles.
- When session teardown exceeds the applicable shutdown bound, `Session.Close()` MUST return an explicit non-nil shutdown error within the deadline; unfinished resources and database ownership MUST NOT be released while outstanding work may still access them, and repeated calls to `Session.Close()` report the cached error.

### Shutdown Timing Contract

All teardown activities within `Session.Close()` are governed by an overall completion bound measured from the invocation of `Session.Close()`:
- **RPC Disabled (`Config.RPCEnabled = false`)**: Every sequential or concurrent invocation of `Session.Close()` MUST complete within the public bound of 5 seconds (internal teardown deadline is 4900ms, reserving a 100ms safety margin).
- **RPC Enabled (`Config.RPCEnabled = true`)**:
  - The RPC shutdown phase is strictly bounded by `Config.RPCShutdownTimeout + 250ms`: active handlers are granted up to `Config.RPCShutdownTimeout` for graceful termination, followed by listener and connection closure within 150ms internal deadline (reserving a 100ms safety margin before the 250ms public bound).
  - In sessions without active torrent workloads, the entire `Session.Close()` invocation MUST complete within the public bound of `Config.RPCShutdownTimeout + 250ms` (governed by internal teardown budget `Config.RPCShutdownTimeout + 150ms`).
  - In sessions with active torrent workloads, the entire `Session.Close()` invocation MUST complete within the public bound of `Config.RPCShutdownTimeout + 5 seconds` (governed by internal teardown budget `Config.RPCShutdownTimeout + 4900ms`, reserving a 100ms safety margin).

**Internal Safety Margin Requirement**:
To guarantee that `Session.Close()` returns deterministically within the public bounds despite operating-system thread scheduling latency, the implementation MUST reserve a fixed internal safety margin of 100 ms before the public deadline (e.g. bounding internal teardown work to 4900 ms when the public bound is 5 seconds, and bounding RPC listener/connection cleanup to 150 ms after `RPCShutdownTimeout` when the public bound is `RPCShutdownTimeout + 250 ms`). Subsystem cleanup operations (including database closure) must be bounded by the remaining shutdown budget rather than blocking indefinitely.

### Teardown Postconditions

- **Normal Shutdown (Teardown completes within bound)**:
  - Database ownership and session-owned resources are released, and open file handles closed.
  - All active torrent workloads, background workers, and RPC listeners/connections/handlers are stopped.
  - `Session.Close()` returns `nil`. Subsequent sequential invocations also return `nil`.
- **Deadline-Exceeded Shutdown (Teardown exceeds deadline)**:
  - `Session.Close()` returns an explicit non-nil shutdown error within the applicable bound.
  - BoltDB and unfinished resources MUST NOT be released while unfinished routines may still access them, and immediate database reopening is not promised.
  - The session retains cleanup responsibility: live resources and the database lock are released when outstanding work eventually terminates, rather than permanently abandoning ownership.
  - Repeated calls to `Session.Close()` deterministically report the cached shutdown error.

## Public contract to preserve

The public package API and exported signatures MUST remain intact. In particular, the following entrypoints MUST be preserved:

- `func NewSession(cfg Config) (*Session, error)`
- `func (s *Session) Close() error`
- `func (s *Session) AddTorrent(r io.Reader, opt *AddTorrentOptions) (*Torrent, error)`
- `func (s *Session) AddURI(uri string, opt *AddTorrentOptions) (*Torrent, error)`
- `func (s *Session) RemoveTorrent(id string, keepData bool) error`
- `func (s *Session) ListTorrents() []*Torrent`
- `func (s *Session) GetTorrent(id string) *Torrent`
- `func (s *Session) StartAll() error`
- `func (s *Session) StopAll() error`
- `func (s *Session) Stats() SessionStats`
- `func (t *Torrent) Start() error`
- `func (t *Torrent) Stop() error`
- `func (t *Torrent) Stats() Stats`
- `func (t *Torrent) ID() string`
- `func (t *Torrent) Name() string`

All exported configuration fields on `Config`, default settings in `DefaultConfig` (specifically including `Config.RPCShutdownTimeout`), and the semantic effects of enabling or disabling optional capabilities (including DHT, RPC, PEX, and blocklists) MUST remain compatible.

### Structural Architecture Boundaries

### Required Internal Shutdown Budget and Active Deadline Boundaries

The refactoring MUST provide the following package-private methods on `Session` to expose the internal shutdown budget calculation and active execution deadlines:

```go
func (s *Session) shutdownBudget() (total time.Duration, rpc time.Duration)
func (s *Session) activeShutdownDeadline() (total time.Time, rpc time.Time)
```

1. **`shutdownBudget() (total time.Duration, rpc time.Duration)`**:
   Computes and returns the exact internal teardown budgets that govern session shutdown:
   - **RPC Disabled (`Config.RPCEnabled = false`)**:
     - `total` MUST be exactly `4900ms` (reserving a 100ms safety margin before the 5000ms public bound).
     - `rpc` MUST be `0`.
   - **RPC Enabled (`Config.RPCEnabled = true`), without active torrent workloads**:
     - `total` MUST be exactly `Config.RPCShutdownTimeout + 150ms` (reserving a 100ms safety margin before `Config.RPCShutdownTimeout + 250ms`).
     - `rpc` MUST be exactly `Config.RPCShutdownTimeout + 150ms`.
   - **RPC Enabled (`Config.RPCEnabled = true`), with active torrent workloads**:
     - `total` MUST be exactly `Config.RPCShutdownTimeout + 4900ms` (reserving a 100ms safety margin before `Config.RPCShutdownTimeout + 5000ms`).
     - `rpc` MUST be exactly `Config.RPCShutdownTimeout + 150ms`.

2. **`activeShutdownDeadline() (total time.Time, rpc time.Time)`**:
   Returns the actual active deadlines calculated during the invocation of `Session.Close()`:
   - Before `Session.Close()` is invoked, both return values MUST be zero `time.Time{}` (`total.IsZero()` and `rpc.IsZero()` are both true).
   - When `Session.Close()` is invoked with RPC disabled (`Config.RPCEnabled = false`):
     - `rpc` MUST remain zero `time.Time{}` (`rpc.IsZero()` is true), because no RPC phase is scheduled and no RPC deadline applies.
     - `total` MUST be set to `start.Add(4900ms)` (the shutdown start time plus `totalBudget`).
   - When `Session.Close()` is invoked with RPC enabled (`Config.RPCEnabled = true`):
     - `rpc` MUST be set to `start.Add(rpcBudget)` (where `rpcBudget = Config.RPCShutdownTimeout + 150ms`).
     - `total` MUST be set to `start.Add(totalBudget)` (where `totalBudget` is `Config.RPCShutdownTimeout + 150ms` without active torrents, or `Config.RPCShutdownTimeout + 4900ms` with active torrents).
   - These internal deadlines MUST actively govern the real shutdown execution path (bounding active RPC handler grace/cleanup, DHT stop, active torrent shutdown, worker wait, and database cleanup). Calculating internal deadlines does not alter the externally observable upper bounds defined in the Shutdown Timing Contract.
   - Subsequent calls or queries after shutdown retain the recorded active deadlines.

### Required Internal Shutdown Timer Boundary

To enable independent verification of the actual execution deadlines and timers (ensuring teardown execution strictly respects internal safety margins rather than reporting valid theoretical budgets while using prolonged execution timers), Session MUST provide the following package-private timer injection boundary:

```go
func (s *Session) setShutdownTimer(fn func(phase string, d time.Duration) (<-chan time.Time, func() bool))
```

1. **`setShutdownTimer` semantics**:
   - `fn` is an optional timer factory invoked whenever `Session.Close()` or its teardown coordinator creates a timer to bound a teardown phase.
   - `phase` identifies the teardown phase being timed:
     - `"total"`: the overall completion timer bounding `Session.Close()`. `d` MUST be calculated from the internal teardown budget (`shutdownBudget().total`).
     - `"rpc"`: the RPC phase deadline timer. `d` MUST be calculated from the internal RPC budget (`shutdownBudget().rpc`).
     - `"dht"`, `"torrents"`, `"workers"`, `"database"`: subsystem wait timers bounded by the remaining shutdown budget.
   - The returned `<-chan time.Time` is the channel that signals timeout when fired, and `func() bool` stops the timer.
   - When `setShutdownTimer` has not been called (or set to `nil`), Session defaults to standard `time.NewTimer(d)`.
   - The actual execution path of `Session.Close()` and `runShutdown` MUST use the timer returned by this factory to enforce phase and total deadlines.

### Required Internal Worker Completion Boundary

The refactoring MUST provide the following package-private completion boundary on Session:

```go
func (s *Session) workerCompletion() <-chan struct{}
```

- The method returns the same stable, non-nil channel for the lifetime of the Session.
- The channel remains open while any session-managed background worker is still running.
- Tracked session background workers include all internal long-running goroutines owned by the session that access shared session state or persistent storage, specifically:
  - `updateStatsLoop` (periodic resume data persistence loop)
  - `processDHTResults` (DHT node lookup result processor)
  - `checkTorrent` (asynchronous torrent file verification and recheck workers)
  - `blocklistReloader` (periodic blocklist refresh worker)
- Session worker completion, torrent cleanup, and RPC handler termination are distinct teardown phases with separate completion criteria and MUST NOT be conflated:
  - `http.Server.Close()` or closing client TCP connections does not guarantee that server-side RPC handlers have finished executing; handlers must be tracked and awaited or interrupted explicitly.
  - Calling `Torrent.Stop()` initiates torrent stopping asynchronously; torrent teardown finishes only when individual torrent resource release completes.
  - Background session workers may continue flushing data or processing queues independently until signaled to stop.
- The `workerCompletion()` channel closes exactly once after all registered session background workers have exited.
- Workers must be registered before their goroutines are started and must signal completion reliably, for example with a shared WaitGroup and deferred Done calls.
- A successful `Session.Close()` returning `nil` must not return before this channel is closed.
- If `Session.Close()` returns a deadline-exceeded error while workers or RPC handlers are still active, the non-nil error MUST be cached and returned idempotently by all subsequent `Close()` calls. Deferred cleanup goroutines MUST continue waiting for active workers and handlers to terminate before finally releasing BoltDB and other shared resources.
- This boundary is required for independent verification of background-worker ownership and completion; it cannot be indirectly substituted by other resource states such as "Close has returned" or "BoltDB is closed".
- This is an internal structural contract and does not change Rain’s exported public API.

## Behavior that must stay unchanged

### Established baseline behaviors to preserve

1. **Successful Session Initialization and Management**:
   - Given a valid `Config` and available external resources, `NewSession` MUST return a usable `*Session` and a `nil` error.
   - When `Config.RPCEnabled` is `true` and `Config.RPCShutdownTimeout <= 0`, `NewSession` MUST return an explicit non-nil error immediately, without opening database storage or silently falling back to a default timeout.
   - When `Config.RPCEnabled` is `false`, `Config.RPCShutdownTimeout` is ignored and non-positive values do not prevent session creation.
   - Managing torrents via `AddTorrent`, `AddURI`, `RemoveTorrent`, `ListTorrents`, `GetTorrent`, `StartAll`, `StopAll`, and querying `Stats` MUST retain established functional semantics.
   - Existing on-disk BoltDB resume data records MUST remain compatible across session restarts without schema migration or corruption.
   - Restored torrents loaded from existing persistent data whose records indicate a previously started state MUST resume activity when `ResumeOnStartup` is enabled, while torrents previously stopped MUST remain stopped.
   - `NewSession` MUST NOT block waiting for resumed torrents to finish asynchronous network startup or data downloads before returning.
   - Corrupted or unreadable torrent records encountered in persistent storage during startup MUST be skipped, allowing valid torrents to continue loading.

2. **Asynchronous Torrent Stop Semantics**:
   - Calling `Torrent.Stop()` MUST remain an asynchronous request: it initiates stopping procedures and returns without waiting for remote network tracker responses to complete.
   - Accepting a stop request MUST NOT be treated as completed shutdown of the torrent or the enclosing session.
   - Calling `Session.Close()` while active data transfer is ongoing MUST halt session-managed torrent work and close the session within the applicable shutdown bound without leaking goroutines.

### Lifecycle guarantees established by this task

1. **Sequential `Session.Close()` idempotency**:
   - Calling `Session.Close()` multiple times sequentially on the same `Session` instance MUST NOT panic.
   - Each invocation MUST complete within the applicable shutdown bound defined in the Shutdown Timing Contract.
   - When no cleanup error occurs on initial shutdown, all sequential invocations of `Session.Close()` MUST return `nil`.

2. **Concurrent `Session.Close()` safety**:
   - Calling `Session.Close()` concurrently from multiple goroutines MUST be thread-safe without panicking or data races.
   - All concurrent callers MUST complete within the applicable shutdown bound defined in the Shutdown Timing Contract.
   - When no cleanup error occurs on shutdown, all concurrent callers MUST return `nil`.

3. **Active torrent work and file-handle release**:
   - Calling `Session.Close()` while torrents are actively allocating disk storage or performing background operations MUST halt allocation and disk work within the applicable shutdown bound.
   - A successful `Session.Close()` invocation (returning `nil`) MUST NEVER return while active torrent operations or session-owned background workers remain active, and MUST close all open file handles before returning.
   - If active torrent teardown or background workers cannot complete before the shutdown deadline, behavior is governed by the deadline-exceeded postcondition.
   - No file descriptors, background worker goroutines, or idle network connections (such as webseed HTTP client connections) may remain open or active after a successful `Session.Close()` returns.

4. **RPC rejection after shutdown begins**:
   - When `Session.Close()` begins, the session MUST stop accepting new RPC requests before executing any potentially blocking teardown phases.
   - Any new session-owned request initiated after shutdown begins MUST be rejected immediately with a terminal non-success outcome (such as connection refused or HTTP error status) before `Session.Close()` returns.

5. **Active RPC handler termination and listener cleanup**:
   - Active session-owned RPC handlers whose execution exceeds `Config.RPCShutdownTimeout` MUST be interrupted as part of the bounded shutdown operation.
   - A successful `Session.Close()` invocation (returning `nil`) MUST NEVER return while an active server-side RPC handler is still executing.
   - If an active server-side handler cannot terminate before the declared RPC shutdown deadline, `Session.Close()` MUST return an explicit non-nil shutdown error. In this error path, all session-owned RPC listeners and client connections MUST still be severed and closed, and the listening port released for immediate rebinding.
   - Client-side context cancellation, client cleanup, or caller-side closing of request streams MUST NOT be required for server-side handlers to terminate.
   - Interrupted handlers MUST receive a terminal non-success outcome.
   - Reopening a session immediately on the same host and port after `Session.Close()` returns MUST succeed without address collisions or residual port retention.

6. **Teardown deadline enforcement and deferred cleanup**:
   - When session teardown exceeds the applicable overall shutdown bound (5 seconds without RPC; `Config.RPCShutdownTimeout + 5 seconds` with RPC and active torrents), `Session.Close()` MUST return an explicit non-nil error within the deadline.
   - BoltDB lock and unfinished resources MUST NOT be released while unfinished routines may still access them. Once outstanding work finishes, deferred cleanup MUST release the database lock.
   - In sessions with active torrent workloads and RPC enabled, the entire `Session.Close()` invocation completes within `Config.RPCShutdownTimeout + 5 seconds`, RPC rejects new requests while torrents stop, and sequential `Close()` calls are idempotent.
   - Subsequent calls to `Session.Close()` report the cached error.

## Test and File Restrictions

- The evaluation framework supplies all regression tests through `test.patch`.
- The candidate patch MUST modify production implementation files only.
- The candidate MUST NOT add, modify, rename, delete, or skip any `*_test.go` file. Any candidate submission that adds, modifies, renames, or deletes any `*_test.go` file will be flagged as cheating (`cheat_test_file_submitted` or `cheat_original_test_modified`) and rejected with a score of 0.
- The candidate may run tests locally during development, but no `*_test.go` files may be included in the submitted patch.
- No framework or evaluator files (such as files under `tests/`, `grader.py`, `test.sh`, `hardgate.py`, `p2p_select.txt`, or `test.patch`) may be added or modified by the candidate.

## constraints

1. MUST preserve existing exported names, function and method signatures, exported configuration fields, and public API semantics, except for the lifecycle guarantees explicitly established by this task.
2. Scope is limited to Session lifecycle shutdown coordination, resource ownership release, and supporting implementation changes.
3. MUST NOT introduce external third-party dependencies beyond those already declared in `go.mod`.
4. MUST NOT alter the on-disk storage format, serialization structure, or semantic meaning of saved resume data.
5. MUST NOT make `Torrent.Stop()` a synchronous blocking call that waits for remote tracker responses.
6. MUST NOT cause unhandled panics or data races on repeated sequential or concurrent invocations of `Session.Close()`. Each invocation MUST complete within the bounds defined in the Shutdown Timing Contract.
7. Pre-existing repository test files MUST remain intact and immutable without modification, deletion, renaming, or weakening of existing assertions or fixtures.
8. All Go packages and tests MUST compile cleanly and satisfy repository-wide build (`go build ./...`) and vet (`go vet ./...`) checks.

IMPORTANT: Create a new branch from the task's base commit `697380ffec04290679230d8d04636eb41c99e0a8` and commit all task changes, including new files, when you are done.
