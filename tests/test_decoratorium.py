import pytest

from decoratorium import decoratorium


@pytest.fixture(scope='session')
def decorator_klass():

    class test_decorator(decoratorium):

        def __init__(self, arg1=100, arg2=200):
            self.arg1 = arg1
            self.arg2 = arg2

        def wrapper(self, func, *args, **kwargs):
            result = func(*args, **kwargs)
            return self.arg1, self.arg2, func, args, kwargs, result

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


def test_metadata(decorator_klass):

    # @decorator_klass
    def foo(*args, **kwargs):
        """ Function `foo` docstring.
        """
        return args, kwargs
    foo.bar = 'fubar'

    dfoo = decorator_klass(foo)

    assert dfoo.__name__ == foo.__name__
    assert dfoo.__doc__ == foo.__doc__
    assert dfoo.bar == foo.bar


def test_decorator_reuse(decorator_klass):

    decorator_klass_500 = decorator_klass(arg2=500)

    def foo1(*args, **kwargs):
        return 500

    def foo2(*args, **kwargs):
        return 600

    dfoo1 = decorator_klass_500(foo1)
    dfoo2 = decorator_klass_500(foo2)

    assert dfoo1() == (
        100,
        500,
        foo1,
        (),
        {},
        500,
    )
    assert dfoo2() == (
        100,
        500,
        foo2,
        (),
        {},
        600,
    )
