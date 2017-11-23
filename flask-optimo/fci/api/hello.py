from flask import Request

from ..providers import BaseHelloProvider


def get(name: str, hello_provider: BaseHelloProvider, request: Request) -> dict:
    #  We can access Request because Flask-Injector prepares it for us
    headers = request.headers

    return {
        'message': hello_provider.say_hello(name),
    }
