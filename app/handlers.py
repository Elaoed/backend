from tornado import web
from tornado import gen
from tornado import escape
from app.aiomyob import AioMyOB

class BasicHandler(web.RequestHandler):

    def error(self):
        return

class PageNotFoundHandler(BasicHandler):

    def get(self):
        respon_json = escape.json_encode(404)
        self.write(respon_json)

    def write_error(self, status_code, **kwargs):
        respon_json = escape.json_encode(status_code)
        self.write(respon_json)

class IndexHandler(BasicHandler):

    async def get(self):
        return self.render("index.html")

class FormHandler(BasicHandler):
    @gen.coroutine
    def get(self):
        return self.render("form.html")

class TableHandler(BasicHandler):
    @gen.coroutine
    def get(self):
        return self.render("table.html")

class ChartHandler(BasicHandler):
    @gen.coroutine
    def get(self):
        return self.render("chart.html")

class PanelHandler(BasicHandler):
    @gen.coroutine
    def get(self):
        return self.render("panel.html")

class UIHandler(BasicHandler):
    @gen.coroutine
    def get(self):
        return self.render("ui.html")

class EmptyHandler(BasicHandler):
    @gen.coroutine
    def get(self):
        return self.render("empty.html")

class TestHandler(BasicHandler):
    async def get(self):
        res = await AioMyOB.select("SELECT * FROM hello")
        self.write(res)
