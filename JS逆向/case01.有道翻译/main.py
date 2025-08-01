from time import time
from js_sign import get_sign
import requests
from hashlib import md5
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import json


response = requests.get('https://shared.ydstatic.com/dict/translation-website/0.6.8/js/app.7eeb3f2d.js')
print(response)

t = response.text.split('webfanyi-key-getter-2025')[1].split('n="')[1].split('"')[0]
print(f't: {t}')
print()

# = = =  = = =  = = =   = = =  = = =  = = =   = = =  = = =  = = =

client = 'fanyideskweb'
timestamp = str(int(time() * 1000))
product = 'webfanyi'

dict_param = {'keyid': 'webfanyi-key-getter-2025',
              'sign': get_sign(client, timestamp, product, t),
              'client': client,
              'product': product,
              'pointParam': 'client,mysticTime,product',
              'mysticTime': timestamp}
response = requests.get('https://dict.youdao.com/webtranslate/key',
                        params=dict_param)
print(response)

dict_ = response.json()
key, aes_key, aes_iv = dict_['data']['secretKey'], dict_['data']['aesKey'], dict_['data']['aesIv']
print(f'key: {key}, aes_key: {aes_key}, aes_iv: {aes_iv}')
print()

# = = =  = = =  = = =   = = =  = = =  = = =   = = =  = = =  = = =

timestamp = str(int(time() * 1000))

data = {'i': '机密',
        'from': 'zh-CHS',
        'to': 'en',
        'keyid': product,
        'sign': get_sign(client, timestamp, product, key),
        'client': client,
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': timestamp}
response = requests.post('https://dict.youdao.com/webtranslate',
                         data=data)
print(response)
print(response.text)
print()

# = = =  = = =  = = =   = = =  = = =  = = =   = = =  = = =  = = =

md5_, md5_2 = md5(), md5()

md5_.update(aes_key.encode()), md5_2.update(aes_iv.encode())
key, iv = md5_.digest(), md5_2.digest()
print(f'key: {key}, length: {len(key)}\niv: {iv}, length: {len(iv)}')

# = = =  = = =  = = =   = = =  = = =  = = =   = = =  = = =  = = =

response = b64decode(response.text.replace('-', '+').replace('_', '/').encode())
aes = AES.new(key, AES.MODE_CBC, iv=iv)
response = json.loads(unpad(aes.decrypt(response), 16).decode())
print(response)
