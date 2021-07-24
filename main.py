#! /usr/bin/env python3
# coding:utf-8
import time

from aliyunsdkcore.acs_exception.exceptions import ServerException, ClientException
from core import *


if __name__ == "__main__":
    try:
        ali_client = AliAcsClient(ali_access_key_id=ALI_ACCESS_KEY_ID,
                                  ali_access_key_secret=ALI_ACCESS_KEY_SECRET,
                                  ali_region_id=ALI_REGION_ID)

        ali_client.update_domain_record(domain=DNS_DOMAIN,
                                        sub_domain=DNS_SUB_DOMAIN,
                                        public_ip=get_public_ip(),
                                        dns_type=DNS_TYPE)

        print('[时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']')
        print("[解析设置成功]}")
    except (ServerException, ClientException) as e:
        print('[时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']')
        print("[解析设置失败,原因：" + e.get_error_msg() + ']}')
