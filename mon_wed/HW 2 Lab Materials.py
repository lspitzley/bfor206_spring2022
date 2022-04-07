#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 11:58:19 2022

@author: kali
"""

#%% imports
import pandas as pd
import re

#%% read in data

aiml_data = pd.read_csv('data/reddit_database.csv')

aiml_data.head()

#%% basic information about the data
aiml_data.info()
aiml_data.describe()

#%% convert date columns to a proper date/time format

aiml_data['author_created_date'] = pd.to_datetime(aiml_data['author_created_utc'], unit='s')

aiml_data['created_date'] = pd.to_datetime(aiml_data['created_date'])

# create a smaller subset of the data to make working faster
# remove this before the full analysis
# aiml_data = aiml_data.sample(10000)


aiml_data.info()

# aiml_data.describe(include='all')

# hide the warning message
aiml_data.describe(include='all', datetime_is_numeric=True)


#%% code for 9-1
"""
#################### Class 9-1 ###################
"""

#%% get the day of the week

aiml_data['dow'] = aiml_data['created_date'].dt.day_name()

# this prints the plot directly, minimal formatting:
aiml_data.groupby('dow')['created_date'].count().plot(kind='bar')
####                ^         ^           ^          ^
#           break down by dow |           |           |
#                      count created_date |           |
#                                    summarization    |
#                                                   plot   

#%% format the plot to be ordered by natural day of the week

aiml_data['dow'] = pd.Categorical(aiml_data['dow'], categories=
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
    ordered=True)


#%% make a professional plot with labels

# to format the plot, store it and add elements.
dow_plot = aiml_data.groupby('dow')['created_date'].count().plot(kind='bar')

# add axis labels and title
dow_plot.set(xlabel="Day Of The Week", ylabel="Total Number of Posts",
             title="AI/ML Posts Per day of the week")


dow_plot.get_figure()

dow_plot.get_figure().savefig('lab9-1.pdf')


"""
######################## Class 9-2 ####################
"""
#%% count words for the posts column

# words = aiml_data['post'].str.split(expand=True).stack().value_counts()

#%% count words with all lowercase

# example

test_string = "This is a test string."
test_string.lower()
test_string.find('test') # shows the location where this is found

# words = aiml_data['post'].str.lower().str.split(expand=True).stack().value_counts()

#%% get word counts for titles
"""
######
Removed for being extremely slow
title_words = aiml_data['title'].str.lower().str.split(expand=True).stack().value_counts()

# show top 20
title_words.head(20)

#%% alternative method
# https://stackoverflow.com/questions/18936957/count-distinct-words-from-a-pandas-data-frame
from collections import Counter
results = Counter()
aiml_data['title'].str.lower().str.split().apply(results.update)
# print(results)

results.most_common(20)
"""

# Alternative count method that is much faster
post_words = aiml_data['post'].str.lower().str.split().explode().value_counts()
print(post_words.head(20))

"""
######################### Class 10-1 ###########################

The code from this has been moved to 
text_processing.py as part of the 10-2
class.

"""


#%% Class 10-2
"""
##################### Class 10-2 ################
"""
# yours is probably in your main folder
# so just do import text_processing
# I add mon_wed. because the script is in a subfolder
import text_processing 


#%% use this function for all of the posts

urls_list = aiml_data['post'].apply(mon_wed.text_processing.find_urls)















