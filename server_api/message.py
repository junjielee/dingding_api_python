#!/usr/bin/env python
# encoding: utf-8

from urllib import urlencode

from config import API_ADDR
from utils import http_post


def send(access_token, touser, toparty, send_type, content, agentid=3873399):
    """
    params:
        content: send_type对应的content，是一个字典，具体type的字段属性看文档
    """
    url = "https://%s/message/send?" % API_ADDR
    args = {
        "access_token": access_token
    }
    url += urlencode(args)
    data = {
        "access_token": access_token,
        "touser": touser,
        "toparty": toparty,
        "agentid": agentid,
        "msgtype": send_type,
        send_type: content
    }
    return http_post(url, data)
