#! /usr/bin/env python3
# coding:utf-8
import time

from aliyunsdkcore.acs_exception.exceptions import ServerException, ClientException
from core import *


def dynamic_dns():
    try:
        ali_client = AliAcsClient(ali_access_key_id=ALI_ACCESS_KEY_ID,
                                  ali_access_key_secret=ALI_ACCESS_KEY_SECRET,
                                  ali_region_id=ALI_REGION_ID)
        public_ip = get_ip_with_tencent_lbs(TENCENT_LBS_KEY, TENCENT_LBS_SK)
        print("当前公网ip：", public_ip)
        record = ali_client.describe_domain_records(domain=DNS_DOMAIN, sub_domain=DNS_SUB_DOMAIN)
        record_value = record['DomainRecords']['Record'][0]['Value']
        if public_ip == record_value:
            print("公网IP无变化，无需更新")
        else:
            resp = ali_client.update_domain_record(domain=DNS_DOMAIN,
                                                   sub_domain=DNS_SUB_DOMAIN,
                                                   public_ip=public_ip,
                                                   dns_type=DNS_TYPE)
            print("解析设置成功:", resp)
    except (ServerException, ClientException) as e:
        print("[解析设置失败,原因：" + e.get_error_msg() + ']}')
    finally:
        print('时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == "__main__":
    dynamic_dns()
