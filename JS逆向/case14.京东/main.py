from hashlib import sha256
import subprocess
import json
import requests


body = '{"tenantCode":"jgm","bizModelCode":5,"bizModeClientType":"M","externalLoginType":"1","key":"汽机油","datatype":"1","page":"1","pagesize":"10","ext_attr":"no","brand_col":"no","price_col":"no","color_col":"no","size_col":"no","ext_attr_sort":"no","merge_sku":"yes","multi_suppliers":"yes","area_ids":"1,72,55674","filt_type":"redisstore,1;","qp_disable":"no","debug":"false","t1":"1755823372748"}'

sha256_ = sha256()
sha256_.update(body.encode())
response = sha256_.hexdigest()

r = {"functionId": "searchKeyword",
     "appid": "jd-cphdeveloper-m",
     "body": response}

result = subprocess.run(['node', './js.js', json.dumps(r)], capture_output=True, text=True, encoding='utf-8')
h5st = result.stdout.strip()

headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "origin": "https://so.m.jd.com",
    "priority": "u=1, i",
    "referer": "https://so.m.jd.com/",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
    "x-referer-page": "https://so.m.jd.com/ware/search.action",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "jsavif": "1",
    "shshshfpa": "07d2f2a9-4474-2445-6181-a14e519a7bd9-1755822323",
    "shshshfpx": "07d2f2a9-4474-2445-6181-a14e519a7bd9-1755822323",
    "__jdu": "1507890925",
    "areaId": "16",
    "ipLoc-djd": "16-1303-1305-48927",
    "PCSYCityID": "CN_350000_350100_0",
    "wlfstk_smdl": "c5zrxfjibc1m59iu6bfpq0nbr7ip840l",
    "__jdc": "76161171",
    "3AB9D23F7A4B3C9B": "HQXSEMIU5PUTULJWIJBQVT54RO474JTRARROAH2GBYNUXDXTBTDGP2EKM4G57NXVNWCHQIEKHYINVCWV422QX4ZT7Q",
    "__jda": "76161171.1507890925.1755822322.1755822803.1755822806.7",
    "unpl": "JF8EALBnNSttC0sBVhNQGxoUSlsHWw8BTh4GbDMHAwheQ1ACTAVLFBN7XlVdWRRKHh9sZBRVVFNJUg4ZBSsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAh8TFkJVVVZeDHsWM2hXNWRZXk1RBRkyGiIRex8AAl4AThQDaCoFUFxeQlwEEwEfIhF7Xg",
    "__jdv": "76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_b1db9c19507b4c84842e3fd7956f6a72|1755823079668",
    "mba_muid": "1507890925",
    "autoOpenApp_downCloseDate__jd_czlogin_openapp_": "1755823120810_1",
    "jcap_dvzw_fp": "57kMS8Nn3wBQrOkr1lyzLQrDzDar4mTKOen09xVh_Mcld27l23D_FYA6F3P8cHIzGgQN3PA51L51BjyjqLChPkUHqLE=",
    "TrackerID": "iCEFYpfd9vJIBlwWrNQh3tiwEvyN4kw1EWlwly6K6TWEo7fBXNRtQtGMij5sJLrqWxrxN-3cqbF79OrJYeK_bxTaodZOyTDaWjv1ECQo10eCren59vj4lolNh3MW7QBqtiiXmzyBTGp-afNunqm_2w",
    "pt_key": "AAJop7wvADAGsykJ8db6FZBh8DuBv9uV-kzQzAYANPHZ0R_7ICphyJCnBPyfu5fDgjXN02Lm4zA",
    "pt_pin": "hu1210882202",
    "pt_token": "z13aw6cc",
    "pwdt_id": "hu1210882202",
    "sfstoken": "tk01m95471ab0a8sMngzeDJ4M05ONa6HYtfU9ybe+5PXrkjtJi6HOTwVaVthHOi989IeX8I25V/MoL/Iz147MVBIz3P/",
    "whwswswws": "",
    "wxa_level": "1",
    "retina": "1",
    "cid": "9",
    "jxsid": "17558231511662817711",
    "appCode": "ms0ca95114",
    "webp": "1",
    "visitkey": "6400022042933735602",
    "pt_st": "1_zQsl1PVitCAxEQZDQFTO5KPfzvlY1LRiflw9oscYGoZpfjWHNOuMSNP1wyqANMBA62eEcQcyTItbPTX0Zg1mdzQeXDfY8ZGtasd4Dg0nTV3qSeeNb3bGOZ4QS9JKEVyAAY9wmrsV2L-shk8EahZkFUxpY4HBISC51HY49F0eF4JjSTQc1wukDhmRFRYs6p4UeIZxtOdl_Uv-S0Km17xl4mlGB0v1zqYeL7e*",
    "autoOpenApp_downCloseDate_auto": "1755823151469_1800000",
    "PPRD_P": "UUID.1507890925",
    "sc_width": "400",
    "e_wq_addr": "CMU3GzPpDzTpDJU2DzHpCMU3GyV1DJCnDyV1DOVLG18vdJY3CUGvdJu2CzCvdJUzC0PpTXU5HUO2TXU1GtUmTXU1HJu3TXU4ENU3TXU5CNUzXyU3GyV1DJCnDyV1DOVLGyV1DUUmCsV1DtcnHMV1EJYzCyV1DJCzGIV1EUVLDsV1DUS1CMV1DUU5DyV1ENq1DyV1EJK1CyV1DtcnHMV1EJYzCyV1DJO2GyV1DJZPHMU3GzOnDs40ENSyDzYvCuCzEG==",
    "wq_addr": "0%7C1_72_55674_0%7C%u5317%u4EAC_%u671D%u9633%u533A_%u9EA6%u5B50%u5E97%u8857%u9053_%7C%u5317%u4EAC%u5E02%u671D%u9633%u533A%u9EA6%u5B50%u5E97%u8857%u9053%u671D%u9633%u516C%u56ED%7C116.482276%2C39",
    "jdAddrId": "1_72_55674_0",
    "jdAddrName": "%u5317%u4EAC_%u671D%u9633%u533A_%u9EA6%u5B50%u5E97%u8857%u9053_",
    "commonAddress": "0",
    "regionAddress": "1%2C72%2C55674%2C0",
    "mitemAddrId": "1_72_55674_0",
    "mitemAddrName": "%u5317%u4EAC%u5E02%u671D%u9633%u533A%u9EA6%u5B50%u5E97%u8857%u9053%u671D%u9633%u516C%u56ED",
    "cd_eid": "jdd03HQXSEMIU5PUTULJWIJBQVT54RO474JTRARROAH2GBYNUXDXTBTDGP2EKM4G57NXVNWCHQIEKHYINVCWV422QX4ZT7QAAAAMYZ422MPYAAAAADWAB3XBFTRQ6VAX",
    "jxsid_s_u": "https%3A//so.m.jd.com/ware/search.action",
    "sbx_hot_h": "null",
    "autoOpenApp_downCloseDate_jd_homePage": "1755823351223_1",
    "wqmnx1": "MDEyNjM1MGg6Li53c2hpZTZCJUFCNzA0NzJsLmkgby5lNWxBIGVpNyhMa2NDZS4waWEvMzJzNFUtNTFPQ0gqKCk%3D",
    "__jdb": "76161171.16.1507890925|7.1755822806",
    "3AB9D23F7A4B3CSS": "jdd03HQXSEMIU5PUTULJWIJBQVT54RO474JTRARROAH2GBYNUXDXTBTDGP2EKM4G57NXVNWCHQIEKHYINVCWV422QX4ZT7QAAAAMYZ45H3MIAAAAAC37NMWTEFDWPWIX",
    "_gia_d": "1",
    "shshshfpb": "BApXSXOsyzP1AJFy5tjPK8dNIyDnqXMoDBhfDJAxo9xJ1PtROLNSHwkKz3nmqYROrtL04",
    "mba_sid": "17558231194811920022473.11",
    "jxsid_s_t": "1755823372483",
    "__jd_ref_cls": "MYL_Display_Init",
    "sdtoken": "AAbEsBpEIOVjqTAKCQtvQu17rHqrmKTdY4zL5CGm0_ZVrqx-x6q0BDHQ8sc4mVSxJriKk64NFcRPMnFMTP5HQuVEmrYWXBMVJUOxqxDaZ7Pv41MbIYhHCISTS7Xbz74CmZPbl7iDuA"
}
url = "https://api.m.jd.com/api"
params = {
    "functionId": "searchKeyword",
    "appid": "jd-cphdeveloper-m",
    "body": body,
    "loginType": "2",
    "x-api-eid-token": "jdd03HQXSEMIU5PUTULJWIJBQVT54RO474JTRARROAH2GBYNUXDXTBTDGP2EKM4G57NXVNWCHQIEKHYINVCWV422QX4ZT7QAAAAMYZ422MPYAAAAADWAB3XBFTRQ6VAX",
    "h5st": h5st
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
