# Refactor PolinePicker to Separate Presentation and Interaction

## Problem background

`PolinePicker` currently combines custom-element lifecycle coordination, its public API, SVG presentation, palette synchronization, and pointer interaction in one implementation. Presentation and interaction maintain different kinds of state and should be independently owned.

Refactor the picker so that `PolinePicker` coordinates separate presentation and pointer-interaction responsibilities. Its public API and externally observable behavior must remain compatible with the base commit, except where this task explicitly corrects that behavior.

## Goal

`PolinePicker` remains the public custom-element facade and lifecycle coordinator. Presentation and pointer interaction must each be owned by a distinct internal collaborator, with the facade delegating those responsibilities instead of retaining their complete implementations.

The presentation collaborator owns SVG construction, visual synchronization, and presentation styling. The interaction collaborator owns pointer input, hit testing, gesture state, anchor movement, and rotary adjustment. The facade owns the public API and coordinates lifecycle, presentation, interaction, and palette state.

Separation concerns responsibility ownership rather than syntax or file layout. The collaborators may be implemented as classes, objects, or closure-based units; may share a source file; and may use any suitable names, constructors, factories, and communication mechanisms. Each collaborator must own substantive state and implementation for its assigned responsibility and must be invoked by the facade. Empty collaborators, a facade that retains the complete implementation, or a single replacement unit combining presentation and interaction do not satisfy the task.

The refactor must also make pointer interaction robust across gesture boundaries, palette replacement, component lifecycle changes, synchronous event re-entry, and repeated connection. Effective palette changes must remain distinguishable from pointer activity that leaves palette data unchanged. The detailed observable contracts are defined below.

Explicit corrections and behavioral rules in this task take precedence where they differ from the base commit. In every other respect, the externally observable behavior of the base commit is the compatibility oracle and must not regress.

## Capabilities and API contract

The `./picker` entry point must continue to export `PolinePicker`, `Poline`, and `positionFunctions`. `<poline-picker>` remains a registered custom element whose implementation extends `HTMLElement`.

Keep the existing public methods and signatures:

- `setPoline(poline: Poline): void` attaches the supplied palette and refreshes its presentation, including its lightness background. It does not dispatch `poline-change`.
- `setAllowAddPoints(allow: boolean): void` changes point-addition behavior immediately for the current connection. It does not dispatch `poline-change`.
- `updateSVG(): void` refreshes the connected presentation for the attached palette. It does not dispatch `poline-change`.
- `addPointAtPosition(x: number, y: number): ColorPoint | null` converts presentation coordinates into palette coordinates, adds an anchor, refreshes the presentation, dispatches `poline-change`, and returns the new point. Without an attached palette, it returns `null` without throwing.

For `addPointAtPosition(x, y)`, `x` and `y` are local CSS-pixel coordinates in the current SVG presentation's content box, measured from its top-left corner. They are not viewport, page, host-element, or already-normalized palette coordinates. Let `width` and `height` be the current SVG presentation's effective content-box width and height. The conversion is `normalizedX = x / width` and `normalizedY = y / height`, and the new palette position is `[normalizedX, normalizedY, normalizedY]`. The implementation may use its established internal presentation extent when a rendered width or height is unavailable, consistent with the base behavior. The picker does not independently clamp `x` or `y` to the presentation bounds before this conversion. Coordinates outside the content box may therefore normalize outside `[0, 1]`; the resulting position is then handled by the attached `Poline` instance according to its existing point-addition and clamping behavior.

Do not add a public `allowAddPoints` property.

`interactive` and `allow-add-points` retain normal HTML boolean-attribute semantics. Both are read on every connection. `setAllowAddPoints()` controls the current connection, while a later connection starts from the current `allow-add-points` attribute.

Keep support for these styling hooks:

- `--poline-picker-line-color`
- `--poline-picker-bg-color`
- `--poline-picker-wheel-saturation`
- `--poline-picker-wheel-lightness`
- `--poline-picker-line-width`
- `--poline-picker-ring-width`
- `.ring-hover`
- `.ring-adjusting`

`poline-change` remains a synchronous `CustomEvent` with detail `{ poline: Poline }`. Its `bubbles`, `cancelable`, and `composed` flags are all `false`.

## Behavioral rules

The rendered picker must remain synchronized with the attached palette. Its polyline uses every flattened sample point in the existing order and projected position; any geometrically equivalent valid SVG coordinate serialization is acceptable. Anchors, intermediate samples, saturation controls, radii, and HSL-derived colors retain their existing visual semantics.

A refresh reconciles the complete presentation. Visual elements that no longer correspond to current anchors or samples must not remain after the palette is reduced. Existing CSS custom properties continue to control their corresponding presentation styles.

The lightness gradient belongs to the shadow presentation. An inverted palette uses `--maxL: #000` and `--minL: #fff`; a non-inverted palette uses `--maxL: #fff` and `--minL: #000`. Attaching a palette and refreshing a connected presentation both synchronize these values.

`updateSVG()` is a safe no-op before the first connection, while disconnected, or without an attached palette.

Without `interactive`, pointer input cannot drag an anchor, adjust saturation, or add a point. Without an attached palette, pointer input is ignored without throwing, changing interaction state, or dispatching `poline-change`. Empty presentation space adds an anchor only while point addition is enabled, and `setAllowAddPoints()` takes effect without requiring reconnection.

Fine pointers retain visible saturation controls, hover feedback, and rotary adjustment. Coarse pointers keep saturation controls hidden, do not perform rotary adjustment, and drag anchors instead.

A `pointerdown` event on the presentation surface is handled by the interaction layer when the picker is interactive:

- On an interactive picker (`interactive` attribute present), any `pointerdown` delivered to the interactive presentation surface is handled and must stop propagation (`stopPropagation()`). This includes clicking an anchor core (initiating anchor drag and acquiring pointer capture), clicking a saturation ring (initiating rotary adjustment and acquiring capture on fine pointers), clicking empty background presentation area (regardless of whether `allow-add-points` is enabled or disabled), secondary pointer input while another pointer already owns an active gesture (the secondary pointer does not preempt the active gesture and does not acquire capture), and pointer input when no `Poline` palette is attached (handled safely without throwing, modifying state, or capturing the pointer).
- When `interactive` is absent, pointer input must not enter interaction processing: `pointerdown` is not handled, does not stop propagation, and continues to bubble up to ancestor elements. The picker must not capture the pointer, must not modify palette data or classes, and must not dispatch `poline-change`.
- Reconnection updates interaction bindings to match the current `interactive` attribute. If `interactive` is removed before reconnection, stale listeners must not remain, and `pointerdown` must bubble to ancestor elements without interception.

An accepted anchor drag or rotary adjustment belongs exclusively to its initiating pointer and captures that pointer while the gesture remains valid. Other pointers cannot update or terminate it. Ending or invalidating the gesture releases any remaining capture and clears gesture-owned interaction and visual state.

Dragging an anchor updates its position and derived color without changing its saturation. Rotary adjustment remains continuous across the angular wraparound. One full revolution spans the saturation range normally; with `Shift`, the same range takes 2.5 revolutions. Reversing direction at either saturation boundary responds immediately, and changing the Shift state during a gesture affects later movement without introducing a jump or reversing direction.

Dispatch `poline-change` only when palette data actually changes. Effective anchor dragging, rotary adjustment, and programmatic point addition dispatch it with the current `Poline` instance. Configuration, presentation refresh, hover-only activity, zero displacement, zero angular movement, and movement whose effective result is unchanged do not dispatch it.

Palette replacement, active-pointer cancellation or capture loss, disconnection, and synchronous re-entry that performs an invalidating operation as defined by the public-method rules below invalidate the affected gesture. Synchronous re-entry alone does not necessarily invalidate a gesture; the method-specific rules below take precedence. Once invalidated, later input from that gesture cannot mutate a previous or current palette, restore transient state or capture, or emit another change event. Palette replacement itself emits no change event. Notifications concerning another pointer do not disturb a still-valid gesture.

Calling public methods affects active gestures, pointer capture, and interaction state according to these exact boundaries:

- `setPoline(poline: Poline)`: Calling `setPoline()` (whether with a new `Poline` instance or the currently attached instance) is an explicit interaction boundary. Any active gesture (anchor drag or rotary adjustment) is immediately cancelled, pointer capture is released, `.ring-hover` and `.ring-adjusting` are cleared, and subsequent events from the old pointer are invalidated (stale) and cannot resume the gesture or modify palette data. The call itself does not emit `poline-change`. Calling `setPoline()` synchronously from within a `poline-change` listener cancels the emitting gesture and prevents the outer operation from restoring state after the listener returns. Afterward, the picker is ready for a fresh gesture.
- `setAllowAddPoints(allow: boolean)`: Calling `setAllowAddPoints()` only updates the policy for subsequent clicks on empty presentation space. It does not cancel an active anchor drag or rotary adjustment, does not release pointer capture, does not clear `.ring-hover` or `.ring-adjusting`, does not invalidate gesture events, and does not dispatch `poline-change`. An ongoing gesture continues without interruption, retaining capture and completing normally. Calling `setAllowAddPoints()` inside a synchronous `poline-change` listener does not cancel or invalidate the active gesture.
- `updateSVG()`: An external call to `updateSVG()` refreshes the visual presentation for the attached palette. It does not cancel an active anchor drag or rotary adjustment, does not release pointer capture, does not clear `.ring-hover` or `.ring-adjusting`, does not invalidate gesture events, and does not dispatch `poline-change`. An ongoing gesture retains capture and continues normally. However, when called re-entrantly from within a synchronous `poline-change` listener, `updateSVG()` enforces synchronous re-entrancy safety: it invalidates the emitting active gesture, releases pointer capture, clears `.ring-hover` and `.ring-adjusting`, and prevents the outer operation from restoring stale gesture state after the listener returns.
- `addPointAtPosition(x: number, y: number)`: In a normal external call, `addPointAtPosition()` adds an anchor point at converted presentation coordinates, refreshes the presentation, dispatches a synchronous `poline-change` event for the added point, and returns the new `ColorPoint` (or `null` without throwing if no palette is attached). Calling `addPointAtPosition()` during an ongoing anchor drag or rotary gesture does not cancel that gesture, does not release capture, and does not clear `.ring-hover` or `.ring-adjusting`; the existing gesture retains capture and subsequent pointer movements continue to update the dragged anchor or rotary adjustment. However, when called re-entrantly from within a synchronous `poline-change` listener, the re-entrant presentation update invalidates the emitting gesture, releasing pointer capture and clearing transient classes so that the outer operation cannot overwrite state after the listener returns.

Connection and presentation changes must not leave additional effective interaction bindings behind. Input from presentation state that is no longer current cannot acquire gesture ownership, affect palette data or host interaction state, emit changes, or interfere with the current interaction. A current connection remains usable for a fresh gesture.

A presentation surface or interaction binding is retired when it belonged to an earlier connection or presentation generation and is no longer the current effective interaction surface or binding. No public generation identifier, counter, property, or particular implementation mechanism is required. If a later connection reuses the same SVG DOM node, bindings from the earlier generation are still retired while the single current binding remains effective. Observable retirement means that events delivered through a retired surface or retired binding cannot acquire pointer capture, acquire or terminate gesture ownership, mutate palette data, dispatch `poline-change`, change transient interaction classes, release capture owned by the current gesture, or otherwise interfere with the current presentation.

Pointer identifiers may be reused after an earlier gesture or presentation has been invalidated. Reusing an identifier does not make events from a retired presentation part of the new gesture. Events delivered through a retired presentation cannot terminate, mutate, release capture from, or alter the visual state of a gesture owned by the current presentation, even when both gestures use the same pointer identifier.

Picker instances remain independent in picker-owned presentation state, active gestures, pointer ownership, interaction bindings, transient classes, and event dispatch. When different Poline instances are attached, palette data is also isolated between pickers.

Instance isolation applies to picker-owned presentation state, active gestures, pointer ownership, interaction bindings, transient classes, and event dispatch. If the caller explicitly supplies the same Poline instance to multiple pickers, each picker retains that shared reference; the palette is not cloned or rejected. A palette mutation performed through one picker is therefore visible through the shared Poline object, but it does not automatically refresh another picker's presentation or cause that picker to dispatch poline-change. The other picker reflects the shared palette data after its own presentation refresh. Gesture state, pointer capture, transient classes, presentation state, and event dispatch remain isolated between the picker instances.

## Constraints and prohibited changes

1. Presentation and pointer interaction must be owned by distinct internal collaborators. A collaborator may be implemented as a class, object, or closure-based unit. `PolinePicker` must not retain their complete implementations.
2. Presentation and interaction must not be recombined into one replacement collaborator. The collaborators may be declared in the same source file.
3. Do not remove, rename, reduce, or replace existing public capabilities.
4. Do not add runtime dependencies, global state, or mutable interaction state shared by picker instances.
5. Limit changes to the picker's production source and any new supporting tests needed for the refactor.
6. Do not modify existing library tests, evaluation infrastructure, package or build configuration, or generated distribution files.
7. No particular collaborator syntax, name, source-file name, file layout, construction pattern, or communication pattern is required beyond the stated responsibility boundaries.

IMPORTANT: Create a new branch from the task's base commit `c0bf44b06d549eb7bd5ecc1ac84cd3c58eb296cc` and commit all task changes, including new files, when you are done.