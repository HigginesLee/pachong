import requests
import requests
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
}
url='https://movie.douban.com/j/chart/top_list'#重新封装参数
pardom={
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "5",
}

resp=requests.get(url,params=pardom,headers=headers)
print(resp.json())