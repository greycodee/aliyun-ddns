FROM python:3.6
LABEL name=greycode
LABEL email=zhengminghui99@gmail.com
COPY core /root/core
COPY main.py /root/main.py
COPY requeirments.txt /requeirments.txt
RUN pip install -r requeirments.txt
# 请替换环境变量为你的数据
ENV ALI_ACCESS_KEY_ID=替换你的阿里云ACCESS_KEY_ID
ENV ALI_ACCESS_KEY_SECRET=替换你的阿里云ACCESS_KEY_SECRET
ENV ALI_REGION_ID=cn-hangzhou
ENV DNS_SUB_DOMAIN=替换你要更新的二级域名名称
ENV DNS_TYPE=A
ENV DNS_DOMAIN=你的域名
ENV TENCENT_LBS_KEY=腾讯位置的应用KEY
ENV TENCENT_LBS_SK=腾讯位置的应用签名SK
WORKDIR /root
CMD ["nohup","python","/root/main.py","&"]
