#This code is written by Yutong Yang. It is used to calculate the max quantity Item description
#And the outcome is that 
# the maximum od quantity =  869879.0
#ID                                       452409
#SHA                                         Q45
#PCT                                         112
#PRACTICE                                 A81630
#BNFCODE                         0410030C0AAAFAF
#BNFNAME     Methadone HCl_Oral Soln 1mg/1ml S/F
#ITEMS                                    1426.0
#NIC                                     9046.75
#ACTCOST                                  8613.1
#QUANTITY                               869879.0
#Name: 452408, dtype: object
# coding:utf-8
import pandas as pd
data = pd.read_csv(r'C:/Users/Lenovo/Desktop/MIEyyt/MIE_group_26/practice_level_prescribing.csv',sep=',')
print(data)
print("the maximum od quantity = ",data['QUANTITY'].max())
chinese_max_index = data['QUANTITY'].idxmax()
chinese_max_row = data.loc[chinese_max_index]
print(chinese_max_row)