# 动态域名解析（DDNS）

## 运行环境
- python3

## 运行前准备
程序从环境变量中获取配置，运行前先设置环境变量

环境变量 | 说明
---- | ---
ALI_ACCESS_KEY_ID | 阿里云 ACCESS_KEY_ID（必填）
ALI_ACCESS_KEY_SECRET |  阿里云 ACCESS_KEY_SECRET（必填）
ALI_REGION_ID | 阿里云区域ID（默认：cn-hangzhou）
DNS_TYPE | 解析类型（默认：A）
DNS_DOMAIN | 域名（必填）
DNS_SECOND_DOMAIN | 二级域名（默认：@）

### 环境字段说明

**DNS_TYPE** 支持的解析类型：
- A：将域名指向一个IPV4地址
- CNAME：将域名指向另外一个域名
- AAAA：将域名指向一个IPV6地址

**DNS_SECOND_DOMAIN** 域名前缀，常见用法有：

- www：解析后的域名为www.aliyun.com。

- @：直接解析主域名 aliyun.com。

- *：泛解析，匹配其他所有域名 *.aliyun.com。

- mail：将域名解析为mail.aliyun.com，通常用于解析邮箱服务器。

- 二级域名：如：abc.aliyun.com，填写abc。

- 手机网站：如：m.aliyun.com，填写m。

- 显性URL：不支持泛解析（泛解析：将所有子域名解析到同一地址）

## 运行
当设置好环境变量后，使用以下命令安装依赖
```shell
pip3 install -r requeirments.txt
```
安装依赖后，直接运行 `main.py`
```shell
python main.py
```

