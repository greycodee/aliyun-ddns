#! /usr/bin/env python3
# coding:utf-8
import json

import requests
import hashlib
from .run_exception import RunTimeException


# 获取腾讯位置 api 返回的 ip
def get_ip_with_tencent_lbs(lbs_key, sk):
    base_url = "https://apis.map.qq.com/ws/location/v1/ip"
    sign_string = "/ws/location/v1/ip?key="+lbs_key+sk
    sign = hashlib.md5(sign_string.encode(encoding='GBK')).hexdigest()
    request_url = base_url+"?key="+lbs_key+"&sig="+sign
    resp = requests.get(request_url).text
    json_obj = json.loads(resp)
    if json_obj['status'] == 0:
        return json_obj['result']['ip']
    else:
        raise RunTimeException("获取IP失败，原因："+json_obj['message'])

