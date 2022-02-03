#! /bin/bash

# Usage: Run this script with arguments and see the first two printed
# out along with the total number of arguments.

# This script will show how to use arguments

echo "The 0th argument is $0, aka the filename"

# Print the first argument
echo "This is the first argument: $1"

# Print the second argument
echo "The second argument is: $2"

# Show the total number of arguments:
echo "There were $# arguments"

echo "Done."
