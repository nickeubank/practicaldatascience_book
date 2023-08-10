#!/usr/bin/env python
# coding: utf-8

# # Week 4 Assessment
# 
# ## Conceptual Questions
# 
# ### Summarization
# 
# For the following, **do not use Python: figure out what each expression would produce**. If the expression would produce an error, write "error". Use the array below for the following problems:

# In[ ]:


import numpy as np

x = np.array([
    [3,6,-2],
    [-9,7,4],
    [8,2,0]
])


# ### Question 1

# In[ ]:


np.min(x)


# ### Question 2

# In[ ]:


y = np.min(x, axis=1)
y[2]


# ### Question 3: Random number reproducibility
# 
# You're helping a colleague run a Monte Carlo simulation and they need some random numbers. They want your help in creating a collection of 10 million random values. They're going to rerun their analysis multiple times, but they want the random values to be the same each time they run it (since they're going to apply different scenarios to the simulation). Which pathway(s) would successfully meet that objective?
# 1. Create code that creates the random numbers with `numpy` and does not set a random seed
# 2. Create code that creates the random numbers with `numpy` and sets a random seed to ensure reproducibility
# 3. Generate the random numbers and save them into a separate file that will be loaded each time the program is run
# 4. Options (1), (2), or (3) are all equally suited approaches
# 5. Options (2) or (3) are equally suited approaches
# 6. Options (1) or (3) are equally suited approaches

# ## Practical Exercises
# 
# ### Questions 4 and 5: Random number generation
# 
# You are given the function below, `gen_random_number`, which is a random number generator from a very specific distribution (the nature of that distribution is not relevant here). You don't know what the data look like, but you want to summarize them in some way, in this case by **finding the mean and standard deviation**. You'll need a lot of samples to get a good estimate, so make sure you use at least one million.

# In[ ]:


import numpy as np
def gen_random_number(n):
    return np.random.gamma(shape=0.5,scale=1.3,size=n)


# ### Questions 6 and 7: Filtering and querying a dataset

# In data science we frequently need to filter data as we've previously discussed: remove missing or anomalous values, remove predictors/features from a dataset, remove redundant values, etc. Additionally, we often want to query the data, exploring subsets of the larger dataset that meet certain criteria. We'll see later in this specialization that Pandas offers many excellent tools for doing that, but they're based on principles we've discussed here around matrix and vector operations. We've also discussed summarization strategies in this course. Let's bring all of these pieces together and create some tools for filtering and querying our data.
# 
# The goal of this exercise is to create a set of functions that can:
# 1. Remove data from a dataset that are greater than a certain value
# 2. Remove data from a dataset that are less than a certain value
# 3. Remove specific values from a dataset
# 4. Remove duplicate values in a dataset
# 
# Once we have the functions to accomplish this, we'll apply this to a dataset.
# 
# The first step is to create the functions. To help get you started, some skeleton code is provided below (replace "pass" with your code to construct the functions):

# In[ ]:


def remove_greater_than(array, threshold):
    '''remove entries in `array' greater than `threshold' '''
    pass

def remove_less_than(array, threshold):
    '''remove entries in `array' less than `threshold' '''        
    pass

def remove_if_equal(array, value_list):
    '''remove entries in `array' that equal any value in `value_list' '''
    pass

def remove_duplicates(array):
    '''remove duplicate entries in `array' leaving only one of each '''
    pass


# Once you have built your functions to filter the data. Generate tests to verify that each function is working properly.
# 
# Now it's time to apply your function. The dataset that we will use will be a set of integer values ranging from 1 to 1000 (the code is provided below - do NOT change the random seed). 

# In[1]:


# Generate the 10000 random numbers [DO NOT MODIFY THIS CODE]
import numpy as np
np.random.seed(14) # This guarantees the code will generate the same set of random numbers whenever executed
random_integers = np.random.randint(1,high=1000, size=(500))

print(random_integers[:100]) # Prints the first 100 numbers to get a sense of the data


# We strongly encourage you to test your code for each of the above four functions on a simple example. For example, when testing the `remove_greater_than()` function, you could input an array `[1,2,20,21,20000]` with a threshold of 20 and verify that the resulting output is `[1,2,20]`.
# 
# Once you are confident in your function, your goal is to filter the data in the following ways:
# 1. Remove values greater than 800
# 2. Remove values less than 25
# 3. Remove values equal to even integers
# 4. Remove all duplicates
# 
# Lastly, summarize the remaining data after your filtering is complete by computing the **mean and median** of the remaining data.

# Once you're confident in your solution, head back to the Week 4 Quiz to enter your solutions for the exercises above and answer some conceptual questions about this chapter.
