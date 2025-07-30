# # 这是一个示例 Python 脚本。
#
# # 按 Shift+F10 执行或将其替换为您的代码。
# # 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#
#
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按装订区域中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

import requests

url = "https://dict.youdao.com/webtranslate"
data = {
    "i": "卧槽",
    "from": "zh-CHS",
    "to": "en",
    "useTerm": "false",
    "domain": "0",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": "2733b6cf116d1eff63208d5f7fb10873",
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": "1753859454709",
    "keyfrom": "fanyi.web",
    "mid": "1",
    "screen": "1",
    "model": "1",
    "network": "wifi",
    "abtest": "0",
    "yduuid": "abcdefg"
}
response = requests.post(url, data=data)

print(response.text)
print(response)