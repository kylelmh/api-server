def authenticated_only(func):
    def wrapper(*args, **kwargs):
        if not args[1].context.user.is_authenticated:
            raise Exception('Not authenticated')
        return func(*args, **kwargs)
    return wrapper