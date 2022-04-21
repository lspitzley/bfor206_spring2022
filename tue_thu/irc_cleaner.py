# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:35:25 2022

This will be the main script that
cleans up the dataframe that
we can then use later for analyzing
the data.


@author: ls458663
"""
#%% imports
import pandas as pd
import irc_parse

#%% read in data
raw_log = []
with open('../data/hackers.log', 'r', errors='ignore') as log_file:
    raw_log = log_file.readlines()

#%% create dataframe
hackers = pd.DataFrame(raw_log, columns=['original_data'])


#%% find rows that start with dates

hackers['is_date_row'] = hackers['original_data'].apply(irc_parse.is_date_row)

#%% apply the is_message function

hackers['is_message'] = hackers['original_data'].apply(irc_parse.is_message)







