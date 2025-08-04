import execjs
import json
import requests


with open('./js_hexin_v.js', 'r', encoding='utf-8') as f:
    js = execjs.compile(f.read())

hexin_v = js.call('R')
print(hexin_v)
print()

headers = {'Content-Type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
           'hexin-v': hexin_v}
data = {'source': 'Ths_iwencai_Xuangu',
        'version': '2.0',
        'add_info': "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\",\"searchInfo\":true}",
        'question': '今日涨停',
        'perpage': 50,
        'page': 1}
data = json.dumps(data, separators=(',', ':'))
response = requests.post('https://www.iwencai.com/customized/chart/get-robot-data',
                         headers=headers,
                         data=data)

print(response.text)
print(response)
