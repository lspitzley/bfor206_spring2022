# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:50:52 2022

@author: ls458663
"""

#%%%  example text

example_phrase = """In this class , presented by Dr. Spitzley, we will process text. How many sentences are there here? One? Two? A fraction, like 3.5 sentences?
                    You should find 6 sentences."""


#%% count sentences
sents = example_phrase.split('.')
len(sents)
print(sents)

#%% better way
import re 
sents = re.split(r'[.?!]\s', example_phrase)
len(sents)
print(sents)
# This still misses common abbreviations (like Dr.)

#%% use NLTK

import nltk

sents = nltk.tokenize.sent_tokenize(example_phrase)
len(sents)
print(sents)

#%% count words

# this one does not handle all whitespace characters
words = example_phrase.split(' ')
# this one is pretty good, but punctuation is still left on words
words = re.split(r'\s+', example_phrase)

# the easiest way
words = nltk.tokenize.word_tokenize(example_phrase)






