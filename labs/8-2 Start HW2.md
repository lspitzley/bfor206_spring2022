# BFOR 206 Lab
## Class 8-2: Analyzing Reddit Posts on Artificial Intelligence


# Task Description

In this lab, we will analyze the posts from
various Reddit communities that cover Artificial
Intelligence/Machine Learning (AI/ML).

The posts were curated as part of a
[Kaggle project](https://www.kaggle.com/maksymshkliarevskyi/reddit-data-science-posts).

The purpose of this lab is to get the data loaded,
fix issues with dates and times, and produce a basic description
of the dataset.

# Normal Scenario

## Input
**Files:**  Data from Kaggle

## Output
**Terminal:** Tables and plots as described below.


# Test Cases


## Case 1: Show Dataset Info
Print a table showing the dataset info. Make sure the
Dtype for the date columns is `datetime64[ns]` and
not `object`.


Expected Output:

|  Column             | Non-Null Count  | Dtype           |  
| :-------------      | :-------------  | :-----          |
| created_date        | 527646 non-null | datetime64[ns]  |    
| created_timestamp   | 527646 non-null | float64         |
| ...                 | ...             | ...             |


# Submission instructions

**Scripts that produce unhandled errors will not be accepted!**

Run your script to show that it produces output that
matches the test cases.

When you are finished, submit two screenshots on Blackboard:
1.  A screenshot of your code.
2.  A screenshot of output that looks very
    similar to the output in the test cases.
