import requests


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i':'我们都爱你',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15853783488690',
    'sign': '6b9a6ce3ff157252d9a388c507e70474',
    'ts': '1585378348869',
    'bv': '70244e0061db49a9ee62d341c5fed82a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)