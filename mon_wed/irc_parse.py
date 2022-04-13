"""
Functions to parse information from
IRC chat files.

"""

#%% imports
import re


#%% function to find hours and minutes

def get_hours_minutes(row):
    return {}


#%% define some test cases

date_changed_row = '--- Log opened Tue Sep 20 00:01:49 2016'
join_quit_row = '00:01 -!- Guest40341 [AndChat2541@AN-pl0gl1.8e2d.64f9.r226rd.IP] has quit [Quit: Bye]'
message_row = '00:25 < ice231> anyone good with exploiting cisco asa with extrabacon?'

#%% write simple tests
assert get_hours_minutes(date_changed_row) == {}
assert get_hours_minutes(join_quit_row) == {'hour': 0, 'minute': 1}
assert get_hours_minutes(message_row) == {'hour': 0, 'minute': 25}
