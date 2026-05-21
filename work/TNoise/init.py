"""Main entry point for TNoise Nuke plugin."""

import logging
import os

import nuke  # ty:ignore[unresolved-import]

try:
    from TNoise._node_setup import setup_knob_changed
    from TNoise._plugin_loader import add_plugin_path_safe
except Exception:
    from _node_setup import setup_knob_changed
    from _plugin_loader import add_plugin_path_safe

logger = logging.getLogger(__name__)

_HOOKS_ENV_VAR = "TNOISE_SCRIPT_HOOKS_DONE"


def _refresh_plugin_path():
    loaded = add_plugin_path_safe()
    if loaded:
        setup_knob_changed()
    else:
        nuke.tprint("[TNoise] Plugin binary not loaded yet.")


def _register_script_hooks():
    if os.getenv(_HOOKS_ENV_VAR) == "1":
        return

    for hook_name in ("addBeforeScriptLoad", "addOnScriptNew", "addOnScriptLoad"):
        hook = getattr(nuke, hook_name, None)
        if callable(hook):
            hook(_refresh_plugin_path)

    os.environ[_HOOKS_ENV_VAR] = "1"


try:
    _register_script_hooks()
    _refresh_plugin_path()
except Exception:  # pragma: no cover - Nuke runtime dependency
    logger.exception("Unexpected failure while initializing the TNoise plugin.")
