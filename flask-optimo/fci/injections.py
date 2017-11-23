import injector
from sqlalchemy.orm.session import Session

from .db import session
from .providers import BaseHelloProvider, CacheHelloProvider, DbHelloProvider, FibonacciProvider


class ApiModule(injector.Module):
    def configure(self, binder: injector.Binder):

        binder.bind(Session, session, scope=injector.SingletonScope)
        binder.bind(BaseHelloProvider, to=DbHelloProvider, scope=injector.ThreadLocalScope)
        binder.bind(FibonacciProvider, scope=injector.ThreadLocalScope)


class CachedApiModule(injector.Module):
    def configure(self, binder: injector.Binder):

        binder.bind(BaseHelloProvider, to=CacheHelloProvider, scope=injector.ThreadLocalScope)
