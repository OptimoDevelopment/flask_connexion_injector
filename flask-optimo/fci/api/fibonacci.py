from ..decorators import injectable_decorator
from ..providers import FibonacciProvider


@injectable_decorator(some_param=True)
def post(body: dict, fibonacci: FibonacciProvider) -> dict:
    index = body['index']
    return {
        'index': index,
        'value': list(fibonacci.get_fib_value(index)),
    }
