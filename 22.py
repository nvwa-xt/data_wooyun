# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

url = 'http://wooyun.org/bugs/wooyun-2015-0146293'
page = urllib.urlopen(url)
html = page.read()
soup = BeautifulSoup(html)
htmls = soup.find_all("h3",limit=11)

pattern = re.compile(r'<h3>(.*?)</h3>')

result = re.match(pattern,'htmls')
print result
