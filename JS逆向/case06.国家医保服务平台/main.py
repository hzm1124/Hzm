from time import time
from base64 import b64encode, b64decode
import execjs
import requests
import json


page = 1
appCode = 'T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ'
encType = 'SM4'
signType = 'SM2'
timestamp = str(int(time()))
version = '1.0.0'
appSecret = 'NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P'
privateKey = 'AJxKNdmspMaPGj+onJNoQ0cgWk2E3CYFWKBJhpcJrAtC'
privateKey = bytes.hex(b64decode(privateKey))
print(privateKey)
print()

with open('./js_enc_data.js', 'r', encoding='utf-8') as f:
    js = execjs.compile(f.read())

n = '{"keyWords":"","drugType":"","pageNo":' + str(page) + ',"pageSize":10,"medListCodg":"X"}'
enc_data = js.call('get_enc_data', n, appCode, appSecret)
print(enc_data)
print()

with open('./js_sign_data.js', 'r', encoding='utf-8') as f:
    js_2 = execjs.compile(f.read())

r = 'appCode=' + appCode + '&data={"medListCodg":"X","pageNo":"' + str(page) + '","pageSize":"10"}&encType=' + encType + '&signType=' + signType + '&timestamp=' + timestamp + '&version=' + version + '&key=' + appSecret

sign_data = js_2.call('get_sign_data', r, privateKey)
sign_data = b64encode(bytes.fromhex(sign_data)).decode()
print(sign_data)
print()

headers = {'Content-Type': 'application/json'}
data = {'data': {'data': {'encData': enc_data},
                 'appCode': appCode,
                 'version': version,
                 'encType': encType,
                 'signType': signType,
                 'timestamp': timestamp,
                 'signData': sign_data}}
data = json.dumps(data, separators=(',', ':'))
response = requests.post('https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryWmTcmpatInfoBFromEs',
                         headers=headers,
                         data=data)
print(response.text)
print(response)
print()

# = = =  = = =  = = =   = = =  = = =  = = =   = = =  = = =  = = =

dict_ = json.loads(bytes(js.call('decrypt', list(bytes.fromhex(response.json()['data']['data']['encData'])), appCode, appSecret)).decode())
print(dict_)
