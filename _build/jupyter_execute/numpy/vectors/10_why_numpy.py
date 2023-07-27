#!/usr/bin/env python
# coding: utf-8

# # Vectors

# The time has come for us to introduce the workhorse that makes nearly all data science in Python possible: the `numpy` `array`.
# 
# ## A Little History
# 
# Python was invented in the early 1990s to be an accessible, general-purpose programming language. As part of that philosophy, it was designed to minimize the amount of "developer time" (the time a programmer actually spends writing code) required to complete a project, rather than to minimize "running time" (the amount of time a program runs). This was done, in part, because at the time programmers who needed code that ran fast already had access to the C and Fortran programming languages, languages which remain the gold standards for speed even today, but which are relatively hard to work with.
# 
# The design choice was clearly a good one, as it explains much of the success of Python today—yes, Python may *run* more slowly than C for most things, but many programmers are happy to accept that in exchange for being able to write and iterate their Python code much faster than they could in other languages.
# 
# Starting in the late 1990s and early 2000s, however, a group of developers realized that it might be useful for programmers working in Python to have access to libraries they could do high-performance numerical computing—doing matrix multiplication, factoring, generating random numbers, etc. They hoped that this would allow data analysts (this was long before the term "data science" was a thing) to benefit from the ease of use and interactivity of Python when writing code while also making it possible to get speed when they needed it for big mathematical operations. And so to make this possible, they created a new third-party library that could be loaded into Python called Numeric, which later became `numpy`.
# 
# ## The numpy array
# 
# While numpy includes lots of functions and ancillary data structures, **the** heart of the numpy library is the *numpy array.* 
# 
# Like the lists and dictionaries we've already seen, arrays are an object for collecting and organizing lots of individual records -- what's sometimes referred to as a *collection*. Unlike lists and dictionaries, however, which can store nearly anything you want to put into them, arrays are *homogeneously typed*, meaning that each array is designed to store a specific type of data, and can *only* store that type of data. An array of integers, for example, can only store integers, and an array of floating point numbers can only hold floating point numbers. 
# 
# While this may initially seem like it makes arrays inferior to more flexible collections, like lists, there is a major upside: this specialization makes arrays *fast*—as in orders of magnitude faster—and it is this speed that makes data science in Python possible.
# 
# And as we'll see in future readings, arrays make possible a style of programming called *vectorized programming* that not only tends to be very fast, but also makes the kind of programming we do a lot in data science especially concise and easy to read. And if you know any linear algebra, you'll also see that this way of programming results in code that looks more like the math of linear algebra, which many data scientists find really appealing.
# 
# Arrays come in many forms, but there are two specific types of arrays whose names will be familiar: when an array organizes its data along a single dimension, we call it a *vector*, and when its data is organized along two dimensions (like how data is laid out in an Excel spreadsheet), we call it a *matrix*. 
# 
# Most of the time when doing data science, these are actually the only two kinds of arrays you are likely to encounter, and so they will be the focus of the following several readings. However, as we'll see towards the end of this course, there isn't really anything different about working with arrays in three, four, or more dimensions; everything you learn in these first few lessons will generalize easily to all arrays. 
# 

# 
# ## Using numpy
# 
# In past lessons, we saw that not all Python functionality is accessible when you first start a Python session—some functionality is located in libraries we have to import to use. For example, in a previous module, we used the command `import math` to gain access to functions like `sqrt()`.
# 
# Numpy basically works the same way -- we can gain access to its functionality by typing `import numpy`:

# In[1]:


import numpy

numpy.array([1, 2, 3])


# But there are two things that are a little different about numpy from the libraries we've used before. 
# 
# First, numpy is what's called a *third-party library*, meaning that you don't automatically get it when you install Python. Instead, you have to install the numpy library before it can be used. numpy has already been installed in the version of Python you have access to here on Coursera, but if you are working with Python on another computer, you'll need to install it using a tool like `pip` or `conda`—we have a reading on installing third-party packages here.
# 
# Second, because we will be working with numpy a lot, we don't want to have to type out `numpy.` every time we access a numpy function. Instead, it is common practice to give numpy an alias (a different name) by typing: `import numpy as np`. Once we do that, we can access functions from the numpy library with the prefix `np.` instead of `numpy.`:

# In[2]:


import numpy as np

np.array([1, 2, 3])


# And now that we know how to access the functionality of numpy, let's turn to using it to create vectors!

# ## The Speed of numpy
# 
# As noted above, one of the main reasons that numpy is the foundation of data science in Python is that it does numerical computations incredibly efficiently both in the sense that it is fast and also in the sense that it is good at not using up all of your computer's memory. In a later lesson, we'll talk more about the exact reasons that numpy is so fast, but before we dive into learning numpy, it's worth taking a moment to illustrate just how impressive numpy is!
# 
# To illustrate, let's create a list with all the numbers from one to one hundred million and sum them up. We will do this twice—once using regular Python tools, and once using numpy. Don't worry about the fact that some of the code that .all()e use isn't familiar yet—we will learn all of these numpy tools soon—the goal is just to give you a basic demonstration of why we're going through the trouble of learning this library. First, let's make a regular list with all the numbers from 1 to 100,000,000 and a numpy array with all the numbers from 1 to 100,000,000:

# In[3]:


# Make a regular Python list
# with all the numbers up to one hundred million

# Remember `range` doesn't include the last number,
# so I have to go up to 100_000_001 to actually get all
# the numbers from 1 to 100_000_000

one_to_one_hund_mil_list = list(range(1, 100_000_001))

# Now make a numpy vector
# with all the numbers up to one hundred million

import numpy as np

one_to_one_hund_mil_vector = np.arange(1, 100_000_001)


# Now let's add up all of the numbers in each of these two objects and keep track of how long it takes to do this with regular Python and with numpy.
# 
# **Note:** to measure how long each of these operations takes, we will use the `time()` function from the `time` module in the Python standard library. When run, `time()` returns the current time measured in the number of seconds that have passed since January 1st, 1970 UTC -- something called "[Epoch time or UNIX time](https://en.wikipedia.org/wiki/Unix_time)." (*Why* is time measured using the number of seconds since 1970?! 🤷‍♂️ Basically it turns out to be helpful for all computers to measure time against a common benchmark, and 1970 is around the time when the UNIX operating system came online.) So if we record the time before we start running our code, then record the time when the code finishes, then the difference is the amount of time (in seconds) that the code took to run. This isn't the way to do really accurate code timing -- for that you would want to run your code over and over and calculate the average running time -- but it's more than sufficient for our purposes!

# **Note 2:** In the following examples, I print my output using *f-strings*. f-strings were added to Python in 2017, and provide an alternate syntax for inserting the value of a variable into a string ("string interpolation"). They work the same way as the `.format()` method of string interpolation (e.g. `"my name is {}".format(name)`), but instead of putting `.format()` at the end of the string, you simply prefix your string with an `f` or `F` and place the name of the variable you want to be interpolated inside the curly braces (e.g. `f"my name is {name}"`). And as with the `.format()` method, you can also tell Python how to format the string with codes you pass inside the `{}`—for example, the `:.3f` that follows `python_total` below tells Python that it should print the number with only three decimal values. There's a [whole mini-language](https://docs.python.org/3/library/string.html#formatspec) for telling Python how to convert numbers into strings, but for now it's enough to know that the colon and stuff that follows are just for formatting.   

# In[4]:


import time

start = time.time()

total = 0
for i in one_to_one_hund_mil_list:
    total = total + i
    pass

end = time.time()
python_total = end - start
print(f" Python took {python_total:.3f} seconds")


# In[5]:


start = time.time()

# Now we sum up all the numbers in the array
# using the numpy `sum` function.
np.sum(one_to_one_hund_mil_vector)

end = time.time()
numpy_total = end - start
print(f"Numpy took {numpy_total:.3f} seconds")


# In[6]:


print(f"Numpy was {python_total / numpy_total:.1f}x faster!")


# Yup... and that's why we use numpy! (Note regular, non-numpy Python would be able to do this more quickly using the Python `sum()` function instead of writing our own loop, but even then numpy would be *substantially* faster.)
# 
# But that's not all -- regular Python required *much* more memory to store its list of numbers than was required by numpy:

# In[7]:


from pympler import asizeof

# `asizeof.asizeof()` gets the size of an object
# and all of its contents in bytes, so we'll
# divide it's output by one billion to get
# the value in gigabytes.

list_size_in_gb = asizeof.asizeof(one_to_one_hund_mil_list) / 1_000_000_000
vector_size_in_gb = asizeof.asizeof(one_to_one_hund_mil_vector) / 1_000_000_000


# In[8]:


print(f"The Python list of numbers took up {list_size_in_gb:.2f} GB of RAM")
print(f"The numpy vector of numbers took up {vector_size_in_gb:.2f} GB of RAM")
print(
    f"That means the Python list took up {list_size_in_gb/vector_size_in_gb:.0f}x "
    "as much space as the numpy vector!"
)


# 

# This is, of course, a toy example; if all we wanted to do as data scientists was sum up the contents of a couple vectors, it wouldn't be worth learning numpy just to save eight seconds. But of course, that's *not* what we do in data science -- we work with data sets that not only have millions of rows, but also hundreds or thousands of columns. And we're not just trying to sum them up; we are inverting and multiplying full matrices over and over, and running millions of calculations to estimate derivatives and evaluate objective functions. As a result, even with numpy, we are often doing tasks that take minutes, hours, or days. 
# 
# As data scientists, we often do computations and manipulations that take minutes, hours, or days. But without numpy, those same tasks would take hours, days, or even months. And that's assuming you could even load your data in the first place!
# 
# And so *that* is why we are learning numpy!
