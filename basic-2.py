import urllib
import os  
import time  
import tushare as ts  
import getreal as ge
import pandas as pd  
import get_vol as vol
import get_pe as pe
import get_rsi as rs
import sys
reload(sys)                         
sys.setdefaultencoding('utf-8') 


df=ts.get_stock_basics()
n=df[u'name']
l=len(n)
e=df[u'reservedPerShare']

while l > 0:
    l -= 1
    if e[l] > 5:
#        print "num is %s"%l
#        print n.index[l]
        s=pe.gp(n.index[l])
        sy=s.p()
        if sy:
            if float(sy) < float(30):
			print n.index[l]
			print "shiying is:%s"%sy
			r=rs.rsi(n.index[l])
			r.get_val()
			b=vol.get_vol(n.index[l])
			b.volume()
#a=ge.get(n.index[l])
#			    real=a.getdata()
#        print real['pchange']
			print "reservedPerShare is %s"%e[l]
        else:
            print "00000"
        time.sleep(2)
        
