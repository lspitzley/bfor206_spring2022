# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:38:41 2022

Class 11-2: Regular Expressions

@author: ls458663
"""

#%% imports
import re

#%% basic examples
string_to_search = 'BFOR206 Programming for Security Analytics'

re.search(r'bfor', string_to_search)
re.search(r'BFOR', string_to_search)

#%% more advanced expressions
hh_mm = 'It is\t13:45\n'
print(hh_mm) # note the tab

time_match = re.search(r'(\d{2}):(\d{2})', hh_mm)
print(time_match)
print(time_match.group())
hours = time_match.group(1)
minutes = time_match.group(2)
new_dict = {}
new_dict['hour'] = hours
print(new_dict)
print(hours, minutes)

#%% find all matches
re.findall(r'BFOR|206', string_to_search) # returns all matches








