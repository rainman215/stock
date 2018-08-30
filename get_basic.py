import tushare as ts
df = ts.get_stock_basics()
df.to_excel("./data/pe.xlsx")
df2=ts.get_report_data(2017,4)