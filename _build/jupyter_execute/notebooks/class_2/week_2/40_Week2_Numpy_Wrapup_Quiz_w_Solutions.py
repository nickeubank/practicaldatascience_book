#!/usr/bin/env python
# coding: utf-8

# # Week 2 Numpy Re-cap Exercises
# 
# 
# **Note**: 
# 
# > This exercise has been written out in something called a Jupyter Notebook. We'll discuss Jupyter Notebooks in more detail later in the course—they are very a powerful tool for data science communication!—but for the time being, the notebook is just a convenient way for us to write out the exercise. You don't need to *do* anything with the notebook except read its contents—just use write your Python code in a regular `.py` file.

# ## Income Inequality
# 
# In these exercises, we will return to the vector with estimates of the total income (from all sources) of a random sample of American households collected by the U.S. Census Bureau between 2015 and 2019 as part of the American Community Survey (ACS).
# 
# (As before, apologies to people who are not from the United States -- most of our users come from the US, so picking the United States seemed like the least bad option. However, if you are interested in completing these same exercises for your own country, head over to [IPUMS International](https://international.ipums.org/international/) to see if analogous income data has been made available by your country's Census Bureau. Simply click on the "Browse Data" button, then "Select Sample" in the top left to find the most recent data available for your country. Then see if you can find income data under the "Select Harmonized Variables" "PERSON" or "HOUSEHOLD" drop-down menus. Note that income data is hard to collect, so it's probably not available for most countries.)
# 
# In particular, we are going to use this data to measure household income inequality in the United States, then analyze how that income inequality might change under a range of different tax policies.

# ### Exercise 1
# 
# Use the command `np.loadtxt("data/us_household_incomes.txt")` to load the vector of incomes, and make sure to assign the result of that command to a new variable.
# 
# How many observations are in this vector?

# 
# ### Exercise 2
# 
# In a previous reading, we saw that plotting a histogram of US household incomes was difficult because must of the plot was taken up by very high earners. Now that we know how to subset our data, create a histogram of US household incomes that includes only households making less than $500,000. For these households—the non-millionaires—do we see a more uniform distribution of incomes? Or is there still a significant [right-skew / positive-skew](https://en.wikipedia.org/wiki/Skewness) (most people are on the left of the distribution, but there are more extreme values in the right tail) in the income distribution?
# 
# In other words, is the skewness in the US income distribution driven by extreme high earners, or is it evident at all income levels?
# 
# **Note:** The x-axis' will range will be determined by the data, with the x-axis being made long enough to include ALL data (but no longer). As a result, there *are* observations across the x-axis, even if there are too few for the bar to be visible.
# 
# **Note:** Be aware that this data only measures *income*—e.g., wages, salaries, etc. As a result, it actually massively underestimates incomes at the top of the United States income distribution because most of the income for high earners comes in the form of capital gains and investment appreciation which are not included here.
# 

# ### Exercise 3
# 
# The US poverty line is *about* 20,000 dollars a year. What share of households in these data fall below the US poverty line? (By "share" I mean the proportion, a value between 0 and 1). Round your answer to 4 decimal places.
# 
# (I say "about" because the actual poverty line for household income depends on the number of people in the household, which we have not included in these data.)

# ## Gini Index
# 
# A standard measure of inequality is the [Gini Index / Gini Coefficient](https://en.wikipedia.org/wiki/Gini_coefficient). The measure takes on a value of 0 when everyone in a population has the same allocation of some resource or property, and a value of 1 when all the resource in population accrues to a single person. It is commonly used to measure income and wealth inequality, although it is also worth noting that it has been used in many other contexts, [including neuroscience.](https://neuroplausible.com/gini) 
# 
# For discrete data, the definition of the Gini Index is given below:
# 
# $$Gini\ Index = \frac{2 \sum_{i=1}^n i y_i}{n \sum_{i=1}^n y_i} -\frac{n+1}{n}$$
# 
# Where $i$ is each observations' rank ordering from those with the fewest resources to those with the most, and $y_i$ is the resources of observation $i$. 
# 
# In an upcoming exercise, you will be asked to code this up yourself in a few different ways, but as that is not the focus of *this* exercise, you can just use the `gini()` function from the `ineqpy` package. You can install it with `pip install ineqpy` (it's a little too small of a package to appear in the conda repositories) and import with `from ineqpy.inequality import gini`.

# ### Exercise 4
# 
# Using the `gini()` function above, calculate the Gini Index of income inequality in the US. Round your answer to 4 digits.
# 
# ### Exercise 5
# 
# Go compare your estimate to that of [other countries here.](https://www.indexmundi.com/facts/indicators/SI.POV.GINI/rankings) (Note: in this table, estimated Gini values have been multiplied 100. In addition, as a result of sampling variation, income binning, differences in the exact methods used to calculate income, year of data, availability of data on top incomes, etc., your Gini for the US will be somewhat different from the Gini for the US in this table. It *should* be close to the data from the [US Census Bureau](https://www.statista.com/statistics/219643/gini-coefficient-for-us-individuals-families-and-households/)). How does the US compare to other countries? Is that what you expected? 
#    - **Note:** The Gini Index of income is only one metric of inequality! Results would be very different if we were to calculate, for example, the ratio of the income of the top 0.1% of earners to the income of the lowest-earning 10% of the population, or if we calculated this metric using wealth instead of income!
# 

# 
# ### Exercise 6
# 
# 
# Congratulations! You have been hired by the President of the United States to advise them on their efforts to reduce income inequality. The first set of policies that the president has asked you to evaluate is whether income inequality would be decreased more under:
# 
# - `Policy A`: giving every household that makes less than 40,000 dollars a check for 5,000 dollars, or 
# - `Policy B`: giving every household that makes less than 30,000 dollars a check for 7,000 dollars. 
# 
# What is the new Gini under Policy A? Round your answer to 4 decimals.
# What is the new Gini under Policy B? Round your answer to 4 decimals.
# 
# Which has lowered inequality more?
# 
# - **Note:** Vectors are mutable (like lists), so you should create a clean copy of your income data with the `.copy()` method (e.g. `experiment1 = income_vector.copy()`) before starting to make changes during each exercise. We'll talk a lot more about vector mutability in a future reading, but so long as you use `.copy()` you will be fine here!

# 
# ### Exercise 7
# 
# Now the president would like to know whether income inequality can be reduced more the policy you decided was preferable above, *or* through `Policy C`: applying a tax of 5% to households making more than 250,000 dollars and using the money to pay down the National Debt. 
# 
# (In other words, `Policy C` would reduce the income of any households earning more than 250,000 dollars by 5%.)
# 
# Calculate the Gini Index resulting from the President's tax proposal? Round your answer to 4 decimals.

# ### Exercise 8
# 
# Now suppose we were thinking about applying a 5% tax to people making more than 250,000 dollars and *evenly distributed that tax revenue* to households earning less than 30,000 dollars. Call this `Policy D`. 
# 
# To estimate the effective such a policy on inequality, first calculate the total amount of money that would be generated by this tax if the households in this data were all households in the US. Round your answer to two decimal places.
#   
# **Note:** because these data are just a *sample* of households in the US, the quantity you calculate isn't the actual revenue such a tax would generate in the real world; if you want to calculate the real amount that would be raised, you can multiply the quantity you calculate by 137 (our data include about 1 out of every 137 households in the US). Don't do that multiplication to generate your answer here—as we'll see below that isn't necessary for the analysis we want to undertake.

# ### Exercise 9
# 
# Now calculate the total number of households earning less than 30,000 dollars in these data, and divide the revenue generated by the tax by the number of households earning less than 30,000 dollars. Round your answer to one decimal place.
# 
# **Note:** unlike in Exercise 8, the quantity you estimate here *is* a good estimate of the amount of money that would be available for each household if we imposed this tax on the real world. Why? Because both the quantity you estimated in Question 8 *and* the number of households you calculate here represent 1/137th the actual, real world quantities in the United States. So when you divide one by the other, you get the true ratio -- the fact that both are 1/137th the real quality cancels out!

# ### Exercise 10
# 
# Finally, update the incomes in our data *as if* we had enacted this policy -- reduce the incomes of households earning more than 250,000 dollars by 5% and increase the incomes of households earning less than 30,000 dollars by the quantity you estimated in Question 8. 
# 
# What is the resulting Gini Index of `Policy D`? Round your answer to 4 decimal places.

# ### Exercise 11
# 
# Now suppose we also wanted to explore a slightly different intervention: `Policy E`. In `Policy E`, we would distribute the revenue generated with the same tax, but this time we would distribute it evenly to all households earning less than 40,000 dollars (instead of less than 30,000 dollars). 
# 
# What is the resulting Gini Index of `Policy E`? Round your answer to 4 decimal places.
# 

# ### Exercise 12
# 
# 
# If the President asked you whether you could better reduce inequality (as measured by the Gini Index) by re-distributing the tax revenue from taxing households earning more than 250,000 dollars even to households earning less than 30,000 dollars (`Policy D`) or households earning less than 40,000 dollars (`Policy E`), which would you recommend?

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

# In[1]:


# Exercise 1

import numpy as np
incomes = np.loadtxt("data/us_household_incomes.txt")
len(incomes)


# In[2]:


# Question 2
from matplotlib import pyplot as plt
plt.hist(incomes[incomes < 500_000])


# In[3]:


# Still strong right skew!


# In[15]:


# Exercise 3

# This can be calculated a number of ways. Here are two:
EX4_SHARE_BELOW_POVERTY = np.mean(incomes < 20_000)
print(f"The Share of Households Below the Poverty Line is {EX4_SHARE_BELOW_POVERTY:.4}")


# In[17]:


# Exercise 4

from ineqpy.inequality import gini 
EX4_GINI = gini(incomes)
print(f"Gini is {EX4_GINI:.4}")


# In[6]:


# Exercise 5

# Not super impressive for one of the richest countries in the world.


# In[7]:


# Exercise 6

policy_A = incomes.copy()
CUTOFF_A = 40_000
CREDIT_A = 5_000
policy_A[policy_A < CUTOFF_A] = policy_A[policy_A < CUTOFF_A] + CREDIT_A
EX6_GINI_POLICY_A = gini(policy_A)


policy_B = incomes.copy()
CUTOFF_B = 30_000
CREDIT_B = 7_000
policy_B[policy_B < CUTOFF_B] = policy_B[policy_B < CUTOFF_B] + CREDIT_B
EX6_GINI_POLICY_B = gini(policy_B)

print(f"Policy A Gini is {EX6_GINI_POLICY_A:.4}")
print(f"Policy B Gini is {EX6_GINI_POLICY_B:.4}")


# In[8]:


print("Policy B does a better job at reducing inequality.")


# In[19]:


# Exercise 7
policy_C = incomes.copy()
TAX_CUTOFF_C = 250_000
TAX_C = 0.05
policy_C[TAX_CUTOFF_C < policy_C] = policy_C[TAX_CUTOFF_C < policy_C] * (1 - TAX_C)
EX7_GINI_POLICY_C = gini(policy_C)
print(f" Policy C Gini is {EX7_GINI_POLICY_C:.4f}")


# In[23]:


# Exercise 8

policy_D = incomes.copy()
TAX_CUTOFF_D = 250_000
TAX_D = 0.05

# Calculate transfers
EX8_REVENUE_RAISED = np.sum(TAX_D * policy_D[TAX_CUTOFF_D < policy_D])
EX8_REVENUE_RAISED

print(f" Policy D Raises {EX8_REVENUE_RAISED:,.2f}")
print(f" Policy D Raises {EX8_REVENUE_RAISED:.2f}")


# In[25]:


# Exercise 9

CREDIT_CUTOFF_D = 30_000
num_hh_under_30k = np.sum(policy_D < CREDIT_CUTOFF_D)
EX9_TRANSFERS = EX8_REVENUE_RAISED / num_hh_under_30k
EX9_TRANSFERS
print(f" Policy D will transfer {EX9_TRANSFERS:,.1f}")
print(f" Policy D will transfer {EX9_TRANSFERS:.1f}")


# In[26]:


# Exercise 10

policy_D[policy_D < CREDIT_CUTOFF_D] = policy_D[policy_D < CREDIT_CUTOFF_D] + EX9_TRANSFERS
policy_D[TAX_CUTOFF_D < policy_D] = policy_D[TAX_CUTOFF_D < policy_D] * (1 - TAX_D)
EX10_GINI_POLICY_D = gini(policy_D)
EX10_GINI_POLICY_D
print(f" Policy D Gini: {EX10_GINI_POLICY_D:,.4f}")
print(f" Policy D Gini: {EX10_GINI_POLICY_D:,.5f}")


# In[28]:


# Exercise 11

policy_E = incomes.copy()
CREDIT_CUTOFF_E = 40_000
TAX_CUTOFF_E = 250_000
TAX_E = 0.05
num_hh_under_40k = np.sum(policy_E < CREDIT_CUTOFF_E)
transfers_E = EX8_REVENUE_RAISED / num_hh_under_40k

policy_E[policy_E < CREDIT_CUTOFF_E] = policy_E[policy_E < CREDIT_CUTOFF_E] + transfers_E
policy_E[TAX_CUTOFF_E < policy_E] = policy_E[TAX_CUTOFF_E < policy_E] * (1 - TAX_E)
EX11_GINI_POLICY_E = gini(policy_E)
EX11_GINI_POLICY_E

print(f" Policy E Gini: {EX11_GINI_POLICY_E:,.4f}")
print(f" Policy E Gini: {EX11_GINI_POLICY_E:,.6f}")


# In[14]:


# Exercise 12

# POLICY D

