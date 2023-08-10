#!/usr/bin/env python
# coding: utf-8

# # 

# # Exercise 1: Replacing the outliers to save your data
# Missing or erroneous data come in a wide variety of forms. Sometimes you may encounter a dataset that has blanks where numbers should appear. Depending on how the dataset was created or if it was digitized, the blanks could be in the form of a null string (e.g. ""), a not applicable string (e.g. "N/A" or "NAN"), or sometimes a unique value (e.g. "missing", "unavailable"). In some cases, when the data need to be in certain forms, such as when the data must be numerical, the data may be entered as unique codes corresponding to missing or erroneous values. The assigned value is generally something outside of the realm of expected values (much higher or lower) so that it is clear to whoever reads the data that the entry was not meant as actual data. For example, if we had a dataset listing the number of children in each household in a village, we would likely raise an eyebrow if we saw the number 88888; it's probably missing or erroneous data. For data that is typically large sometimes 0 is used&emdash;if we had a dataset of personal weight in kilograms and we saw a 0 value, that would likely raise a red flag. Erroneous data can sometimes be a bit trickier to identify because it could be due to an unintentional mistake and may fail silently: e.g. hitting an extra keystroke on data entry or missing one.
# 
# Let's see if we can clean up some missing data. Imagine you are the record keeper for a local municipality that has 500 citizens aged 55 and over. The town is known for its longevity and you've been asked by a team of researchers to identify the oldest citizen in town. The problem is, the records are occasionally in error and in those cases, an age of 999 is entered instead of the correct age. Remove the erroneous data from the array and determine the age of the oldest citizen.
# 
# The data are provided for you below.

# In[1]:


import numpy as np
ages = np.array([92, 108, 75, 63, 62, 66, 90, 98, 97, 92, 60, 107, 90, 71, 97, 86, 55, 55,
                 98, 57, 96, 104, 96, 94, 72, 98, 111, 98, 89, 69, 77, 92, 85, 101, 93, 100,
                 90, 101, 96, 98, 999, 87, 106, 86, 108, 55, 67, 65, 68, 59, 67, 72, 57, 79,
                 95, 67, 86, 70, 91, 111, 67, 75, 59, 88, 90, 99, 94, 65, 111, 103, 100, 70,
                 63, 65, 100, 110, 999, 70, 57, 75, 56, 104, 111, 90, 74, 100, 90, 86, 88, 99,
                 58, 103, 88, 103, 64, 96, 105, 89, 83, 65, 100, 62, 73, 105, 83, 105, 58, 96,
                 77, 74, 95, 109, 91, 101, 91, 999, 63, 111, 97, 108, 75, 77, 73, 58, 94, 83,
                 90, 61, 110, 107, 105, 85, 64, 66, 71, 107, 105, 72, 78, 66, 100, 102, 72, 999,
                 74, 68, 73, 72, 90, 93, 99, 55, 92, 83, 58, 71, 89, 75, 98, 87, 999, 78,
                 97, 71, 106, 83, 58, 81, 100, 72, 93, 70, 65, 60, 95, 107, 94, 77, 87, 90,
                 82, 56, 99, 107, 86, 56, 73, 96, 64, 69, 64, 92, 57, 104, 110, 69, 66, 68,
                 84, 89, 72, 80, 55, 75, 87, 57, 106, 69, 66, 62, 102, 76, 111, 999, 96, 83,
                 84, 61, 102, 63, 107, 63, 76, 58, 83, 58, 61, 71, 77, 90, 74, 100, 103, 74,
                 92, 102, 63, 87, 93, 61, 63, 86, 74, 98, 64, 999, 78, 95, 84, 81, 107, 85,
                 79, 82, 89, 65, 107, 57, 74, 77, 97, 92, 58, 96, 105, 60, 55, 74, 57, 80,
                 62, 85, 87, 62, 999, 71, 74, 70, 97, 59, 82, 96, 105, 70, 89, 105, 60, 70,
                 87, 999, 64, 108, 107, 104, 85, 95, 108, 74, 64, 97, 89, 88, 79, 67, 81, 92,
                 63, 80, 76, 94, 104, 67, 73, 61, 99, 96, 68, 90, 86, 79, 85, 111, 75, 98,
                 81, 111, 108, 103, 85, 72, 108, 102, 999, 64, 107, 112, 66, 93, 89, 78, 66, 92,
                 63, 101, 92, 64, 72, 56, 71, 64, 87, 78, 107, 85, 109, 95, 69, 111, 64, 72,
                 55, 66, 99, 57, 78, 55, 58, 90, 88, 71, 90, 103, 92, 98, 67, 97, 77, 68,
                 77, 59, 78, 69, 77, 81, 61, 99, 999, 85, 78, 104, 97, 95, 74, 70, 69, 83,
                 68, 68, 77, 60, 85, 82, 93, 66, 71, 62, 64, 107, 999, 65, 78, 59, 83, 67,
                 108,  58,  95, 106,  83,  79,  67,  59,  96,  90,  55,  55,  96, 109,  82,  55, 101,  58,
                 97, 77, 60, 81, 999, 81, 75, 100, 66, 65, 105, 94, 101, 56, 999, 59, 105, 59,
                 93, 56, 104, 74, 81, 62, 76, 65, 107, 60, 107, 98, 77, 86, 83, 104, 74, 69,
                 97, 80, 91, 56, 108, 87, 65, 91, 93, 60, 91, 110, 107, 88, 96, 70, 60, 99,
                 66, 91, 107, 65, 81, 109, 84, 106, 80, 92, 78, 84, 91, 59])


# 1. First, replace or eliminate the erroneous values. In this case, since we're only interested in the true maximum age, they can be replaced with the value of 0.
# 2. Calculate the maximum age

# In[2]:


ages[ages == 999] = 0
age_max = np.max(ages)
age_max


# # Exercise 2: Changes in extreme poverty
# 
# Extreme poverty is often defined as living on less than $1.90 per day and the trend of those living in extreme poverty globally may surprise you. Let's explore how the distribution of those living in extreme poverty has changed globally in just the past 30 years, since 1990. 
# 
# *Note: the data used in this exercise are from Our World in Data and can be found at [https://ourworldindata.org/extreme-poverty](https://ourworldindata.org/extreme-poverty); their sources include World Bank and PovcalNet. All data are under a CC-BY license.*
# 
# **Our goal is to answer the following question: which region of the world saw the most significant change in poverty over the period of 1990 through the present?**
# 
# We'll walk through this step by step.
# 
# 1. Let's start by getting our data. We'll explain how to load data in an upcoming lesson, but for now, you can use the following code to load the data. Each column in the data represents a different region of the world with column 0 representing "East Asia and Pacific" through column 5 representing "Sub-Saharan Africa". The rows represent a year and range from 1990 to 2018 (29 years in total). All values are in percent.

# In[2]:


import numpy as np 

poverty_data = np.loadtxt("data/poverty.csv", delimiter=',')

regions = ['East Asia and Pacific',	
           'Europe and Central Asia',
           'Latin America and the Caribbean',
           'Middle East and North Africa',
           'Other high income countries',
           'Sub-Saharan Africa']


# 2. Before we analyze data, we should always start by making sure our data match what we expect. What is the shape of the `property_data` matrix that you expect? Write that down. Now run `poverty_data.shape`. Does it match?

# In[3]:


poverty_data.shape


# 3. Do you expect that extreme poverty has increased or decreased over the past 29 years? Note your prediction.
# 
# 4. Qualitatively investigate the data. Print your data and look at the trend. Time is increasing as the index of the row increases (down the page). Is extreme poverty trending upwards or downwards? How does it vary geographically?

# In[4]:


poverty_data


# 4. Not let's work towards quantifying those changes. Which regions started with the highest/lowest percentage of the population in extreme poverty in 1990? Which regions had the highest/lowest as of 2018? In what direction was the percentage of people in extreme poverty trending for most parts of the world?
# 

# In[7]:


poverty_1990 = poverty_data[0]
poverty_1990


# In[8]:


poverty_2018 = poverty_data[-1]
poverty_2018


# East Asia and the Pacific had the highest extreme poverty rate in 1990 (60.9%) and high-income countries had the lowest (0.4%). In 2018, high-income countries still had the lowest incidence of extreme poverty at 0.60% and the highest was Sub-Saharan Africa at 40.39%. In most places, extreme poverty was decreasing except for the Middle East and high-income countries.

# 5. Compute the minimum and the maximum percentage of people in extreme poverty across all years for each region. You can do this with 2 lines of code. 

# In[6]:


poverty_max = np.max(poverty_data, axis=0)
poverty_min = np.min(poverty_data, axis=0)
poverty_max


# In[7]:


poverty_min


# 6. We often want to monitor and understand regional changes in poverty so we can learn from their experiences. It's useful to understand regions that have reduced the prevalence of poverty and those in which poverty has increased, in both cases to learn from what drove those changes and to work towards remediating extreme poverty wherever possible. To that end, we want to know which parts of the world experienced the largest change in the percentage of its population in extreme poverty. Since we've already explored the trends in poverty, calculate the change in the percentage of those in extreme poverty by computing the difference between the maximum and minimum percentages. Which region experienced the largest change? Which experienced the smallest change? Were those trends increasing or decreasing (how do you know based on what you've investigated so far)?

# In[8]:


poverty_change = poverty_max - poverty_min
poverty_change


# The largest change was experienced in the East Asia and Pacific region falling from 60.9% to 1.2% and the smallest change occurred among high-income countries (which increased a bit over those years). We know the increase or decrease based on the reference values from 1990 and 2018.
