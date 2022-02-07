#! /bin/bash

#########################
# Example if statements #
#########################

if [ $1 -eq 0 ]
	then echo "The first argument is 0"
elif [ $1 -lt 0 ] 
	then echo "The first arguemnt is less than 0. Quitting."
	exit # this will abort the script if it is reached
else 
	echo "The argument is $1"
fi

echo "Done."
