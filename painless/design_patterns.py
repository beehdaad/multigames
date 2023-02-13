

class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwds)
        return self._instance


