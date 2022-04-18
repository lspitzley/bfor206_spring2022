"""
This script will apply the functions
from irc_parse.py to the real dataset
and produce a clean dataframe that is 
suitable for analysis in a Jupyter Notebook.

"""
#%% imports
import pandas as pd


# import our functions
import irc_parse

#%% read in data
raw_log = []
with open('../data/hackers.log', 'r', errors='ignore') as log_file:
    raw_log = log_file.readlines()

#%% create dataframe
hackers = pd.DataFrame(raw_log, columns=['original_data'])


#%% use the is_date_row function
# check if a row is actually a date.
hackers['is_date_row'] = hackers['original_data'].apply(irc_parse.is_date_row)
