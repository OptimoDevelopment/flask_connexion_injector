import injector

from .injections import ApiModule
from .providers import BaseTalkingProvider

injected = injector.Injector([ApiModule])

our_provider = injected.get(BaseTalkingProvider)

while True:
    our_provider.say_hello()
