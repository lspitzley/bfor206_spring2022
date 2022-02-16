#! /bin/bash

# script to show how redirects work

echo "test1"
echo "test2"

# input is the variable name
read input < input.txt
echo "The input is $input"

#  put the date into our log file
#+ so that we can see *when* something happens

echo `date` >> output.log

#  run the ping command using the URL from the
#+ input.txt file

ping -c3 $input >> output.log


echo "Done."
