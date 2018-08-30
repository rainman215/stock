#! /usr/bin/env python
#coding=utf-8
import tushare as ts
import threading
def get_yeji():
    df = ts.get_report_data(2018,1)
    file='./data/yeji.xlsx'
    df.to_excel(file)
    print "import yeji done!"
    
def get_tiger():
    file2='./data/jigou.xlsx'
    df=ts.inst_tops(5)
    df2 = df.sort_values(by='bcount',ascending=False)
    df2.to_excel(file2,index=False)
    print "import jigou done!"
    
def get_info():    
    file3='./data/pe.xlsx'
    df = ts.get_stock_basics()
    df.to_excel(file3)
    print "import basic stock message done!"

def get_cur_data():    
    file4='./data/currentday.xlsx'
    df = ts.get_today_all()
    df.to_excel(file4)
    print "import current data done!"

def _start():
    _list=['get_yeji','get_tiger','get_info','get_cur_data']
    threads=[]
#     for i in range(len(_list)):
#         print _list[i]
#         a=threading.Thread(target=_list[i])
#         threads.append(a)
    t1=threading.Thread(target=get_yeji)
    threads.append(t1)
    t2=threading.Thread(target=get_tiger)
    threads.append(t2)
    t3=threading.Thread(target=get_info)
    threads.append(t3)
    t4=threading.Thread(target=get_cur_data)
    threads.append(t4)
    print threads
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    




if __name__=='__main__':
    _start()


#df2=ts.get_report_data(2017,4)