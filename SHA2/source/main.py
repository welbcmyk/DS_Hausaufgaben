# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:18:16 2020

@author: Robin
"""

import hashlib
import random
import pandas

dataFile = pandas.read_csv('../data/data.csv')
hashData = []

for index, row in dataFile.iterrows():
    dataFile.iloc[index, 0] = str(dataFile.iloc[index, 0]) + str(random.randint(1,100000))
    hashData.append(hashlib.sha256(str(dataFile.iloc[index, 0]).encode('utf-8')).hexdigest())
    dataFile.iloc[index, 0] = ""
    
    dataFile.iloc[index, 2] = str(dataFile.iloc[index, 2]) +  str(random.randint(1,100000))
    hashData.append(hashlib.sha256(str(dataFile.iloc[index, 2]).encode('utf-8')).hexdigest())
    dataFile.iloc[index, 2] = ""

print(dataFile.head())
dataFile.to_csv('../output/anom_data.csv')
hashDataFrame = pandas.DataFrame(hashData)
hashDataFrame.to_csv('../output/hash_identifier.csv')