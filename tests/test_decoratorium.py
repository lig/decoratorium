import pytest

from decoratorium import decoratorium


@pytest.fixture(scope='session')
def decorator_klass():

    class test_decorator(decoratorium):

        def __init__(self, arg1=100, arg2=200):
            self.arg1 = arg1
            self.arg2 = arg2

        def wrapper(self, *args, **kwargs):
            result = self.func(*args, **kwargs)
            return self.arg1, self.arg2, self.func, args, kwargs, result

    return test_decorator


def test_bare_args_decorator(decorator_klass):

    # @decorator_klass
    def foo(*args, **kwargs):
        return args, kwargs

    dfoo = decorator_klass(foo)

    assert dfoo(300, bar=400) == (
        100,
        200,
        foo,
        (300,),
        {'bar': 400},
        ((300,), {'bar': 400},),
    )


def test_default_args_decorator(decorator_klass):

    # @decorator_klass()
    def foo(*args, **kwargs):
        return args, kwargs

    dfoo = decorator_klass()(foo)

    assert dfoo(300, bar=400) == (
        100,
        200,
        foo,
        (300,),
        {'bar': 400},
        ((300,), {'bar': 400},),
    )


def test_explicit_args_mixed_decorator(decorator_klass):

    # @decorator_klass(arg2=500)
    def foo(*args, **kwargs):
        return args, kwargs

    dfoo = decorator_klass(arg2=500)(foo)

    assert dfoo(300, bar=400) == (
        100,
        500,
        foo,
        (300,),
        {'bar': 400},
        ((300,), {'bar': 400},),
    )
