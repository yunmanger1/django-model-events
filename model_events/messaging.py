import json
from channels import Group

from .settings import SETTINGS

GROUP_NAME = SETTINGS['GROUP_NAME']


def notify(message, message_type="notification"):
    Group(GROUP_NAME).send({
        "text": json.dumps({
            "type": message_type,
            "payload": message
        })
    })
