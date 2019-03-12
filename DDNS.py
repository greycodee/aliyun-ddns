#! /usr/bin/env python3
#coding:utf-8
from aliyunsdkcore.acs_exception.exceptions import ServerException, ClientException

import Utils
from aliyunsdkcore.client import CommonRequest
import mAcsClient
import time
import configparser

def DDNS():
    #读取配置文件
    cf = configparser.ConfigParser();
    cf.read('config.conf')
    DnsName=cf.get('dns','dns_name')
    Type=cf.get('dns','type')
    # 工具
    mIP=Utils.getIP()
    reCordIP=Utils.getRecordIp(DnsName)
    print('{[公网IP:'+mIP+']')
    client = mAcsClient.mAcsClient()
    request=CommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')
    request.add_query_param('RecordId', reCordIP)
    request.add_query_param('RR', DnsName)
    request.add_query_param('Type', Type)
    request.add_query_param('Value', mIP)

    reponse=client.do_action_with_exception(request)
    print(reponse)
if __name__ == "__main__":
    try:
        DDNS()
        print('[时间:'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+']' )
        print("[解析设置成功]}")
    except (ServerException,ClientException) as e:
        print('[时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']')
        print("[解析设置失败,原因："+e.get_error_msg()+']}')



