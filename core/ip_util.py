#! /usr/bin/env python3
# coding:utf-8
import requests
import re


# 获取Ip
def get_public_ip():
    return get_ip_138()


def get_ip_138():
    resp = requests.get("https://ip.qiyutech.tech/")
    result = resp.text
    pat = r"(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
    match = re.search(pat, result)
    ip = match.group(0)
    print(ip)
    return ip
