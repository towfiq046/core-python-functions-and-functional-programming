def escape_unicode(func):
    def wrap(*args, **kwargs):
        return ascii(func(*args, **kwargs))
    return wrap


@escape_unicode
def spam():
    return 'yy©®yy'


print(spam())
