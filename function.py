# Функции
class Function:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __eq__(self, other):
        if isinstance(other, Function):
            return self.func.__code__.co_code == other.func.__code__.co_code
        return False

    def __lt__(self, other):
        return str(self.func.__code__.co_code) < str(other.func.__code__.co_code)

    def __str__(self):
        return self.func.__name__
