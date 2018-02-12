#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
baidu translate api.
'''
import requests
import hashlib
import random
import json

def translate(q, fromLang='en', toLang='zh'):
    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'

    myurl = 'https://api.fanyi.baidu.com/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    salt = str(salt)
    sign = appid+q+salt+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    reqData={'appid': appid, 'q': q , 'from': fromLang, 'to': toLang, 'salt': salt, 'sign': sign}

    try:
        r = requests.post(myurl, data=reqData)
        return json.loads(r.text.encode('latin-1').decode('unicode_escape'))
    except Exception as e:
        return e
