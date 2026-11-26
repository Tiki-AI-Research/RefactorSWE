## Background
The API service currently selects which provider configuration model to build by comparing the provider's name string against a fixed chain of literals, and it re-derives region and AMI defaults for two specific providers when those values are missing at the top level of the configuration. Provider identity, model construction, and default-value normalization are therefore entangled in one central branch chain: provider-specific policy is expressed through incidental name comparisons and duplicated across branches instead of being owned by the provider types that already exist. The non-essential coupling to remove is this name-keyed dispatch and its repeated normalization; the capabilities that must survive are the construction results for every currently supported provider, the existing listing and retrieval payloads, secret exclusion, and unchanged error behavior.

## Goal
- Move each provider's construction and configuration-normalization responsibility onto the provider type itself, so adding or adjusting a provider does not require editing a shared chain of name comparisons.
- Eliminate the duplicated region/AMI default-derivation logic by letting each provider type derive its own defaults from the configuration it receives.
- Keep unrecognized or unmodeled provider names working through the existing generic fallback instead of failing.
- Preserve the observable behavior of the provider endpoints and the public model surface exactly.

## Public contract to preserve
- The provider-model factory stays available at its current public name and location in the API application module, callable as `get_provider_model(provider_name: str, provider_config: dict)`, returning a provider model instance from the existing hierarchy; it must remain the call path used by the provider listing route so existing callers and overrides of that name keep working.
- The provider model types `BaseProvider`, `DigitalOceanProvider`, `AWSProvider`, `GCPProvider`, `HetznerProvider`, plus the instance and scaling models, remain importable from their current public location with unchanged field names and validation expectations (for example: digitalocean region required, GCP zone/image_project/image_family required, scaling minimum/maximum bounds, AWS spot flag).
- `GET /providers` returns HTTP 200 with a payload containing metadata and a providers mapping from every configured provider name to that provider's model, with secrets excluded.
- `GET /providers/{provider}`, taking the provider name as a path parameter, returns message, metadata, provider (enabled, ips, scaling.min_scaling, scaling.max_scaling, size, region) and instances for known providers.
- Unknown provider names on retrieval return HTTP 404 with detail `Provider '<provider>' not found`.
- Internal module placement, dispatch mechanism, and helper structure are free to change as long as every item above holds.

## Behavior that must stay unchanged
- `get_provider_model("aws", config)` MUST backfill region and ami from the default instance entry when they are absent at the top level and return the AWS model with those values; `get_provider_model("digitalocean", config)` MUST similarly backfill region from the default instance entry.
- `get_provider_model` MUST NOT raise for an unknown or unmodeled provider name; it MUST return the generic base provider model.
- `get_provider_model` MUST accept scaling values provided either as a scaling model instance or as a min_scaling/max_scaling mapping, and MUST expose normalized scaling values on both the provider and each of its instances.
- `GET /providers` MUST include an entry for every configured provider and MUST NOT expose secrets at either the provider top level or the instance level.
- `GET /providers/{provider}` MUST return HTTP 404 with detail exactly `Provider '<provider>' not found` for names that are not configured, and MUST keep the same payload fields for configured providers.
- Constructing a provider model MUST NOT add backfilled keys to the top level of the caller-supplied configuration mapping.

## constraints
1. Do not rename, remove, or reduce any existing public name, model field, endpoint, payload field, status code, or error message.
2. Do not add runtime dependencies, network calls, or external services; the change must stay self-contained within the existing runtime environment.
3. Do not narrow provider coverage: every configured provider must keep working, and unmodeled names must keep falling back to the generic provider model.
4. Do not alter behavior outside provider-model construction and normalization, including authentication, proxy listing, queue processing, and provider lifecycle logic.
5. Limit modifications to the production code, tests, and supporting adjustments strictly necessary for this refactor, leaving unrelated modules, configuration, and documentation untouched.

IMPORTANT: Please work on this in a new branch from main and commit everything when you are done.