#!/usr/bin/env python
# coding: utf-8

# # Subsetting and Indexing Series
# 
# 

# ## Subsetting Series
# 
# Extracting a subset of elements from a Series is an extremely important task, not least because it generalizes nicely to working with ever-larger datasets (which are at the heart of data science). This process—whether applied to a Series or a dataset—is often referred to as "taking a subset", "subsetting", or "filtering". If there is one skill that is key for enhancing your data science skills quickly, it's this, because this allows you to get your data into the right format for processing as quickly as possible.
# 
# In `pandas`, there are three ways to filter a Series: using a separate logical Series, using row-number indexing, and using index labels. I tend to use the
# first method most, but all three are useful. The first and second of these you will recognize from `numpy` arrays, while the last one (since it uses index labels, which only exist in `pandas`) is unique to `pandas`. 

# ### Subsetting using row-number indexing
# 
# A different way to subset a Series is to specify the row-numbers you want to keep using the `iloc` function. (`iloc` stands for "integer location," since row numbers are always integers). This will give you the behavior you're more familiar with from `numpy`. Just remember that, as in all of Python, the first row is numbered `0`!

# In[1]:


import pandas as pd

fruits = pd.Series(["apple", "banana"])
fruits.iloc[0]


# You can also subset with lists of rows, or ranges, just like in `numpy`:

# In[2]:


fruits.iloc[[0, 1]]


# In[3]:


fruits.iloc[0:2]


# ### Subsetting using index values
# 
# Lastly, we can subset our rows using the index values associated with each row using the `loc` function. 
# 

# In[4]:


attendance = pd.Series(
    [132, 94, 112, 84, 254, 322, 472],
    index=[
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
)


# In[5]:


attendance.loc["Monday"]


# You can also ask for ranges of index labels. Note that unlike in integer ranges (like the `0:2` we used above to get rows 0 and 1), index label ranges *include* the last item in the range. So for example, if I ask for `.loc["Monday":"Friday"]`, I will get Friday included, even if `.iloc[0:2]` doesn't include 2.

# In[6]:


attendance.loc["Monday":"Friday"]


# ### Subsetting with Logical Tests 
# 
# Let's jump right into an example, using our Zoo attendance Series:

# In[7]:


attendance = pd.Series(
    [132, 94, 112, 84, 254, 322, 472],
    index=[
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
)
attendance


# Suppose we want to only get days with at least 100 people attending. We can subset our Series by using a simple test to build a Series of Booleans (`True` and `False` values), then asking `pandas` for the rows of our Series for which the entry in our test Series is `True`:

# In[8]:


was_busy = attendance > 100
was_busy


# In[9]:


busy_days = attendance.loc[was_busy]
busy_days


# We can summarize these methods in the figure below:
# 
# <img src="img/3.2.15-pandas_series_subsetting.png">

# There is one really important distinction between how subsetting works in `pandas` and most other languages though, which has to do with indices. Suppose we want to subset a Series with fruits to only get the entry "apple". We could do the following:

# In[10]:


fruits = pd.Series(["apple", "banana"])
apple_selector = pd.Series([True, False])
fruits.loc[apple_selector]


# Just like in `numpy`. 
# 
# *But...*
# 
# Just as pandas uses *index alignment* to match entries based on index values when you do an operation between two Series (e.g., `first_series * second_series`), it also uses *index alignment* for subsetting with logical tests and `.loc`.
# 
# In the case above, because we did not specify indices for either `fruits` or `apple_selector`, they both got the usual default index values of their initial row numbers. But let's see what happens if we change their indices so that they don't match their order:

# In[11]:


fruits  # We can leave fruits as they are


# In[12]:


apple_selector = pd.Series([True, False], index=[1, 0])
apple_selector


# Note that we've *flipped* the index order for `apple_selector`: the first row has index value 1, and the second row has value 2. Now watch what happens when we put `apple_selector` in square brackets:

# In[13]:


fruits.loc[apple_selector]


# We get `banana`! That's because in `apple_selector`, the index value associated with the `True` entry is 1, and the row of `fruit` that had index value 1 was `banana`, even though they are in different rows.
# 

# But note this only happens if your Boolean array is a Series (and thus has an index). If you pass a `numpy` Boolean array or a list of Booleans (neither of which have a concept of an index), then despite using `loc`, alignment will be based on row numbers, *not* index values (because there *are* no index values to align). 

# In[14]:


fruits.loc[[True, False]]


# **UGH** I know. If I wrote pandas, this would not work and this would throw an exception. But that's how it is. 

# While this distinction between row numbers and index values is important, though, it comes up less often than you'd think. That's because we don't usually subset by creating a new Series by hand for subsetting; normally, we build our Boolean Series by executing a test on the Series we're using. And when we do that, the new Series of Booleans will have the same index as the old Series, so they align naturally. 
# 
# Look back at our example of `was_busy`: you'll see that it automatically ended up with the same index as our original Series, `attendance`. As a result, the first row of our Boolean Series will have the same index value as the first row of our original Series, the second row of our Boolean Series will have the same index value as the second row of our original Series, and so on. As a result, there's no difference between matching on row order and matching on index value. But it does *occassionally* come up (like if you tried to re-sort one of these), so keep it in mind!

# ## Summary
# 
# Being able to select the data you need for a given analysis is a foundational skill to develop. Having the programming proficiency to be able to do this quickly will significantly reduce the time you need to prepare your data for analysis. There are three primary methods of accessing and filtering data: logical indexing, row-number indexing (e.g. `iloc`), and index labels, and together this toolkit can enhance your ability to access and filter data. Next, you'll explore an exercise for trying out these skills yourself.
