import tushare as ts
import time
import sys
reload(sys)                         
sys.setdefaultencoding('utf-8') 
class get_vol(object):
    def __init__(self,code):
        self.code=code
    def volume(self):
        t=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        df = ts.get_sina_dd(self.code,date=t,vol=10)
#        print df
        df.to_excel("./data/%s_vol.xlsx"%self.code)
        if df is None:
            print "No trade"
        elif not df.empty:
            tt = df['time']
            vv=df['volume']
            l=len(df['volume'])
            while l > 0:
                l -= 1
                if vv[l] > 1000000:
                    print (tt[l],vv[l])
if __name__=='__main__':
    a=get_vol("601899")
    a.volume()
#    a=get_vol("300628")
#    a.volume()