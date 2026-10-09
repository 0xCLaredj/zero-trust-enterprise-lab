def is_portal_admin(roles):
    """Fail closed for missing/malformed role claims."""
    return isinstance(roles, list) and 'portal-admin' in roles
