#!/usr/bin/env python
# coding: utf-8

# # Numbers in Computers
# 
# As a data scientist, you will spend a *lot* more time playing with numbers than most programmers. As a result, it pays to understand how numbers are represented in computers, and how those representations can get you into trouble. 
# 
# This lesson is divided into two parts. In the first part, we'll cover the basics of how computers think about numbers, and what issues can potentially arise with the two main numerical representations you'll use. In the second part, we'll discuss when you need to worry about these hazards both (a) when using vanilla Python, and (b) when using `numpy` and `pandas`. 
# 
# ## The Two Classes of Numbers: Integers and Floating Point Numbers
# 
# Broadly speaking, computers have two ways of representing numbers: integers and floating point numbers. In most intro computer science courses, students are taught that integers are for... well, integers (whole numbers), and floating point numbers are for numbers with decimal points. That is true to a point. But below the hood, integers and floating point numbers work in very different ways, and there are distinct hazards when working with both. 
# 
# To learn the ins-and-outs of how integers and floating point numbers work, please review the following materials (these explanations are *very* good, and there's no reason to try to write my own explanations when these exist). Then continue to the section below on Python-specific hazards.  
# 
# ### Integers
# 
# To see a great discussion of integers (and their major pitfall: integer overflow), [please watch this video.](https://www.youtube.com/watch?v=vA0Rl6Ne5C8)
# 
# If after watching you would like to learn more, Chapters 7 and 8 of *Code: The Hidden Language of Computer Hardware and Software* by Charles Petzold get into integers in great detail.   
# 
# ### Floating Point Numbers
# 
# Integers, as a datatype, are wonderful. They are precise and pretty intuitive. But they also have their weaknesses: namely, they can't represent numbers with decimal points (which we use all the time), and they can't represent really big numbers. 
# 
# So how do we deal with decimals and really big numbers? Floating point numbers!
# 
# To learn about floating point numbers, please: 
# 
# - [Watch this video](https://www.youtube.com/watch?v=pQs_wx8eoQ8)
# - [Read This](https://ciechanow.ski/exposing-floating-point/) 
# 
# 
# ## Numeric Hazards in Python, Numpy, and Pandas
# 
# So in general terms, the dangers with integers and floating points are: 
# 
# - Integers can overflow, resulting in situations where adding two big numbers produces a ... negative number. 
# - Floating point numbers are always imprecise, resulting in situations where apparently simple math breaks (e.g., in Python `0.1 + 0.1 + 0.1 == 0.3` returns `False`).
# - Floating point numbers can only keep track of so many leading digits, meaning that you can't work with BOTH very large and very small floating points at the same time (e.g., in Python, `2.32781**55 + 1 == 2.32781**55` returns `True`).
# 
# But when do we need to worry about these issues?
# 
# The answer is that it depends on whether you're using regular, vanilla Python, or `numpy` / `pandas`. 
# 
# ### Integer Overflows *in Python*
# 
# Python is meant to be a friendly language, and one manifestation of that is that in vanilla Python, you can't overflow your integers! That's because whenever Python does an integer computation, it stops to check whether you the integer in question has been allocated enough bits to store the result, and, if not, it just adds more bits! So if you do math with an integer that won't fit in 64 bits, it will just allocate more bits to the integer!

# In[1]:


# Here's a really big integer
x = 2**63


# In[2]:


# Now let's make it bigger so it can't fit in 64 bits!
x = x**4
x


# See? No problem!

# ### Integer Overflows *in numpy and pandas*
# 
# The problem with what Python does with integers is that, while convenient, it's slow. Asking Python to add two integers doesn't just require the computer to add two integers; it requires it to *also* check the size of the result, and if that size is so big it won't fit in the existing number of bits that have been allocated, it has to allocate more bits. This makes adding integers in Python much, much slower than it could be. Like... 10x slower. 
# 
# That's why libraries like `numpy` and `pandas` — which are designed for performance when working with huge datasets — don't check for integer overflows. This makes them *much* faster, but if you add two really big integers in `numpy` (or add even small numbers to a *really* big number) and the result is bigger than what fits in the available bits, you'll just end up with a negative number. 
# 
# How much faster? Here's a comparison of adding up all the integers from 1 to 1,000,000 using regular Python integers (which check for overflows) and using `numpy` tools (which do not). Some of this difference is coming from things other than overflow checking, but this gives you a sense of the performance cost of making integers safer in regular Python:

# In[3]:


# Regular Python:
get_ipython().run_line_magic('timeit', 'sum(range(1000000))')


# In[4]:


import numpy as np
# Numpy
get_ipython().run_line_magic('timeit', 'np.sum(np.arange(1000000))')


# But as I said, while it may be fast, it can also be dangerous:

# In[5]:


import numpy as np

a = np.array([2**63 - 1, 2**63 - 1], dtype="int")
a


# In[6]:


a + 1


# It's also important to understand that with `numpy` and `pandas`, you control the size of integers, and thus how big of an integer you can make before you have overflow problems. By default, `numpy` will make your integers the size your system processor works with natively (usually 64 bits on a modern computer, but sometimes 32 bits on an older computer). But  `numpy` also let's you make arrays that are 16 bits (`int16`), 32 bits (`int32`) or 64 bits (`int64`). This can be very useful when working with big datasets: smaller integers take up less memory, and sometimes calculations with smaller integers can be faster due to some intricacies of how computers use memory. But if you do use smaller integer sizes, then you really need to be careful with your overflows! `int16` can only store numbers up to 32,768! 

# In[7]:


x = np.array(32768, dtype="int16")
x + 1


# Also, note that `numpy` and `pandas` have "unsigned" integers (`uint16`, `uint32`, `uint64`). These are like regular integers, except they don't allocate half their values to negative numbers, so their upper limit is 2x the same-sized regular integer. In general, though, it's good to avoid `uints`, as it's too easy to *underflow* by hitting the *bottom* of the values it can tolerate (i.e., going below zero):

# In[8]:


x = np.array([2], dtype="uint64")
x


# In[9]:


x - 3


# ## Floating Point Precision
# 
# Unfortunately, while vanilla Python can protect you from integer overflows, it can't do anything about floating point precision. Whether you're using `numpy` or not, you're stuck with these types of things:

# In[10]:


0.1 + 0.1 + 0.1 == 0.3


# and

# In[11]:


2.32781**55 + 1 == 2.32781**55


# But you also get weird things like 7.5 rounding up and 10.5 rounding down: 

# In[12]:


round(7.5)


# In[13]:


round(10.5)


# So just remember: whatever you're doing with floating point numbers, exact, knife-edge tests may do weird things.
# 
# **If you want protection against this**, consider using the `isclose` function from `numpy` library, which will return `True` if the two arguments it is passed are *really* close. (by *really* close, I mean that `np.isclose(a, b)` checks for whether $absolute(a - b) <= (atol + rtol * absolute(b))$ where the relative tolerance ($rtol$) is $10^{-5}$, and the absolute tolerance ($atol$) is $10^{-8}$ by default. You can also change these tolerances if you want, as shown in the help file). 

# In[14]:


np.isclose(0.1 + 0.1 + 0.1, 0.3)


# ## Random Numbers
# 
# Another oddity about how computers think about numbers is that while it *seems* like computers generate random numbers for you all time time — for example, your computer is happy to give you a random subsample of your data if you ask — the reality is that because computers are deterministic, they actually *can't* generate truly random numbers. Instead, they generate [*pseudo-random* numbers](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) (PRNG), which are sequences of numbers that have all the statistical properties that we want from random numbers, but are actually created deterministically. 
# 
# For data scientists, this is actually pretty useful, because we can take advantage of this to make code that is both "random" and reproducible. This is accomplished using "seeds." 
# 
# To generate pseudo-random numbers, computers begin with a starting number, which can be something like "the number of seconds since the Unix operating system was created." It then feeds that initial number through a series of manipulations. In early PRNGs, for example, you'd start with a four digit number, square it, keep the *middle* four digits of the result, then repeat this process over and over. The results of this process, after sufficient iterations, would be uniformly distributed on the interval [0, 9999]. (Today the algorithms are *much* more sophisticated, but the principle is often the same — take a number, do weird calculations, grab a subset of digits, repeat). 
# 
# Because this is deterministic, if you know the number the computer starts with, you can predict all numbers that follow. This turns out to be very bad for cyber-security, but good for data science, because if we specify that starting number, then we can re-create the same "randomness" tomorrow that we get today. 
# 
# In Python, you can generate randomness quickly with the `numpy.random` library (note there is also a non-numpy library for random numbers called `random`, but I think most people in data science use the `numpy` random library since it quickly generates arrays of random numbers): 

# In[15]:


import numpy.random as npr

npr.rand()  # Generate a random number between 0 and 1, uniformly distributed.


# In[16]:


npr.rand()  # Now another!


# But if we want reproducibility, we can "seed" our random number generator, which effectively means we're setting the number it is starting with, and thus ensuring that we always get the same numbers. So here's a sequence generated when the *seed* is set to 42:

# In[17]:


npr.seed(42)
for i in range(5):
    print(npr.rand())


# And now we set the seed BACK to 42, and we'll get the same sequence of apparently random numbers:

# In[18]:


npr.seed(42)
for i in range(5):
    print(npr.rand())


# Seeding also affects the behavior of functions that *use* randomness, even if you don't see the random numbers explicitly. For example, if we shuffle a numpy array with the numpy function `shuffle`, setting a seed first will get us reproducible results. 

# In[19]:


npr.seed(48)
x = np.array([1, 2, 3, 4])
npr.shuffle(x)
x


# In[20]:


npr.seed(48)
x = np.array([1, 2, 3, 4])
npr.shuffle(x)
x


# ### Cautionary Notes
# 
# A few cautionary notes about random number generators:
# 
# - Different functions can rely on different random number generators. For example, the Python standard library has a `random` library, *and* numpy has a `numpy.random` library. If you set the seed for the standard library random number generator, then use a function that uses the `numpy` random number generator, you won't get reproducible results. 
# - Some libraries you will use in Python don't use Python or numpy random number generators; they use a C random number generator you can't see. This can make it hard, or, depending on how the library was written, impossible to set a seed. 
# - While setting a seed for the numpy random number generator will get you reproducible results across computer systems, this is not true for all random number generators. Some (especially ones written in C) will be reproducible *only for a given computer architecture*. If you share your Mac code with a Windows user, you may not get reproducible results. 
# 
# So random seeds are *very* useful, but if you really need reproducibility, make sure you test your code by running it over and over (and potentially on different computers) to be sure it's configured correctly. 

# ### Want to learn more?
# 
# I highly recommend this [great video](https://youtu.be/C82JyCmtKWg)!

# ### Random numbers and cryptography
# 
# The predictability of pseudo-random number generators is nice for data scientists, but it's very dangerous for cryptography. If you're interested in how people deal with this when security is important, [you can learn about how the internet runs on lava lamps here!](https://www.youtube.com/watch?v=1cUUfMeOijg)
