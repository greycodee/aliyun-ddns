#! /usr/bin/env python3
# coding:utf-8
from aliyunsdkcore.acs_exception.exceptions import ServerException, ClientException

from utils import util
from aliyunsdkcore.client import CommonRequest
from core import ali_acs_client
import time
import configparser
import os


def dynamic_dns():
    # 获取环境变量
    env_list = os.environ
    for key in env_list:
        print(key + "#######" + env_list[key])
    # 读取配置文件
    cf = configparser.ConfigParser()
    # cf.read('config.conf')
    cf.read(env_list['DDNS'] + '/config.conf')
    dns_name = cf.get('dns', 'dns_name')
    ty = cf.get('dns', 'type')
    # 工具
    m_ip = util.get_ip()
    re_cord_ip = util.get_record_ip(dns_name)
    print('{[公网IP:' + m_ip + ']')
    client = ali_acs_client.acs_client()
    request = CommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')
    request.add_query_param('RecordId', re_cord_ip)
    request.add_query_param('RR', dns_name)
    request.add_query_param('Type', ty)
    request.add_query_param('Value', m_ip)

    resp = client.do_action_with_exception(request)
    print(resp)


if __name__ == "__main__":
    try:
        dynamic_dns()
        print('[时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']')
        print("[解析设置成功]}")
    except (ServerException, ClientException) as e:
        print('[时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']')
        print("[解析设置失败,原因：" + e.get_error_msg() + ']}')
