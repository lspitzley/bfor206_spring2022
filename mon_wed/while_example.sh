#! /bin/bash

##### Script to demonstrate while loops
##### content from the slides

LIMIT=10


if [ $1 -eq 1 ]
then
	counter=0

	while [ "$counter" -le "$LIMIT" ]
	do
		echo -n "$counter " # prints all output on the same line
		counter=$(( $counter + 1 ))
	done


# Use the continue statement
elif [ $1 -eq 2 ]
then
	a=0
	while [ $a -le $LIMIT ]
	do
		let "a=a+1"
		if [ $a -eq 3 ] || [ $a -eq 11 ]
			then continue # this goes back to the while statement
				      # substitute with break and see what changes
		fi 
		echo -n "$a " 
	done
fi





echo	# empty echo so the next statement prints on a new line.
echo "Done."
