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
aiml_data = aiml_data.sample(10000)


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

words = aiml_data['post'].str.split(expand=True).stack().value_counts()

#%% count words with all lowercase

# example

test_string = "This is a test string."
test_string.lower()
test_string.find('test') # shows the location where this is found

words = aiml_data['post'].str.lower().str.split(expand=True).stack().value_counts()

#%% get word counts for titles

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
######################### Class 10-1 ###########################
"""

#%% define find_urls function 

def find_urls(text):
    """
    This function will take a string and
    scan it for any URLs. It will
    return any URLs as a list.

    The method used is from
    http://urlregex.com/  
    
    Parameters
    ----------
    text : string
        Some string of text that may contain 
        one or more URLs.

    Returns
    -------
    A list of URLs, if any.

    """
    # print the value for debug purposes
    # print(text)
    # force things to string if they are not already with str(text)
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(text))
    
    return urls


#%% run the function with a test case

# Test 1 - a single URL
case_1_input = "https://www.github.com/"
case_1_output = ["https://www.github.com/"]
assert find_urls(case_1_input) == case_1_output

# Test 2 - directory after the site name
case_2_input = "https://www.github.com/lspitzley/bfor206_spring2022"
case_2_output = ["https://www.github.com/lspitzley/bfor206_spring2022"]
assert find_urls(case_2_input) == case_2_output

# Test 3 - no URLs in the text
case_3_input = "There are no URLs in this string"
case_3_output = []
assert find_urls(case_3_input) == case_3_output

# Test 4 - Multiple URLs
case_4_input = "I like https://github.com, I also like https://bitbucket.com/"
case_4_output = ["https://github.com,", "https://bitbucket.com/"]
# test_4 = find_urls(case_4_input)
assert find_urls(case_4_input) == case_4_output

# Test 5 - np.nan gets passed
import numpy as np
case_5_input = np.nan
case_5_output = []
assert find_urls(case_5_input) == case_5_output


#%% use this function for all of the posts

urls_list = aiml_data['post'].apply(find_urls)















