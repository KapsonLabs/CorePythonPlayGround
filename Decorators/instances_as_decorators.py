"""
1. Python calls an instance's __call__()
when it's used as a decorator
2. __call__()'s return value is used as the 
new function
3. Creates groups of callables that you can
dynamically control as a group
"""

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

l = [1,2,3]
t = rotate_list(l)
print(t)

#disable the tracer
tracer.enabled = False

t = rotate_list(l)
print(t)