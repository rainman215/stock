#! /usr/bin/env python
#coding=GB18030
import matplotlib

import tushare as ts

import pandas as pd

import matplotlib.pyplot as plt
#from matplotlib.dviread import fname


fig=plt.gcf()
plt.title(u'东方航空')

df=ts.get_hist_data('600115',start='2018-05-10',end='2018-06-5')
df=df.sort_index()
print df
with pd.plotting.plot_params.use('x_compat',True):
    plt.plot((df.index),df.close)
    df.high.plot(color='r',figsize=(10,6),grid='on')
    df.low.plot(color='b',figsize=(10,6),grid='on')
    plt.xticks(rotation=90)
    plt.xticks(fontsize=6)
 
    plt.show()
 #   fig.savefig('./data/1.png')
    
#from matplotlib.font_manager import FontPoperties
#font = FontProperties(fname=r"c:\windows\Fonts\simsunb.ttf",size=14)
#plt.xlabel(u"23",FontProperties=font)
#plt.ylabel(u"23",FontProperties=font)
#plt.show()