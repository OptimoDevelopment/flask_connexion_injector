from ..providers import BaseTalkingProvider


def get(name: str, talking_provider: BaseTalkingProvider) -> dict:
    return {
        'message': talking_provider.say_hello(name),
    }
