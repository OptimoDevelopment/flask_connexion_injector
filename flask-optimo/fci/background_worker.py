import injector

from .injections import ApiModule
from .providers import BaseHelloProvider

injected = injector.Injector([ApiModule])

our_provider = injected.get(BaseHelloProvider)

while True:
    our_provider.say_hello()
