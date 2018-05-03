# -*- coding: utf-8 -*-
"""Entrance"""

# import signal
import asyncio
# import threading

import uvloop
from tornado import httpserver
from tornado.options import options
# from tornado.ioloop import IOLoop
from tornado.platform.asyncio import BaseAsyncIOLoop
import tornado.platform.asyncio as tornado_asyncio

from app import create_app

class TornadoUvloop(BaseAsyncIOLoop):
    '''采用uvloop加速ioloop事件循环'''

    def initialize(self, **kwargs):
        loop = uvloop.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            super().initialize(loop, **kwargs)
        except Exception:
            loop.close()
            raise

def stop(server, io_loop, sig=None, frame=None):
    server.stop()
    io_loop.stop()

if __name__ == "__main__":
    # HTTP_SERVER = httpserver.HTTPServer(create_app())
    # HTTP_SERVER.listen(options.config['port'])
    # IOLoop.configure(TornadoUvloop)
    # TornadoUvloop().install()
    # io_loop = IOLoop.current()
    # if isinstance(threading.current_thread(), threading._MainThread):
    #     def on_signal(sig, frame):
    #         io_loop.add_callback_from_signal(stop, HTTP_SERVER, io_loop, sig=sig, frame=frame)

    #     signal.signal(signal.SIGINT, on_signal)
    #     signal.signal(signal.SIGTERM, on_signal)

    # options.config['logger'].info('Listen on port %d......' % options.config['port'])
    # io_loop.start()
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    tornado_asyncio.AsyncIOMainLoop().install()
    server = httpserver.HTTPServer(create_app(), xheaders=True)
    server.listen(options.config['port'])
    options.config['logger'].info('Listen on port %d......' % options.config['port'])
    asyncio.get_event_loop().run_forever()
