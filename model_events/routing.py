from channels.routing import route

from .consumers import ws_add, ws_disconnect, ws_message
from .receivers import *


routes = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]
