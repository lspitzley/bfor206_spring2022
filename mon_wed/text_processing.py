# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:46:59 2022

This module contains functions 
that are useful for text processing.

It also contains tests. To run
the tests, run the script directly.

@author: ls458663
"""

#%% imports
import re

#%% define find_urls function 

def find_urls(text):
    """
    This function will take a string and
    scan it for any URLs. It will
    return any URLs as a list.

    The method used is from
    http://urlregex.com/  
    
    Parameters
    ----------
    text : string
        Some string of text that may contain 
        one or more URLs.

    Returns
    -------
    A list of URLs, if any.

    """
    # print the value for debug purposes
    # print(text)
    # force things to string if they are not already with str(text)
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(text))
    
    return urls


def test_find_urls():
    # Test 1 - a single URL
    case_1_input = "https://www.github.com/"
    case_1_output = ["https://www.github.com/"]
    assert find_urls(case_1_input) == case_1_output

    # Test 2 - directory after the site name
    case_2_input = "https://www.github.com/lspitzley/bfor206_spring2022"
    case_2_output = ["https://www.github.com/lspitzley/bfor206_spring2022"]
    assert find_urls(case_2_input) == case_2_output

    # Test 3 - no URLs in the text
    case_3_input = "There are no URLs in this string"
    case_3_output = []
    assert find_urls(case_3_input) == case_3_output

    # Test 4 - Multiple URLs
    case_4_input = "I like https://github.com, I also like https://bitbucket.com/"
    case_4_output = ["https://github.com,", "https://bitbucket.com/"]
    # test_4 = find_urls(case_4_input)
    assert find_urls(case_4_input) == case_4_output

    # Test 5 - np.nan gets passed
    import numpy as np
    case_5_input = np.nan
    case_5_output = []
    assert find_urls(case_5_input) == case_5_output



if __name__ == '__main__':
	print('Running module text_processing.py')
	# run the function with the tests
	test_find_urls()
	print('Done.')










