#!/usr/bin/env python
# coding: utf-8

# # Doing Math With Vectors
# 
# If vectors were just for storing data, they wouldn't be super useful. Thankfully, they're not! 
# 
# ## Math with Scalars
# 
# One of the great things about vectors is that we can use them to do math in a very concise manner. For example, if you try and do a math mathematical operation between a vector and either a scalar number or another vector of length one, numpy will just repeat the mathematical operation with each entry in the longer vector (a behavior called "broadcasting"). This is a very valuable trick -- since we often use vectors to store a collection of measurements of the same phenomenon (e.g. the salaries of employees, the dollar value of sales, temperature measurements, etc.), it is also the case that we often want to apply the same mathematical function to all of the entries in a vector.  
# 

# In[1]:


import numpy as np

# Suppose we are working with data on car sales,
# and we have the value of all the cars we sold last year

sales = np.array([34_255, 27_222, 42_250, 12_000])
sales


# In[2]:


# Now suppose that for every car we sell,
# we have to pay a sales tax of 10%.
# How could we calculate the after-tax revenue
# from each of the sales?

# Simple!
after_tax = sales * 0.90


# In[3]:


# And suppose we also had to pay a
# flat fee of 500 dollars to process each
# sale. Now what would our final revenue be?

final = after_tax - 500
final


# In addition to working with obvious math functions (e.g. `+`, `-`, `*`), this logic also applies to logical comparisons like `>`, `<`, `==`, etc. For example, suppose we wanted to identify sales for more than $30,000. We could do:

# In[4]:


final > 30_000


# ### Functions
# 
# The same thing happens with most functions -- the function gets applied to each entry. Suppose we wanted to round off all of these numbers to the nearest dollar:

# In[5]:


# Round to the nearest dollar
np.round(final)


# ## Math with Equal-Length Vectors

# But we can do more than just repeat the same operation for each entry. If you have two vectors of the same length, mathematical operations will occur "element-wise", meaning the mathematical operation will be applied to the two 1st entries, then the two 2nd entries, then the two 3rd entries, etc. For example, if we were to add our vector of the values 0 through 4 to a vector with two 0s, then two 1s, then a 0 numpy would do the following:
# 
# ```
# 0    +     0    =    0  +  0    =    0 
# 1    +     0    =    1  +  0    =    1 
# 2    +     1    =    2  +  1    =    3 
# 3    +     1    =    3  +  1    =    4 
# 4    +     0    =    4  +  0    =    4 
# ```
# 
# (Obviously, numpy likes to print out vectors sideways, but personally, we think of them as column vectors, so have written them out like that here).
# 

# In[6]:


# Two vectors with the same number of elements 
numbers = np.arange(5)
numbers


# In[7]:


numbers2 = np.array([0, 0, 1, 1, 0])
numbers2


# In[8]:


numbers3 = numbers2 + numbers
numbers3


# How might this be helpful? Suppose that in addition to information about the sale price of all of the cars we sold last year, we also had data on what those cars cost us (the dealership):

# In[9]:


prices = np.array([27_750, 23_500, 39_200, 6_700])
prices


# Now we can combine the after-tax revenue we made from each sale with what the cars we sold cost the dealership to estimate the net profit from each sale:

# In[10]:


final - prices


# Cool! As we can see, we made substantially more on some of those sales than others. In fact, from this, we can see that we need to have a discussion with whoever negotiated the third sale since we ended up *losing* $1,675 on that sale!

# ### Other Shapes

# We've now seen how we can do math with numpy vectors + scalars, numpy vectors + other vectors of length 1, and numpy vectors + other vectors of the same length. But if you try an operation with two vectors of different lengths, and one *isn't* of size one, you get an error that, for the moment, will feel a little cryptic but which we'll dive into in detail soon:
# 
# ```python
# vect1 = np.array([1, 2, 3])
# vect2 = np.array([1, 2, 3, 4, 5, 6])
# vect1 + vect2
# 
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# /var/folders/tj/s8f2_ks15h315z5thvtnhz8r0000gp/T/ipykernel_30350/1706447136.py in <module>
#       1 vect1 = np.array([1, 2, 3])
#       2 vect2 = np.array([1, 2, 3, 4, 5, 6])
# ----> 3 vect1 + vect2
# 
# ValueError: operands could not be broadcast together with shapes (3,) (6,) 
# ```

# ## Vectorized Code / Vectorization
# 
# It's worth quickly noting that the way that numpy broadcasts mathematical operations across vectors results in a style of programming that is relatively unique to data science: vectorization/writing vectorized code.
# 
# If you ask the average programmer to take two vectors `1, 2, 3, 4, 5` and `6, 7, 8, 9, 10` and add the first number of the first vector to the first number of the second vector, then add the second number of the first vector to the second number of the second factor, etc., you would probably get a loop that looks something like this:

# In[11]:


# Either this or you'd get lists
vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

results = list()
for i in range(len(vector1)):
    # Note you can pull items from a vector like 
    # items from a list with `[]`. We'll talk more
    # about that in an upcoming reading.
    summation = vector1[i] + vector2[i]
    results.append(summation)


# And this code isn't *wrong*. But hopefully, it's easy to see how much more verbose this is than `vector1 + vector2`. And because we do this type of operation *all the time* in data science, this ability to avoid writing explicit loops over the entries in a vector is a *really* important feature of numpy. It makes code much, much easier to read and understand. In fact, as we'll discuss at length in a later reading, it is also a style of programming that allows numpy to run much more quickly than it would if we wrote for loops all the time.
# 
# So if you're reading all this and saying "But I just want to write a loop!", please bear with us and try to embrace this style of programming when working with numpy arrays -- we promise, there's a reason it's how nearly all data science code is written!

# ## Summarizing Vectors 
# 
# In the previous examples, we did mathematical operations that acted on the individual entries in a vector, but another type of mathematical operation we sometimes do with vectors is to calculate a property of the entries *as a group*. For example, if we had a vector where each element was a person's height, we might want to know the height of the tallest person in the vector, the height of the shortest person in the vector, the median or mean height of the group, or even the standard deviation of heights. 
# 
# For that, numpy provides a *huge* range of numeric functions:

# In[12]:


# Toy height vector
# (Obviously you could easily find the tallest, shortest, etc.
# in this data set without numpy -- this is just an example!)
heights_in_cm = np.array([155, 171, 162, 170, 171])

# Tallest
np.max(heights_in_cm)


# In[13]:


# Shortest
np.min(heights_in_cm)


# In[14]:


# Median
np.median(heights_in_cm)


# In[15]:


# Standard deviation
np.std(heights_in_cm)


# Here's a short (very incomplete!) list of these kinds of functions:

# ```python
# len(numbers) # number of elements 
# np.max(numbers) # maximum value
# np.min(numbers) # minimum value
# np.sum(numbers) # sum of all entries
# np.mean(numbers) # mean
# np.median(numbers) # median
# np.var(numbers) # variance
# np.std(numbers) # standard deviation
# np.quantile(numbers, q) # the qth quintile of numbers
# ```

# **Don't** worry about memorizing these or anything—basically, you just need to have a sense of the kinds of things you can do with functions, and if you ever need one but can't remember the name of the function, you can google "numpy [what you want to do]" to get the specific function name, or check out the [numpy documentation](https://numpy.org/doc/stable/reference/routines.math.html).

# And of course, these different types of manipulation can also be combined! For example, suppose we wanted to know the number of sales that generated more than $30,000 in revenue. First, we could do the same manipulation we did up top:

# In[16]:


large_sales = final > 30_000
large_sales


# Then we can sum up that vector (remember: `True` in Python is treated like `1` and `False` is treated like `0` when passed to functions like `np.sum()` and `np.mean()`):

# In[17]:


np.sum(large_sales)


# ## Exercises
# 
# 1. Suppose the following were the heart rates reported by your Fitbit over the day: `68, 65, 77, 110, 160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162, 100, 90, 97, 72, 60, 70`. Put these numbers into a numpy array.
# 2. A commonly used measure of health is a person's *resting heart rate* (basically, how low your heart rate goes when you aren't doing anything). Find the minimum heart rate you experienced over the day.
# 3. One measure of exercise intensity is your maximum heart rate—suppose that during the day these data were collected, you are deliberately exercising. Find your maximum heart rate.
# 4. Let's try to calculate the share of readings that were taken when you were exercising. First, create a new vector that takes on the value of `True` when your heart rate is above 120, and `False` when your heart rate is below 120.
# 5. Now use a summarizing function to calculate the share of observations for which your heart rate was above 120!
