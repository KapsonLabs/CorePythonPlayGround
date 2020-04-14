"""
1. Classes are callable objects
2. Functions decorated with a class are replaced by
an instance of the class
3. These instances must themselves be callable by 
implementing the __call__ method.
"""

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print('Hello, {}!'.format(name))

hello('Fred')
hello('Allan')
hello('Will')
hello('Men')

print(hello.count)
