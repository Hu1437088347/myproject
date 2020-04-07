import random
import requests
import time


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    # print("random = ",s)
    # print("ts= ",t)
    # print("salt= ",t+s)
    return  t+s
    # return '15853783488690'



def get_sign():
    return '6b9a6ce3ff157252d9a388c507e70474'


def get_ts():
    return '1585378348869'


form_data={
    'i':'我们都爱你',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': '70244e0061db49a9ee62d341c5fed82a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,data=form_data)
print(response.text)