#! /usr/bin/env python3
#coding:utf-8
import json
import mAcsClient
from aliyunsdkcore.client import CommonRequest
#获取RecodeId

def getRecordIp(dnsName):
    client=mAcsClient.mAcsClient()
    request=CommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('DescribeDomainRecords')
    request.add_query_param('DomainName', 'mjava.top')

    response=client.do_action_with_exception(request).decode("utf-8")
    jsonObj=json.loads(response)
    DNSList=jsonObj['DomainRecords']['Record']
    for item in DNSList:
        if item['RR']==dnsName:
            return item['RecordId']