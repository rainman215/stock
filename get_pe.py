import urllib
import re
import pandas as pd
import pymysql
import os
import time
import sys
reload(sys)                         
sys.setdefaultencoding('utf-8') 

f="C:\\Users\\tonnicheng\\Desktop\\stoc\\temp.txt"
f2="./sy.txt"
class pe(object):
    def __init__(self,code):
	    self.code=code
    def getHtml(self):
        if self.code[0] == '6':
            url='http://quote.eastmoney.com/sh%s.html'%self.code
        else:
            url='http://quote.eastmoney.com/sz%s.html'%self.code
        html = urllib.urlopen(url).read()
        html = html.decode('gbk')
        return html
def getStockdata(s,html):
    	pat = re.compile(s)
    	code = pat.findall(html)
    	return code

class stock(object):
    def __init__(self,cod,sy,pb):
        self.cod=cod
        self.sy=sy
        self.pb=pb
    def wr_file(self):
        file=open(f2,'a')
        file.write("stock code is:%s\n"%self.cod)
        file.write("shiying is :%s\n"%self.sy)
        file.write("shijing is :%s\n"%self.pb)
        file.close()

class gp(object):
    def __init__(self,code):
        self.code=code
    def p(self):
        content = pe(self.code)
        content = content.getHtml()
        componet = r'<span id=\"gt6_2\">\d+\.\d+</span>'
        shiyin = getStockdata(componet,content)
        componet = r'<span id="gt13_2">\d+\.\d+</span>'
        shijin = getStockdata(componet,content)
        if any(shiyin):
            for i in shiyin:
                sy = re.findall(r'\d+\.\d+',i)
            for j in shijin:
                pb = re.findall(r'\d+\.\d+',j)
                mes=stock(self.code,sy[0],pb[0])
                mes.wr_file()
                return sy[0]
        else:
#shiying is nothing
            print "shiying is:None"
            return -1
if __name__=='__main__':
	cd=gp('601899')
	cd.p()
else:
	print "import pe"