# What is the current behavior?

The environment, world, and path parameter modules each maintain a duplicate module-level proxy implementation, including instance storage, a current-instance alias, a binding entry point, and attribute and subscript routing.

Consumers, including objects, worlds, sensors, and plotting and keyboard helpers, also repeat parameter-access logic: prefer the owning environment's or world's parameter instance, then fall back to the global module through a deferred import. The plotting helper's environment-parameter accessor is an exception: it reads the global binding directly.

This duplication spreads the same routing responsibility across multiple locations, leaves fallback rules implicit and prone to divergence, and makes it harder to determine which environment a parameter read resolves to.

# What is the new behavior?

Extract the duplicated module-level proxy logic into one shared parameter-store abstraction. Each parameter module retains only its own dataclass and field definitions while continuing to expose its existing public entry points.

Replace consumers' duplicated owner-first, global-fallback accessor implementations with one shared resolution path so that parameter lookup rules are maintained in one place. Leave the plotting helper's environment-parameter lookup unchanged.

This refactor changes only internal organization. Preserve all public entry points and observable behavior of the parameter modules and their consumers so that existing callers need no changes. Do not redesign parameter semantics, widen the public API, or add a new configuration surface.

# Public contract to preserve

1. **Module exports and dataclasses**
   - Keep `env_param`, `world_param`, and `path_param` importable from the configuration package.
   - Preserve their respective public dataclasses: `EnvParam`, `WorldParam`, and `PathManager`.
   - Preserve existing field names, value types, defaults, documented meanings, and dataclass semantics.

2. **Binding entry points and module state**
   - Each parameter module must retain a module-level `bind(instance)` entry point that accepts an instance of that module's dataclass and returns `None`.
   - The module-level `_instances` list and `_current` alias must remain readable and directly assignable.

3. **Attribute and indexing entry points**
   - `env_param` and `world_param` must retain module-level parameter attribute reads and writes and module subscripting.
   - `path_param` must retain callable module-level `__getitem__` and `__setitem__` functions and the `path_manager` attribute proxy.

4. **Environment and consumer interfaces**
   - Environments must continue to expose their own world, environment, and path parameter instances.
   - Objects, worlds, sensors, keyboard helpers, and plotting helpers must retain their existing parameter accessors.

# Behavior and implementation boundaries to preserve

1. **Attribute routing**
   - Parameter attribute reads and writes on the environment and world modules must resolve against the most recently bound instance.
   - Reads and writes through `path_param.path_manager` must resolve against the most recently bound `PathManager`.
   - Before any explicit binding, module-level parameter attribute access must use the default instance at index 0.
   - Assignments to non-parameter names on the environment and world modules, including their bookkeeping attributes, must remain ordinary module assignments and must not be forwarded to the bound instance.
   - Reads of names already present on these modules must use normal module lookup. Reads of names absent from the module must retain the existing fallback to the currently bound instance, including names that are not dataclass fields.

2. **Binding updates**
   - Calling `bind` must replace the instance at index 0 when storage is non-empty, or append the supplied instance at index 0 when storage is empty.
   - Binding must update the current-instance alias and make the supplied instance the target of subsequent module-level parameter attribute access.

3. **Indexed reads**
   - Subscript reads on the environment and world modules and the path module's `__getitem__` function must return the stored instance at the requested index under existing list-indexing semantics.
   - Negative indices must continue to resolve from the end; a read must not be rejected merely because its index is negative.
   - Do not add or remove existing negative-index guards on reads or change existing out-of-range behavior.

4. **Indexed assignment**
   - Subscript assignment on the environment and world modules and the path module's `__setitem__` function must store the supplied instance at the specified non-negative index.
   - Assigning beyond the current storage range must extend storage with default dataclass instances up to the target index.
   - Assigning index 0 must update the current-instance alias.
   - Assigning a negative index must raise `IndexError`, preserving each module's existing error message.

5. **Consumer resolution**
   - Objects, worlds, sensors, and keyboard helpers must return the owning environment's or world's parameter instance when an owner exists; otherwise, they must fall back to the current global binding.
   - Global fallback must reflect the current binding without copying parameters or pinning an earlier instance.
   - The plotting helper must resolve world parameters through its world's own parameter instance when present, and otherwise through the current global binding.
   - The plotting helper must always read environment parameters from the global binding; this accessor must not become owner-first.

6. **Multi-environment isolation**
   - Different environments created in the same process must hold independent world, environment, and path parameter instances.
   - A parameter mutation through one environment must not be observable through another environment's own parameter instances or its objects and sensors.

7. **Internal implementation boundaries**
   - Internal helper types and names, how the shared store is installed, where consumers obtain their fallback, and file placement are free to change.
   - These changes must not alter the public contract or runtime behavior specified above.

# Constraints

1. Do not rename, remove, or narrow any existing public capability. Preserve the public names, signatures, return shapes, field sets, and error behavior specified above.
2. Keep parameter routing, indexing, multi-environment isolation, and simulation semantics unchanged. Do not fix, alter, or extend unrelated behavior while extracting the shared abstraction.
3. Do not add runtime dependencies or change packaging metadata. The shared abstraction must rely only on existing project dependencies.
4. Do not introduce new required arguments, flags, or configuration keys, or change existing defaults, public error types, or error messages.
5. Limit changes to the three parameter modules, the duplicated consumer fallback accessors described above, and the minimal supporting adjustments needed to keep the contract verifiable, including existing tests and documentation. Leave unrelated code untouched.

**IMPORTANT: Please work on this in a new branch from main and commit everything when you are done.**
