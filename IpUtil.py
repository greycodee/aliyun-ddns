#! /usr/bin/env python3
#coding:utf-8
import requests
import re

def getIP():
    respones=requests.get("http://2019.ip138.com/ic.asp")
    result=respones.text
    patte=r"(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
    matchs=re.search(patte,result)
    mIP=matchs.group(0)
    return mIP



