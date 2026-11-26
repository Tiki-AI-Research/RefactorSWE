# Split BitComet protocol implementations

Replace BitComet's per-operation integer-version branches with separate JSON-API and legacy-HTML clients selected by detection. Each owns its transport/decoding and unsupported-operation behavior; no version comparison remains in operations. Remove the public version code without an equivalent public discriminator: callers outside this family should not need to know the protocol. Private types, helpers, builders, and response shapes are yours to choose.

Keep the dispatch client interface's names, parameters, and results for type/config path, URL setup, login, torrent/peer listing, block/shadow-ban submission, and detection. Shared torrent/peer models and IP-keyed block inputs with hash/port stay unchanged. Both implementations report BitComet and configured BitComet still selects this family.

Detection first probes `/api_v2/task_list/get`, accepting 200 or 401 as JSON. Only on a miss, probe `/panel/`, accepting 401 with WWW-Authenticate containing BitComet as legacy. Neither match means failed probing. When configuration explicitly selects BitComet but probing fails, outer detection still reports success with an instance whose unsupported operations fail, without panic or accidental JSON behavior.

JSON listing reads movie_list from `/api_v2/task_list/get?state_group=ACTIVE`, keeps only BT torrents, and uses task ids as hashes. Peers come from `/api/task/peers/get?task_id=<id>&groups=peers_connected` and peers_connected, converting 0–100 progress to 0–1. Ban POSTs to `/api/task/peers/ban_ip` retain task_id, ban_time=`ban_ip_forever`, and ip_list, grouping addresses per hash and succeeding only if every ban is accepted. JSON login still succeeds on panel status 200.

Legacy login likewise accepts panel 200 and reads torrents/peers from their existing task/detail HTML tables. Preserve numeric task-id hashes and placeholder tracker/leech values. URL setup, blocking, and shadow banning continue reporting failure and must issue no JSON-API requests. HTML helpers retain positive results and malformed-input negative sentinels, including empty results for nonremote peers.

Completion requires detection-selected implementations and removed type-code dispatch, supported by necessary tests, including adaptations of version-code assertions. Do not change probe acceptance, unsupported failures, payloads, or caller capabilities. Add no dependencies, configuration keys, logging changes, or public API beyond the split. Limit edits to necessary production code, tests, and direct support; leave other clients, transport, proxy, and configuration behavior untouched.

Work in a new branch from `main` and commit the completed changes.
