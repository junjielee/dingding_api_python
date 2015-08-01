#!/usr/bin/env python
# encoding: utf-8

from urllib import urlencode

from config import API_ADDR
from utils import http_upload, http_download


def upload_media(access_token, media_type, media_file):
    url = 'https://%s/media/upload?' % API_ADDR
    args = {
        'access_token': access_token,
        'type': media_type
    }
    url += urlencode(args)
    data = {
        'access_token': access_token,
        'type': media_type,
        'media': media_file
    }
    return http_upload(url, data)


def download_media(access_token, media_id):
    url = 'https://%s/media/get?' % API_ADDR
    args = {
        'access_token': access_token,
        'media_id': media_id
    }
    url += urlencode(args)
    return http_download(url)
