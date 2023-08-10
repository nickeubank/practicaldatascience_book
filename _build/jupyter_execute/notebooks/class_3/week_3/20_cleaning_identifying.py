#!/usr/bin/env python
# coding: utf-8

# # Identifying Data Problems

# In a perfect world, our datasets would all arrive containing only accurate data formatted in exactly the way we need. Sadly, the world we live in is *not* perfect. Either because of clumsy data entry, bad translation between data formats, survey participants trying to be jerks, or the coding errors of other data scientists, messy data is a fact of life. As a result, a key part of being a data scientist is to learn to (a) seek out and identify data cleanliness problems, and (b) learn to correct them. 
# 
# These parts of data science are not nearly as cool or widely discussed as new machine learning packages or the latest learning algorithm, but as anyone who has done data science in the real world will tell you, data cleaning and wrangling will take up a very large portion of your working life. Indeed, it is often said that "data scientists spend 80% of their time cleaning data and only 20% doing analyses" (or, in the version I prefer, "data scientists spend 80% of their time cleaning data and the other 20% of their time complaining about cleaning data.") That's probably a little high on average—a [recent survey by Anaconda](https://www.anaconda.com/state-of-data-science-2020) found on average data scientists reported data wrangling took up about 45% of their time—but what is undisputed is its importance to being a successful data scientist.
# 
# So in this reading we will discuss tools in pandas for identifying problems before we turn to tools for correcting problems in our next reading!

# ## Identifying Data Problems in Pandas 
# 
# Everything I said above may sound... well, awful, but here's the good news: once you get into it, data cleaning begins to feel less like grunt work and more like being a detective, and it can actually be a lot of fun.
# 
# 
# ### Your Challenge
# 
# Suppose you have been asked to calculate the overall US employment rate and average incomes for men and women, as well as the employment rate and average income of people in their 30s and 40s. To accomplish this task, you have been handed a 0.1% sample of the US American Community Survey—a representative survey of residents of the United States published by the US Census Bureau. This is real data, and so like all real data comes with lots of quirk and oddities we'll need to navigate.
# 
# Moreover, you've even been told that the variable for gender in the dataset is `sex`, the variable for age is `age`, the variable for income is `inctot`, and the variable for whether someone is employed is `empstat`. Should be pretty easy, right? Let's do it!
# 
# So the first thing, of course, is we'll load the data and subset for the variables we want:

# In[1]:


import pandas as pd

# Here we load the American Community Survey data.
# Note that here we're using a data loading trick
# we didn't discuss in detail in our previous readings:
# pandas will read data directly from a URL!

acs = pd.read_stata(
    "https://github.com/nickeubank/MIDS_Data/blob/master"
    "/US_AmericanCommunitySurvey/US_ACS_2017_10pct_sample.dta?raw=true"
)

# For this exercise, we'll focus on just these five variables,
# which from the official documentation provided by the US census 
# bureau we know consist of the year the survey was conducted,
# the gender of the respondent, their age, their total income, 
# and their employment status.
#
# You can find the documenation for this data here: 

acs = acs[["year", "sex", "age", "inctot", "empstat"]]


# Now let's start to analyze our data. For starters, let's get warmed up by just getting the average income in our data:

# In[2]:


acs["inctot"].mean()


# Tada! Well that was easy. Except... that result says the average income in the US is... 1,723,646 dollars. And that's *clearly* not right—the United States is a very economically fortunate country, but the average American is definitely not a millionaire. 
# 
# OK, let's try something different—how about the overall employment rate? The person who gave you the data told you that people who are employed have `empstat` values of `"employed"`, so this should be easy too!

# In[3]:


(acs["empstat"] == "employed").mean()


# Uh.... ok well the US employment rate is definitely not 47%. That'd imply an unemployment rate of 53%!
# 
# So what's going wrong? At this point, there's no way to know, because we jumped to analyzing our data without ever getting to know it. So let's stop, take a step back, and get to know our ACS data before we start trying to analyze it. 

# ## Getting to Know Your Data

# Whenever you get a new dataset, the first thing you probably want to do is just look at a few rows of the data! Seriously. Just look at it—it's amazing how often people skip this step. 
# 
# While there are many ways to do this, I personally recommend using the `.sample()` method, which will provide a random sample of rows from your data. By default, it only returns 1 row, but you can pass in the number of rows you want to get more (e.g., `.sample(5)` for five rows).
# 
# Note that many people also like to use `.head()` (to get the first 5 rows of the data) or `.tail()` (to get the last 5). These are also fine tools to use, but be aware that because most data has been sorted in some way, the first or last 5 rows are unlikely to be *representative* of the data as a whole. Because `.sample()` gives you a random sample of rows, by contrast, it will give you a better sense of what the average row in your dataset looks like. 

# In[4]:


import numpy.random as npr

# The rows that `.sample()` picks will be random.
# Normally that's advantageous, but in 
# this case it results in getting 
# a slightly different set of rows every time
# I run this code, so I'm going to set a 
# seed—something we talked about in Course 2 
# on numpy—so that the rows being picked 
# stay the same every time I run this code.
npr.seed(42)

acs.sample(5)


# Right off the bat, even these few rows have taught us a lot. For example, we can see that at least in this sample, all of our data comes from 2017. We can also see how `sex` has been encoded (as `male` and `female`, not `M` and `F` or `Male` and `Female`), and that our data includes respondents from a wide range of ages including both adults and young children.
# 
# We can also begin to see the causes of some of our problems. For example, it's not clear to see why `acs["inctot"].mean()` didn't get what we wanted. Why? Because in five random rows, we've already gotten three people who report making 9,999,999 dollars, and all three are less than 12 years old. So clearly the variable doesn't just contain actual income data! 
# 
# (What are these `9999999` values? They're something called a "Sentinel Value"—a very old-school way of representing missing data, in which a special value that would never occur naturally was used to indicate when the field was "missing." It was used back in the day when computers didn't use data types that had an actual special way of representing missing data, and some people still use it for backwards compatibility. We'll talk more about these and other ways of representing missing data in an upcoming reading.)
# 
# Similarly, we can also see that while some observations of `empstat` make sense (`employed` or `not in labor force`), there are also values of `n/a` we need to figure out. `n/a` is a common shorthand for "Not Applicable", meaning it didn't make sense to ask the respondent that question. Since we see those appearing for respondents who are under 18, that probably means that `n/a` was filled in for all children, but that's something we'll have to investigate more. But it definitely tells us why we can't calculate the employment rate by running `(acs["empstat"] == "employed").mean()`, since all the `n/a` values would pull down the share of respondents who are employed even though we don't consider children when calculating the employment rate!
# 
# ### Other Introspection Methods
# 
# While looking at a sample of rows is helpful for getting a sense of our data, we of course use pandas (and statistics in general!) because most datasets are too big to look at and understand fully! So how do we get a better grasp of our data?
# 
# The first pair of tools I would suggest are `.value_counts()` and `.describe()`. These are methods to tell you about *all* the values in a single variable. 
# 
# **.value_counts()**
# 
# `.value_counts()`, for example, will show all the unique values a variable takes on *and* the number of occurrences of each value. For example, using `value_counts()` we can see that `empstat` takes on 4 values:

# In[5]:


acs.empstat.value_counts()


# And if we pass the keyword `normalize=True`, we can see the *proportion* of observations that take on each value (instead of the count):

# In[6]:


acs.empstat.value_counts(normalize=True)


# From this, we can see that in addition to the `n/a` observations that appear to be children, we also have two categories of people who aren't employed: `unemployed` and `not in labor force`. A little googling will tell us that `not in the labor force` connotes someone who is not looking for work, and is thus not considered unemployed when calculating the employment (or unemployment) rate—it turns out that the unemployment rate is only meant to tell us about the share of people *who want to work* who haven't found jobs, not the proportion of the overall population with a job.
# 
# So now that we know that, we can calculate our unemployment rate by subsetting for people in those two categories, then calculating our average:

# In[7]:


# Employment Rate
emp_rate = (acs.loc[acs["empstat"].isin(["employed", "unemployed"]), "empstat"] == "employed").mean()


# In[8]:


# Or as we more commonly see it, the
# UNemployment rate:


# In[9]:


1 - emp_rate


# Much better!
# 
# Of course `.value_counts()` stops being useful when the number of unique values a variable takes on gets too big. For example, it isn't that useful to look at `.value_counts()` of total income, because, as we see below, it takes on over 8,000 unique values! Yes we can see there's a cluster at 0 and a cluster at our old friend `9999999`, but beyond that it isn't very helpful. 

# In[10]:


acs["inctot"].value_counts()


# **.describe()**
# 
# So for continuous numeric variables, we instead use `.describe()`, which provides summary statistics for a variable. Statistics is not required for this course, so not everything here will be familiar to all students, but just looking at the minimum value in the data (`min`), the maximum value in the data (`max`), and the the average value (`mean`) can tell you a lot:

# In[11]:


acs["inctot"].describe()


# For example, in addition to our friend `9999999` being the max value, we can see that some people have total incomes of `-9000`. Now that *could* be a real value (maybe someone is in debt?), but we would want to check the documentation for the dataset to see if `-9000` has a special meaning in this case. (Note: turns out it's a real value, but I only know because I checked!).

# ## Summary
# 
# So that's a quick overview of why it's *so* important to explore your data before you charge ahead with your analyses. In particular, here we've shown the value of:
# 
# - Checking a few random rows of your data with `.sample(5)`
# - Checking all the values of a variable with a limited number of discrete values with `.value_counts()`
# - Summarizing the distribution of a continuous variable with lots of values with `.describe()`.
# 
# Now let's talk about how to fix problems when they crop up!
