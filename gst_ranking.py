import pandas as pd
import numpy as np
'''
data = pd.read_csv('lf_1_.csv')
print(data.columns)
'''
data = pd.read_csv('/root/A/final121.csv')
# for name in data.columns:
# 	print(name)

data['find_gst'] = np.where(data['TAX NO. 3.1'].str[-2]=='Z', 1, 4)
print(data.shape[0])


'''
#print(data[['TAX NO. 3.1','Region_code']])
#print(data['Region_code'].unique())
data['Regional_code'] = data['TAX NO. 3.1'].str[:2]
#print(data['Regional_code'].unique())

di = {'36':'TG','02':'HP', '24':'GJ','23':'MP','27':'MAH','29':'KAR','33':'TN','37':'AP','03':'PB','07':'DEL'}
data = data.replace({'Regional_code':di})
data['RG_ranking'] = np.where(data['Region_code']==data['Regional_code'], 1, 4)
data.to_csv('final_121(gst).csv')

'''

data['regional_code'] = np.where(data['find_gst'] ==4,'04', data['TAX NO. 3.1'].str[:2])
data['regional_code1'] = data['regional_code']
#print(data['regional_code'][data['regional_code']!=4])

print(data['regional_code'].unique())


di = {'36':'TG','02':'HP', '24':'GJ','23':'MP','27':'MAH','29':'KAR','33':'TN','37':'AP','03':'PB','07':'DEL','04':'04'}
data['regional_code'] = data['regional_code'].map(di)

condition = [(data['regional_code'] =='04'),(data['regional_code']==data['Region_code']),(data['regional_code']!=data['Region_code'])]
choice =[4,1,4]

data['RG_ranking'] = np.select(condition,choice)
print(data['RG_ranking'][data['RG_ranking']==1].shape[0])

#print(data[['TAX NO. 3.1','Region_code','RG_ranking']][data['RG_ranking']==1])
data.to_csv('final_121(gst).csv')
data = pd.read_csv("final121(gst).csv")
print(data.head(20))
