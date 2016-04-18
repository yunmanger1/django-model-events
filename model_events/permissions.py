import importlib

from .utils import default_permission
from .settings import SETTINGS


is_message_allowed = is_connection_allowed = default_permission


try:
    if "CONNECT_PERM" in SETTINGS:
        mod_name, func_name = SETTINGS["CONNECT_PERM"].rsplit(".", 1)
        is_connection_allowed = getattr(importlib.import_module(mod_name), func_name)
except (ImportError, AttributeError):
    pass

try:
    if "MESSAGE_PERM" in SETTINGS:
        mod_name, func_name = SETTINGS["MESSAGE_PERM"].rsplit(".", 1)
        is_message_allowed = getattr(importlib.import_module(mod_name), func_name)
except (ImportError, AttributeError):
    pass
