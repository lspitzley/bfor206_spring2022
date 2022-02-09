#! /bin/bash

# demonstrate for loops

if [ "$1" -eq 1 ]
	then

	for i in {0..5}
	do 
		echo "The value of \$i is $i"
	done
elif [ "$1" -eq 2 ]
	then
	name="Lee A Spitzley"
	for part in $name
	do	
		echo $part
	done
elif [ "$1" -eq 3 ]
	then
	for n in {0..10..2}
	do
		echo "The value of \$n is $n"
		echo "Before: $sum"
		(( sum=$sum + $n ))
		echo "after: $sum"
	done
elif [ "$1" -eq 4 ]
	then 
	N=10
	for (( i=0; i<N; i++ ))
	do
		echo "The value of \$i is $i"
	done

elif [ "$1" -eq 5 ]
	# Show how to print on the same line
	then
	for i in {0..10}
	do
		echo -n "$i " # NOTICE THE SPACE!
	done
	echo # adds a new line at the end
fi

echo "Done."
