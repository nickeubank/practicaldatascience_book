#!/usr/bin/env python
# coding: utf-8

# # Fixing Data Value Problems

# In our previous reading, we saw the value of always looking at your data and not assuming your data looks the way you expect. Now let's turn to what we can do once we've found a problem in our data.
# 
# In pandas, there are, broadly, two ways to edit problematic values: 
# 
# - You can use a general cleaning function, or 
# - you can directly modify problematic values. 
# 
# In this reading, I'll provide an overview of how to do make global edits before we learn to edit specific locations in the next reading.
# 
# In these exercises, we'll work with our `world-very-small` toy dataset. We're doing so because working with a small dataset makes it easier to see everything the functions we use are doing. However, in some of the examples that follow we'll do things that seem a little silly given the size of the dataset (like print out all values of a variable with `.value_counts()` even though we can see all the values!), but we'll do they anyway since you would need them when working with any real data. 

# ## General Cleaning Functions
# 
# Because we so often have to fix "bad" values in our data, pandas comes with a range of in-built tools for data cleaning. I won't try and cover all of them, but here are a few of the most important to know. 

# ### .replace()
# 
# Probably the first go-to tool for fixing data issues is the `.replace()` method. As the name suggests, `replace` finds specific values in a Series and replaces them with other values. For example, let's begin with this little dataset we've used a few times before with countries, their regions, GDP per capita, and Polity IV scores (a measure of how close countries are to being liberal democracies):

# In[1]:


import pandas as pd

smallworld = pd.read_csv(
    "https://raw.githubusercontent.com/nickeubank/"
    "practicaldatascience/master/Example_Data/world-very-small.csv"
)
smallworld


# Now suppose that we want to change country names from their anglicized names to what their own citizens would call them. Here we start by replacing "Germany" with "Deutschland": 

# In[2]:


smallworld["country"] = smallworld["country"].replace("Germany", "Deutschland")
smallworld


# Voila! Replace works for numbers too -- so suppose we learned that Polity had mis-coded all scores of 15 as 16, so we wanted to change all 16s to 15s:

# In[3]:


smallworld["polityIV"] = smallworld["polityIV"].replace(16, 15)
smallworld


# Note here that `.replace()` replaces all entries with a given value (here, the values for both Mozambique and Ukraine). If you wanted to, say, just change Mozambique's score because of a recent coup, you'd need a different tool, which we'll discuss below. 

# **.replace() with Dictionaries**
# 
# If you want to make lots of changes at once, `.replace` will also accept a dictionary instead of a pair of distinct values. When you pass a dictionary, `.replace` will replace each occurrence of each key in the dictionary with the associated values. 
# 
# For example, if we could continue changing our country names to their native spellings this way:

# In[4]:


changes = {"Mexico": "México", "Russia": "Российская Федерация", "Ukraine": "Україна", "Brazil": "Brasil"}

smallworld["country"] = smallworld["country"].replace(changes)

smallworld


# **.replace() with Regular Expressions**
# 
# Finally, `.replace()` also works with regular expressions when one passes the `regex=True` keyword argument. We haven't covered regular expressions in this course, but basically they are a way of telling Python you want to look for *patterns* to replace instead of exact matches. If you don't know about regular expressions, feel free to skip this sub-section, but since some students may be familiar with them, here's a quick use of their overview:
# 
# Basically, when one passes `regex=True` to `.replace`, `.replace()` will treat the first argument as a regular expression rather than a literal value. Note that this will obviously only work when string values are provided.
# 
# (`.replace(regex=True)` uses `re.sub` on each observation in a Series under the hood, and so supports all the same syntax as `re.sub`.)
# 
# So if, for example, I wanted to remove all the `.`s in region names (e.g., I wanted `S. America` to be `S America`) and I wanted to replace all the `&` with ` and `, I could do:

# In[5]:


smallworld["region"] = smallworld["region"].replace("\.", "", regex=True)
smallworld


# In[6]:


smallworld["region"] = smallworld["region"].replace("\&", " and ", regex=True)
smallworld


# Note the backslash before the `.` and `&`: those are necessary because those characters have special meanings in regular expressions, so if you don't "escape" them with a backslash, Python won't interpret them as a literal period and a literal ampersand. [Here are the official docs on regular expressions in Python](https://docs.python.org/3/library/re.html) if you want to know more!

# ### The .str. String Methods

# Of all the formats of data you'll come across, none are more prone to problems than strings. There are just SO MANY ways to get problems in strings -- capitalization issues, differences in spellings, differences in accents, etc. 
# 
# As a result, pandas comes with a special set of methods for manipulating strings. These can be accessed through the `.str.` methods (e.g. `smallworld["country"].str.upper()` will capitalize your country names). Here's a short list of available string methods: 
# 
# - `.str.lower()` / `.str.upper()`: Change the case of strings (there are lots of these formatting methods...)
# - `.str.contains()`: Look for a substring, return `True` if found
# - `.str.isnumeric()`: `True` if value could be converted to a number easily (e.g. "10"), returns `False` if not (e.g. "Nick").
# - `.str.strip()`: Removes whitespaces at start or end of strings (a common cleanliness problem)
# 
# For a full list, [head over to the official pandas docs here!](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#string-methods)
# 
# To illustrate, let's capitalize all of our country names:

# In[7]:


smallworld["country"].str.upper()


# Or make them all lowercase!

# In[8]:


smallworld["country"].str.lower()


# This may seem trivial, but it can be *very* useful when you get datasets in which some people have written their names in all caps while have written their names in proper case (capitalized first letter, lower case after that) and you need to match up those names with names in a different dataset where names are all capitalized! 

# ## Review
# 
# Substituting instances of one value with another is a very common data cleaning task, and so unsurprisingly pandas has some great utilities. 
# 
# - `.replace()` is the workhorse method for this purpose, and can not only be used for one off substitutions (`.replace(10, 12)`), but also bulk substitutions using dictionaries, and pattern-based substitutions using regular expressions!
# - When working with strings, pandas provides a set of methods accessible with `.str.`.
