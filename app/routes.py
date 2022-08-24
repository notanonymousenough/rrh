from aiohttp import web
from app.handlers.proxy import ProxyHandler
from app.context import AppContext


def setup_routes(app: web.Application, ctx: AppContext):
    proxy_handler = ProxyHandler(ctx)
    app.router.add_route("*", '/{path:.*?}', proxy_handler.handle)
