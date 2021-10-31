class CallCount:
    def __init__(self, func):
        self._func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self._func(*args, **kwargs)

    def get_call_count(self):
        return self._count


@CallCount
def hello(name):
    print(f'Hello, {name}!')


hello('abc')
hello('spam')
hello('eggs')
print(hello.get_call_count())
