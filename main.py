import asyncio
import logging
import datetime
import argparse
from aiohttp import web

from app.context import AppContext
from app.routes import setup_routes
from balance.factories import BalancerFactory

logging.basicConfig(
    filename=f'rrh{datetime.datetime.now().strftime("%m-%d-%Y_%H:%M:%S")}.log',
    filemode='w',
    level=0,
    format='%(levelname)s [%(asctime)s] %(message)s'
)


async def create_app(args):
    app = web.Application()
    ctx = AppContext(args.config_path, BalancerFactory.arg_to_balancer(args.balancer))

    app.on_startup.append(ctx.on_startup)
    app.on_shutdown.append(ctx.on_shutdown)

    setup_routes(app, ctx)

    return app


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', type=int, default=8000)
    parser.add_argument('--config-path', '-c', type=str, default="rrhood.yml")
    parser.add_argument('--balancer', '-b', type=str, default="rr", help="rr - RoundRobin")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    app = asyncio.new_event_loop().run_until_complete(create_app(args))
    web.run_app(app, port=args.port)
