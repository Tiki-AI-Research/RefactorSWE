# Third-party notices

The [task source table](./PROVENANCE.md#task-sources) records the upstream revision and license for each RefactorSWE task. The source table and the links below point to the upstream licenses and attribution notices. Include the applicable notices when redistributing an individual task, patch, or archive.

## Bundled materials

- **Setup Go.** The reference patch changes the generated `dist/setup/index.js` and `dist/cache-save/index.js` bundles. The upstream dependency records include notices and identify two MIT declarations whose full notices still need verification if their code is redistributed. [Reference patch](./tasks/setup-go-cache-restore-save-04/solution/solution.patch) · [Bundled dependency notices](https://github.com/actions/setup-go/tree/fba3fb4ead8c8e09a06f1d32ae5436e5818eff15/.licenses/npm)
- **Shiv, Waitress, and Stellar SDK.** The upstream repositories provide Shiv's `NOTICE`, Waitress's `COPYRIGHT.txt`, and the Stellar SDK's `COPYING`. [Shiv](https://github.com/linkedin/shiv/blob/ff542cbe75ea832df3a989d07c7fdf5214f727fa/NOTICE) · [Waitress](https://github.com/Pylons/waitress/blob/016eea527dd4a3eb4a18d6dca4d0bfe32039e470/COPYRIGHT.txt) · [Stellar SDK](https://github.com/stellar/go-stellar-sdk/blob/d8c8acf5f56cae47fcf033522349565c6fc86764/COPYING)

## Refactoring patches

Reference patches record benchmark changes and identify the affected files in their diff headers. The applicable upstream terms also cover code copied or adapted into verifier patches, replay patches, and fixtures. Preserve the original notices and carry change statements and dates into the modified files where required. Rights for independently sourced additions, including replay contributions, depend on their own source records.

| Upstream | RefactorSWE modifications | License for upstream-derived material |
|---|---|---|
| Apple Music-like Lyrics | Extracts lyric group relations and updates the DOM lyric player in `packages/core`. [Reference patch](./tasks/refactor-applemusic-like-lyrics-dom-02/solution/solution.patch) | [AGPL-3.0-only](https://github.com/amll-dev/applemusic-like-lyrics/blob/5c0959686d18ca185b81811added3cd31299569f/LICENSE) |
| Boxes | Reorganizes generator discovery and the server's generator catalog. [Reference patch](./tasks/refactor-boxes-generator-registry-06/solution/solution.patch) | [GPL-3.0-or-later](https://github.com/florianfesti/boxes/blob/d23a70c4912258407161243ed50e06f126d3fca8/LICENSE.txt) |
| Plover | Moves machine connection and keymap handling out of the steno engine. [Reference patch](./tasks/refactor-plover-machine-manager-03/solution/solution.patch) | [GPL-2.0-or-later](https://github.com/opensteno/plover/blob/e87c4ef2982fcdeea587d2e612dff829fd331386/LICENSE.txt) |
| Waitress | Extracts WSGI response preparation and metadata into `src/waitress/response.py`. [Reference patch](./tasks/pylons-waitress-20260918003129-70962a/solution/solution.patch) | [ZPL-2.1](https://github.com/Pylons/waitress/blob/016eea527dd4a3eb4a18d6dca4d0bfe32039e470/LICENSE.txt) |

## Prebuilt images

The [image references](./PROVENANCE.md#published-container-images) identify the agent, verifier, and base images by digest. Image-layer contents, image-specific notices, and corresponding source for any distributed GPL or AGPL object code remain to be verified.
