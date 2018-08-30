import pandas as pd
import tushare as ts
class get(object):
    def __init__(self,code):
        self.code=code
    def getdata(self):
        df = ts.get_today_ticks(self.code)
        df.to_excel("./data/%s_real.xlsx"%self.code)
#        return df.head(1)
        print df.head(1)

if __name__ == '__main__':
    data=get('601318')
    data.getdata()
    print "1111"
else:
    print "import getreal"
#data=get('601318')
#data.getdata()