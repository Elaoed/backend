#!/usr/bin/python
# coding:utf-8
"""Entrance"""
from tornado import httpserver
from tornado import ioloop
from tornado.options import options
from app import create_app

if __name__ == "__main__":
    HTTP_SERVER = httpserver.HTTPServer(create_app())
    HTTP_SERVER.listen(options.config['port'])
    options.config['logger'].info('Listen on port %d......' % options.config['port'])
    ioloop.IOLoop.instance().start()
