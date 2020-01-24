import pandas as pd
import numpy as np

data = pd.read_csv('final_121_weightages.csv')

conditions = [(data['Quantity-deliver-percent_y'] < 75),(data['Quantity-deliver-percent_y'] >=75) & (data['Quantity-deliver-percent_y'] < 84),(data['Quantity-deliver-percent_y'] >= 85) & (data['Quantity-deliver-percent_y'] <= 94), (data['Quantity-deliver-percent_y'] >=95) & (data['Quantity-deliver-percent_y'] == 100) ]
choice = [4,3,2,1] 
data['Quantity-Ranking'] = np.select(conditions,choice)

print(data[['Quantity-Ranking','Quantity-deliver-percent_y','Delivered_x','Sched-Qty_y','Delivered_x']][data['Quantity-Ranking']==0])
print(data.shape[0])
'''
for name in data.columns:
	print(name)
'''
