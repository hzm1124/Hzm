import execjs
from time import time
import requests


with open('./js_sign.js', 'r', encoding='utf-8') as f:
    js = execjs.compile(f.read())

cid = '508'
param = {'cityId': '301',
         'serialId': '11108'}
o = '19DDD1FBDFF065D3A4DA777D2D7A81EC'
timestamp = str(int(time() * 1000))

sign = js.call('get_sign', cid, param, o, timestamp)
print(sign)
print()

dict_param = {'cid': cid,
              'param': sign['json_param']}
dict_header = {'x-platform': 'pc',
               'x-sign': sign['sign'],
               'x-timestamp': timestamp}
response = requests.get('https://mhapi.yiche.com/hcar/h_car/api/v1/param/get_param_details',
                        params=dict_param,
                        headers=dict_header)
print(response.text)
print(response)
