import requests
#原网址
url='https://pearvideo.com/video_1749564'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    #防盗链:溯源：当前请求的上一级
    'Referer':url,
}
contId=url.split('_')[1]
video_status=f'https://pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.16093705483459098'
resp=requests.get(video_status,headers=headers)
dic=resp.json()
srcUrl=dic['videoInfo']['videos']['srcUrl']
systime=dic['systemTime']
srcUrl=srcUrl.replace(systime,f"cont-{contId}")
# print(srcUrl)
#下载视频
with open("a.mp4",'wb') as f:
    f.write(requests.get(srcUrl).content)