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
import nltk
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

hackers['chat_message'] = hackers.loc[hackers['is_message'] == True, 'original_data'].apply(irc_parse.get_chat_message)

"""
could define a function
def some_function(x):
    return nltk.tokenize.word_tokenize(x.lower())
# or just use a lambda
"""
hackers['chat_message_words'] = hackers.loc[hackers['is_message'] == True, 'chat_message'].apply(lambda x: nltk.tokenize.word_tokenize(x.lower()))


#%% count non-english words

"""
Things we need:
    - A list of English words
    - The individual words in our dataset
    -
    
What need to do:
    - Count the words
    - Compare words in the dataset to English words
    - Omit symbols & numbers

"""

# List of English words
# https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
from nltk.corpus import words

print(words.words())


# Count the words
# First, get the individual tokens/words in our dataset
# if we convert the column to a list, we get nested lists
# test = hackers.loc[hackers['is_message'] == True, 'chat_message_words'].tolist()

# adapted from
# https://stackoverflow.com/questions/55566866/count-the-occurence-of-words-in-a-list-of-all-rows-of-dataframe
# convert to a flat list
all_tokens = [y for x in hackers.loc[hackers['is_message'] == True, 'chat_message_words'] for y in x]

# Count the words
from collections import Counter

token_counts = Counter(all_tokens)
print(token_counts.most_common(10))


# find non-English words
# https://stackoverflow.com/questions/41125909/python-find-elements-in-one-list-that-are-not-in-the-other
non_english = set(words.words())
non_english_tokens = [item for item in all_tokens if item not in non_english]

non_english_counts = Counter(non_english_tokens)
non_english_counts.most_common(100)



#%% save data to csv

hackers.to_csv('hackers_clean.csv')




