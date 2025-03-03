import _thread
class MyObject:
    def __init__(self):
        self.data = 'Hello, World!'
        self.lock = _thread.RLock()

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['lock']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.lock = _thread.RLock()