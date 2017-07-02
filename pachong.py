# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')
linelist = list()
for archives in range(1,747):

	url = 'http://drops.hduisa.cn/archives/' + str(archives)
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }

	code = urllib.urlopen(url).code
	

	if code == 200:
		request = urllib2.Request(url,headers = headers)
		response = urllib2.urlopen(request)
		content = response.read()
		soup = BeautifulSoup(content,'html.parser')

		Text = soup.find("div","post-content").find_all("p")
		for p in Text:
			i = str(p.text)
			if '\n' in i:
				i.replace('\n',' ')
				i = i + '\n'
				linelist.append(i)
	


		f = open("drops.txt",'w')



		for i in linelist:
			f.write(i)

		f.close()


