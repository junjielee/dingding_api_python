#!/usr/bin/env python
# encoding: utf-8

from urllib import urlencode

from config import API_ADDR
from utils import http_get, http_post


def get_user(access_token, userid):
    url = 'https://%s/user/get?' % API_ADDR
    args = {
        'access_token': access_token,
        'userid': userid
    }
    url += urlencode(args)
    return http_get(url)


def create_or_update_user(access_token, userid, name, department,
                          position, mobile, email, extattr):
    url = 'https://%s/user/create?' % API_ADDR
    args = {
        'access_token': access_token
    }
    url += urlencode(args)
    data = {
        'access_token': access_token,
        'userid': userid,
        'name': name,
        'department': department,
        'position': position,
        'mobile': mobile,
        'email': email,
        'extattr': extattr
    }
    return http_post(url, data)


def delete_user(access_token, userid):
    url = 'https://%s/user/delete?' % API_ADDR
    args = {
        'access_token': access_token,
        'userid': userid
    }
    url += urlencode(args)
    return http_get(url)


def delete_user_list(access_token, useridlist):
    url = 'https://%s/user/batchdelete?' % API_ADDR
    args = {
        'access_token': access_token
    }
    url += urlencode(args)
    data = {
        'access_token': access_token,
        'useridlist': useridlist
    }
    return http_post(url, data)


def get_department_simple_userlist(access_token, department_id,
                                   fetch_child=0):
    url = 'https://%s/user/simplelist?' % API_ADDR
    args = {
        'access_token': access_token,
        'department_id': department_id,
        'fetch_child': fetch_child
    }
    url += urlencode(args)
    return http_get(url)


def get_department_detail_userlist(access_token, department_id,
                                   fetch_child=0):
    url = 'https://%s/user/list?' % API_ADDR
    args = {
        'access_token': access_token,
        'department_id': department_id,
        'fetch_child': fetch_child
    }
    url += urlencode(args)
    return http_get(url)
