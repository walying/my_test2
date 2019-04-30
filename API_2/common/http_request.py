# -*- coding: utf-8 -*-
# @Time     :2019/4/17  9:59
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :http_request.py

import requests
from API_2.common import logger
from API_2.common import config

class HTTPRequest:
    """
    使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """
    def request(self,method,url,data=None,json=None,cookies=None):
        if type(data)==str:
            data=eval(data)
        if method.upper()=='GET':
            resp=requests.get(url,params=data,cookies=cookies)
        elif method.upper()=='POST':
            if json:
                resp=requests.post(url,json=json,cookies=cookies)
            else:
                resp=requests.post(url,data=data,cookies=cookies)
        else:
            print('UN-support method')

        return resp


class HTTPRequest2:
    """
    使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """
    # 生成Log文件
    logger = logger.get_logger(__name__)
    def __init__(self):
        #打开一个session
        self.session=requests.sessions.session()

    def request(self,method,url,data=None,json=None):
        if type(data)==str:
            data=eval(data)
        #拼接url
        url=config.ReadConfig().get('api','pre_url')+url
        self.logger.debug('请求url:{0}'.format(url))
        self.logger.debug('请求data:{0}'.format(data))
        if method.upper()=='GET':
            resp=self.session.request(method=method, url=url, params=data)
        elif method.upper()=='POST':
            if json:
                resp = self.session.request(method=method, url=url, json=data)
            else:
                resp = self.session.request(method=method, url=url, data=data)
        else:
            resp=None
            self.logger.error('UN-support method')
        self.logger.debug('请求response:{0}'.format(resp.text))
        return resp

    def close(self):
        self.session.close()

if __name__ == '__main__':
    params={'mobilephone':'13011836510','pwd':'123456'}
    resp=HTTPRequest2()#登录、充值打开同一个session
    resp2=resp.request('post','/member/login',data=params)
    print(resp2.text)

    params2 = {'mobilephone': '13011836510', 'amount': '1111'}
    resp3 = resp.request('post', url='/member/recharge', data=params2)
    print(resp3.text)