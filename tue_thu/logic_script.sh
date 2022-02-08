#! /bin/bash

############################################
# Demonstrate if statements                #
############################################


if [ 1 -lt 0 ]
	then echo "The if statement was true"
elif [ 0 -eq 0 ]
	then echo "The elif statement is true. Exiting"
	exit
else
	echo "None of the conditions were true."
fi 

echo "Done."
