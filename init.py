"""TNoise Nuke plugin loader — place this file and the TNoise/ folder in your .nuke directory."""

import os

import nuke  # ty:ignore[unresolved-import]

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
nuke.pluginAddPath(  # ty:ignore[unresolved-attribute]
    os.path.join(_THIS_DIR, "TNoise").replace(os.sep, "/"),
)
