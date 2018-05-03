from tornado import web
from tornado import gen
from tornado import escape

class PageNotFoundHandler(web.RequestHandler):

    def get(self):
        respon_json = escape.json_encode(404)
        self.write(respon_json)

    def write_error(self, status_code, **kwargs):
        respon_json = escape.json_encode(status_code)
        self.write(respon_json)


class IndexHandler(web.RequestHandler):

    async def get(self):
        return self.render("index.html")

    @gen.coroutine
    def write_error(self, status_code, **kwargs):
        respon_json = escape.json_encode(status_code)
        self.write(respon_json)

class FormHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        return self.render("form.html")

    @gen.coroutine
    def write_error(self, status_code, **kwargs):
        respon_json = escape.json_encode(status_code)
        self.write(respon_json)

class TableHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        return self.render("table.html")

    @gen.coroutine
    def write_error(self, status_code, **kwargs):
        respon_json = escape.json_encode(status_code)
        self.write(respon_json)

class ChartHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        return self.render("chart.html")

    @gen.coroutine
    def write_error(self, status_code, **kwargs):
        respon_json = escape.json_encode(status_code)
        self.write(respon_json)

class PanelHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        return self.render("panel.html")

    @gen.coroutine
    def write_error(self, status_code, **kwargs):
        respon_json = escape.json_encode(status_code)
        self.write(respon_json)

class UIHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        return self.render("ui.html")

    @gen.coroutine
    def write_error(self, status_code, **kwargs):
        respon_json = escape.json_encode(status_code)
        self.write(respon_json)

class EmptyHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        return self.render("empty.html")

    @gen.coroutine
    def write_error(self, status_code, **kwargs):
        respon_json = escape.json_encode(status_code)
        self.write(respon_json)
