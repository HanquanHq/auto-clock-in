
# -*- coding: utf-8 -*-
'''
@date: 2021-10-3
@author: Li Jinxing, Chu Yumo
'''
import requests
import json
import urllib.parse
import smtplib
from os import environ
from email.mime.text import MIMEText

# EMAIL_USERNAME = environ['EMAIL_USERNAME']
# EMAIL_PASSWORD = environ['EMAIL_PASSWORD']
# EMAIL_SERVER = environ['EMAIL_SERVER']
# EMAIL_PORT = int(environ['EMAIL_PORT'])

# URL_SESSION = 'http://bjut.sanyth.com:81/nonlogin/qywx/authentication.htm?appId=402880c97b1aa5f7017b1ad2bd97001b&urlb64=L3dlaXhpbi9zYW55dGgvaG9tZS5odG1s'
# URL_CLOCKIN = 'http://bjut.sanyth.com:81/syt/zzapply/operation.htm'
# URL_CLOCKIN = 'xgxt.bjut.edu.cn/syt/zzapply/operation.htm?data={"xmqkb":{"id":"2c95de297d4f8bfa017d85f53d267613"},"c15":"无情况","c16":"在校且住宿","c17":"在京","c18":"低风险地区","type":"YQSJSB","id":"2c95de297d9d0879017d9d2789d20e5c"}&msgUrl=syt/zzapply/list.htm?type=YQSJSB&xmid=2c95de297d4f8bfa017d85f53d267613&uploadFileStr={}&multiSelectData={}&type=YQSJSB'
URL_CLOCKIN = 'http://xgxt.bjut.edu.cn/syt/zzapply/operation.htm'
data = {
    'data': '{"xmqkb":{"id":"2c95de297d4f8bfa017d85f53d267613"},"c15":"test1","c16":"在校且住宿","c17":"在京","c18":"低风险地区","type":"YQSJSB","id":"2c95de297d9d0879017d9d2789d20e5c"}',
    'msgUrl': 'syt/zzapply/list.htm?type=YQSJSB&xmid=2c95de297d4f8bfa017d85f53d267613&uploadFileStr={}&multiSelectData={}&type=YQSJSB'
}
# Part0 Read user info
# with open('./info.json', 'r') as f:
#     core = json.load(f)

# Part1 Get session
# HEADER_SESSION = {
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
#     'Connection': 'keep-alive',
#     'Host': 'bjut.sanyth.com:81',
#     'Cookie': 'id='+core['id']+'; token='+core['token'],
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2102K1C Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045735 Mobile Safari/537.36 wxwork/3.1.18 ColorScheme/Dark MicroMessenger/7.0.1 NetType/4G Language/en Lang/en'
#     'Chrome/85.0.4183.83 Safari/537.36 '
# }
# s = requests.Session()
# response = s.get(URL_SESSION, headers=HEADER_SESSION)
# session = response.history[0].headers['Set-Cookie'].split(';')[0]
# print(response.history[0])
# print(response.history[0].headers)
#cookie = 'id=' + core['id'] + '; token=' + core['token'] + '; ' + session
# cookie = 'id=' + core['id'] + '; token=' + core['token'] + '; ' + 'JSESSIONID=41F087100FC71DDD73FB79DC85697308.jvm1'

# print(cookie)

# Part2 Get header & data
HEADER = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en,en-US;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Content-length': '525',
    'Cookie': 'id=2c95de297d9d0879017d9d274d590e52; token=AC01E99F424F9C099BCA18DBC45DDA3E; JSESSIONID=883397E434BD26A927CB8DD1DB0A41E4.jvm1',
    'Host': 'xgxt.bjut.edu.cn',
    'Origin': 'http://xgxt.bjut.edu.cn',
    'Referer': 'http://xgxt.bjut.edu.cn/webApp/xuegong/index.html',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2102K1C Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045735 Mobile Safari/537.36 wxwork/3.1.18 ColorScheme/Dark MicroMessenger/7.0.1 NetType/4G Language/en Lang/en'
    'Chrome/85.0.4183.83 Safari/537.36',
    'X-Requested-With': 'com.tencent.wework',
}

# # user info
# info = {
#     'xmqkb': {
#         'id': '2c95de297d4f8bfa017d85f53d267613'
#     },
#     'c15': core['c15'],
#     'c16': core['c16'],
#     'c17': core['c17'],
#     'c18': core['c18'],
#     'type': 'YQSJSB',
#     'id':'2c95de297d8646d5017d8e7e9ae618f1'
# }

# suffix info (static)
# suffix_raw = '&msgUrl=syt%2Fzzapply%2Flist.htm%3Ftype%3YQSJSB%26xmid=2c95de297d4f8bfa017d85f53d267613&uploadFileStr=%7B%7D&multiSelectData=%7B%7D&type=YQSJSB'
# suffix_raw = '&msgUrl=syt/zzapply/list.htm?type=YQSJSB&xmid=2c95de297d4f8bfa017d85f53d267613&uploadFileStr=%7B%7D&multiSelectData=%7B%7D&type=YQSJSB'
# prefix info (user info mostly)
# prefix_data = json.dumps(info, ensure_ascii=False)
# prefix_raw = 'data='+urllib.parse.quote_plus(prefix_data)
# DATA = prefix_raw + suffix_raw

# Part3 Clock in
response_clockin = requests.post(url=URL_CLOCKIN, headers=HEADER, data=data)


print(response_clockin.text)
print(response_clockin.status_code)
# print(response_clockin.text)
# result = '打卡失败'

# if response_clockin.text == 'success':
#     result = '打卡成功'
# else:
#     if response_clockin.text == 'Applied today':
#         result = '今天已经打过卡'
#     else:
#         result += f
        
'''
HTTP status: {response_clockin.status_code}
打卡数据:
{
    json.dumps(info, ensure_ascii=False, sort_keys=True, indent=2)
}
'''


# message = MIMEText(result, 'plain', 'utf-8')
# message['Subject'] = 'YQT打卡结果'
# message['FROM'] = EMAIL_USERNAME
# message['To'] = EMAIL_USERNAME

# server = smtplib.SMTP(EMAIL_SERVER)
# server.connect(EMAIL_SERVER, EMAIL_PORT)
# server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
# server.sendmail(EMAIL_USERNAME, [EMAIL_USERNAME], message.as_string())
