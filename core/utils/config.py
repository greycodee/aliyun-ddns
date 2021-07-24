import os

ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
ACCESS_KEY_SECRET = os.getenv("ACCESS_KEY_SECRET")
REGION_ID = os.getenv("REGION_ID", "cn-hangzhou")
DNS_NAME = os.getenv("DNS_NAME")
TYPE = os.getenv("TYPE", "A")
