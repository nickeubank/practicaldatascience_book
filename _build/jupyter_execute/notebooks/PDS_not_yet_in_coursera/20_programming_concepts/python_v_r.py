#!/usr/bin/env python
# coding: utf-8

# # Python vs. R: Important Differences To Be Aware Of

# R and Python have a lot of similarities, but there are some important differences. The biggest, discussed below, is the idea that there is a distinction between a variable and the object associated with it. But before we dive into that, a few smaller differences that tend to get people tripped up: 
# 
# * **The analogue of `data.frames` and `vectors` are in `numpy` and `pandas` libraries, not Python itself**: When you watch basic Python tutorials, you'll find yourself wondering where the vectors and data.frames are — don't worry! They exist, but they're in distinct libraries called `numpy` and `pandas`, so basic Python tutorials won't talk about them. 
# * **Periods are operators in Python**: In R, it's common to use periods in variable names (like: `my.list`). There are many syntax differences between R and Python, but for some reason people really struggle with this one — periods are an operator in Python, so don't use them in names! The convention is to use underscores, as in: `my_list`.
# * **In Python, you always count starting at 0, not 1.** For example, to get the first entry in a list, you type `my_list[0]`, not `my_list[1]`. `my_list[1]` will get you the *second* entry in the list. 

# ## Variables vs. Objects
# 
# Now the big conceptual difference between Python and R: the variable / object distinction. 
# 
# Say you make a new vector as follows:
# 
# ``my.list <- list(1,2,3)``
# 
# In R, there's no difference between a variable (``my.list``) and the object associated with it (the list 1, 2, 3). But this is actually a sleight of hand used by R to hide something fundamental about how computers work, and it does not happen in Python.
# 
# In Python, variables and the objects they point to actually live in two different places in your computer. As a result, in Python, it's best to think of variables as *pointing* to the objects they're associated with, rather than *being* those objects. Personally, I've always liked the analogy of your computer being a big warehouse, where variables are just the entries in the inventory book used by the warehouse manager: the variable tells you how to find the thing you want, but it is not the thing itself. 
# 
# So when you create a new list, Python puts that list somewhere in memory, kind of like how you might put something big on a shelf in a warehouse. The variable associated with that list (say, ``my.list``) actually just stores the *location* of the shelf where that list was placed. And because this behavior is normal in most languages, you may not see it emphasized in Python tutorials written by programmers not coming from R.
# 
# The reason this matters is that it's possible for multiple variables to be pointed at the same object. As a result, changes made to an object through one variable will impact what you get if you call the other variables pointed at that object! For example:

# In[1]:


# Make a new list
x = [1, 2, 3]
# Make new var Y, and assign it x. In R this would make a copy.
y = x
# Add to the end of the string
x.append(4)
# We see this new addition is now at end of x
x


# In[4]:


# But look! It's also at the end of y!
# That's because both variables are actually pointing to the same object in memory ("in the warehouse"), 
# so when you appended something to x, you changed the underlying object. And 
# since y was also pointed at that same object, when you next call y, it 
# "sees" those changes to the underlying list. 
y


# This is a HUGE place students get in trouble, so please go read the full tutorial on [this topic here](vars_v_objects.ipynb)!
