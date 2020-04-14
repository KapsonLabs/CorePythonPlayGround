"""
Decorating functions may lead to loss of important
data that might be used by IDEs and Debuggers
"""

def hello():
    "Print a known message"
    print('Hello Allan')

print(hello.__name__)
print(hello.__doc__)

#Decorating it with a simple dcorator
def noop(f):
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello_decorated():
    "Print a known message"
    print('Hello Allan')

#Notice how we loase important infor about the function
print(hello_decorated.__name__)
print(hello_decorated.__doc__)

import functools

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello_decorated():
    "Print a known message"
    print('Hello Allan')

print(hello_decorated.__name__)
print(hello_decorated.__doc__)




