#! /usr/bin/env python3
# coding:utf-8
import configparser
import os


from aliyunsdkcore.client import AcsClient


def acs_client():
    env_list = os.environ
    cf = configparser.ConfigParser()
    # cf.read('config.conf')
    cf.read('./config.conf')
    access_key_id = cf.get('acs', 'accesskey_id')
    access_key_secret = cf.get('acs', 'accesskey_secret')
    region_id = cf.get('acs', 'region_id')
    client = AcsClient(access_key_id, access_key_secret, region_id)
    return client
