#!/usr/bin/env python
# coding: utf-8

# # Exercise: Data Cleaning

# **Exercise 1**
# 
# Today, we will be using the American Community Survey data to examine the racial wealth gap (how income varies by race) in the United States. Note that because the US income distribution has a very small number of people with *extremely* high incomes, and the ACS only collects data from *sample* of Americans, these extreme values are not well represented in the data. However, this data is sufficient to provide a pretty good sense of wealth inequality in the United States.
# 
# To begin, load the ACS Data we used in our first pandas exercise. That [data can be found here](https://github.com/nickeubank/MIDS_Data/tree/master/US_AmericanCommunitySurvey). We'll be working with `US_ACS_2017_10pct_sample.dta` (this is a 10% sample of the original 2017 ACS survey, which included 1% of Americans. Thus the data includes 0.1% of Americans).

# In[1]:


import pandas as pd
acs = pd.read_stata("https://github.com/nickeubank/MIDS_Data/blob/master"
    "/US_AmericanCommunitySurvey/US_ACS_2017_10pct_sample.dta?raw=true")


# In[2]:


acs.columns


# **Exercise 2**
# 
# For this analysis, we will restrict our attention to the variables `age`, `inctot`, `race`, `hispan`, and `empstat`. Keep only these variables.

# In[4]:


acs = acs[["age", "inctot", "race", "hispan", "empstat"]]


# **Exercise 3**
# 
# What is the average (`mean`) age of respondents in our data?
# 
# Note 1: You will hit a couple of the problems we've discussed in our readings this week trying to answer this. 
# 
# Note 2: Any observations whose age is `"90 (90+ in 1980 and 1990)"` are 90 years old. This label is telling us that in the 1980 and 1990 censuses, 90 was the highest age recorded (it was a "top-code"), so even people older than 90 were recorded as 90. But our data comes from 2017, so this does not apply.

# In[8]:


acs.loc[~acs["age"].str.isnumeric(), "age"].unique()


# In[10]:


acs["age"] = acs["age"].astype("object")


# In[11]:


acs.loc[acs["age"] == "less than 1 year old", "age"] = 0
acs.loc[acs["age"] == "90 (90+ in 1980 and 1990)", "age"] = 90
acs["age"] = acs["age"].astype('float')
acs["age"].mean()


# OK if they drop less than 1 year olds, or set to 1 too, so add margin here!

# **Exercise 4**
# 
# Now let's calculate the mean US incomes from this data (recall that income is stored in the `inctot` variable). If you just calculate the average, what do you get? (You may recall from our past reading this answer will be weird—just run with it for now!)

# **Exercise 5**
# 
# Hmmm... That doesn't look right. The average American is definitely not earning 1.7 million dollars a year. Let's look at the values of `inctot` using `value_counts()`. Do you see a problem?
# 
# Now use `value_counts()` with the argument `normalize=True` to see proportions of the sample that report each value instead of the count of people in each category. What percentage of our sample has an income of 9,999,999? What percentage has an income of 0?

# **Exercise 6**
# 
# As we discussed before, the ACS uses a value of 9999999 to denote that income information is not available for someone. The problem with using this kind of "sentinel value" is that pandas doesn't understand that this is supposed to denote missing data, and so when it averages the variable, it doesn't know to ignore 9999999. 
# 
# To help out `pandas`, use the `replace` command to replace all values of 9999999 with `np.nan`. 

# **Exercise 7**
# 
# Now that we've properly labeled our missing data as `np.nan`, let's calculate the average US income once more. 

# **Exercise 8**
# 
# OK, now we've been able to get a reasonable average income number. As we can see, a major advantage of using `np.nan` is that `pandas` knows that `np.nan` observations should just be ignored when we are calculating means. 
# 
# But it's not enough to just get rid of the people who had `inctot` values of 9999999. We also need to know *why* those values were missing. Suppose, for example, that the value of 9999999 was used for anyone who made more than 100,000 dollars: if we just dropped those people, then our estimate of average income wouldn't mean much, would it?
# 
# So let's make sure we understand *why* data is missing for some people. If you recall from our last exercise, it seemed to be the case that most of the people who had incomes of 9999999 were children. Let's make sure that's true by looking at the distribution of the variable `age` for people for whom `inctot` is missing (i.e. subset the data to people with `inctot` missing, then look at the values of `age` with `value_counts()`).
# 
# What is the maximum value of `age` for people for whom `inctot` is missing? Recall that subsetting for observations that are missing requires special functions!

# **Exercise 9**
# 
# Then do the opposite: look at the distribution of the `age` variable for people who whom `inctot` is *not* missing. 
# 
# Can you determine when 9999999 was being used? Is it ok we're excluding those people from our analysis?
# 

# **Exercise 10**
# 
# Great, so now we know why those people had missing data, and we're ok with excluding them. 
# 
# But as we previously noted, there are also a lot of observations of zero income in our data, and it's not clear that we want everyone with a zero-income *should* be included in this average, since those may be people who are retired, or in school. 
# 
# Let's limit our attention to people who are currently working. We can do this using `empstat`. Remember you can use `value_counts()` to see what values of `empstat` are in the data!

# **Exercise 11**
# 
# Now let's estimate the racial income gap in the United States. Subsetting using the `race` variable, what is the average salary for employed Black Americans, and what is the average salary for employed White Americans? In percentage terms, how much more does the average White American make than the average Black American?
# 
# **Note:** these values are not quite accurate estimates. As we'll discuss in later lessons, to get completely accurate estimates from the ACS we have to take into account how people were selected to be interviewed. But you get pretty good estimates in most cases even without taking into account the sampling weights—your estimate of the racial wage gap without weights is within 5\% of the corrected value. 
# 
# **Note:** This is probably an underestimate of the wage gap, at least as you're thinking of it. The reason is that the US Census Bureau treats Hispanic respondents as a sub-category of "White." While all ethnic distinctions are socially constructed, and so on some level these distinctions are *all* problematic and subjective, this coding is inconsistent with what most Americans think of when they hear the term "White", which is though of as a category that is distinct from "Hispanic or Latino." So when we subset our data for "White Americans" using the `race` variable, the population we were actually looking at was what most Americans think of as "White Americans & Hispanic Americans." As Hispanic respondents tend to earn less than White Non-Hispanic respondents, including them in the "White" category lowers the average income for that group, making the wage gap look smaller than it really is. If you want, you can also use the `hispan` variable to separate out "White, Hispanic" respondents from "White, Non-Hispanic" respondents (someone is a White Non-Hispanic respondent if their `race` value is White and their `hispan` value is "Not Hispanic").
# 
# ## Want more practice?
# 
# **(1)** As noted above, these estimates are not actually *quite* correct because we aren't using survey weights. To calculate a weighted average that takes into account survey weights, you need to use the following formula:
# 
# $$weighted\_mean\_of\_x = \frac{\sum_i x_i * weight_i}{\sum_i weight_i}$$
# 
# (As you can see, when $weight_i$ is constant for all observations, this just simplifies to our normal formula for mean values. It is only when weights vary across individuals that weights must be explicitly addressed).
# 
# In this data, weights are stored in the variable `perwt`, which is the number of people for which each observation is a stand-in (the inverse of that observations sampling probability). 
# 
# Using the formula, re-calculate the *weighted* average income for both populations. 
# 
# **(2)** Now calculate the weighted average income gap between *non-hispanic* White Americans and Black Americans.
