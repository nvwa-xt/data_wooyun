# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/txapi/weixin/wxhot?num=10&rand=1&word=唐朝&page=1'


req = urllib2.Request(url)

req.add_header("apikey", "b09c696d7853aaf0f15638a5bc2e3c12")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
