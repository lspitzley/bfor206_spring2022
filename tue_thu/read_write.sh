#! /bin/bash

# Script to demonstrate reading and writing files.

echo "test1"

# read data from a file
# read [variable name] < [input file]

read input < input.txt

echo "the value of \$input is $input"

# empty echo will print a new line, i.e. "\n"
# printf formats the output

# add the date and time to our log file
printf "\n\n `date` \n\n" >> output.log


# run the ping command
ping -c 3 $input >> output.log


echo "Done."
