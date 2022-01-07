from urllib.request import urlopen

url='http://148.100.78.8'
req=urlopen(url)
with open('./TestHtml.html','w') as f:
    f.write(req.read().decode('utf-8'))
print('Over')