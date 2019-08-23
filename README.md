# DDNS

## 1.修改config.conf配置文件，改成你的相关消息

## 2.服务器安装python3（如已安装跳过）

## 3.服务器安装阿里云的python SDK 
* 如果您使用Python 2.x，执行以下命令，安装阿里云SDK核心库：
pip install aliyun-python-sdk-core
* 如果您使用Python 3.x，执行以下命令，安装阿里云SDK核心库：
pip install aliyun-python-sdk-core-v3
>地址：https://help.aliyun.com/document_detail/53090.html
## 4.把代码放在/opt/DDNS目录下面

## ５.设置linux的定时启动任务,在定时任务里加上这一条
* */10 * * * * export DDNS=/opt/DDNS;/usr/bin/python3 /opt/DDNS/DDNS.py>>/opt/DDNS/ddns.log



