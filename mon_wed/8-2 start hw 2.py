#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 11:58:19 2022

@author: kali
"""

#%% imports
import pandas as pd

#%% read in data

aiml_data = pd.read_csv('data/reddit_database.csv')

aiml_data.head()

#%% basic information about the data
aiml_data.info()
aiml_data.describe()

#%% convert date columns to a proper date/time format

aiml_data['author_created_date'] = pd.to_datetime(aiml_data['author_created_utc'], unit='s')

aiml_data['created_date'] = pd.to_datetime(aiml_data['created_date'])

aiml_data.info()

# aiml_data.describe(include='all')

# hide the warning message
aiml_data.describe(include='all', datetime_is_numeric=True)



