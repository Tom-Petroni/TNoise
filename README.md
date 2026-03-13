# TNoise

TNoise is a native Nuke node for procedural noise generation. It is built for production use and runs natively on Linux, Windows, and macOS.

## Features

**Noise types**
- Perlin, Simplex
- Voronoi — shapes: Voronoi, Cells, Crystals, Cracks, Web, Bubbles
- Pattern — modes: Concentric, Linear, Radial
- Fractal stacking: fBm, Billow, Ridged (or none)

**Output modes**
- Grayscale noise with optional color ramp
- Vector field
- STMap
- Normal map

**Inputs**
- `PRef` — 3D position override for true 3D noise. Without it, the node works in 2D.
- `Warp` — external vector map for domain warping. Overrides the internal warp controls.
- `mask` — optional mask applied to the final output.

**Domain warping** — internal warp layer with its own noise type, transform and blend controls.

**RGB separation** — per-channel spatial or temporal offset with configurable chroma pairs.

**Post-processing** — quantize, pixelate, halftone (dots, hatches), color ramp editor.

**Animation** — `z speed`, `translate speed` and all transform knobs are fully keyframeable.

## Compatibility

| Platform | Architecture | Nuke versions |
|---|---|---|
| Linux | x86_64 | 13.0 – 16.0 |
| Windows | x86_64 | 13.0 – 16.0 |
| macOS | x86_64 | 13.0 – 16.0 |
| macOS | aarch64 (Apple Silicon) | 15.0 – 16.0 |

## Installation

1. Copy the `TNoise` folder and `init.py` into your `.nuke` directory.
2. If your `.nuke/init.py` already exists, add the following line to it:

```python
nuke.pluginAddPath("./TNoise")
```

If there is no `init.py` yet, the one included in this package is ready to use as-is.

3. Restart Nuke.
4. The node is available under `Nodes > TNoise`.

## Troubleshooting

- If the node does not appear, check the Script Editor for TNoise log messages.
- Make sure the `TNoise/bin/<version>/<os>/<arch>/` folder contains the binary for your Nuke version and OS.
- On macOS Apple Silicon, ARM binaries are loaded only on Nuke 15.0 and above.

## Documentation

- [Installation](docs/INSTALL.md)
- [Node reference](docs/NODE_REFERENCE.md)
