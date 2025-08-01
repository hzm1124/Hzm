import execjs
import requests


with open('./js_data.js', 'r', encoding='utf-8') as f:
    js = execjs.compile(f.read())

i0x = {'rid': 'R_SO_4_1852762860',
       'threadId': 'R_SO_4_1852762860',
       'pageNo': '1',
       'pageSize': '20',
       'cursor': '-1',
       'offset': '0',
       'orderType': '1',
       'csrf_token': ''};

dict_data = js.call('get_data', i0x)
print(dict_data)
print()

response = requests.post('https://music.163.com/weapi/comment/resource/comments/get',
                         data=dict_data)
print(response)
print()

dict_ = response.json()

list_comment = dict_['data']['comments']
for i, comment in enumerate(list_comment):
    print(f'''{i + 1}. {comment['content'].strip()}''')
print()

cursor = dict_['data']['cursor']
print(cursor)
print()

dict_data = js.call('get_data', {**i0x, 'cursor': cursor})
print(dict_data)
print()

response = requests.post('https://music.163.com/weapi/comment/resource/comments/get',
                         data=dict_data)
print(response)
print()

dict_ = response.json()

list_comment = dict_['data']['comments']
for i, comment in enumerate(list_comment):
    print(f'''{i + 1}. {comment['content'].strip()}''')
print()
