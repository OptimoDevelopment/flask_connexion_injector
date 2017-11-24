from functools import wraps

from .providers import BaseHelloProvider


def injectable_decorator(some_param=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, __injected_hello_provider__, **kwargs):

            print(
                __injected_hello_provider__.say_hello('Super Decorator')
            )

            if some_param:
                return func(*args, **kwargs)
            else:
                raise Exception('Ups you did it again')

        original_annotations = getattr(func, '__annotations__', {})

        wrapper.__annotations__ = {
            **original_annotations,
            '__injected_hello_provider__': BaseHelloProvider,
        }
        return wrapper
    return decorator
