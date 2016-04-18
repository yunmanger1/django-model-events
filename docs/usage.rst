========
Usage
========

To use django-model-events in a Django project add model_events to ``INSTALLED_APPS`` setting::

    from model_events.messaging import notify


Configure it using::

    MODEL_EVENTS = {
        "MODEL_WHITELIST": (
            "users.user",
        ),
        "ON_MESSAGE_HANDLER": "path.to.handler.on_message",
        "CONNECT_PERM": "path.to.connect_perm_checker",
        "MESSAGE_PERM": "path.to.message_perm_checker",
    }
