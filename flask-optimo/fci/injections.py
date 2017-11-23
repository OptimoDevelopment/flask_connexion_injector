import injector


class ApiModule(injector.Module):
    def configure(self, binder: injector.Binder):
        from sqlalchemy.orm.session import Session
        from .db import session

        from .providers import BaseTalkingProvider, DbTalkingProvider, FibonacciProvider

        binder.bind(Session, session, scope=injector.SingletonScope)
        binder.bind(BaseTalkingProvider, to=DbTalkingProvider, scope=injector.ThreadLocalScope)
        binder.bind(FibonacciProvider, scope=injector.ThreadLocalScope)


class CachedApiModule(injector.Module):
    def configure(self, binder: injector.Binder):
        from .providers import BaseTalkingProvider, CachedProvider

        binder.bind(BaseTalkingProvider, to=CachedProvider, scope=injector.ThreadLocalScope)


class AppProviderModule(injector.Module):
    def configure(self, binder: injector.Binder):
        from flask import Request, request

        binder.bind(Request, request)
