# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:53:45 2022

@author: ls458663
"""

#%% imports
import re

#%% some examples
string_to_search = 'BFOR 206: Progamming for Security Analytics'

re.search(r'bfor', string_to_search)
re.search(r'BFOR', string_to_search)

#%% times
hh_mm = 'It is\t13:45\n'
# [0-9]{2} --- find exactly two digits﻿ in a row
result = re.search(r'[0-9]{2}:[0-9]{2}', hh_mm)
print(result)

#shorter regex
result = re.search(r'\d{2}:\d{2}', hh_mm)
print(result)

#%% groups

# if want hours and minutes, there are several ways we could do this
# you could add a split on the ':'
hours = result.group(0).split(':')[0]
minutes = result.group(0).split(':')[1]

# use regular expression groups instead
result = re.search(r'(\d{2}):(\d{2})', hh_mm)
print(result)
print(result.group(1))
hours = result.group(1)
minutes = result.group(2)

# both methods end up with the same end product
# the second is probably faster

#%% other uses
# findall

re.findall(r'BFOR|206', string_to_search) # returns all matches in a list











