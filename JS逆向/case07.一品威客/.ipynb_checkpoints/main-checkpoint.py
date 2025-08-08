from time import time
import execjs
import requests


timestamp = int(time())
NonceStr = f'{timestamp}abcde'
username = '13756268412'
password = '123456'
code = '9u9m'

with open('./js_signature.js', 'r', encoding='utf-8') as f:
    js = execjs.compile(f.read())

signature = js.call('get_signature', timestamp, NonceStr, username, password, code)
print(signature)
print()

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Access-Token;": "",
    "App-Id": "4ac490420ac63db4",
    "App-Ver;": "",
    "CHOST": "www.epwk.com",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Device-Os": "web",
    "Device-Ver;": "",
    "Imei;": "",
    "NonceStr": NonceStr,
    "Origin": "https://www.epwk.com",
    "Os-Ver;": "",
    "Pragma": "no-cache",
    "Referer": "https://www.epwk.com/login.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Signature": signature,
    "Timestemp": str(timestamp),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "X-REQUEST-ID": "6b5c940d11fac42adc95817ba523104e",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "login_fail_need_graphics": "1",
    "HWWAFSESID": "f75df732e53904bd3c",
    "HWWAFSESTIME": "1754526782448",
    "Hm_lvt_387b8f4fdb89d4ea233922bdc6466394": "1754466695,1754526782",
    "Hm_lpvt_387b8f4fdb89d4ea233922bdc6466394": "1754526782",
    "HMACCOUNT": "180D1B1278F51E25",
    "PHPSESSID": "418dc4c15dd3074295146f4a0740cf431cff2163",
    "time_diff": "-1",
    "XDEBUG_SESSION": "XDEBUG_ECLIPSE",
    "banners_show_cookie_ip": "112.111.13.248"
}
url = "https://www.epwk.com/api/epwk/v1/user/login"
data = {
    "username": username,
    "password": password,
    "code": code,
    "hdn_refer": ""
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)
