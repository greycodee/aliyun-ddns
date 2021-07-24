#! /usr/bin/env python3
# coding:utf-8
import json

from .ip_util import get_public_ip
from .config import *

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.client import CommonRequest


def acs_client():
    client = AcsClient(ALI_ACCESS_KEY_ID, ALI_ACCESS_KEY_SECRET, ALI_REGION_ID)
    return client


# 获取RecodeId
def get_record_ip(dns_name):
    client = acs_client()
    request = CommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('DescribeDomainRecords')
    request.add_query_param('DomainName', DNS_DOMAIN)

    response = client.do_action_with_exception(request).decode("utf-8")
    json_obj = json.loads(response)
    dns_list = json_obj['DomainRecords']['Record']
    for item in dns_list:
        if item['RR'] == dns_name:
            return item['RecordId']


def dynamic_dns():
    # 工具
    public_ip = get_public_ip()
    re_cord_ip = get_record_ip(DNS_NAME)
    print('{[公网IP:' + public_ip + ']')
    client = acs_client()
    request = CommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')
    request.add_query_param('RecordId', re_cord_ip)
    request.add_query_param('RR', DNS_NAME)
    request.add_query_param('Type', DNS_TYPE)
    request.add_query_param('Value', public_ip)

    resp = client.do_action_with_exception(request)
    print(resp)
