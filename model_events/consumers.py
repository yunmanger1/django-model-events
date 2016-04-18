from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from .settings import SETTINGS
from .permissions import is_connection_allowed, is_message_allowed
from .handlers import on_message

GROUP_NAME = SETTINGS['GROUP_NAME']


@channel_session_user_from_http
def ws_add(message):
    if is_connection_allowed(message.user):
        Group(GROUP_NAME).add(message.reply_channel)
    else:
        msg = {"text": "Bye bye!", "close": True}
        message.reply_channel.send(msg)


@channel_session_user
def ws_message(message):
    if not is_message_allowed(message.user):
        return
    text = message.content['text']
    if text == "PING":
        Group(GROUP_NAME).add(message.reply_channel)
        message.reply_channel.send({"text": "PONG"})
        return
    on_message(message)


@channel_session_user
def ws_disconnect(message):
    Group(GROUP_NAME).discard(message.reply_channel)
