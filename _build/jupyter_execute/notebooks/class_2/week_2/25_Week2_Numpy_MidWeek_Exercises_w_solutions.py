#!/usr/bin/env python
# coding: utf-8

# # (Ungraded) Vector Exercises
# 
# **Note**: 
# 
# > This exercise has been written out in something called a Jupyter Notebook. We'll discuss Jupyter Notebooks in more detail later in the course—they are very a powerful tool for data science communication!—but for the time being, the notebook is just a convenient way for us to write out the exercise. You don't need to *do* anything with the notebook except read its contents—just use write your Python code in a regular `.py` file.
# 
# ## Exercise 1: Favorite Numbers
# 
# 1. Make a vector called `my_favorite_numbers` containing my favorite numbers: `42`, `47`, and `10,213,223`.
#    - (Can you figure out why each one is interesting to me? There's a story behind every one!)
# 2. Use the `np.mean()` function to find out the average of my favorite numbers. 
# 3. Can you get Python to report back to you the length of my vector in two ways?
# 4. Create a vector will all the numbers from 1-10 *without* typing out all the numbers from 1 to 10 called `first_ten` (note I'm asking for all of the numbers from **1** to 10, including 10 itself, not zero to 10).
# 5. Now double all the values of `first_ten` in one operation.
# 6. Now create a new variable by adding `first_ten` to itself.

# ## Vector Exercise 2: The US Income Distribution
# 
# In these exercises, we will load and work with a vector that contains estimates of the total income (from all sources) of a random sample of American households collected by the U.S. Census Bureau in 2015-2019 as part of the American Community Survey (ACS).
# 
# (Apologies to people who are not from the United States -- most of our users come from the US, so picking the United States seemed like the least bad option. However, if you are interested in completing these same exercises for your own country, head over to [IPUMS International](https://international.ipums.org/international/) to see if analogous income data has been made available by your country's Census Bureau. Simply click on the "Browse Data" button, then "Select Sample" in the top left to find the most recent data available for your country. Then see if you can find income data under the "Select Harmonized Variables" "PERSON" or "HOUSEHOLD" drop-down menus. Note that income data is hard to collect, so it's probably not available for most countries.)
# 
# 1. Estimate your own *household's* gross (pretax) income and write it down (we will be working with household gross income, so if multiple people in your household work add up their incomes.) 
#    - If you aren't an American, head over to [this OECD website](https://data.oecd.org/conversion/purchasing-power-parities-ppp.htm) to find the Purchasing Power Parity (PPP) exchange-rate between your currency and the US dollar in 2019. Note that this exchange rate may be quite different from the official exchange rate -- [PPP is a method of calculating exchange rates](https://en.wikipedia.org/wiki/Purchasing_power_parity) that is meant to take into account differences in cost-of-living and labor across countries to generate an exchange rate that accurately reflects buying power.
# 2. Now make a guess about what share of American households earn less money than your household (in other words, what is your household's *income percentile*). For example, if I thought my household earned more than 90% of households, I would say that my household is in the 90th income percentile.
# 3. We are now going to load a vector of total incomes for a representative sample of US households between 2015 and 2019. Use the command `np.loadtxt("data/us_household_incomes.txt")` to load the vector. Make sure to assign the result of that command to a new variable.
# 4. What was the mean (average) household income in the United States between 2015 and 2019?
# 5. What was the median household income in the United States during this period? (hint: if `np.mean()` returns the mean of a vector, you can probably guess how to get the median... :) ). The median income is the income of the household that earned more than 50% of American households, and earned less than 50% of American households.
#    -  You will notice that the median household income is significantly less than the average -- that's because there are a small amount of households in the US that earn a great deal of money and pull up the average.
# 6. Now let's see if your impression of where *your* household sat in the US income distribution was correct! The function `np.percentile(v, p)` returns the value for which the percent of observations `p` in the vector `v` have values less than the return value. So for example, `np.percentile(incomes, 10)` will return the household income (if I named the vector that I got in question 3 `incomes`) that is greater than 10% of the values in `incomes` (and implicitly the income that is less than the income of the other ~90% of households). If you plug in the percentile that you guessed in question 2, does that look like your household's gross income? 
#    - Odds are that you guessed that you are somewhere near the middle of the US income distribution, but that you are not -- this is actually [a well-documented sociological phenomenon!](https://www.theatlantic.com/politics/archive/2013/08/why-americans-all-believe-they-are-middle-class/278240/).
# 7. Try out different percentiles until you find where *your* household fits into the US income distribution!
# 8. In the recent *Occupy Wall Street* movement in the United States, protesters could often be seen holding signs that read "We Are The 99%!" and "Tax the 1%!". Without checking the data, what household income cut off do you think defines people who are in the 1%?
# 9. Now check your data -- using `np.percentile()`, what is the income cut off that puts a household in the 1%? Is that more or less than what you expected? Then [check out this article!](https://www.chicagobooth.edu/review/never-mind-1-percent-lets-talk-about-001-percent) **Note:** This data cannot be used to reliably measure income cutoffs much above the top 1% given the number of observations in the data.

# ## Want to Check Your Answers?
# 
# While this is an ungraded exercise, there is a quiz on Coursera where you can submit your answers to verifiable questions (i.e., questions for which everyone will have the same answer) to check you got the right thing.

# ### Data Citation
# 
# The ACS data used in this exercise are a subsample of the IPUMS USA data available from [usa.ipums.org.](usa.ipums.org)
# 
# Please cite use of the data as follows: Steven Ruggles, Sarah Flood, Sophia Foster, Ronald Goeken, Jose Pacas, Megan Schouweiler and Matthew Sobek. IPUMS USA: Version 11.0 [dataset]. Minneapolis, MN: IPUMS, 2021. https://doi.org/10.18128/D010.V11.0
# 
# These data are intended for this exercise only. Individuals analyzing the data for other purposes must submit a separate data extract request directly via IPUMS USA.
# 
# Individuals are not to redistribute the data without permission. Contact ipums@umn.edu for redistribution requests.

# ## Solutions
# 
# ### Exercise 1

# In[1]:


# Question 1
import numpy as np

my_favorite_numbers = np.array([42, 47, 10_213_223])
my_favorite_numbers
# 42: Answer to the Ultimate Question of Life, the Universe, and Everything
# 47: My alma mater's favorite number, and a favorite of my favorite show (Star Trek) 
    #  https://en.wikipedia.org/wiki/47_(number)#In_popular_culture
# 10_213_223: Self describing, in order! One 0, two 1s, three 2's, two 3's


# In[2]:


# Question 2
np.mean(my_favorite_numbers)


# In[3]:


# Question 3
len(my_favorite_numbers)


# In[4]:


my_favorite_numbers.size


# In[5]:


# Question 4

first_ten = np.arange(1, 11)
first_ten


# In[6]:


# Question 5

first_ten * 2


# In[7]:


# Question 6

doubled = first_ten + first_ten
doubled


# 
# ### Exercise 2

# In[8]:


# Question three
import numpy as np

income = np.loadtxt("data/us_household_incomes.txt")
income


# In[9]:


# Question 4

np.mean(income)


# In[10]:


# Question 5

np.median(income)


# In[11]:


# Question 6/7

np.percentile(income, 93)


# In[12]:


# Question 9

np.percentile(income, 99)

# Not even a million!

