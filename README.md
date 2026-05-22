# TNoise

TNoise est un node Nuke de generation procedurale pour produire du bruit 2D/3D, des vectors, des STMaps et des normal maps dans un workflow production.

## Pourquoi TNoise

- Noise families: Perlin, fBm, Turbulence, Ridged, Voronoi, Pattern
- Domain warping interne ou via input `Warp`
- Sorties multiples: Noise, Vectors, STMap, Normal Map
- Post-process integres: quantize, pixelate, halftone, color ramp
- Compatible pipeline Nuke via package Python + binaire natif

## Structure du repo

```text
TNoise/
  publish/        # payload a copier dans .nuke
  work/           # source rust/c++ + tooling build
  node.json
  VERSION
  CHANGELOG.md
```

## Prerequis

- Nuke installe (version cible)
- Rust/Cargo
- Toolchain C++ compatible Nuke (MSVC sous Windows)

## Compiler

Depuis la racine du repo:

```powershell
cd work
cargo xtask --compile --nuke-versions 16.0 --target-platform windows --output-to-package --limit-threads
```

Exemples cibles:

- Linux: `--target-platform linux`
- macOS Intel: `--target-platform macos-x86-64`
- macOS Apple Silicon: `--target-platform macos-aarch64`

## Installer dans Nuke (utilisateur final)

1. Cloner le repo
2. Glisser `publish/TNoise` dans `C:/Users/<user>/.nuke/`
3. Redemarrer Nuke

Les binaires (`.dll`, `.so`, `.dylib`) sont versionnes dans `publish/TNoise/bin/...`.

Si ton setup Nuke ne charge pas automatiquement le dossier, ajoute en fallback dans `.nuke/init.py`:

```python
import nuke
nuke.pluginAddPath(r"C:/Users/<user>/.nuke/TNoise")
```

## Verification rapide

- Le menu `Nodes > TNoise` apparait
- Le binaire est present dans:
  `TNoise/bin/<nuke_version>/<os>/<arch>/`

## Build / docs techniques

- `work/docs/BUILD.md`
- `work/docs/INSTALL.md`
- `work/docs/NODE_REFERENCE.md`
- `work/docs/ARCHITECTURE.md`

## Build CI GitHub

Le repo contient un workflow GitHub Actions (`.github/workflows/nuke-build.yml`) qui:

- build les versions Nuke 13.0 -> 17.0
- build Windows/Linux/macOS (x86_64 + arm64 quand disponible)
- genere un zip de release pret a copier dans `.nuke`

## Licence

Usage commercial soumis a la licence du repo (`LICENSE` + `EULA.md`).
