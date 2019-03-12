#! /usr/bin/env python3
#coding:utf-8

import IpUtil
import DescribeDomains
#获取Ip
def getIP():
    return IpUtil.getIP()

#获取RecodeID
def getRecordIp(dnsName):
    return DescribeDomains.getRecordIp(dnsName)