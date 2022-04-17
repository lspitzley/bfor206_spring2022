# Homework 3

Processing Internet Relay Chat (IRC) logs from an online
hacking community..

# Overview
The purpose of this homework is to analyze textual log data from
an online chat forum related to the Anonymous hacktivist group.
You will learn how to apply regular expressions, summarize log data,
quantify text data, and summarize time trends.


# Data
IRC is an early protocol for instant messaging developed in the
early years of the Internet. The openness and ability to remain
anonymous has made IRC a popular tool for hacker networks to
collaborate and share ideas.

The data comes from the
[AZSecure Project](https://www.azsecure-data.org/internet-relay-chat.html).
It contains two years of chats between hackers associated with the
hacktivist group Anonymous. In these logs they share information
about malware, setting up servers to deploy attacks, and other
information related to hacking systems.

The collection and analysis of these chats is a form of
cyber-threat intelligence. The analysis of these chats and
other dark web data sources enable proactive defense against
attacks.

# Analysis
## 1. User Data (8pts)

1.  Which users posted the most messages (2pts)?
2.  Which users logged in the greatest number of times? (2pts)
3.	Which users spent the most *time* in the chat? (3pts)
4.  Who are the administrators (username begins with `@`) (1pt).

## 2. Messages (8pts)
1.	Count the total number of written messages
    (only those with actual text content) (1 pts).
2.	Find the most common words (only include message content) (2 pts)
3.	Find and rank (by count) words not in an English dictionary (2 pts).
    This is a simple method that can identify some names of malware tools.
4.	How many distinct URLs were posted in the chat? (1 pt)
5.  Which URLs were posted the most (top 5)? (1 pt)
6.  Which domains (e.g. `github.com/` or `youtube.com`) were shared the most. 
6.  Generate a list of sites on the Dark Web (sites ending in
    .onion) (1pt)

## 3. General Activity (4pts)
1.  Which hours of the day had the most messages (1 pt)?
2.  Which days had the most messages (top 10 days) (2pts)?
2.	Rank the days of the week by average message count (1pt).

## 4. Unit Tests
1. Each unit test that passes on Github will receive 1 point. There are 
   11 total tests. These are documented in the Homework 3 repo.

# Grading
There are 31 points available (20 from questions, 11 from tests).
The assignment is graded out of 25 points. Scores above 25 will
receive extra credit.

All analysis questions must be submitted using a Jupyter Notebook.
Screenshots will not be considered for this assignment!


# Submission

Follow this link to
[create your Homework 3 submission](https://classroom.github.com/a/zqHqNfTj).
You can work indvidually or with a patner. Please
add your name and your partner's name to the readme to 
make grading easier.

Commit and push your code to this Git repository. The
instructor will grade the last commit before the due
date. The instructor may
wish to see a demonstration of your code.

# Tips

- <+evilbot> This user is a bot. If possible, filter this user’s
  posts from the chat
- You can identify changes in days with the messages
  “--- Day changed Mon Sep 26 2016”. There are some instances of
  this measure missing. It is possible to correct this issue by
  looking at the times of the day (i.e. the hour rolls over to 00).
- Users can change their usernames. An alternative to usernames
  for login-logout behavior is to use their login identifiers
  (for example: [androirc@AN-l8e.7dp.8hdu3q.IP]).


