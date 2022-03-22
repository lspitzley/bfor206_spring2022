#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:40:13 2022

@author: kali
"""

#%% imports

import numpy as np
import pandas as pd

#%% create a random matrix

matrix = np.random.randint(0, 100, size=(100, 4))
print(matrix)

# get row 55
print(matrix[55])

# get all rows of column 2
print(matrix[:, 2])

# get rows 10 to 20
print(matrix[10:20])

# get a single value
print(matrix[1, 1])

#%% create a dataframe from the matrix

# use data from matrix to create new dataframe with column names
random_df = pd.DataFrame(matrix, columns=['A', 'B', 'C', 'D'])

# show the contents of column A
random_df['A']

# histogram for column A
random_df['A'].plot.hist()


#%% add a new column from a normal distribution

random_df['E'] = np.random.normal(loc=5, scale=2, size=100)

random_df['E'].plot.hist()

#%% add column of labels

labels = np.random.choice(['A_1', 'A_2', 'B_1', 'B_2'], size=100)
random_df['labels'] = labels

# show the column names
list(random_df)

#%% break up the label column to get the first value (A or B)

# split string (default is by spaces)
"Hello BFOR 206. Today is Tuesday".split()

# split by period character '.'
"Hello BFOR 206. Today is Tuesday".split('.')

label_group = random_df['labels'].str.split('_')

# get different parts of the lists
label_group.str[0]
label_group.str[1]
label_group.str[2]   # outputs NaN (not a number; aka it is empty)

random_df['group'] = label_group.str[0]


# show the first five rows
random_df.head()

# show the last five rows
random_df.tail()


#%% summarize data by group

# basic summary stats
random_df.describe()

# summary stats including text columns
random_df.describe(include='all')

# get the mean for each distinct value in the 'group' column
random_df.groupby('group').mean()

# do the same thing with labels column

random_df.groupby('labels').mean()

random_df.groupby('labels').count()

random_df.groupby('group')[['C', 'D']].mean()


#%% load in data from a file

mtcars = pd.read_csv('data/mtcars.csv')

list(mtcars)
mtcars.describe()

mtcars.rename(columns={"Unnamed: 0": "make_model"}, inplace=True)

list(mtcars)








