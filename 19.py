# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json  
import base64,Image
import StringIO  
 
#imageurl = 'http://wooyun.org/captcha.php'
#u=urllib.urlopen(imageurl)
#datas = u.read()
#f = open("1.jpg",'wb')
#f.write(datas)
#f.close

url = 'http://apis.baidu.com/apistore/idlocr/ocr' 

data = {}  
data['fromdevice'] = "pc"  
data['clientip'] = "211.137.2.4"  
data['detecttype'] = "LocateRecognize"  
data['languagetype'] = "ENG"  
data['imagetype'] = "1"  
  
#读取图片  
imageurl = 'http://jw.syu.edu.cn/VerifyCode.aspx'
u=urllib.urlopen(imageurl)  
image= u.read()    

data['image'] = base64.b64encode(image)  
decoded_data = urllib.urlencode(data)  
 
req = urllib2.Request(url, data = decoded_data)  
  
req.add_header("Content-Type", "application/x-www-form-urlencoded")  
req.add_header("apikey", "b09c696d7853aaf0f15638a5bc2e3c12")  
  
resp = urllib2.urlopen(req)  
content = resp.read()  
if(content):  
        print(content) 
