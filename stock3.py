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
#f2="C:\\Users\\tonnicheng\\Desktop\\stoc\\sy.txt"
f2="./sy.txt"
def getHtml(url):
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

Url = 'http://quote.eastmoney.com/stocklist.html'
componet = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
#print componet
code = getStockdata(componet,getHtml(Url))

CodeList = []
for item in code:
    if item[0]=='6':
        CodeList.append(item)

for code in CodeList:
  #  code = 603383
    ur='http://quote.eastmoney.com/sh%s.html'%code
    print ur
    content = getHtml(ur)
#     print content
   # content.to_excel('./1.xlsx')
    shiy = """r'<span id=\"gt6_2\">\d+\.\d+</span>'"""
#    print shiy
    componet = r'<span id=\"gt6_2\">\d+\.\d+</span>'
    shiyin = getStockdata(componet,content)
    componet = r'<span id="gt13_2">\d+\.\d+</span>'
    shijin = getStockdata(componet,content)
#    print shijin
    if any(shiyin):
        for i in shiyin:
            sy = re.findall(r'\d+\.\d+',i)
        for j in shijin:
            pb = re.findall(r'\d+\.\d+',j)
        print "shiying is :%s"%sy[0]
        print "shijin is :%s"%pb[0]
        mes=stock(code,sy[0],pb[0])
        mes.wr_file()
    else:
#shiying is nothing
        mes=stock(code," "," ")
        mes.wr_file()
   # time.sleep(5)
#    print('get%s'%code)
#    urllib.urlretrieve(url, filepath+code+'.csv')
