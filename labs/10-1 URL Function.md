# BFOR 206 Lab
## Class 10-1: A function to find URLs


# Task Description

In this lab, we will build and test a function to find
URLs in a string of text. This function will have some
formal tests.



# Function Description

**Function name:** find_urls

**Arguments:**  a string (we will name it "text")

**Return:** A list containing any URLs found


# Test Cases

## Case 1
Input: "https://www.github.com/"
Output: ["https://www.github.com/"]

## Case 2

Input: "https://www.github.com/lspitzley/bfor206_spring2022"
Output: ["https://www.github.com/lspitzley/bfor206_spring2022"]

## Case 3
Input: "There are no URLs in this string"
Output: []

# Case 4
Input: "I like https://github.com, I also like https://bitbucket.com/"
Output: ["https://github.com", "https://bitbucket.com/"]


# Submission instructions

**Scripts that produce unhandled errors will not be accepted!**

Run assertions to show that the function passes the tests
shown above.

When you are finished, submit two screenshots on Blackboard:
1.  A screenshot of your code.
2.  A screenshot of output that looks very
    similar to the output in the test cases.
