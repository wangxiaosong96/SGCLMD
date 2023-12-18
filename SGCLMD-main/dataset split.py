# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 22:56:58 2023

@author: xs
"""
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
'''
data = pd.read_csv('F:/2023年/新课题突变药物/SBGCL-main/datasets/new data/association_2173_M1224_K949.csv')

X_train, X_test, y_train, y_test = train_test_split(data.drop('label', axis=1), data['label'], test_size=0.2, random_state=42)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

X_train.to_csv('F:/2023年/新课题突变药物/SBGCL-main/datasets/new data/drug_mutation_training.csv',index=False)
X_test.to_csv('F:/2023年/新课题突变药物/SBGCL-main/datasets/new data/drug_mutation_test.csv',index=False)
X_test.to_csv('F:/2023年/新课题突变药物/SBGCL-main/datasets/new data/drug_mutation_val.csv',index=False)
'''


'''
y_true1=pd.read_csv('F:/2023年/新课题突变药物/SBGCL-main/datasets/new data/drug_mutation_val.csv',header=None)
np.savetxt("F:/2023年/新课题突变药物/SBGCL-main/datasets/new data/drug_mutation_val.txt", y_true1,fmt='%s',newline='\n')
'''
import csv

def csv_to_txt(input_csv, output_txt):
    with open(input_csv, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        with open(output_txt, 'w') as txtfile:
            for row in csv_reader:
                # 使用制表符连接数据并写入TXT文件
                txtfile.write('\t'.join(row) + '\n')

# 示例用法
csv_file_path = 'F:/2023年/新课题突变药物/SBGCL-main/datasets/new data/drug_mutation_test.csv'  # 用实际的CSV文件路径替换
txt_file_path = 'F:/2023年/新课题突变药物/SBGCL-main/datasets/new data/drug_mutation_test.txt'  # 用实际的TXT文件路径替换

csv_to_txt(csv_file_path, txt_file_path)

