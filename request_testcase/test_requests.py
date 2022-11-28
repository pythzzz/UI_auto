import requests
import pytest
import yaml

def test_baidu(login):
    url='https://www.baidu.com'
    res=requests.request(method='get',url=url)
    print('请求百度')
    print(res.json)
    # print(res.text)
    print(res.encoding)
    print(res.cookies)
