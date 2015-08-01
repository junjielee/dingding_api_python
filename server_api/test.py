#!/usr/bin/env python
# encoding: utf-8

from config import CorpID, secret
import auth
import message
import user
import department
import media

def print_dict(result):
    for k, v in result.iteritems():
        print '%s : %s' % (k, v)

is_success, result = auth.get_access_token(CorpID, secret)
access_token = result.get('access_token')

# department
# is_success, result = department.get_department_list(access_token)
# print_dict(result)

# message
touser = 'manager7701'
toparty = '1868210'
# send_type = 'text'
# content = {'content': 'dingding'}

send_type = 'image'
content = {'media_id': '@lADOAMnd1M0Bqc0CgA'}
is_success, result = message.send(access_token, touser, toparty,
                                  send_type, content)
print result


# media
# media_type = 'image'
# media_file = open('./picture_test.jpg', 'rb')
# is_success, result = media.upload_media(access_token, media_type, media_file)
# print result

# picture_media_id = '@lADOAMnd1M0Bqc0CgA'
