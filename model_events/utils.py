def default_permission(user):
    return user.is_superuser


def allow_all(user):
    return True
