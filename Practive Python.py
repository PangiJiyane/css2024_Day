# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:51:21 2024

@author: ccm
"""
"""
x=50
age=50
_age=50
my_age=50
mY_agE=50
my_age_2=50
"""
import pandas 
file=pandas.read_csv("country_data.csv")
print (file)
print (file.info())
print (file.describe())
import pandas 
file=pandas.read_csv("country_data.csv")
print(file)
#storing data
B1=30
B2=40
B3=30
B4=49
print(B1)
print(B2)
#Using List
age=[30,40,30,49,22,35,22,46,29,25,39]
print(age)
#Lists indexes start at 0 which has the value of 30
print (age[0])
print(age[1])
print(age[10])
#This will give a error as there is no value at index 11
print (age[11])
#Basic Stats
age =[30, 40, 30, 49, 22, 35, 22, 46,29 ,25 ,39]
print(min(age))
"""
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)
"""
#Storing Text
C2 ="M"
C3 ="M"
C4 ="F"
print(C2)
print(C3)
print(C4)

 
