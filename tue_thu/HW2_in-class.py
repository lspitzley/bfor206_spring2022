#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:53:45 2022

@author: kali
"""

#%% imports

import pandas as pd

#%% read in the data

aiml_data = pd.read_csv('data/reddit_database.csv')

#%% get information about the dataframe

aiml_data.info()

# store descriptive stats in a variable
# this will make it easy to see all the data
aiml_descriptives = aiml_data.describe()

#%% convert date columns to datetime format

aiml_data['author_created_date'] = pd.to_datetime(aiml_data['author_created_utc'], unit='s')

# overwrite the orignal data in 'created_date' column
aiml_data['created_date'] = pd.to_datetime(aiml_data['created_date'])

aiml_data.info()

#%% get full descriptive stats

aiml_descriptives = aiml_data.describe(include="all", datetime_is_numeric=True)



"""
################## Class 9-1 #####################
"""

#%% create day of the week column

# https://stackoverflow.com/questions/30222533/create-a-day-of-week-column-in-a-pandas-dataframe-using-python

aiml_data['dow'] = aiml_data['created_date'].dt.day_name()




#%% plot a bar chart

aiml_data.groupby('dow')['created_date'].count().plot(kind='bar')
####                ^         ^           ^          ^
#           break down by dow |           |           |
#                      count created_date |           |
#                                    summarization    |
#                                                   plot  

#%% order the days of the week

aiml_data['dow'] = pd.Categorical(aiml_data['dow'], categories=
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
    ordered=True)

aiml_data.info()

#%% plot it again

aiml_data.groupby('dow')['created_date'].count().plot(kind='bar')


#%% add elements by storing the plot in a variable

dow_plot = aiml_data.groupby('dow')['created_date'].count().plot(kind='bar')

dow_plot.set(xlabel="Day Of The Week", ylabel="Total Number of Posts",
             title="AI/ML Posts Per day of the week")

dow_plot.get_figure()


#%% save to a file
# this is probably not need if using a jupyter notebook
dow_plot.get_figure().savefig('lab9-1.pdf', bbox_inches='tight')












