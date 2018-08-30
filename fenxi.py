#coding=utf-8
import tushare as ts
import talib as ta
import numpy as np
import pandas as pd
import os,time,sys,re,datetime
import csv
import scipy
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
def Get_Stock_List():
    df = ts.get_stock_basics()
    return df
def Get_MACD(df_Code):
    operate_array=[]
    for code in df_Code.index:
        df = ts.get_hist_data(code,start='2014-11-20')
        dflen = df.shape[0]
        operate = 0
        if dflen>35:
            macd, macdsignal, macdhist = ta.MACD(np.array(df['close']), fastperiod=12, slowperiod=26, signalperiod=9)
            SignalMA5 = ta.MA(macdsignal, timeperiod=5, matype=0)
            SignalMA10 = ta.MA(macdsignal, timeperiod=10, matype=0)
            SignalMA20 = ta.MA(macdsignal, timeperiod=20, matype=0)
#在后面增加3列，分别是13-15列，对应的是 DIFF DEA DIFF-DEA
            df['macd']=pd.Series(macd,index=df.index) #DIFF
            df['macdsignal']=pd.Series(macdsignal,index=df.index)#DEA
            df['macdhist']=pd.Series(macdhist,index=df.index)#DIFF-DEA
            MAlen = len(SignalMA5)
#2个数组 1.DIFF、DEA均为正，DIFF向上突破DEA，买入信号。 2.DIFF、DEA均为负，DIFF向下跌破DEA，卖出信号。
            if df.iat[(dflen-1),13]>0:
                if df.iat[(dflen-1),14]>0:
                    if df.iat[(dflen-1),13]>df.iat[(dflen-1),14]:
                        operate = operate + 1
            else:
                if df.iat[(dflen-1),14]<0:
                    if df.iat[(dflen-1),13]:
                        operate = operate - 1#卖出
#3.DEA线与K线发生背离，行情反转信号。
if df.iat[(dflen-1),7]>=df.iat[(dflen-1),8] and df.iat[(dflen-1),8]>=df.iat[(dflen-1),9]:#K线上涨
    if SignalMA5[MAlen-1]<=SignalMA10[MAlen-1] and SignalMA10[MAlen-1]<=SignalMA20[MAlen-1]: #DEA下降
        operate = operate - 1
elif df.iat[(dflen-1),7]<=df.iat[(dflen-1),8] and df.iat[(dflen-1),8]<=df.iat[(dflen-1),9]:#K线下降
    if SignalMA5[MAlen-1]>=SignalMA10[MAlen-1] and SignalMA10[MAlen-1]>=SignalMA20[MAlen-1]: #DEA上涨
        operate = operate + 1
#4.分析MACD柱状线，由负变正，买入信号。
if df.iat[(dflen-1),15]>0 and dflen >30 :
    for i in range(1,26):
        if df.iat[(dflen-1-i),15]<=0:#
            operate = operate + 1
            break
#由正变负，卖出信号
if df.iat[(dflen-1),15]<0 and dflen >30 :
    for i in range(1,26):
        if df.iat[(dflen-1-i),15]>=0:#
            operate = operate - 1
            break
operate_array.append(operate)
df_Code['MACD']=pd.Series(operate_array,index=df_Code.index)
return df_Code
#输出CSV文件，其中要进行转码，不然会乱码
def Output_Csv(df,Dist):
    TODAY = datetime.date.today()
    CURRENTDAY=TODAY.strftime('%Y-%m-%d')
    reload(sys)
    sys.setdefaultencoding( 'gbk' )
    df.to_csv(Dist+CURRENTDAY+'stock.csv',encoding='gbk')#选择保存
def Close_machine():
    o='c:\\windows\\system32\\shutdown -s'#########
    os.system(o)#########
#发送邮件
def Send_Mail (Message,Dist):
    TODAY = datetime.date.today()
    CURRENTDAY=TODAY.strftime('%Y-%m-%d')
    msg = MIMEMultipart()
    TODAY = datetime.date.today()
    CURRENTDAY=TODAY.strftime('%Y-%m-%d')
    att = MIMEText(open(Dist+CURRENTDAY+'stock.csv', 'rb').read(), 'base64', 'gb2312') #设置附件的目录
    att['content-type'] = 'application/octet-stream'
    att['content-disposition'] = 'attachment;filename='stock.csv'' #设置附件的名称
    msg.attach(att)
    content = str(Message) #正文内容
    body = MIMEText(content,'plain','GBK') #设置字符编码
    msg.attach(body)
    msgto = ['xx@126.com'] # 收件人地址多个联系人，格式['aa@163.com'; 'bb@163.com']
    msgfrom = 'xx@126.com' # 寄信人地址 ,
    msg['subject'] = 'Finish at '+CURRENTDAY #主题
    msg['date']=time.ctime() #时间
#msg['Cc']='bb@junbao.net' #抄送人地址 多个地址不起作用
    mailuser = 'xx'# 用户名
    mailpwd = 'xx' #密码
    try:
        smtp = smtplib.SMTP()
        smtp.connect(r'smtp.126.com')# smtp设置
        smtp.login(mailuser, mailpwd) #登录
        smtp.sendmail(msgfrom, msgto, msg.as_string()) #发送
        smtp.close()
        print 'success mail'
    except Exception, e:
        print e
df = Get_Stock_List()
df = Get_MACD(df)
Dist = 'E:\\08 python\\Output\\'
Output_Csv(df,Dist)
#生成的csv文件中，macd列大于0的就是可以买入的，小于0的就是卖出的
Send_Mail ('Finish TA',Dist)
Close_machine()