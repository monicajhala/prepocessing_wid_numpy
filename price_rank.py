import pandas as pd
import numpy as np
df_final_merge = pd.read_csv('final_12.csv')
for i in df_final_merge.columns:
	print(i)
# df_final_merge['net_price_deviation'] = 
df_final_merge['net_price_deviation'] = np.where(df_final_merge['net_price_deviation'] == '#NA',3,df_final_merge['net_price_deviation'])
df_final_merge['net_price_deviation'] = df_final_merge['net_price_deviation'].astype(float)
conditions = [(df_final_merge['net_price_deviation'] < 2),(df_final_merge['net_price_deviation'] >=2) & (df_final_merge['net_price_deviation'] < 5),(df_final_merge['net_price_deviation'] >= 5) & (df_final_merge['net_price_deviation'] <=9), (df_final_merge['net_price_deviation'] >=10) ]
choice = [1,2,3,4]
df_final_merge['net_price_ranking'] = np.select(conditions,choice)

df_final_merge.to_csv('final12.csv')


