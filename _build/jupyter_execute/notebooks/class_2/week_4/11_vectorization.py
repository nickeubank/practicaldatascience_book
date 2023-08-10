#!/usr/bin/env python
# coding: utf-8

# # Vectorization in Python
# 
# Vectorizing code is a technique that will typically enable you to create faster and more readable code. Vectorization is the process of performing computation on a set of values at once instead of explicitly looping through individual elements one at a time. The difference can be readily seen in a simple example. Let's say we want to add together each element of two arrays, $a = [a_0, a_1, a_2]$ and $b = [b_0, b_1, b_2]$ such that we create a new array $c = [a_0 + b_0, a_1 + b_1, a_2 + b_2]$. Let's show how this is done in a non-vectorized way (using loops) and using vectorization.
# 

# In[2]:


import numpy as np

# create our data
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])


# Let's first complete this using a non-vectorized approach that uses a for loop...

# In[3]:


# nonvectorized approach
c = [] # Start with an empty array that we will populate in the loop
for i in range(len(a)):
    c.append(a[i] + b[i])
    
print('Nonvectorized approach ->', c)


# Now, let's try a vectorized approach...

# In[4]:


# vectorized approach
c = a + b

print('Vectorized approach ->', c)


# One thing is immediately clear - the notation of the vectorized approach is far clearer than the non-vectorized approach. It says exactly what is happening - an element-wise addition of vectors. This approach is even clearer with 2D matrices since 2D matrices would require nested loops. In data science we are often working with vectors or matrices of data and need to perform element-wise operations on them as we discussed before, so vectorized notation is often preferable for clarity of the code. 
# 
# ## Performance benefits of vectorization
# 
# Perhaps the largest benefit is not the code clarity, but the performance improvement that vectorization provides: an increase in computational efficiency/speed. Let's explore this aspect of vectorization through a simple example. Let's say we have a large array of numbers and we want to double each of them.

# We can start by using a non-vectorized approach which loops through each element in the array, doubling it along the way. Let's create a function that does just that:

# In[13]:


def double_nonvectorized(array):
    doubled = array.copy()
    for i in range(len(array)):
        doubled[i] = array[i] * 2
    return doubled


# Next, let's create the equivalent function, but vectorize it:

# In[14]:


def double_vectorized(array):
    return array * 2


# Again, note how comparatively simple this version is. Now let's verify they produce the same, correct output:

# In[17]:


array = np.array([1,2,3,4])
print('Nonvectorized = ',double_nonvectorized(array))
print('Vectorized    = ',double_vectorized(array))


# Now let's evaluate the speed difference between the two. To do that, we need to time our code. There are many strategies for doing so, but let's use Python's built-in timing package `time`. There's often some variability in how long it takes to run depending on other processes that are going on, so let's run the code 5 times each and take the average. We'll get to practice many of the tools we've been learning in the course so far.
# 
# The `time` package has a function `time` that returns the current time in seconds; so taking the difference between `time.time()` between two points in time provides the number of seconds that have elapsed.

# In[18]:


import time

def timer(function,argument,num_runs):
    total_time = 0
    # Rerun the code num_runs times
    for i in range(num_runs): 
        t0 = time.time() # Capture the initial time
        function(argument) # Run the function we're timing
        t1 = time.time() # Capture the final time
        total_time += t1-t0
    return total_time / num_runs # Return the average across the runs


# All that's left to be done is to create a very large array that we want to double and time how long it takes

# In[62]:


big_array = np.arange(1000000)
num_runs = 5

time_nonvectorized = timer(double_nonvectorized,big_array,num_runs)
time_vectorized = timer(double_vectorized,big_array,num_runs)

print('Nonvectorized code took ',time_nonvectorized, 's')
print('Vectorized code took    ',time_vectorized, 's')
print('Vectorized code was ', time_nonvectorized/time_vectorized ,' times faster')


# That's more than a *700x* speedup! For the exact same code!!!! *Note: if you rerun this code, your output will likely vary depending on the computer you're using and the activity on that computer, but you will consistently see a speedup.*
# 
# OK, so why does this happen? The answer is twofold. 
# 
# First, in the vectorized function, Python (or rather, the `numpy` code written in C that gets called) is designed to understand that it's about to do something to every entry of an array, so it remembers where the array is located, and so only has to look up where to find the array once. 
# 
# In addition, arrays are *typed*, meaning that Python also knows that every entry of the array it's modifying is an integer. As a result, it doesn't have to check the type of every entry in the array when the operation is vectorized, it checks once and knows that it's working with an array of integers. 

# ### Caution: optimize when needed
# 
# While starting with efficient coding practices is the best approach, there are times when the solutions we can think of for a problem are effective but inefficient. If you don't think of the most optimized approach to a problem at the start, that's okay. If you follow the practices of creating modular code and never duplicating code, you can always refactor your code later and improve its efficiency through optimization. Don't let the perfect be the enemy of the good. Get a working solution created for your problem or analysis and if it's sufficiently modular, you can optimize the performance as you identify opportunities to do so without delaying your minimum viable product.

# ## Vectorization syntax parallels much of the math of data science
# Often in data science, we use linear algebra to perform matrix operations. Linear regression, principle components analysis, and correlation analyses all involve matrix operations. Many of these matrix operations can be directly expressed through vectorized operations in much the same way that the math would be expressed.  For example, we often need to multiply one matrix by another - a common operation for a data scientist. We will explore in the exercises just how much more concise and readable vectorized code can be in such circumstances, and how much of an increase in speed it results in.

# ## Recap
# - Vectorization can drastically increase the speed of execution versus looping over arrays
# - Vectorization keeps code simpler and more readable so it's easier to understand and build on later
# - Much of the math of data science is similar to vectorized implementations, making it easier to translate into vectorized code
# - While performance may be important for your particular problem, prioritize module implementations that can be optimized later over a delayed deliverable
