# Centralize Lyric Group Relationships

## Goal

The order of lyric groups, the indexes of lyric lines, which lyric group owns each DOM element, and when groups are created or disposed are currently managed separately by the base player, the DOM player, and the lyric group objects. As a result, the same relationships are maintained in multiple places, so changing one part can easily leave another part inconsistent.

Reorganize this code so that one unified internal mechanism handles lyric-group registration, ordering, lookup, and cleanup. Rebuilding lyrics, handling mouse events, updating sizes, hiding and showing groups, and changing DOM positions must all use this same relationship instead of maintaining separate relationships.

This refactor also fixes a measurement-index bug. The baseline records group positions when rebuilding lyrics, then uses those saved positions in size callbacks even after callers change `currentLyricGroups`. Size callbacks must instead use the group's position in the current array. For example, after `[A, B]` is reversed to `[B, A]`, a changed main-element size for A must update layout height at position 1, rather than the baseline's position 0. If A has been removed from the array, its size callback must not write to any layout height slot.

## Completion Criteria

1. Lyric-group registration, ordering, lookup, and cleanup use one unified internal relationship. Rebuilding, events, measurements, hiding/showing, DOM placement, and layout heights must use this relationship and reflect the current contents of `currentLyricGroups`.
2. Existing public APIs, inheritance relationships, protected extension points, lyric data, and processing configuration remain available. Callers can still replace and modify `currentLyricGroups`, and subclasses can continue creating lyric groups through the existing mechanism.
3. Lyric groups are ordered by start time, while preserving the existing construction order for equal start times. Measurement height updates use the group's current position after array replacement, reordering, removal, or re-appending. This corrects the baseline behavior described above; unchanged-size filtering, group size caching, and size-change notifications keep their existing behavior. Rebuilding, background-vocal handling, timeline initialization, playback state, and layout calculations otherwise retain their existing behavior. Changing the array alone does not require rebuilding the timeline or resetting playback state.
4. Main lyric elements and background lyric elements owned by lyric groups must produce the corresponding lyric events when clicked and update their group when their sizes change. Elements that do not belong to a lyric group must not trigger these operations. When a group is hidden and shown again, the original group and lyric lines are retained, the group returns to the correct DOM position, and observation is restored or preserved according to the existing behavior.
5. Lyric-group disposal, timestamp errors, non-finite playback times, event propagation, and lyric-processing configuration must continue to follow the existing behavior without clearing associations that still need to be retained.

## Constraints

1. Existing subclasses and callers must not be required to use a new lyric-group registration mechanism.
2. `currentLyricGroups` remains externally owned and mutable; the internal relationship management must support replacing the array, mutating it in place, reordering it, and appending to it.
3. Apart from the lyric-group relationship refactor and its necessary tests, do not modify unrelated functionality, dependencies, or platform requirements.
4. Add or update focused tests covering the main scenarios affected by the change, including subclasses creating or appending lyric groups directly, layout heights after replacing or reordering `currentLyricGroups`, event and size routing for lyric elements, remounting hidden groups, preserving objects and associations, and observer and DOM cleanup during disposal.

New release-note Markdown files may be added directly under `.nx/version-plans/`. Existing version plans must not be modified or deleted.

Candidate file scope uses a denylist rather than a source-directory allowlist.
Existing upstream tests and fixtures, dependency manifests and lockfiles,
build/test configuration, existing `.nx` metadata and version plans, CI and
repository patch assets, and verifier-owned tests are protected from modification
or deletion. New files at those protected file paths or inside verifier-owned
or CI/patch directories are also forbidden. Other paths are not rejected solely
for being outside the lyric-player directory; the task goals and behavioral,
compilation, path-safety, and anti-tampering checks still apply.
