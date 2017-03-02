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
          
    def wrapper(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
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


## Authors

* [Serge Matveenko](https://github.com/lig)


## How to contribute

Use [the decoratorium github page](https://github.com/lig/decoratorium) to post issues and questions and to send pull requests.

## License

[MIT License](LICENSE)
