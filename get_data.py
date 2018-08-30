import pandas as pd
import code
class data(object):    
    def __init__(self,code):
        self.code=code
    def get_d(self):        
        file = './data/currentday.xlsx'
        df=pd.read_excel(file)
        a=df[(df.code == self.code)]
#        print df[u'changepercent'][1932]
        print a
#       print a[u'changepercent'][1932]
if __name__ == '__main__':
    d=data(300140)
    d.get_d()