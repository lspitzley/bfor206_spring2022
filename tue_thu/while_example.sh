#! /bin/bash


# this script shows some while loop examples.

# USAGE:
# while_example.sh [OPTION]
#
# To run the first while loop
# bash while_example.sh 1 
#
# To run the second while loop
# bash while_example.sh 2



#  define LIMIT here, otherwise it would have to 
#+ be defined in each if or elif statement.

LIMIT=10

if [ $1 -eq 1 ]
then
	counter=0
	# LIMIT=10  --> moved this outside the if statement
	while [ $counter -le $LIMIT ]
	do 
		counter=$(( $counter + 1 ))
		echo "counter is $counter"
	  	# counter=$(( $counter + 1 ))
	done

elif [ $1 -eq 2 ]
then
	a=0
	
	# These two statements were used to debug, uncomment to use them again.
	# echo "a is $a"
	# echo "LIMIT is $LIMIT"
	while [ $a -le $LIMIT ]
	do
		let "a=$a+1"
		if [ $a -eq 3 ] || [ $a -eq 11 ]
			then continue	# continue takes us to the start of the while
		fi

		echo -n "$a "
	done
fi

echo
echo "Done."
