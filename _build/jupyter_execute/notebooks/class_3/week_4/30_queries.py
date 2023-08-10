#!/usr/bin/env python
# coding: utf-8

# # Queries reprised: asking your data questions
# 
# Much of this week has focused on data preparation: combining datasets together, reconfiguring and aggregating them into groups, all for the purpose of preparing the data to help us develop insights and ask questions. In this lesson, we'll be returning to how we can programmatically ask questions of our datasets using queries. We have seen all of this before when we discussed subsetting our data and filtering based on different logical expressions. Here we will introduce a compact way to execute such queries to add another tool into your programmatic toolbox for working with data. A few of you may have encountered structured query language (SQL) before, and if so, there will be many connections to what we discuss today.
# 
# Let's start with our sales data from a previous lesson:

# In[32]:


import pandas as pd

sales = pd.DataFrame(data={
    "employee":["Katrina","Guanyu","Jan","Roman","Jacqueline","Paola","Esperanza","Alaina","Egweyn"],
    "sales":[14,17,6,12,8,3,7,15,5],
    "year":[2018,2019,2020,2018,2020,2019,2019,2020,2020]
})
sales


# To query a `pandas` DataFrame, we need to use the `query` method which takes a query string. This string allows you to ask a world of questions of your data for example, see the table below for a set of examples of quieries and their corresponding query strings for our `sales` dataset:
# 
# | Query      | Query string |
# | ----------- | ----------- |
# | Show me sales greater than 10 | "sales > 10" |
# | Show me data from 2018 | "year == 2018" |
# | Show me sales are greater than 13 and the year is 2018| "sales > 13 and year == 2018" |
# | Show me everything EXCEPT for when sales are greater than 13 and the year is 2018 | "not (sales > 13 and year == 2018)" |
# | Show me data where sales divided by 3 are greater than 3 | "sales/3 > 3" |
# | Show me employees whose names are alphabetically after J | "employee > 'J'" |
# 

# Let's show each of these queries in action below:

# In[33]:


sales.query('sales > 10')


# In[34]:


sales.query('year == 2018')


# In[35]:


sales.query('sales > 13 and year == 2018')


# In[36]:


sales.query('not (sales > 13 and year == 2018)')


# In[37]:


sales.query('sales/3 > 3')


# In[38]:


sales.query('employee > "J"')


# Now, these same queries could have been accomplished using selection and filtering concept we discussed earlier, as shown below, but requiring more sytax (and the `query` method is often more computationally efficient). Let's try rewriting `sales.query('sales > 13 and year == 2018')` using the techniques we described earlier:

# In[39]:


sales[(sales['sales'] > 13) & (sales['year'] == 2018)]


# The `query` method makes our code far easier to follow.
# 
# Another nice feature of `query` is that we can bring in variables from our local workspace, but outside of the DataFrame by prefixing the `@` symbol to the variable name. Let's say we knew that each sale was worth $1,000. Then we could query based on the total dollar amount of sales as follows:

# In[40]:


revenue_per_sale = 1000
sales.query('sales * @revenue_per_sale > 10000')


# ## Computation with columns
# 
# In a similar way that we were able to create more readable and efficient queries with the `query` method, `pandas` also has a faster, more readable method for performing a number of computations on columns. let's create a DataFrame with some data to demonstrate:

# In[41]:


import numpy as np
rand_matrix = np.random.rand(5,4)
data = pd.DataFrame(rand_matrix, columns=['speed_initial','speed_final','time_initial','time_final'])
data_copy = data.copy() # Make a copy to use later
data


# In physics, we can calculate acceleration of an object by it's change in velocity divided by the time it took to change that velocity. Let's calculate that using the tools we've discussed alread:

# In[42]:


data['acceleration'] = (data['speed_final'] - data['speed_initial'])/(data['time_final'] - data['time_initial'])
data


# Instead we can use the `eval` function, which has a syntax similar to that of `query`, but lets us do a number of common computations more clearly (and more quickly, since the code will run more quickly as well):

# In[43]:


data_copy.eval('acceleration = (speed_final - speed_initial) / (time_final - time_initial)', inplace=True)
data_copy


# Similarly, we could prefix a local variable name with the `@` symbol to incorporate the variable into the `eval` expression. While not appropriate for cases which use complex functions, `eval` is a helpful tool for simple expressions.

# ## Summary
# 
# While none of the ends that were achieved by the tools in this section were unable to be reached using the tools from earlier parts of this course, the `query` and `eval` tools discussed here help to make that process easier to understand, easier to implement, and more efficient for processing.
