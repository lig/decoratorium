from collections import Callable
from functools import partial

from decorator import decorate


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
        """ Builds decorated function.
        """
        return decorate(func, self.wrapper)

    def __init__(self, *args, **kwargs):
        """ Allows to catch decorator arguments via `@decorator(args)` syntax.
        """
        pass

    def wrapper(self, func, *args, **kwargs):
        """ A wrapper interface to be implemented.

        Uses decorate module approach to have `func` being passed explicitly.
        This allows to reuse the same decorator class on several functions.
        """
        return NotImplemented


decoratorium = Decoratorium
