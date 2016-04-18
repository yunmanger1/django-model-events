from django.conf import settings

SETTINGS = {
    "MODEL_WHITELIST": ["auth.user"],
    "GROUP_NAME": 'admin-notifications',
}

SETTINGS.update(getattr(settings, "MODEL_EVENTS", {}))
