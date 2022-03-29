# Homework 2

In this homework, we will analyze posts from
artificial intelligence/machine learning communities
on Reddit.

From this analysis, we will learn how to summarize
data with timestamps, use grouping with `pandas`, and
apply some basic text analysis techniques.

# Data

The data we will use comes from a
[Kaggle data repo](https://www.kaggle.com/maksymshkliarevskyi/reddit-data-science-posts).  


# Setup

You can download the data directly from the Kaggle page
(account required), or from the BFOR 206 Blackboard
(in the 8-2 lecture notes).

Use the tools and techniques from the Python labs
that demonstrate how to use `pandas`. Some parts
of the assignment may have been completed during labs.


<!--  -->
# Scoring
This assignment will be graded out of [12] points. There is a
maximum of [14] possible points.

## 1. Summarize the data (4 points)

1. Which subreddit has the most posts (top 5)?
2. Which user has the most posts (top 5)?
3. Which subreddit has the most distinct post authors?
4. Which subreddit contains the greatest percentage of posts
   with a post body (i.e. contains a value in the `post` column)?

## 2. Visualize the data (4 points)

1. Plot the total number of posts across all subreddits over time (line plot).
2. Plot a histogram showing the distribution of post scores.
3. Plot the average number of posts per day of the week.
4. Plot the average number of posts per hour of the day.


## 3. Get insights from the data (4 points)

1. Which subreddits had the most new posts in the latest 30 days of data (top 5)?
2. Does the length of a post title correlate with score of the post?
3. What are the top 20 words used in post titles?
4. What are the top 10 most linked website domains?

## 4. Make your results professionally pretty (2 pts)

Use a **Jupyter Notebook** to produce your results. This tool is
easy to use and will produce professional output. They are also
rendered by Github, so you do not need to do any screenshots
or other trickery to make things look nice.

For an example of a notebook, check out this example on
[basic `pandas` functionality](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.03-Operations-in-Pandas.ipynb).



# Submission

You may work individually or in pairs.

The homework is due April 15.

Create a new repository using this
[Github Classroom link](https://classroom.github.com/a/2HqhSXL1).

Commit and push your code to this Git repository. The
instructor will grade the last commit before the due
date.


# Checkpoints
These are some quantities/values that you can use to check the
correctness of your code. I will update these as needed.

   1. Total number of rows: 527,646
   2. The subreddit with the second-most distinct authors (Q1.3) is
      `statistics`, with 32,982 different post authors.
      `datascienceproject` has the fewest, at 232 distinct post authors.
