# -*- coding: utf-8 -*-
import time
import json
import subprocess
from config import Config
import requests

def jd(data):
    return json.dumps(data)

def sysfunc(func, params, port="18608"):
    cmd = ["java", "-cp", Config.jmx_path, "com.wanmei.mhzx.InvokeMethod", "127.0.0.1", port, "controlRole", "kym", "IWEB:type=GameControl", func] + params
    s = subprocess.check_output(cmd)
    return s

def get_role_id(role_name, port="18608"):

    res = sysfunc("getRoleidByName", ["java.lang.String", role_name], port)
    print(res)

def charge(role_name, server_id, amount=68, productId="tw.zx.1usd"):
    role_id = get_role_id(role_name)
    print(role_id)
    exit()
    if role_id is None:
        return jd({'code': 1, 'msg': "role_id is None"})

    if server_id is None:
        return jd({'code': 1, 'msg': "server_id is None"})

    now = int(time.time())
    sd_ts = "SD" + str(now)
    params = {
        'pOrderId': sd_ts,
        'userId': 0,
        'creditId': role_id,
        'currency': "CNY",
        'amount': amount,
        'RCurrency': "CNY",
        'RAmount': amount,
        'gameCode': "twzx",
        'serverCode': server_id,
        'stone': amount,
        'stoneType': "diamond",
        'md5Str': "wBv78qM7QeEhJ6BGeZAwBStQVMKmTNG1f2QIDAQAB",
        'time': now,
        'productId': productId,
        'activityExtra': 0,
        'orderStateMonth': 0,
        'point': 0,
        'freePoint': 1,
        'payType': "platform"
    }
    print(params)
    res = requests.get(Config.charge_url, params)
    print(res.content)
    print(res.json()['code'] == "1000")
    return "Finish"

if __name__ == "__main__":
    print(get_role_id("avbcx"))
