#!/usr/bin/env python
# encoding: utf-8
import time
import hashlib

from urllib import urlencode
from config import API_ADDR
from utils import http_get
from random import randint

default_char_list='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456_'


def get_access_token(corp_id, secret):
    url = 'https://%s/gettoken?' % API_ADDR
    args = {
        'corpid': corp_id,
        'corpsecret': secret
    }
    url += urlencode(args)
    return http_get(url)


def get_jsapi_ticket(access_token):
    url = 'https://%s/get_jsapi_ticket?' % API_ADDR
    args = {
        'access_token': access_token,
        'type': 'jsapi'
    }
    url += urlencode(args)
    return http_get(url)


def get_timestamp():
    return str(int(time()))


def sha1(s):
    return hashlib.sha1(s).hexdigest()


def get_random_string(length=16, char_list=default_char_list):
    string = ''
    for i in range(length):
        string += char_list[randint(0, len(char_list) - 1)]
    return string


def sign(jsapi_ticket, noncestr, timestamp, url):
    string = 'jsapi_ticket=%s&noncestr=%s&timestamp=%s&url=%s' % \
        (jsapi_ticket, noncestr, timestamp, url)
    return sha1(string)
