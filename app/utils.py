# -*- coding: utf-8 -*-
"""Utilities functions"""
import time
import requests
from requests import Session
from config.conf import conf

def self_req(url, method="POST", logger=None, **kwargs):

    session = kwargs.pop('session', None)
    if not session:
        session = Session()
    try:
        res = session.post(url=url, **kwargs)
        return res.status_code, res
    except requests.exceptions.ConnectionError:
        return 1, {}
    except requests.exceptions.Timeout:
        return 2, {}
    except Exception as err:
        return -1, err

def id_exist(server_id):

    if server_id is None:
        return False

    sql = """SELECT server_id FROM ipliven WHERE server_id = %s"""
    res = conf['mysql'].select(sql, [server_id], one=True)
    return True if res else False

def get_cookies(cookies):
    dic = {}
    if not cookies:
        return dic
    for item in cookies.split(';'):
        _kv = item.split('=')
        dic[_kv[0].strip()] = _kv[1]
    return dic

def get_time(timestamp=None):
    if timestamp is None:
        timestamp = time.time()
    return time.strftime('%Y-%m-%d %X', time.localtime(timestamp))

def compose_url(protocol, _ip, port, uri):

    url = protocol + "://" + _ip + ":" + str(port) + uri
    return url

def get_sleep_time():
    """get sleep time to next minutes"""
    now = int(time.time())
    next_ts = now - now % 60 + 60
    sleep_time = 60 - now % 60
    return sleep_time, next_ts
