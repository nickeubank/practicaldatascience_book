#!/usr/bin/env python
# coding: utf-8

# # Groupby and Arrest Data
# 
# In our merging exercises, we examined the relationship between county-level violent arrest totals and county-level drug arrest totals. In those exercises, you were given a dataset that provided you with county-level arrest totals. But that's not actually how the data is provided by the state of California. This week we will work with the *raw* California arrest data, which is not organized by county or even county-year. 
# 
# 

# **(1)** Download the raw California arrest data from the State Attorney General's office [here](https://openjustice.doj.ca.gov/data) by scrolling down to the "Arrests" category and downloading the "Arrests - CSV, 5.8 MB" file. 

# ## Learning the Group Structure of Your Data
# 
# **(2)** What is the unit of observation for this dataset? In other words, when row zero says that there were 505 arrests for `VIOLENT` crimes, what exactly is that telling you -- 505 arrests in 1980? 505 arrests in Alameda County?

# ### Testing Your Assumptions
# 
# It's important to be able to test whether the data you are working with really is organized the way you think it is, especially when working with groupby, so let's discuss how to check your answer to number 2 with `duplicated`. Consider the following data:

# In[3]:


import pandas as pd

df = pd.DataFrame(
    {
        "social_security_numbers": [
            111111111,
            222222222,
            222222222,
            333333333,
            333333333,
        ],
        "second_column": ["a", "a", "a", "a", "b"],
    }
)
df


# If we want to see if there are any duplicate rows in the dataset, we can use `.duplicated()`:

# In[4]:


df.duplicated()


# As you can see, `.duplicated()` looks at each row, and returns `True` if it has seen the row it is looking at before. Note that it doesn't tag *all* the rows that look similar -- it treats the first instance of a row as unique, and only tags subsequent repitions are "duplicates" (You can change this behavior with keyword arguments if you want all rows tagged).
# 
# Duplicated can also be used to test for duplicates on a sub-set of rows. For example, if we want to test for rows with duplicate values of the variable `social_security_numbers`, we can type:

# In[5]:


df.duplicated(["social_security_numbers"])


# Since `duplicated` is now only looking at the first column, the last row is now a duplicate (because 333333333 is duplicated), where when we considered all columns, it was not a duplicate (because the value in the second column varied. 
# 
# We can now pair `.duplicated()` with the `.any()` function to test for the presence of duplicates in your dataset, which is how we test if we really understand what constitutes a unique observation (i.e. if we think each row of our data is a unique person, then we shouldn't see any duplicated values of social security numbers, which are unique to each person in the United States). 
# 
# When you run `.any()` on an array of booleans, it returns a single value of `True` if *any* entries are `True`, and a single value of `False` if *no* entries are `True`. (You can also use `.all()` to test if all entries are false). 
# 
# Thus the command: `df.duplicated(['social_security_numbers'])` will return `False` if `social_security_numbers` uniquely idenfies every row in our dataset (since there are no duplicates)! If any rows are duplicated, then `social_security_numbers` doesn't uniquely identify our observations (i.e. each row does not represent a unique person):

# In[6]:


df.duplicated(["social_security_numbers"]).any()


# This might feel backward, so you can also add a `not` before the test if you want. :) In fact, in my code I add an explicit test using the `assert` statement. The command `assert` says "if the thing that follows this is `True`, don't do anything; if it's False, raise an exception. So in my code, I often write:  

# In[7]:


assert not df.duplicated(['social_security_numbers']).any()


# (which in this case raises an exception! Because the rows *aren't* unique!)

# **(3)** Use `duplicated` to test if the variables *you* think uniquely identify rows in your data really do uniquely identify rows. If you were wrong, update your beliefs!

# **(4)** Once you have a handle on how the data looks now, please **collapse the data** to be one observation per county-year-racial group. 
# 
# **Hint:** Think carefully about the most appropriate aggregation function given the data we're working with!

# **Note:** By default, `pandas` likes to make your grouping variables into a hierarchical index. Personally, I find hierarchical indices very weird and not worth dealing with. To avoid this, use the `as_index=False` option in `groupby`. 

# **(5)** Given your answer from 3, what groups where you collapsing in question 4?

# **(6)** Does the racial composition of arrests in each county vary by arrest type? In other words, do Blacks make up a larger portion of the people arrested for drug offenses than violent offenses? To answer this question, you will need to compute the proportion of all arrests in a county-year that occur within each racial group. 
# 
# In trying to do this, break the problem down into pieces: 
# 
# - What two variables do you want in your data you don't have now to answer this question?
# - What two *intermediate* variables do you need in order to calculate those two final variables?
# - How would you get those *intermediate* variables in your data?
# 
# There is a temptation to try and use a function like `apply` to do this all in one big swing, but it's much safer, easier, and actually faster to do the problem in smaller steps. 
# 
# **Hint:** `transform` should probably make an appearance...

# This merges are an easy place to do things wrong, so I'd also recommend eye-balling your data to be sure you did things right!

# **(6a)** We're about to start studying this data by plotting the share of violent arrestees that are Black against the share of felony drug arrestees that are Black. But the moment where you finish your data manipulations and are about to start you data analysis is a *great* time to just make sure everything in your data looks good. Let's run a few checks:
# 
# - Are your values of the share of felony arrestees who were arrested for violent crimes reasonable (greater than 0 and less than 1)?
# - You're about to analyze the data using only the rows for the Black racial group. How many unique counties are there with data for Black arrestees? How many for White arrestees? Do you remember how many counties there are in CA (google is your friend if not!).
# - Do you have the same number of observations for all the years you're studying? 

# **(7)** Now plot the share of violent arrestees that are Black against the share of felony drug arrestees that are Black. Do they look proportionate?
# 
# **Hint:** You can add a reference line with the code `geom_abline()`. Just specify an intercept and slope (`intercept=` and `slope=`) as keyword arguments. 

# (A quick note of warning on interpretation: these results can tell you whether Black Californians make up a larger proportion of *arrests* for certain types of crimes, not whether they make up a larger proportion of people who *commit* a give type of crime! For example, there is extensive data that shows that Black and White Americans *use* drugs at the same rate, but Black Americans are arrested for drug use *much* more often. So be aware that arrests != crimes committed.)

# **(8)** Let's look at look at trends in arrests over time. For example, is the proportion of arrests for drug use that are Californians of Color categories changing over time? (for non-Americans: "people of color" is a term for people who do not identify as White, and includes a range of identities, including Black, Hispanic, Asian, Middle Eastern, etc...)
# 
# Plot the proportion of drug arrestees that are White over time. 

# **(9)** As you look at the results you just plotted, you should see that the share of arrestees who are White has been declining over time. Does that necessary imply that police have been shifting their attention away from White Californians and towards Californians of Color? 
# 
# **Hint:** If you don't see the problem with that interpretation, [check out this table](https://en.wikipedia.org/wiki/Demographics_of_California#Native_American_Indians). 

# **(10)** To address this, let's merge in demographic data for California over time. Download [this file with racial demographic breakdowns for the US](https://www.dropbox.com/s/3f4mnl6869je2pf/County_Demographics.zip?dl=0). In the zipped folder you download, you will find both data *and* a codebook you'll need to interpret your data. 
# 
# **Note:** In interpreting these variables, bear in mind that the US government considers "Hispanic" to be an identity that is distinct from "race". As such, most hispanic Americans are classified as "White". So if it is not explicitly stated otherwise, "White" includes Hispanic Californias. In our analysis, we wish to consider "Hispanic" as it's own category. 
# 
# Read in this data and find the variables you need to normalize racial arrest shares by population shares and merge it in to our arrest data, keeping all years of arrest data. 
# 
# **Note:** You will probably hit a problem when you try and import the CSV. The error you will likely get is something like `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 2: invalid continuation byte`.
# 
# This error occurs when file that pandas is trying to read isn't encoded with the format it expects by default (`utf-8`). You can learn more about string encodings by [watching this](https://www.youtube.com/watch?v=MijmeoH9LT4)! 
# 
# To fix this, you normally have to guess and check different formats by passing different encodings to the `encoding` option for `read_csv` and seeing what works. In this case, I'll tell you the encoding is 'latin-1', so pass that to `encoding'. 

# **(11)** Because the US Census occurs once every 10 years, we only have population data for once every 10 years (ok, that's not quite true -- the [census bureau publishes their own interpolations using data they collect between censuses](https://www.census.gov/programs-surveys/popest.html) -- but let's pretend it is for this exercise). To fill in the gaps in our data, we can *interpolate* the values between each census wave. For example, if a county is 75% White in 1990 and 25% in 2000, we could infer it was likely about 50% White in 1995.
# 
# `pandas` offers an `interpolate` method that will do this for you, but `interpolate` just doesn't interpolations for one set of observations. In this case, however, we need to do our interpolations *within each group*, so you'll have to figure out how to use `interpolate` with groupby. (*Hint:* this is probably a job for `apply`). 

# **(12)** Now that we have the share of the population in each county that is White, and the share of drug arrestees who are White all in one dataset, we can look at how the *ratio* of these two numbers changes over time. Plot the trend, over time, in this ratio. 

# Do we see any substantial change in the racial incidence of drug arrests over the 40 years of this data, a period in which there have been several waves of changes in public attitudes and rhetoric around policing, including the rise of the war on drugs, the "tough on crime 1990s", and the more recent wave of concern about the mass incarceration of black Americans?
