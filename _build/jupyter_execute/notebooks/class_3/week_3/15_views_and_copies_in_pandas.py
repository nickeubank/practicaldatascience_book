#!/usr/bin/env python
# coding: utf-8

# # Views and Copies in pandas

# > The implementation of `Copy-On-Write`, discussed below, is one of the largest substantive changes between `pandas 1.0` and `pandas 2.0`. Because this is a new feature as of the Summer of 2023, don't be surprised if you don't see this behavior discussed in older books or in forum posts on sites like Stack Overflow.

# As we reviewed in our last reading, when we subset a numpy array, the result is not always a new array; sometimes what numpy returns is a *view* of the data in the original array. 
# 
# Since pandas Series and DataFrames are backed by numpy arrays, it will probably come as no surprise that something similar sometimes happens in pandas. Unfortunately, while this behavior is relatively straightforward in `numpy`, in `pandas`... it's a hot mess.
# 
# Thankfully, as of `pandas 2.0`, there's a workaround to the historically unpredictable behavior of `pandas` called "Copy on Write" or CoW. In `pandas 2.0` CoW is not the default behavior of `pandas`, but it can be easily enabled, and is expected to become the default soon (when `pandas 3.0` is released).
# 
# Because Copy-on-Write is clearly the future and *so* much easier to understand than the status quo, we'll start by discussing CoW before discussing what happens if it *isn't* enabled.

# ## Copy on Write
# 
# Views were implemented in numpy as a way of improving performance. Arrays are often very large objects, and creating new copies of those objects every time one subsets or modifies an array takes a lot of computer time (and memory).
# 
# At the same time, however, by tying the fates of apparently distinct arrays, views are also an easy way to inadvertently corrupt your data. Moreover, while there are consistent rules about when you get a view and when you get a copy *in numpy*, for technical reasons pandas has never managed to make consistent promises. 
# 
# However, this *is* a way to (generally) get both speed *and* predictability with arrays, and that is with Copy on Write (CoW).
# 
# The idea of Copy-on-Write is that, from the perspective of the user, `pandas` behaves *as if* all operations return a copy. Thus, from the user's perspective, one need never worry about changing one array and have the effects of those change unintentially propagate. 
# 
# But behind the scenes, `pandas` doesn't actually make copies as soon as the user does something like subset a DataFrame; instead, if it can `pandas` will create a view (so it's faster) and make a note that if either the original array or the subset are ever changed, it needs to actually make the copy before allowing those changes to take place.
# 
# The beauty of this solution is that it recognizes that views and copies look the same to the user right up until the user tries to edit the values in one array ("write" a change into the data). So by not making a copy until it's absolutely necessary, `pandas` can get by using views whenever possible!
# 
# (Copy-on-Write, it should be noted, is not unique to pandas—it is the default in some other languages like R)
# 
# 
# 
# ### An Example
# 
# To illustrate how CoW works, let's do a simple example and talk through what's going on behind the scenes.
# 
# First, we'll enable CoW. This will become the default behavior in pandas, but for now you have to run this command in each Python session. Personally, I've just written a little shortcut to add this below `import pandas as pd`.
# 

# In[1]:


import pandas as pd

pd.set_option("mode.copy_on_write", True)


# Then we can create a simple `DataFrame` and take a slice of the `DataFrame` (`my_slice`).

# In[2]:


df = pd.DataFrame({"a": [10, 20, 30, 40], "b": [11, 12, 13, 14]})
df


# In[3]:


my_slice = df.iloc[1:3,]
my_slice


# Now, suppose we modify one of the entries in our DataFrame `df`. As discussed above, CoW means that everything behaves *as if* our indexing operation returned a copy, so this modification should not propagate to our slice `my_slice`—and indeed, we can see that it doesn't!

# In[4]:


df.iloc[1, 1] = -1
df


# In[5]:


my_slice


# But here's the fun part—when we ran the command `my_slice = df.iloc[1:3,]`, `my_slice` was actually created as a view, not a copy, for speed. 
# 
# It was only when we modified the data in `df` with the command `df.iloc[1, 1] = -1` that `my_slice` was converted into a copy. In this example, the timing of the copy doesn't matter, but if we had never modified the entries in `df` with that command, `pandas` never would have made the copy, and we'd never have to pay the penalty of that copy!

# ## Life Without Copy on Write: The View/Copy Headache in pandas

# At this point, you may be saying "ugh, but I don't want to write `pd.set_option("mode.copy_on_write", True)` at the top of all my files!". I hear you. I don't either. But allow me to explain what happens *without* CoW enabled: 
# 
# > Without Copy on Write, whether you get a view or a copy in pandas—and whether changes made to a view will propagate back to the original `DataFrame`—depends not only on the operations you execute (`.loc`, `.iloc`, etc.), but also on the structure of the data in the original DataFrame in ways that are, essentially, impossible to predict consistently.
# 
# Want to know more? Check out the [next reading!](17_views_and_copies_in_pandas_wo_CoW.ipynb)
