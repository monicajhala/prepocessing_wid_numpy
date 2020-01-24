import pandas as pd 
# df = pd.read_csv("data1(MAIN_FILE).csv", encoding= 'cp1252')
df2 = pd.read_csv("EKBE1. OCT'16 to MAY'17 .csv", encoding='cp1252')
for i in df2:
	print(i)
# print(df2.head(20))

# print(type(df['Createdon']))
# print(df['Createdon'])

# print(df['Createdon'].str[-4:])
# print(df['Createdon'])
# print(ooo)
# print
# df = df[df['Createdon'] == df['GRN_Posting_Date']]
# print(df)
# print(df['Invoice Document No.'])
# df['Invoice Document No.'] = df['Invoice Document No.'].astype(str)
# print(df['Invoice Document No.'].str.len())

# df1 = df[df['Invoice Document No.'] != 16]
# print(df['Invoice Document No.'])
# # print(df1)
# print(df['Createdon'][:-4])


# import pandas as pd
# data1 = pd.read_csv("rseg 2017 1 series material ecc.csv")
# # # data2 = pd.read_csv("rbkp 2017 Fiscal year.csv")
# for i in data1:
# 	print(i)
# # data1 = data1[['Purchasing Document','Document Number','Vendor']]
# data1['Invoice Document No.'] = data1['Document Number']
# data2 = data2[['Invoice Document No.','Document Date','Gross invoice amount','Time of Entry']]
# data4= pd.merge(data2, data1, on = 'Invoice Document No.', how ='right')
# data4 = data4.fillna(0)
# print(data4)

# data4 = data4[data4['Vendor'] == 0]
# data4.to_csv("/root/A/Mongo/data4.csv")
# print(data4.head(20))

# data1['Purchasing Document'] = data1['Purch-Doc-']

# data1= pd.merge(data1, data2, on = 'Purchasing Document', how ='left')


# data['Delivered'] = data['Delivered'].astype(str)
# data1['Invoice Document No.'] = data1['Invoice Document No.'].astype(str)
# not_require = data1[data1['Invoice Document No.'] != 16]
# print(len(not_require))

# import pandas as pd 
# data1 = pd.read_csv("data1.csv")
# data1 = data1[['Purchasing Document']]
# f1 = pd.read_csv("EKBE1. OCT'16 to MAY'17 .csv", encoding= 'cp1252')
# f1['Purchasing Document'] = f1['Purch.Doc.']
# f1 = f1[['Purchasing Document','Mat. Doc.','Pstng Date']]
# f1.to_csv("f1.csv")
# f2 = pd.read_csv("EKBE2_June'17_To_Dec'17.csv", encoding='cp1252')
# f2['Purchasing Document'] = f2['Purch.Doc.'f2 = f2[['Purchasing Document','Mat. Doc.','Pstng Date']]
# data1 = pd.merge(data1,f1, on ='Purchasing Document', how = 'left')
# data1.to_csv("data1.csv")
# for i in data1:
#  	print(i)


#  # data1 = data1[['Purch.Doc.','Mat. Doc.','Pstng Date']]

# data2 = pd.read_csv()








# import pandas as pd
# df1 = pd.read_csv("final_121_weightages.csv", encoding = 'cp1252')
# for i in df1:
# 	print(i)
# df1 = df1[['Invoice Document No.','Posting Date']]
# df2 = pd.read_csv("rseg 2017 1 series material ecc.csv", encoding = 'cp1252')
# df2 = df2[['Document Number','Purchasing Document']]
# df2['Invoice Document No.'] = df2['Document Number']
# df3 = pd.read_csv("rseg_2017.csv", encoding = 'cp1252')
# df3 = df3[['DocumentNo','Purchasing Document']]
# df3['Invoice Document No.'] = df3['DocumentNo']
# df9 = pd.merge(df2,df1, on = 'Invoice Document No.', how = 'left')
# df10 = pd.merge(df3,df1, on = 'Invoice Document No.', how = 'left')
# invoice_data = pd.concat([df9,df10])
# invoice_data.to_csv("invoice_data.csv")
# print(invoice_data.head(20))





# df2 = df2[[]]
# df3= pd.read_csv("rseg_2017.csv", encoding = 'cp1252')

	
