#!/usr/bin/env python
# coding: utf-8

# # The View/Copy Headache in pandas without Copy on Write

# After the last reading, you may be saying "ugh, but I don't want to write `pd.set_option("mode.copy_on_write", True)` at the top of all my files!" I hear you. I don't either. But allow me to explain what happens *without* Copy on Write (CoW) enabled: 
# 
# > Without Copy on Write, whether you get a view or a copy in pandas—and whether changes made to a view will propagate back to the original `DataFrame`—depends not only on the operations you execute (`.loc`, `.iloc`, etc.), but also on the structure of the data in the original DataFrame in ways that are, essentially, impossible to predict consistently.
# 
# Allow me to demonstrate.

# ## The Problem: A Demonstration
# 
# To illustrate how weird views and copies can be in pandas without CoW, let's look at two examples of *basically* identical manipulations that result in very different behavior.
# 
# First, here is some code that takes a subset of a DataFrame and then modifies the data in the DataFrame. As we will see, this results in a change in the slice: 

# In[1]:


import pandas as pd

# This is the default option so I don't strictly
# need this command, but I'll add it to be explicit
pd.set_option("mode.copy_on_write", False)

df = pd.DataFrame({"a": [10, 20, 30, 40], "b": [11, 12, 13, 14]})
df


# In[2]:


my_slice = df.iloc[1:3,]
my_slice


# In[3]:


df.iloc[1, 1] = -1
df


# In[4]:


my_slice


# Voilà, the change to the DataFrame has propagated to the slice, so clearly, the slice was a view, right? Well... kinda.
# 
# Now observe what happens if we do the same operation, but now instead of changing the entry at `df.iloc[1, 1]` to `-1`, we change it to `3.14`. You would *assume* the behavior of pandas would be unchanged, but...:

# In[5]:


# Same DataFrame and subset:
df = pd.DataFrame({"a": [10, 20, 30, 40], "b": [11, 12, 13, 14]})
my_slice = df.iloc[1:3,]
my_slice


# In[6]:


# But now we set the value to 3.14 instead of -1.
df.iloc[1, 1] = 3.14
df


# In[7]:


# And as you can see, in this instance
# the data in `my_slice` is unchanged.
my_slice


# (Why this happens isn't actually important to understand, but for those who are interested: in the first modification, I replaced one integer with another, so that operation could be done in the existing integer array; in the second, I try to put a floating point number into an integer array. This can't be done, so a new floating point array was created, and that new array replaced the old one as column `a` in the original DataFrame, breaking the "view" connection.)

# Note that this behavior applies not just to row slices, but also column slices:

# In[8]:


df


# In[9]:


# This initial change propagates
column_a = df["a"]
df.iloc[0, 0] = -42
column_a


# In[10]:


# But this does not
df.iloc[0, 0] = "a"
df


# In[11]:


column_a


# ### Dealing with Views If You Don't Want To Use CoW
# 
# I won't mince words: I think this behavior deeply problematic, I've long advocated for it to be changed, and I'm fully on the Copy on Write train. But if for some reason you think you don't need it...
# 
# **SettingWithCopyWarning**
# 
# To help address this issue, `pandas` has a built-in alert system that will **sometimes** warning you when you're in a situation that may cause problems, called the `SettingWithCopyWarning`, which you can see here:

# In[12]:


import numpy as np

df = pd.DataFrame({"a": np.arange(4), "b": ["w", "x", "y", "z"]})
my_slice = df["a"]
my_slice


# In[13]:


my_slice.iloc[1] = 2


# Any time you see a `SettingWithCopyWarning`, go up to where the possible view was created (in this case, `my_slice = df["a"]`) and add a `.copy()`:

# In[14]:


my_slice = df["a"].copy()
my_slice.iloc[1] = 2


# **The Problem with `SettingWithCopyWarning`**
# 
# The bad news is that the `SettingWithCopyWarning` will only flag one pattern where the copy-view problem crops up. Indeed, if you follow the link provided in the warning, you'll see it wasn't designed to address the copy-view problem *writ large*, but rather a more narrow behavior where the user tries to change a subset of a DataFrame incorrectly (we'll talk more about that in our coming readings). Indeed, you'll notice we didn't get a single `SettingWithCopyWarning` until the section where we started talking about that warning in particular (and I created an example designed to set it off). 
# 
# So: if you see a `SettingWithCopyWarning` do **not** ignore it—find where you may have created a view or may have created a copy and add a `.copy()` so the error goes away. **But just because you don't see that warning doesn't mean you're in the clear!** 
# 
# Which leads me to what I will admit is an infuriating piece of advice to have to offer: **if you take a subset for any purpose other than immediately analyzing, you should add .copy() to that subsetting.** Seriously. Just when in doubt, `.copy()`.

# ### An Aside: No, the problem doesn't *only* emerge when you change the data type of a column
# 
# Some readers may have noticed a pattern in the illustrations I've presented, and from them developed an intuition that a column will only lose it's "view-ness" when one changes the datatype of that column. Though this will always cause problems, it is not the only place problems can arise. What follows isn't something you *need* to know, but may be useful if you're deeply interested. 
# 
# In the examples above, each column was it's own object, and so behaved independently. But this is not always the case in `pandas`. If a DataFrame is created from a single numpy matrix with multiple columns, `pandas` will try to be efficient by just keeping that matrix intact. 
# 
# But as a result, if you do something (like change the type) of *one* of the columns that is tied to that matrix, `pandas` will create new arrays to back *all* the columns that were once tied to the matrix. As a result, a view of a single column can stop being a view due to changes to a different column. For example:

# In[15]:


my_matrix = np.arange(6).reshape(3, 2)
my_matrix


# In[16]:


df = pd.DataFrame(my_matrix, columns=["a", "b"])
df


# In[17]:


# Column_a starts of it's life as a view
column_a = df["a"]
df.iloc[0, 0] = -42
column_a


# In[18]:


# But if I make a change to column b...
df.loc[0, "b"] = "new entry"
df


# In[19]:


# Then the same type of change to column a of `df` will no longer
# be shared

df.iloc[0, 0] = 999999
column_a


# So, as noted before: it is best to never to try and infer whether a subset of a DataFrame if a view or a copy until you have *explicitly* made a copy with `.copy()`.
