#综合训练-抓取网易云音乐的热评信息
#找到未加密的参数
#想办法把参数加密（params,encSecKey
#2022-1-11暂时处理不了加密内容，等以后再来解决吧
import requests
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode
import json
url='https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}

#原始加密数据
data={
    "csrf_token": "",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",
    'pageSize': "20",
    'rid': "R_SO_4_1325905146",
    'threadId': "R_SO_4_1325905146",
}
#加密程序 windows.asrsea(参数,xxxxxx,xxxx)
e='010001'
f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g='0CoJUm6Qyw8W8jud'
i="7kBeYsPxwWHYItLA"
def get_encSecKey():
    return "3a7347d070be1e5de95c01adb369eb0e5dad9a74d428b65ffa1eda5a57eb0e901b59af608278c85f0e7dcdd81b19af88e92970438100e49d471b639a5c245ea09f4a2cd8f67b8acea1970f334e7a6fbbf66bfba8a057c1f53e468fc29407b64e99426a7f753951bd5790682a19d70dbaf906c75331467f23fa941abf405b8439"
'''
function a(a=16) {#随机16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)#循环16次
            e = Math.random() * b.length,#随机数
            e = Math.floor(e),#取整
            c += b.charAt(e);#字符串
        return c
    }
    function b(a, b) {#a为加密内容，b=值
        var c = CryptoJS.enc.Utf8.parse(b)#b密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)#数据
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d, #偏移量
            mode: CryptoJS.mode.CBC #模式是CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {    #d=数据; e=010001;f=很长
        var h = {}
          , i = a(16);#i 就是16位随机值
        return h.encText = b(d, g),#g、i密钥
        h.encText = b(h.encText, i),#pramas,两次加密 数据+g->b->+i->b
        h.encSecKey = c(i, e, f),#encSecKey
        h
    }
'''
def get_params(data):#默认收到的是字符串
    first_enc=enc_params(data,g)
    second=enc_params(first_enc,i)
    return second
def enc_params(data,key):
    backend=default_backend()
    iv='0102030405060708'
    aes=Cipher(algorithms.AES(key.encode('utf-8')),modes.CBC(iv.encode('utf-8')))
    bs=aes.encryptor()
    bs=bs.update(data=data)
    return str(b64encode(bs),"utf-8")#转化成字符串

params={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
}
resp=requests.post(url,headers=headers,params=params)
print(resp.text)