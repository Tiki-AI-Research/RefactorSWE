# Share dict-hook generation machinery

The attrs/dataclass and TypedDict factories each assemble and compile dict hooks. They repeat source assembly, internal bindings, generated naming, traceback-source registration, compilation, override attachment, and detailed-validation wrapping. Consolidate those common responsibilities into one shared generator within `gen`, used by both families' structure and unstructure factories.

Share the machinery without unifying the families' semantics. Attrs aliases, `init=False`, defaults, attribute converters, and omit-if-default behavior remain distinct from TypedDict required/not-required fields and extra-key handling. Choose the shared generator's internal organization and representation freely.

## Factory compatibility

Keep existing imports, public names, signatures, defaults, and return shapes. In particular, `cattrs.gen` retains:

```python
make_dict_unstructure_fn_from_attrs(attrs, cl, converter, typevar_map={}, _cattrs_omit_if_default=False, _cattrs_use_linecache=True, _cattrs_use_alias="from_converter", _cattrs_include_init_false=False, **kwargs)
make_dict_structure_fn_from_attrs(attrs, cl, converter, typevar_map={}, _cattrs_forbid_extra_keys="from_converter", _cattrs_use_linecache=True, _cattrs_prefer_attrib_converters="from_converter", _cattrs_detailed_validation="from_converter", _cattrs_use_alias="from_converter", _cattrs_include_init_false=False, **kwargs)
```

Its class/dataclass `make_dict_unstructure_fn` and `make_dict_structure_fn` also keep their current signatures, supported generation flags, and `**kwargs` overrides. `cattrs.gen.typeddicts` retains:

```python
make_dict_unstructure_fn(cl, converter, _cattrs_use_linecache=True, **kwargs)
make_dict_structure_fn(cl, converter, _cattrs_forbid_extra_keys="from_converter", _cattrs_use_linecache=True, _cattrs_detailed_validation="from_converter", **kwargs)
```

Keep `AttributeOverride` and `override(...)` unchanged. Every factory retains `_cattrs_use_linecache`. Existing `"from_converter"` resolution for alias use, extra-key forbidding, attribute-converter preference, and detailed validation uses the same converter settings and fallback behavior. Generated hooks expose the effective `overrides` mapping, including the information needed for subsequent regeneration.

## Hook behavior and debugging

Attrs/dataclass hooks retain results for renaming, aliases, omitted defaults, `init=False` inclusion, defaults, converters, and `typing.Annotated` overrides. TypedDict hooks keep their separate boundaries:

- Unstructuring returns the original object where no transformation currently needs a copy. Where it returns a transformed copy, it still creates a new dict and leaves the caller's mapping unchanged.
- Required keys remain in valid inputs unless an override omits them. Renaming is preserved, and absent not-required keys are not introduced.
- Structuring tolerates absent not-required keys. Forbidden extra keys produce the same `ForbiddenExtraKeysError` and unknown-key set, including containment in `ClassValidationError` under detailed validation.

Detailed validation preserves `ClassValidationError`, aggregation of field failures, and `AttributeValidationNote` annotations with unchanged text. Non-mapping TypedDict inputs keep their existing mapping-type error and wrapping. Recursive and self-referential class graphs continue producing working hooks with the same results and no unbounded recursion.

With `_cattrs_use_linecache=True`, retain generated-source registration, filename collision handling, deduplication, and traceback source lookup. With it false, generation adds no linecache entry. Exact generated source text, generated-function argument names, and shared-state representation may change within these observable debugging contracts.

## Completion and scope

Both families must actually use shared generation machinery while retaining every supported flag, type-specific capability, result, exception type and text, debugging behavior, and performance characteristic. Consolidate only genuinely common work; identical handling of attrs and TypedDict fields is not a goal.

Use existing support facilities without adding or widening runtime dependencies. Keep changes to necessary production generation code, directly related tests, and supporting adjustments. Leave unrelated refactors, formatting, and feature work out.

Work on a new branch from `main` and commit the completed changes.
