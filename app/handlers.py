from tornado import web
from tornado import escape
# from app.aiomyob import AioMyOB
from .mysqlob import MySqlOB
import subprocess

class BasicHandler(web.RequestHandler):

    def format(self, key, value):

        if key == 'is_test':
            return '测试订单' if value == 1 else '正式订单'
        if key == 'paySuccess':
            return '支付成功' if value == 0 else '支付失败'
        dmap = {
            None: "",
        }
        return dmap.get(value, value)

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

class AnnounceHandler(BasicHandler):
    def get(self):
        return self.render("announce.html")

    def post(self):

        jmx_path = "/www/wwwroot/111.6.78.66/mhzxBackend/JMXTool.jar"
        content = self.get_argument("content")
        s = subprocess.check_output(["java", "-cp", jmx_path,
                                     "com.wanmei.mhzx.InvokeMethod", "127.0.0.1", "18608", "controlRole",
                                     "kym", "IWEB:type=GameControl", "sendNotice", "java.lang.String",
                                     content])
        # s = [x for x in s.decode('utf-8').split('\n') if x]
        # s = s[-1].split(' ')[-1].split("=")[-1]
        # return s
        return self.write({'code': 0, 'msg': "success"})


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
        data = [{k: self.format(k, v) for k, v in x.items()} for x in data]
        return self.render("orders.html", data=data)
