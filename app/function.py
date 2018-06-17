# -*- coding: utf-8 -*-

import subprocess
from config import Config

def sysfunc(func, params, port="18608"):
    cmd = ["java", "-cp", Config.jmx_path, "com.wanmei.mhzx.InvokeMethod", "127.0.0.1", port, "controlRole", "kym", "IWEB:type=GameControl", func] + params
    s = subprocess.check_output(cmd)
    return s

def get_role_id(role_name, port="18608"):

    res = sysfunc("getRoleidByName", ["java.lang.String", role_name], port)
    print(res)

if __name__ == "__main__":
    print(get_role_id("avbcx"))
