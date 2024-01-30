# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:53 2024

@author: ccm
"""
"""
Storing data in Python
1. Lists
2. Dictionares 
3. Data Frames - specific to pandas
""" 

import pandas 

file = pandas.read_csv("country_data.csv") 



print (file)


age1 = 30
age2 = 25
age3 = 29
age = [30,25,29,46,22]
print (age)

print (age[0])


print (age[1])
print (age[2])
print (min (age))
print(sum(age)) 
print (len(age))
print (sum(age)/len(age)) 

""" 
names = ["A","B","C"]
file = pandas. read_csv("housing_data_csv")
"""
"""
Dictionaries - key:value pairs
cat: "a cute animal"
"""
mammals= {"cat":"a cute animal", "lion":"king of the jungle", "elephant":"a gigantic herbivore"}

print (mammals ["cat"])
"""
Data frames 
"""
fruits = ["apples", "banana", "orange", "grape", "kiwi"]
size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]
fruit_size = {'fruits': fruits, 
    'sizes': size_nm} 
"""
df = dataframe 
import pandas as pd 
df = pd.DataFrame(fruit_size)
print (df['fruits'])
print (df['sizes'])       
print(df['sizes'].min)
print (df['sizes'].mean)
print (df.describe())
print (df[df["sizes"]>10])
print (df[1:3])
"""




