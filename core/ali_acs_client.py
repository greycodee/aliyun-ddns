#! /usr/bin/env python3
# coding:utf-8
import json

from .ip_util import get_public_ip
from .config import *

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.client import CommonRequest


class AliAcsClient(object):
    acs_clients = None

    def __init__(self, ali_access_key_id=None, ali_access_key_secret=None, ali_region_id=None):
        if ali_access_key_id == '' or ali_access_key_id is None:
            raise Exception("ali_access_key_id is Blank")
        if ali_access_key_secret == '' or ali_access_key_secret is None:
            raise Exception("ali_access_key_secret is Blank")
        if ali_region_id == '' or ali_region_id is None:
            raise Exception("ali_region_id is Blank")
        self.acs_clients = AcsClient(ali_access_key_id, ali_access_key_secret, ali_region_id)

    # DescribeDomainRecords
    # https://help.aliyun.com/document_detail/29776.html?spm=a2c4g.11186623.6.672.290e3d1dI65dDm
    # 获取指定 sun_domain 的 record 信息
    def describe_domain_records(self, domain, sub_domain):
        request = CommonRequest()
        request.set_domain('alidns.aliyuncs.com')
        request.set_version('2015-01-09')
        request.set_action_name('DescribeDomainRecords')
        request.add_query_param('DomainName', domain)
        request.add_query_param('RRKeyWord', sub_domain)

        response = self.acs_clients.do_action_with_exception(request).decode("utf-8")
        json_obj = json.loads(response)
        return json_obj

    def get_sub_domain_record_id(self, domain, sub_domain):
        records = self.describe_domain_records(domain, sub_domain)
        return records['DomainRecords']['Record'][0]['RecordId']

    def update_domain_record(self, domain, sub_domain, public_ip, dns_type):
        request = CommonRequest()
        request.set_domain('alidns.aliyuncs.com')
        request.set_version('2015-01-09')
        request.set_action_name('UpdateDomainRecord')
        request.add_query_param('RecordId', self.get_sub_domain_record_id(domain, sub_domain))
        request.add_query_param('RR', sub_domain)
        request.add_query_param('Type', dns_type)
        request.add_query_param('Value', public_ip)

        resp = self.acs_clients.do_action_with_exception(request)
        print(resp)
