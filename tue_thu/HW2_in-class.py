#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:53:45 2022

@author: kali
"""

#%% imports

import pandas as pd
import re

#%% read in the data

aiml_data = pd.read_csv('data/reddit_database.csv')

# take a subsample to make things faster
aiml_data = aiml_data.sample(10000)

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



"""
#################### Class 9-2 ######################
"""

#%% word counts

# ﻿https://stackoverflow.com/questions/46786211/counting-the-frequency-of-words-in-a-pandas-data-frame
words = aiml_data['post'].str.split(expand=True).stack().value_counts()

# this method counts words with capitalization separately

# instead we can use .str.lower() to convert everything to lowercase
words = aiml_data['post'].str.lower().str.split(expand=True).stack().value_counts()

#%% examples of how to change strings with built-in functions

test_string = "This is a test string."
test_string.lower()
test_string.upper()
test_string.find('test')


#%% count the words in the title using lower case

title_words = aiml_data['title'].str.lower().str.split(expand=True).stack().value_counts()

# get top 20 from a pandas Series
title_words.head(20)

#%% alternative method that is probably a bit more efficient

from collections import Counter
results = Counter()
aiml_data['title'].str.lower().str.split().apply(results.update)
# print(results)

results.most_common(20)


"""
################# Class 10-1 ##################
"""

#%% define find_urls function

def find_urls(text):
    """
    This function will take a string
    and search for URLs. It will 
    return a list of any URLs that 
    it finds. If the input is not
    a string, it will attempt to 
    force it into a string.
    
    The regular expression is from
    http://urlregex.com/

    Parameters
    ----------
    text : string
        The text to search for URLs.

    Returns
    -------
    A list of URLs. It will be an empty
    list if there no URLs.

    """
    # print(text)
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(text))
    return urls



#%% test the function to see if it works

# Test 1 - A single URL as input
case_1_input = 'https://www.github.com/'
case_1_output = ["https://www.github.com/"]
assert find_urls(case_1_input) == case_1_output

# Test 2 - longer URLs
case_2_input = "https://www.github.com/lspitzley/bfor206_spring2022"
case_2_output = ["https://www.github.com/lspitzley/bfor206_spring2022"]
assert find_urls(case_2_input) == case_2_output

# Test 3 - no URLs
case_3_input = "There are no URLs in this string"
case_3_output = []
assert find_urls(case_3_input) == case_3_output

# Test 4 - multiple URLs
case_4_input = "I like https://github.com, I also like https://bitbucket.com/"
case_4_output = ["https://github.com,", "https://bitbucket.com/"]
assert find_urls(case_4_input) == case_4_output

# Test 5 - numpy nan value as input
import numpy as np
case_5_input = np.nan
case_5_output = []
assert find_urls(case_5_input) == case_5_output

#%% apply the function to the post column

urls_list = aiml_data['post'].apply(find_urls)


















