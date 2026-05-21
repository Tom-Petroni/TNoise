# Fiche Node - TNoise

## Resume

TNoise est un node Nuke natif (Rust/C++) avec package Python pour l'UI/menu.

## Prerequis

- Nuke installe (version cible: 13.x a 17.x selon votre build)
- Rust/Cargo
- Toolchain C++ compatible Nuke (MSVC sur Windows)

## Compiler

Depuis la racine du repo:

```powershell
cd work
cargo xtask --compile --nuke-versions 16.0 --target-platform windows --output-to-package --limit-threads
```

Exemples plateforme:

- Linux: `--target-platform linux`
- macOS Intel: `--target-platform macos-x86-64`
- macOS Apple Silicon: `--target-platform macos-aarch64`

## Installer dans Nuke

1. Copier `publish/TNoise` dans `C:/Users/<user>/.nuke/TNoise`
2. Ajouter dans `C:/Users/<user>/.nuke/init.py`:

```python
import nuke
nuke.pluginAddPath(r"C:/Users/<user>/.nuke/TNoise")
```

3. Relancer Nuke

## Verification

- Verifier la presence de `Nodes > TNoise`
- Verifier que le binaire existe dans `TNoise/bin/<nuke_version>/<os>/<arch>/`
