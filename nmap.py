#!/usr/bin/python
# -*- coding: utf-8 -*-
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser
import requests
x=90

while x < 255:
	print "\033[1;31mstart 172.16.%s.0/24\033[0m" %(str(x))
	#调用nmap扫描段内开放80端口的IP
	mission = NmapProcess("172.16.%s.0/24" % (str(x)),options = "-p 80")
	mission.run()
	hosts_hash = {}
	#处理nmap输出结果
	report = NmapParser.parse(mission.stdout)
	#得到每一个开放80端口的IP，结果存放到hash中
	for _host in report.hosts:
		if _host.is_up() and _host.services[0].state =='open':
			hosts_hash[_host.address] = str(_host.services[0].port)+"/"+_host.services[0].state
	print hosts_hash.keys()
	#对每一个IP反向域名解析
	for ips in hosts_hash.keys():
		print "\033[1;32m[+]"+ips+"\033[0m"
		target_page = 1
		count = 1
		#循环遍历每一页
		while 1:
			try:
				r = requests.get("http://dns.aizhan.com/index.php?r=index/domains&ip=%s&page=%s" % (ips,str(target_page)))
				#对每一个域名验证连接
				for domain in  r.json()[u'domains']:
					try:
						test_domain = requests.get("http://" + domain)
						print count,":",domain,"\t:",test_domain.status_code
					except:
						print count,":",domain,"\t:","error"
					count += 1
				#若不是最后一页，就继续，否则就退出循环
				if int(r.json()[u'maxpage'])>target_page:
					target_page += 1
				else:
					break
			except:
				#没有域名解析到此IP
				print "NONE"
				break
	x += 1