from functools import wraps

from .providers import BaseTalkingProvider


def injectable_decorator(some_param=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, __injected_talking_provider__, **kwargs):

            print(
                __injected_talking_provider__.say_hello('Super Decorator')
            )

            if some_param:
                return func(*args, **kwargs)
            else:
                raise Exception('Ups you did it again')

        original_annotations = getattr(func, '__annotations__', {})

        wrapper.__annotations__ = {
            **original_annotations,
            '__injected_talking_provider__': BaseTalkingProvider,
        }
        return wrapper
    return decorator
