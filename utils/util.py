#! /usr/bin/env python3
# coding:utf-8

from core import describe_domains
import requests
import re


# 获取Ip
def get_ip():
    return get_ip_138()


# 获取RecodeID
def get_record_ip(dns_name):
    return describe_domains.get_record_ip(dns_name)


def get_ip_138():
    resp = requests.get("http://2019.ip138.com/ic.asp")
    result = resp.text
    pat = r"(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
    match = re.search(pat, result)
    ip = match.group(0)
    return ip
