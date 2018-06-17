import os
from tornado import web
from tornado.options import define
from tornado.options import options
from .config import DEV_CONFIG
from .config import PROD_CONFIG
from .handlers import IndexHandler, FormHandler, TableHandler, TestHandler
from .handlers import PanelHandler, ChartHandler, UIHandler, EmptyHandler
from .handlers import PageNotFoundHandler, OrderHandler, AnnounceHandler
from .log import get_logger

def create_app():

    define('env',
           default='dev',
           help='[dev|prod](dev is default)',
           type=str)
    options.parse_command_line()

    if options.env == 'dev':
        define('config', default=DEV_CONFIG, type=dict)
    else:
        define('config', default=PROD_CONFIG, type=dict)

    # === mysql initialize

    options.config['logger'] = get_logger("acg")
    settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        debug=options.config['debug'],
        cookie_secret=options.config['cookie_secret'],
        gzip=True,
    )
    app = web.Application([
        (r'/', IndexHandler),
        (r'/form', FormHandler),
        (r'/orders', OrderHandler),
        (r'/announce', AnnounceHandler),
        (r'/table', TableHandler),
        (r'/panel', PanelHandler),
        (r'/chart', ChartHandler),
        (r'/ui', UIHandler),
        (r'/empty', EmptyHandler),
        (r'/test', TestHandler),
        (r'/(robots\.txt)', web.StaticFileHandler),
        ('.*', PageNotFoundHandler)], **settings)
    return app
