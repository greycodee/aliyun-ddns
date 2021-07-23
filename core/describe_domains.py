#! /usr/bin/env python3
# coding:utf-8
import json
from core import ali_acs_client
from aliyunsdkcore.client import CommonRequest


# 获取RecodeId

def get_record_ip(dns_name):
    client = ali_acs_client.acs_client()
    request = CommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('DescribeDomainRecords')
    request.add_query_param('DomainName', 'mjava.top')

    response = client.do_action_with_exception(request).decode("utf-8")
    json_obj = json.loads(response)
    dns_list = json_obj['DomainRecords']['Record']
    for item in dns_list:
        if item['RR'] == dns_name:
            return item['RecordId']
