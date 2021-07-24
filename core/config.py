import os

ALI_ACCESS_KEY_ID = os.getenv("ALI_ACCESS_KEY_ID")
ALI_ACCESS_KEY_SECRET = os.getenv("ALI_ACCESS_KEY_SECRET")
ALI_REGION_ID = os.getenv("ALI_REGION_ID", "cn-hangzhou")
DNS_TYPE = os.getenv("DNS_TYPE", "A")
DNS_DOMAIN = os.getenv("DNS_DOMAIN")
DNS_SECOND_DOMAIN = os.getenv("DNS_SECOND_DOMAIN")

