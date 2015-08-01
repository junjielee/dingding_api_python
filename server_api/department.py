#!/usr/bin/env python
# encoding: utf-8

from urllib import urlencode

from config import API_ADDR
from utils import http_get, http_post


def get_department_list(access_token):
    url = 'https://%s/department/list?' % API_ADDR
    args = {
        'access_token': access_token
    }
    url += urlencode(args)
    return http_get(url)


def create_department(access_token, name, parentid, order=1):
    url = 'https://%s/department/create' % API_ADDR
    args = {
        'access_token': access_token
    }
    url += urlencode(args)
    data = {
        'access_token': access_token,
        'name': name,
        'parentid': parentid,
        'order': str(order)
    }
    return http_post(url, data)


def update_department(access_token, name, parentid, order, department_id):
    url = 'https://%s/department/update?' % API_ADDR
    args = {
        'access_token': access_token
    }
    url += urlencode(args)
    data = {
        'access_token': access_token,
        'id': department_id,
        'name': name,
        'parentid': parentid,
        'order': order
    }
    return http_post(url, data)


def delete_department(access_token, department_id):
    url = 'https://%s/department/delete?' % API_ADDR
    args = {
        'access_token': access_token,
        'id': department_id
    }
    url += urlencode(args)
    return http_get(url)
