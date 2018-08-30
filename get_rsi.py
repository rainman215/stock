import tushare as ts
class rsi(object):
	def __init__(self,code):
		self.code=code
	def get_val(self):
		df=ts.get_hist_data(self.code)
		df.to_excel("./data/%s_rsi.xlsx"%self.code)
		if df is None:
			print "not value"
		else:
			p=df[u'price_change']
	#		print p
			a=[]
			b=[]
			for i in range(0,6):
				if p[i]>0:
					a.append(p[i])
				else:
					b.append(p[i])
			x=sum(a)
			y=abs(sum(b))
			rs=x/y
			rsi=rs/(1+rs)*100
			rsi='%.3f'%rsi
			print "rsi is:%s"%rsi
if __name__=='__main__':
	x=rsi('300584')
	x.get_val()
		
