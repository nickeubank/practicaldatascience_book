#!/usr/bin/env python
# coding: utf-8

# # (OPTIONAL) Subsetting and Indexing with Single Square Brackets (`[]`)

# As discussed previously, because Series have both an order of rows, and labels for each row, you should always think carefully about which method of subsetting you are invoking. Given that, my advice is to always be explicit in your code and **use `.loc` (for index labels) and `.iloc` (for row numbers).** If you use these, the *only* surprising behavior to watch out for is that `loc` will align on row numbers if you pass a list or array of Booleans with no index. But since you *can't* align on an index in that case, there's no alternative behavior you would be expecting in that situation.
# 
# However, there is another way to subset Series that is a little... stranger. In an effort to be easier for users, `pandas` allows subsetting using *just* square brackets (without a `.loc` or `.iloc`). With just square brackets, `pandas` will do different things depending on what you put in the square brackets. *In theory* this should always "do what you want it to do," but in my experience it's a recipe for disaster. With that in mind, I don't suggest using it, but in this reading I will detail how it works. 
# 
# If this makes your head swim, just remember: **you can always use `loc` and `iloc`. Single square brackets do not offer any functionality you can't get with `.loc` or `.iloc`.**
# 
# ## Passing Index Values into `[]`
# 
# If you pass a value that is in your index into square brackets, `pandas` will subset based on index values (as though you were using `.loc`):

# In[1]:


import pandas as pd

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


# In[2]:


attendance["Sunday"]


# Similarly, if you pass a Series of Booleans in square brackets, then `pandas` will behave like you are using `.loc` as well:

# In[3]:


attendance[attendance > 100]


# (If it's not clear to you why `attendance[attendance > 100]` is a test with an index: Python first evaluates `attendance > 100`. That generates a new Series of booleans with the same index as `attendance`. Then Python evaluates the `attendance[]` part of the problem.)

# ## Passing Integers to `[]`

# Up till now this may all see fine. But suppose you put an integer in `[]`, what happens?
# 
# Well, *if* the Series has an index that only contains integers, you will get the observation associated with that *index value*:

# In[14]:


series_w_numeric_index = pd.Series(["dog", "cat", "fish"], index=[2, 1, 0])
series_w_numeric_index


# In[15]:


# This gives you the first row,
# which has index value `2`:
series_w_numeric_index[2]


# But if your Series has an index that does *not* only consist of integers, then `[2]` will be interpreted as though the integer were being passed to `.iloc`, not `.loc` (`.iloc[2]`) and get you the entry from the corresponding *row number*:

# In[16]:


attendance


# In[17]:


attendance[0]


# As a result, for someone reading your code to understand what `[]` is doing, they have to also be keeping track of the data type of the index of the pandas object being manipulated. And while you may think "yeah, but my code is just for me, so who cares?" let me let you in on a secret: that "other person" who may struggle to understand your code maybe you when you come back to your code in a week to fix something and no longer remember everything that feels obvious to you right now!

# ## Summary
# 
# You may see this single-bracket approach used in online forums and other tutorials, and may even be tempted to save a few keystrokes by using it yourself. But because its behavior is dependent on features of your data that aren't obvious, it can make your code difficult to understand. 
# 
# Given that, our strong recommendation is to always use `.loc` (for index labels) and `.iloc` (for row numbers).
