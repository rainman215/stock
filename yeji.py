import tushare as ts
import pandas as pd
import os
import code
#df = ts.get_report_data(2017,4)
#file='./data/yeji.xlsx'
#df.to_excel(file)
class yj(object):
    def __init__(self,code):
        self.code=code
    def se_yj(self):
        df=pd.read_excel('./data/yeji.xlsx')
  #      df=pd.read_excel('./data/yeji.xlsx',index_col=None, na_values=['NA'], parse_cols = "0,5:AA")
  #      print df
#        print df.code[0]
#        for co in df['code']:
#            if self.code==co:
#                print df.index
        a=df[(df.code==self.code)]
        print a
if __name__=='__main__':
    rs=yj(300140)
    rs.se_yj()