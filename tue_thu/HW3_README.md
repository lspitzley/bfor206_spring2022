# Homework 3 Planning

# Observations
- Lots of people coming and going
- Rows have a time at the start of the line
- Lots of different quit messages when someone leaves
- Some usernames have a symbol in front
- Rows that are actions (like join/quit) have `-!-` in the beginning
- Rows that show that the date has changed begin with `---`
- Usernames have `< >` around them
- Users can issue commands. Example on line 874
- user `+evilbot` is a bot that posts a response to the -tools command

## Analysis Requirements
- Data needs to be in a dataframe

### Dataframe Columns
- date & time column(s)
- user
- message content
- type of row (message, connect/disconnect/date change/...) 


# Files We Need

- [ ] README.md (this file) to lay out the project plan
- [ ] irc_parse.py to store functions that help parse the rows in the file
- [ ] test_irc_parse.py to store the tests (instructor will provide this)
- [ ] a script to run the functions and actually process the data (can be any name)
    This should result in a nice, clean dataframe that is ready for analysis.
- [ ] Jupyter Notebook to get the statistics and answer the questions.