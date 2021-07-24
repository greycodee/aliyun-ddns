import os

ALI_ACCESS_KEY_ID = os.getenv("ALI_ACCESS_KEY_ID")
ALI_ACCESS_KEY_SECRET = os.getenv("ALI_ACCESS_KEY_SECRET")
ALI_REGION_ID = os.getenv("ALI_REGION_ID", "cn-hangzhou")
DNS_TYPE = os.getenv("DNS_TYPE", "A")
DNS_DOMAIN = os.getenv("DNS_DOMAIN")
DNS_SUB_DOMAIN = os.getenv("DNS_SUB_DOMAIN")

# 腾讯位置
# https://lbs.qq.com/
TENCENT_LBS_KEY = os.getenv("TENCENT_LBS_KEY")
TENCENT_LBS_SK = os.getenv("TENCENT_LBS_SK")
