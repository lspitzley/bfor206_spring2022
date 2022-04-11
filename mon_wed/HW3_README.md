# Homework 3 Notes

## General Observations
- many rows of people leaving or joining
- logs name changes
- chat messages from users
- identifies when people are searching 
- evilbot responds to commands starting with `-` (line 625)
- most lines have a timestamp (24-hour format)
- User `Hell` seems to be important
- usernames seem to be surrounded by `< >`
- It shows when dates change (rows start with `---`)
- each row or message is a single line
- rows where users join/quit have `-!-` after the time.
- some usernames start with a special character (`@` or `%`, etc.)

## Analysis Requirements
- Data needs to be in a dataframe

### Dataframe Columns
- date & time column(s)
- user
- message content
- type of row (message, connect/disconnect/date change/...) 

# Which files will we need?
Overall structure of the project.

- README.md (this file)
- File for our functions (`irc_parse.py`)
- File for unit tests (`test_irc_parse.py`) - Instructor will provide
- File that applies the functions to create a dataframe (`irc_cleaner.py`)
- Jupyter to get the results using the cleaned dataframe

# Functions for `irc_parse.py`
[ ] `get_username()`
[ ] `get_timestamp()`
[ ] `get_message()`
[ ] `get_date_change()`