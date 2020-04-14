"""
Decorators modify or enhance an existing function in 
an non intrusive and maintainable way.

Implemented as a callble that accepts a callable
and returns a callable.
"""

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

def northern_city():
    return 'Troms$'

print(northern_city())

@escape_unicode
def northern_city_decorated():
    return 'Troms$'

print(northern_city_decorated())
