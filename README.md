# decoratorium

Decorator class implementation for Python


## Installation

```shell
pip install decoratorium
```


## Usage

```python
from decoratorium import decoratorium

class my_decorator(decoratorium):

    def __init__(self, arg1=100, arg2=200):
        self.arg1 = arg1
        self.arg2 = arg2
          
    def wrapper(self, func, *args, **kwargs):
        result = func(*args, **kwargs)
        return self.arg1 * self.arg2 / result

@my_decorator
def f1():
    pass

@my_decorator()
def f2():
    pass

@my_decorator(arg2=500)
def f3():
    pass
```

It is safe to reuse the same once created decorator instance on a different
functions. 

```python
my_decorator_500 = my_decorator(arg2=500)

@my_decorator_500
def f1():
    print('f1')

@my_decorator_500
def f2():
    print('f2')

f1()
f2()
```


## Authors

* [Serge Matveenko](https://github.com/lig)


## How to contribute

Use [the decoratorium github page](https://github.com/lig/decoratorium) to post issues and questions and to send pull requests.

## License

[MIT License](LICENSE)
