import tushare as ts
file='./data/hangye.xlsx'
df = ts.get_concept_classified()
df.to_excel(file)