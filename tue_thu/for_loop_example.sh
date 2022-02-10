#! /bin/bash

# examples of different for loop control statements

# usage: Argument between 1 and 5 to run a specific loop
# example: bash for_loop_example.sh 3 

# make sure there is an argument
if [ $# -ne 1 ]
then
	echo "Need exactly 1 argument. Quitting"
	exit
fi


if [ $1 -eq 1 ]
then
	for i in {0..5}
	do
		echo "The value of \$i is $i"
	done

elif [ $1 -eq 2 ]
then
	name="Lee A Spitzley"
	for part in $name
	do
		echo "$part"
	done

elif [ $1 -eq 3 ]
then
	for n in {0..10..2}
	do
		
		echo "The value in \$sum is $sum" 
		echo "The value of \$n is $n"
		# let "sum=$sum + n" # this is one way
		sum=$(( $sum + n ))
		echo "After adding \$n, the sum is $sum"
	done
	
elif [ $1 -eq 4 ]
then 
	N=10
	for (( i=0; i<N; i++ ))
	do
		echo "The value of \$i is $i"
	done

elif [ $1 -eq 5 ]
then
	for (( i=0; i<5; i++ ))
	do
		echo -n "$i " # NOTICE THE SPACE!
	done
	echo 
fi

echo "Done."
