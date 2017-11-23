class BaseHelloProvider:
    def say_hello(self, name: str):
        raise NotImplemented


class DbHelloProvider(BaseHelloProvider):
    def say_hello(self, name: str):
        return f'Database says "Hello { name }!"'


class CacheHelloProvider(BaseHelloProvider):
    def say_hello(self, name: str):
        return f'Cache says "Hello { name }!"'


class FibonacciProvider:
    def get_fib_value(self, index):
        a, b = 0, 1
        while index:
            yield a
            a, b = b, a + b
            index -= 1