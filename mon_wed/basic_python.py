#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:57:43 2022

@author: kali
"""

#%% define an empty function
def new_function():
    pass

#%% run function
new_function()

#%% function with an argument
def func2(arg1):
    print("the argument is", arg1)
    
#%% run function 2
func2("Hello World")
func2("Different argument")
# the variable arg1 is only availble in the function
# This next line will be an error
# print(arg1)

#%% function with a default arg value
def func3(arg1, arg2=True):
    if arg2:
        print('arg2 is True')
    # un indent so the next line is not part of the if statement
    print('The value of arg1 is', arg1)

#%% call func3
# run with just one argument
func3('bfor 206')

# run with two arguments
func3('bfor 206', False)

# you can name the arguments, then order is not important
# exactly the same as the previous call
func3(arg2=False, arg1='bfor 206')


#%% function to add two numbers
def add_numbers(a, b):
    """ add two numbers """
    
    result = float(a) + float(b)

    return result

#%% call add numbers function

c = add_numbers(11, 22)

#%% basic tests for add_numbers

assert add_numbers(2, 2) == 4
assert add_numbers(-2, -2) == -4
assert add_numbers(3.3, 1) == 4.3 # fails when we add int() around variables in the functions
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

#%% check if empty
d = False
d = 'not nothing'

# if d is anything but None (or False), this is true
if d:
    print(d)
    

#%% for loops
for i in range(10):
    print("The value of i is", i)
    
    
    
#%% nested loops

# lists 
my_list = ["This", "is", "a", "list."]

for item in my_list:
    print(item)
    for j in range(2):
        print("j is ", j)

print("Done.")

#%% helpful for the lab
e = None

if not e:
    print('e is None')

if e == None:
    print('e is None')

    
    










