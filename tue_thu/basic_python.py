#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:37:39 2022

Examples of functions and 
for loops and if statments.

@author: kali
"""

#%% create empty function

def new_function():
    pass


#%% call the new function

new_function()


#%% function with a single argument
def func2(arg1):
    print('The argument is:', arg1)
    
#%% call func2
func2('hello world')
# func2() # no arguments will produce an error

#%% function with two args and a default value
def func3(arg1, arg2=True):
    if arg2:
        print('arg2 is True')
    
    print("The value of arg1 is", arg1)
    
#%% run function 3

# run function with 1 argument
func3('bfor 206')

# run with different arg2
func3('bfor 206', False)

# we can call function with named arguments
func3(arg2=False, arg1='bfor 206')

#%% function to add two numbers

def add_numbers(a, b):
    """ add two numbers together """
    result = float(a) + float(b)
    return result

#%% call the add_numbers function
c = add_numbers(11, 22)
print(c)

#%% define some basic tests

assert add_numbers(2, 2) == 4
assert add_numbers(-2, -2) == -4
assert add_numbers(3.3, 1) == 4.3
assert add_numbers('2', '2') == 4


#%% if statements
a = 1
b = 1

if a > b:
    print('a is greater than b')
elif b > a:
    print('b is greater than a')
else:
    print('a and b must be the same')


#%% the None keyword
d = 'test'

if d:
    print("d has a value")

e = None
# the if statement will be false if e = None
if e:
    print('e has a value')
    
if not e:
    print('e is None')

#%% for loops

for i in range(10):
    print(i)
    
#%% lists

my_list = ["Hello", "BFOR", 206, None, "Bye!"]
print(my_list[0])
print(my_list[4])

#%% for loop to iterate over a list
for item in my_list:
    print(item)


















