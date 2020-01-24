import pandas as pd
import numpy as np
from pymongo import MongoClient 
client = MongoClient('mongodb://localhost:27017/Vendor_Data',connect=False)
mydb = client['Vendor_Data']
mycol = mydb['EKKO']
mycol1 = mydb['EKPO']
cursor = mycol.find()
df = pd.DataFrame(list(cursor))
cursor1 = mycol1.find()
df1 = pd.DataFrame(list(cursor1))


for i in df1.columns:
	print(i)
df.columns = df.columns.str.replace(' ','')
df1.columns = df1.columns.str.replace(' ','')
df = df[['Purch-Doc-','Vendor']]
df1 = df1[['Purch-Doc-','Material','MatlGroup','Plnt']]
data = pd.merge(df1,df, on = 'Purch-Doc-', how = 'left')
data.to_csv('plant_ranking.csv')
data1['Count'] = 1
data1 = data.groupby(['Vendor','Plnt','MatlGroup'])['Count']
data1 = data1.reset_index()
print(data1)