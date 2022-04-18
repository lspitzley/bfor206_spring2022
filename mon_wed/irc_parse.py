"""
Functions to parse information from
IRC chat files.

"""

#%% imports
import re

#%% test to make sure pytest works
def sanity_check():
    """This test should always pass.
    The purpose is to make sure Github actions are functioning properly.
    """
    return True


#%% function to find hours and minutes

def get_hours_minutes(row):
    hour_minute = {}
    hour_minute['hour'] = 1
    return hour_minute


#%% define some test cases
def test_get_hours_minutes():
    date_changed_row = '--- Log opened Tue Sep 20 00:01:49 2016'
    join_quit_row = '00:01 -!- Guest40341 [AndChat2541@AN-pl0gl1.8e2d.64f9.r226rd.IP] has quit [Quit: Bye]'
    message_row = '00:25 < ice231> anyone good with exploiting cisco asa with extrabacon?'
    

    assert get_hours_minutes(date_changed_row) == {}
    assert get_hours_minutes(join_quit_row) == {'hour': 0, 'minute': 1}
    assert get_hours_minutes(message_row) == {'hour': 0, 'minute': 25}






def is_date_row(row):
    
    if re.search(r'---', row):
        return True
    return False
    







