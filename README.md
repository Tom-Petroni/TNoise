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

## Installer dans Nuke

1. Copier `publish/TNoise` vers `C:/Users/<user>/.nuke/TNoise`
2. Dans `C:/Users/<user>/.nuke/init.py`, ajouter:

```python
import nuke
nuke.pluginAddPath(r"C:/Users/<user>/.nuke/TNoise")
```

3. Redemarrer Nuke

## Verification rapide

- Le menu `Nodes > TNoise` apparait
- Le binaire est present dans:
  `TNoise/bin/<nuke_version>/<os>/<arch>/`

## Build / docs techniques

- `work/docs/BUILD.md`
- `work/docs/INSTALL.md`
- `work/docs/NODE_REFERENCE.md`
- `work/docs/ARCHITECTURE.md`

## Licence

Usage commercial soumis a la licence du repo (`LICENSE` + `EULA.md`).
