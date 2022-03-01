#!/bin/bash

# this script just echos a date to a file.

echo "`date`: cron script running."

# another way would be to redirect inside the script
# echo "`date`: cron script running." >> bfor206_spring2022/tue_thu/output.log

# you could even get fancy and use an argument
#+instead of hard-coding the output location

# echo "`date`: cron script running." >> $1


