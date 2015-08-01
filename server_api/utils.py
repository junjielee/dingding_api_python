#!/usr/bin/env python
# encoding: utf-8

import urllib2
import logging
import json

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

path_log_file = '/tmp/dingding_test.log'

logger = logging.getLogger('dingding')
file_handler = logging.FileHandler(path_log_file)
formatter = logging.Formatter('%(asctime)s:%(name)s-->%(levelname)s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def http_get(url):
    try:
        response = urllib2.urlopen(url, timeout=10)
    except urllib2.URLError, e:
        logger.error(e)
    result = json.loads(response.read())
    return handle_result(result)


def http_post(url, data):
    headers = {
        "Content-Type": "application/json",
        "Accept-Charset": "utf-8"
    }
    request = urllib2.Request(url, json.dumps(data), headers)
    try:
        response = urllib2.urlopen(request, timeout=10)
    except urllib2.URLError, e:
        logger.error(e)
    result = json.loads(response.read())
    return handle_result(result)


def http_upload(url, data):
    # 在urllib2上注册http流处理句炳
    register_openers()
    # datagen 是一个生成器对象，返回编码过后的参数
    datagen, headers = multipart_encode(data)
    request = urllib2.Request(url, datagen, headers)

    try:
        response = urllib2.urlopen(request, timeout=10)
    except urllib2.URLError, e:
        logger.error(e)
    result = json.loads(response.read())

    return handle_result(result)


def http_download(url, media_file):
    try:
        response = urllib2.urlopen(url, timeout=10)
    except urllib2.URLError, e:
        logger.error(e)
    media_file.write(response.read())
    media_file.close()
    return True, 'success'


def handle_result(result):
    """
    return: 成功则返回True和结果，否则返回False和错误信息
    """
    if result.get('errcode') == 0:
        result.pop('errcode')
        result.pop('errmsg')
        return True, result
    else:
        errcode = result.get('erroce')
        errmsg = result.get('errmsg')
        logger.error('Error: %s | %s') % (errcode, errmsg)
        return False, errmsg
