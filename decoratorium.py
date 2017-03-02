from collections import Callable


__all__ = ['decoratorium']


class Decoratorium:

    def __new__(cls, *args, **kwargs):
        """ Hack to handle @decorator and @decorator() cases identically.
        """
        self = super().__new__(cls)

        if not kwargs and len(args) == 1 and isinstance(args[0], Callable):
            self.__init__()
            return self(args[0])

        return self

    def __call__(self, func):
        """ An actual decorator.
        """
        self.func = func
        return self.wrapper

    def __init__(self, *args, **kwargs):
        """ Allows to catch decorator arguments via `@decorator(args)` syntax.
        """
        pass

    def wrapper(self, *args, **kwargs):
        """ A wrapper interface to be implemented.

        Has access to the decorated function via `self.func`.
        """
        return NotImplemented


decoratorium = Decoratorium
