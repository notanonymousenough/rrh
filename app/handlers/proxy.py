import logging
import aiohttp
import random
from urllib.parse import urljoin
from aiohttp import web

from app.context import AppContext

logger = logging.getLogger(__name__)


class ProxyHandler:
    def __init__(self, ctx: AppContext):
        self.ctx = ctx

    async def handle(self, request: web.Request) -> web.Response:
        target_server_base_url = self.ctx.balancer.select_host().name
        request_id = random.randint(1, 2 ^ 16)

        target_url = urljoin(target_server_base_url, request.match_info['path'])

        data = await request.read()
        params = request.rel_url.query

        logger.info(f"REQUEST{request_id} {target_url}, {request.headers}, {request.method}, {data}, {params}")

        async with aiohttp.ClientSession() as session:
            async with session.request(
                    request.method,
                    target_url,
                    headers=request.headers,
                    params=params,
                    data=data
            ) as resp:
                res = resp
                raw = await res.read()

        headers = dict(res.headers)
        if 'Transfer-Encoding' in headers:
            del headers['Transfer-Encoding']
            headers["Content-Length"] = str(len(raw))
        logger.info(f"RESPONSE{request_id} {res.status}, {raw}, {headers}")
        return web.Response(body=raw, status=res.status, headers=headers)
