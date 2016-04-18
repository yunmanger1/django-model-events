import importlib
from .settings import SETTINGS


on_message = lambda m: m


try:
    if u"ON_MESSAGE_HANDLER" in SETTINGS:
        mod_name, func_name = SETTINGS["ON_MESSAGE_HANDLER"].rsplit(".", 1)
        on_message = getattr(importlib.import_module(mod_name), func_name)
except (ImportError, AttributeError) as e:
    print(e)
    pass
