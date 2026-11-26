## Background
The struct data source mixes reflected field access with collecting rules and translation metadata from tags. It also owns static template construction, sharing and per-instance replay. Several traversals independently inspect struct fields for metadata, classification and value-dependent collection. They have different visitation policies, so consolidating their shared field discovery must preserve those differences. Separate rule collection from source binding and field access while preserving public capabilities, validation results, template concurrency and pooled reuse.

## Goal
- Move struct-tag rule collection (validation rules, filter rules, optionals, default values, field names, label and output-name maps, custom messages) out of the data source type into a separate rule-engine-side collection component, leaving the data source responsible only for source binding, field value access, optional interface dispatch and marking source updates.
- Consolidate duplicated field discovery into one authoritative struct-type scan. Its results must support metadata, static/dynamic classification and value-dependent rule collection with their existing visitation policies; value traversal may still expand pointers and container elements without independently enumerating struct-type fields.
- Keep the static/dynamic distinction and its consequences: static types may reuse one immutable per-type template, dynamic types keep per-value collection.
- Keep the change internal to the module: callers must observe no API or behavior difference.

## Public contract to preserve
- `StructData` remains the exported struct data source returned by `FromStruct(s any) (*StructData, error)` and must keep implementing `DataFace` with `Type() uint8`, `Src() any`, `Get(key string) (any, bool)`, `TryGet(key string) (any, bool, bool)`, `Set(field string, val any) (any, error)`, `Create(err ...error) *Validation` and `Validation(err ...error) *Validation`.
- Struct entry points keep their signatures and semantics: `Struct(s any, scene ...string) *Validation`, `New(data any, scene ...string) *Validation`, `NewValidation(data DataFace, scene ...string) *Validation`, plus the data source create and validation methods; a non-nil error passed to creation must still be reported by the returned validation.
- Optional source interfaces keep working: `ConfigValidation(v *Validation)`, `Translates() map[string]string` and `Messages() map[string]string`.
- Tag configuration stays driven by the exported `GlobalOption` fields `ValidateTag`, `FilterTag`, `FieldTag`, `LabelTag`, `MessageTag`, `ValidatePrivateFields` and `CheckSubOnParentMarked`, set through `Config(...)` and reverted by `ResetOption()`. Configuration changes affecting collection must invalidate relevant metadata and templates, including field visibility and nested cascade settings; `ResetTypeCache()` must keep working.
- `Factory` keeps `NewFactory() *Factory`, `Factory.Struct(s any, scene ...string) *Validation`, `Validation.Release()` and `Validation.ValidateR()` semantics, including equivalence with the non-pooled path.
- Public errors keep their meaning: `FromStruct` returns `ErrInvalidData` for nil, non-struct and `time.Time` input, and `Set` on an unknown field keeps returning `ErrNoField`.
- Unexported helpers, caches, template representations and the internal division of work may change freely; no new public API is required by this task.

## Behavior that must stay unchanged
- Rule collection MUST produce the same rules, filter rules, optionals, default values, field-name entries, label translations, output-name entries and custom messages for the same input and configuration. Declaration and indexed-element order MUST remain unchanged where currently stable. Map expansion MUST preserve existing key and value semantics; map-key iteration has no guaranteed order.
- Static/dynamic classification MUST stay identical: pointer-to-struct (other than `time.Time`), slice/array-of-struct and map-of-struct make a type dynamic; `time.Time` remains a leaf. Type metadata MUST preserve its existing struct-pointer traversal; value-dependent collection MUST preserve its existing pointer, container and nested cascade behavior. Self- or mutually-recursive types MUST terminate as before.
- Nil pointers, empty containers and nil container elements MUST retain their existing outcomes, including panics during collection; this refactor MUST NOT introduce new recovery or silently skip inputs that currently panic.
- Unexported fields MUST be skipped unless `ValidatePrivateFields` is enabled, in which case they MUST be collected exactly as before, and `CheckSubOnParentMarked` semantics MUST NOT change.
- Static types MUST build their template at most once per type and effective collection configuration, MUST be safe under concurrent validation, and MUST keep per-instance isolation: only builtin-validator rules whose arguments were successfully converted during template construction may be shared read-only and MUST NOT be mutated at runtime; rules using custom, unknown or unsuccessfully converted validators, and all filter rules, MUST remain per-instance copies.
- Struct validation MUST still mark the source for update, and default-value or filter writes MUST remain observable through the data source getters afterwards.
- Pooled reuse MUST NOT leak rules, field values, translations, errors or scene data between validations, including when one pool serves different struct types.
- A non-nil error passed at creation MUST still be reported as the validation's failure, with unchanged error keys and messages.

## constraints
1. Do not rename, remove or shrink exported APIs, signatures, parameters, return types, flags or error values.
2. Do not change observable validation outcomes, errors, stable rule ordering, translation output or static/dynamic classification; consolidated traversal must preserve each existing visitation policy, including cycles and unexported fields.
3. Do not add third-party dependencies or new public configuration flags; reuse what the module already provides.
4. Do not alter unrelated behavior or code: map, form and request binding, validators, message rendering, result binding, scenes and the default lifecycle must stay as they are, with no unrelated reformatting or cleanup.
5. Limit changes to the production code required to separate rule collection from the data source and remove the duplicated traversal, plus only the tests and supporting adjustments needed to verify those behaviors.

