class Trace:
    def __init__(self):
        self._enabled = True

    def __call__(self, func, *args, **kwargs):
        def wrap(*args, **kwargs):
            if self._enabled:
                print(f'Calling {func}')
