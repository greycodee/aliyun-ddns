#! /usr/bin/env python3
# coding:utf-8
import time

from aliyunsdkcore.acs_exception.exceptions import ServerException, ClientException
from core import dynamic_dns

if __name__ == "__main__":
    try:
        dynamic_dns()
        print('[时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']')
        print("[解析设置成功]}")
    except (ServerException, ClientException) as e:
        print('[时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']')
        print("[解析设置失败,原因：" + e.get_error_msg() + ']}')
