from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .messaging import notify
from .settings import SETTINGS


WHITELIST = SETTINGS["MODEL_WHITELIST"]


@receiver(post_save)
def on_any_save(sender, instance, created, **kwargs):
    meta = instance._meta
    label = meta.label_lower
    if not label in WHITELIST:
        return
    notify({
        "created": created,
        "id": instance.pk,
        "label": label,
        "verbose_name": str(meta.verbose_name),
        "verbose_name_plural": str(meta.verbose_name_plural),
        "event": "post_save"
    }, message_type="db_event")


@receiver(post_delete)
def on_any_delete(sender, instance, **kwargs):
    meta = instance._meta
    label = meta.label_lower
    if not label in WHITELIST:
        return
    notify({
        "id": instance.pk,
        "label": label,
        "verbose_name": str(meta.verbose_name),
        "verbose_name_plural": str(meta.verbose_name_plural),
        "event": "post_delete"
    }, message_type="db_event")
