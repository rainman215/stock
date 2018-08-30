#!/usr/bin/python
#coding=gbk
import os
import pandas as pd
import code
class f(object):
    def __init__(self,code):
        self.code=code
    def fi(self):
        print "111"
        file1='./data/pe.xlsx'
        file2='./data/pe_shai.xlsx'
        file='./data/pe-2.xlsx'
        if os.path.exists(file2):
            os.remove(file2)
        table = pd.read_excel(file1)
        tot=table['totals']
        out=table['outstanding']
        val = tot*out
        table['tot_val']=val
#print table.head()
        table.to_excel(file)
        print self.code
#        converters={table['code']:str,self.code:str}
        df3=table[(table['code'])==self.code]
        print df3
#print tot,out
#            df = table[(table['pe']<20)&(table['pe']>0)&(table['rev']>0)&(table['tot_val']>100)&(table['tot_val']<1000)]
#            df2 = df.sort_values(by='tot_val',ascending=True)
#            df2.to_excel(file2)
if __name__=='__main__':
    p=f(2397)
    p.fi()

