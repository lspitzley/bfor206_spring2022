"""
This script will apply the functions
from irc_parse.py to the real dataset
and produce a clean dataframe that is 
suitable for analysis in a Jupyter Notebook.

"""
#%% imports
import pandas as pd
import nltk

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


#%% check if it is a message row

hackers['is_message_row'] = hackers['original_data'].apply(irc_parse.is_message)

#%% tokenize the message row

hackers['chat_words'] = hackers.loc[hackers['is_message_row']==True, 'original_data'].apply(irc_parse.get_chat_message)

# use a lambda: https://www.w3schools.com/python/python_lambda.asp
hackers['chat_word_list'] = hackers.loc[hackers['is_message_row']==True, 'chat_words'].apply(lambda x: nltk.tokenize.word_tokenize(x.lower()))



#%% count non-english words

"""
Things we need:
    - an English Dictionary
    - Counter
    - messages
    - words/tokens
    - a way to compare our words to the words in the dictionary

Steps to solve this:
    1. Import dictionary (https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python)
    2. Import Counter
    3. Get the message rows
    4. Get the message content
    5. Getting the individual words (tokenize)
    6. Count the words
    7. Filter English/non-English words
    8. Rank the words
"""

# steps 1 & 2
from nltk.corpus import words
from collections import Counter

# steps 3, 4, 5 were already done earlier
# try this like HW2
# word_counts = hackers['chat_word_list'].value_counts()
# it doesn't work in reasonable time

# step 5.2 - get a list of all the words
all_messages = hackers.loc[hackers['is_message_row']==True, 'chat_word_list'].tolist()

# that results in a list of lists
# need a single list
# https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
all_words = [item for sublist in all_messages for item in sublist]

# 6. Count the words
word_counts = Counter(all_words)

# see top words (still need to remove punctuation)
word_counts.most_common(10)


# 7. Filter non-english words
print(words.words())

# 'any' in words.words()

english_words = set(words.words())
# https://stackoverflow.com/questions/2104305/finding-elements-not-in-a-list
non_english = [x for x in all_words if x not in english_words]

non_english_counts = Counter(non_english)

# 8.
non_english_counts.most_common(50)

# filter out formatting characters (like '-', '?')

#%% save the cleaned dataframe
# save the cleaned dataframe to our working folder
hackers.to_csv('hackers_clean.csv')












