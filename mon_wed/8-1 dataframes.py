#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:59:46 2022

This script will show basic pandas
usage.

@author: kali
"""

#%% imports
import numpy as np
import pandas as pd
from matplotlib.pyplot import hist


#%% create matrix of random numbers

# generate matrix/array with four columns
# and 100 rows filled with random
# numbers between 0 and 100
matrix = np.random.randint(0, 100, size=(100, 4))
print(matrix)

# just show row 10
print(matrix[10])

# value from row 90, column 2
print(matrix[90, 2])

# get several rows at one time
print(matrix[20:25])

#%% create a dataframe
# create dataframe with our data from aboce
random_df = pd.DataFrame(matrix, columns=['A', 'B', 'C', 'D'])

# see the data in column A
print(random_df['A'])

# print a histogram of column A
random_df['A'].plot.hist()

 #%% add a new column
 
 # generate 100 numbers from random normal distribution
 # center of dist is 5, sd is 2, and 100 numbers generated
 new_col = np.random.normal(loc=5, scale=2, size=100)

# add to dataframe
random_df['E'] = new_col

# plot the histogram
random_df['E'].plot.hist()


#%% add column of textual data

labels = np.random.choice(['A_1', 'A_2', 'B_1', 'B_2'], size=100)

random_df['labels'] = labels


#%% string splitting
# default split is " " [space]
"hello everybody in today's class".split()
# we can split by anything, here split by ' [escaped with \']
"hello everybody in today's class".split("\'")

#%% split a column
label_group = random_df['labels'].str.split('_')
print(label_group)
# we can get different items from the lists in label_group
print(label_group.str[0])
print(label_group.str[1])
print(label_group.str[2]) # NaN, which means Not a Number

random_df['group'] = label_group.str[0]

#%% get summary statistics

# summarize the numerical columns
random_df.describe()

# get the mean of all numeric columns,
# broken down by group.
random_df.groupby('group').mean()

# get the average of columns B, C, E
# broken down by the values in the 'group' column
random_df.groupby('group')['B', 'C', 'E'].mean()


#%% read in mtcars

mtcars = pd.read_csv('data/mtcars.csv')

# get descriptive stats
mtcars.describe()

# rename first column
mtcars.rename(columns={"Unnamed: 0": "make_model"})

# have to use inplace=True to actually change value
# in our dataframe
mtcars.rename(columns={"Unnamed: 0": "make_model"}, inplace=True)






