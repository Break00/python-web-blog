# -*- coding: utf-8 -*-
"""
@author: Lee
@description: code
@date: 2023/2/1 
"""
import asyncio
from aiohttp import web
import logging

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
