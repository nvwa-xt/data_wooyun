# -*- coding:gb2312 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

url = 'http://wooyun.org/bugs/wooyun-2015-0146515'
page = urllib.urlopen(url)
html = page.read()
soup = BeautifulSoup(html)
print soup.h3.a.string
print u'--1------------------------------------------------------'
print soup.h3.next_sibling.next_sibling.string
print u'--2------------------------------------------------------'
print soup.h3.next_sibling.next_sibling.next_sibling.next_sibling.a.string
print u'--3------------------------------------------------------'
print soup.h3.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.a.string
print u'--4------------------------------------------------------'
print soup.h3.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
print u'--5------------------------------------------------------'
print soup.h3.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
print u'--6------------------------------------------------------'
print soup.h3.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
print u'--7------------------------------------------------------'
print soup.h3.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
print u'--8------------------------------------------------------'
print soup.h3.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
print u'--9------------------------------------------------------'
print soup.h3.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.a.string
