# -*- coding: utf-8 -*-
import requests
import json

URL_CLOCKIN = 'http://xgxt.bjut.edu.cn/syt/zzapply/operation.htm'
data = {
    'data': '{"xmqkb":{"id":"2c95de297d4f8bfa017d85f53d267613"},"c15":"test1","c16":"在校且住宿","c17":"在京","c18":"低风险地区","type":"YQSJSB","id":"2c95de297d9d0879017d9d2789d20e5c"}',
    'msgUrl': 'syt/zzapply/list.htm?type=YQSJSB&xmid=2c95de297d4f8bfa017d85f53d267613&uploadFileStr={}&multiSelectData={}&type=YQSJSB'
}

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

response_clockin = requests.post(url=URL_CLOCKIN, headers=HEADER, data=data)

print(response_clockin.text)
print(response_clockin.status_code)
