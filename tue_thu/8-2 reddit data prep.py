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


















