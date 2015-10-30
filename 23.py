import re
import urllib.request
def getUrl(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    return html
def getHtnlList(html):
    reg = r'正则表达式'
    reglist = re.compile(reg)
    return reglist
html = getUrl("网址")
getHtml(html
