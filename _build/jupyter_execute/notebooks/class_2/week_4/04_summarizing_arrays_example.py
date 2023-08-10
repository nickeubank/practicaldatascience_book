#!/usr/bin/env python
# coding: utf-8

# # Practical Example: comparing weather by counting like-values
# 
# Often in data science, we want to know how our data are distributed. If we were summarizing the weather in a region we may want to know how many days a year it rains, snows, is cloudy or sunny.  To answer these questions, we typically need to count like-values. To explore an example of this, let's flex our `numpy` array summarization muscles now. Let's say we have a matrix containing weather data over a 2-week period for 5 cities. Each entry in the matrix is an integer between 0 and 4 where these represent the following weather conditions:
# 
# | Label | Weather Condition |
# |-------|-------------------|
# | 0 | Cloudcover |
# | 1 | Sun |
# | 2 | Rain |
# | 3 | Wind |
# | 4 | Snow |
# 
# 

# In[1]:


import numpy as np

weather = np.array([
        [0, 1, 0, 1, 1, 1, 2, 3, 2, 1, 1, 1, 2, 1],
        [1, 0, 0, 2, 2, 2, 0, 0, 1, 0, 2, 3, 0, 0],
        [0, 0, 2, 1, 3, 1, 0, 2, 1, 2, 1, 3, 3, 0],
        [4, 0, 0, 4, 2, 0, 1, 0, 0, 1, 2, 4, 4, 1],
        [2, 3, 1, 1, 2, 3, 4, 2, 2, 4, 2, 3, 0, 3],
    ])
print(weather)


# This matrix has 5 rows and 14 columns. We want to know how many values *of each kind of weather* are present in *each city* (row). That means there are two steps to what we're trying to do here. First, (1) determine how many of each integer (kind of weather) there are in an array (a row, which represents a city), then (2) repeat this for each city (each row). We'll see later how to do this in just a few lines of code using `pandas`. Let's create a function for part (1).
# 
# For the first question around how many of each kind are there, we want to know how many `0`'s are in a given row (array), how many `1`'s are there, etc.? Therefore if our input row was:
# ```
# [2 1 1 4 0 0 0 0 0 0 0 0 0 0]
# ```
# Then we'd want the output to be an array where each entry at index 0 represents how many "0" values were present, and the entry at index 1 to be how many "1" values were present, etc.:
# From this, we can see that there are ten 0's (cloud cover), two 1's (sun), one each of 2 (rain) and 4 (snow) and no 3's (wind), which is correct. Let's create a function to do that automatically for the above dataset and test it out on our known example.
# 
# 

# In[2]:


def count_values(array):
    counts = np.zeros(5)  # Create an array of 5 zeros, one for each value we'll want to count
    # Each entry corresponds to one of the 5 possible values: [0,1,2,3,4]

    # For each value in the array, increment the count of the value corresponding to that number
    for value in array:
        counts[value] += 1

    return counts


# Let's test our function out:

# In[3]:


test_input = [2, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count_values(test_input)


# It works! Really what we have here is a very basic histogram function. A histogram is a representation of the frequency of numerical data; this is precisely what we are getting with our function above and our weather data. 
# 
# But this was only the first step. The second step is to apply this to every row (city) in our `weather` matrix above. Let's create a new function, that makes use of our `count_values` function to count the values in each row by looping over each row (each city):

# In[4]:


def count_values_in_each_row(matrix):
    # For each row, count the values and output that as a matrix
    row_counts = []  # start with an empty array that we collect our histograms in

    for row in matrix:
        counts = count_values(row)
        row_counts.append(counts)  # add the result to the output

    return row_counts


# Let's give it a try and apply this function to `weather`:

# In[5]:


count_values_in_each_row(weather)


# Recalling that the first row (city) of `weather` matrix was `[0 1 0 1 1 1 2 3 2 1 1 1 2 1]`, we indeed see that the first row of our output above indicates that there were two 0's (cloudy days), eight 1's (sunny days), three 2's (rainy days), one 3 (windy day), and no 4's (snow days). We could rewrite these data into a table with the weather headers for easier reading:
# 
# | City id | Cloudy days | Sunny days | Rainy days | Windy days | Snowy days |
# |---------|-------------|------------|------------|------------|------------|
# | City 0  | 2 | 8 | 3 | 1 | 0 |
# | City 1  | 7 | 2 | 4 | 1 | 0 |
# | City 2  | 4 | 4 | 3 | 3 | 0 |
# | City 3  | 5 | 3 | 2 | 0 | 4 |
# | City 4  | 1 | 2 | 5 | 4 | 2 |
# 
# Summarized as such we immediately can learn more about our data. We see that City 0 had 8 sunny days in that two week period while City 1 and 4 had only two. There also was no snow in cities 0, 1, or 2. We immediately get a richer view of our data by applying these summarization techniques.

# This exercise can be applied to many applications. For example, in earlier examples we explored the distribution of income; we may be interested in how national or global income is distributed and a similar process could be applied to those data to extract corresponding insights.
# 
# In data science, we will be constantly summarizing collections of data in ways simple and complex. These basic tools will be the building blocks for those approaches.

# # Recap
# - Summarizing arrays through counting entries can be used to better understand how data are distributed through the use of histograms
# 
# In the next lesson, we will explore how vectorization and make our code more efficient and readable.
