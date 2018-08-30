import tushare as ts
import content as con
import yeji as yej
import pandas as pd
def analysis():
    file='./data/jigou.xlsx'
    df=pd.read_excel(file)
    df2 = df.sort_values(by='bcount',ascending=False)
    df2.to_excel(file,index=False)
    #print df2
    df3=pd.read_excel(file)
    print df3.head(5)
    cod=df3['code']
    print cod[0]
    content=con.f(cod[0])
    content.fi()
    yeji=yej.yj(cod[0])
    yeji.se_yj()
