import json
import execjs
import requests
from time import time


headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://y.qq.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://y.qq.com/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "pgv_pvid": "9871390400",
    "fqm_pvqid": "12044ca1-341a-4948-b969-e1307aaf3d7f",
    "ts_uid": "9685035776",
    "ptui_loginuin": "1210882202",
    "RK": "1ml8G147QP",
    "ptcz": "9b125697dde105f03a87c2021f22cd7397ee9772ab9973ea59414469b6b3b447",
    "music_ignore_pskey": "202306271436Hn@vBj",
    "fqm_sessionid": "33373c78-6d00-4793-aeee-35c6d51f2b74",
    "pgv_info": "ssid=s8136997953",
    "ts_last": "y.qq.com/n/ryqq/search",
    "_qpsvr_localtk": "0.7382564119068027",
    "login_type": "1",
    "tmeLoginType": "2",
    "psrf_musickey_createtime": "1754632071",
    "psrf_qqrefresh_token": "00C700824AD9715EA48FECF17B0B8395",
    "qqmusic_key": "Q_H_L_63k3Nm2QSGjcnIg_GV-ReBvNpU3FdstmEcQXsSuPcy_tMSMSgupvsKaYI3TA_2a2bGfof5cSbDyiI2sRAoQRYZLxl",
    "euin": "oK-5oecFow-zoc**",
    "psrf_qqunionid": "77594EF6098BE9D4DD671155BE9CA278",
    "psrf_qqaccess_token": "C6DE4D405373FC2F53CDACB1FB6BC129",
    "uin": "1210882202",
    "psrf_access_token_expiresAt": "1759816071",
    "qm_keyst": "Q_H_L_63k3Nm2QSGjcnIg_GV-ReBvNpU3FdstmEcQXsSuPcy_tMSMSgupvsKaYI3TA_2a2bGfof5cSbDyiI2sRAoQRYZLxl",
    "psrf_qqopenid": "C72280C5252B6E9B254BDAF2CAC14EC8",
    "wxopenid": "",
    "wxrefresh_token": "",
    "wxunionid": ""
}
data = {'comm': {'cv': 4747474,
  'ct': 24,
  'format': 'json',
  'inCharset': 'utf-8',
  'outCharset': 'utf-8',
  'notice': 0,
  'platform': 'yqq.json',
  'needNewCode': 1,
  'uin': 1210882202,
  'g_tk_new_20200303': 1164859883,
  'g_tk': 1164859883},
 'req_1': {'method': 'DoSearchForQQMusicDesktop',
  'module': 'music.search.SearchCgiService',
  'param': {'remoteplace': 'txt.yqq.top',
   'searchid': '58782687719576779',
   'search_type': 0,
   'query': '离别的秋天',
   'page_num': 1,
   'num_per_page': 10}}}
data = json.dumps(data, separators=(',', ':'))

with open('./js_sign.js', 'r', encoding='utf-8') as f:
    js = execjs.compile(f.read())

sign = js.call('get_sign', data)
print(sign)
print()

params = {
    "_": str(int(time() * 1000)),
    "sign": sign
}

response = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg',
                         headers=headers,
                         cookies=cookies,
                         params=params,
                         data=data)

print(response.text)
print(response)
