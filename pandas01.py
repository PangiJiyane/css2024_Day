# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:47:23 2024

@author: ccm
"""
import pandas
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())
print(file.describe())
import pandas
file =pandas.read_csv("iris.csv")
print(file)
print(file.info())
file = pandas.read_csv("diab_data.csv")
print (file)
file= pandas.read_csv("housing_data.csv")
print (file)
file = pandas.read_csv("insurance_data.csv")
print(file)


