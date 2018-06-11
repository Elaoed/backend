from tornado import web
from tornado import escape
# from app.aiomyob import AioMyOB
from .mysqlob import MySqlOB

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

    def get(self):
        return self.render("index.html")

class FormHandler(BasicHandler):
    def get(self):
        return self.render("form.html")

class TableHandler(BasicHandler):
    def get(self):
        return self.render("table.html")

class ChartHandler(BasicHandler):
    def get(self):
        return self.render("chart.html")

class PanelHandler(BasicHandler):
    def get(self):
        return self.render("panel.html")

class UIHandler(BasicHandler):
    def get(self):
        return self.render("ui.html")

class EmptyHandler(BasicHandler):
    def get(self):
        return self.render("empty.html")

class TestHandler(BasicHandler):
    async def get(self):
        # res = await AioMyOB.select("SELECT * FROM hello")
        res = None
        self.write(res)

class OrderHandler(BasicHandler):
    def get(self):
        sql = "SELECT * FROM orders"
        mdb = MySqlOB()
        data = mdb.select(sql, one=False)
        return self.render("orders.html", data=data)
