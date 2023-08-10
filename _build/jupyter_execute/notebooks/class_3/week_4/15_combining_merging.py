#!/usr/bin/env python
# coding: utf-8

# # Combining datasets: merging
# 
# In the last lesson, we saw how `concatenate` can be used to append rows or columns to a DataFrame. However, we also saw the potential pitfalls where there are data mismatches between the two datasets. In this lesson, we'll explore `merge` and how to bring datasets together in ways the factor in the existing content of the DataFrame. 
# 
# Suppose...
# - You are analyzing the accounts of a firm and were given one dataset with that contained transactions with the corresponding dollar amounts and vendor ID number and a second dataset that contained the vendor ID and the name and industry of the vendor. How could you determine which vendor corresponds to each transaction?
# - You are developing a system to compute the credits that each student received from taking classes. You have one dataset that has the students and the name of the class they're taking, and a separate dataset that list the classes and the number of credits each class provides. How do you determine the number of credits each student is taking?
# - You are on the marketing team where each employee is signed to one of the clients of the firm. In most cases, multiple employees are signed to a single client (forming the client team) and those employees may, themselves work with multiple clients (they are part of multiple teams). Each client has one or more products. How do we get a list of each product that each employee is working on?
# 
# We can address each of the above issues by combining datasets using `merge`. In fact, we'll see that each of the above examples represents a different type of merge (one-to-one, one-to-many, many-to-many, respectively).
# 
# To help us with this discussion, let's again create two DataFrames that we want to combine; these will be a little different this time:

# In[104]:


import pandas as pd
dfa = pd.DataFrame({'animals': ['dog', 'cat', 'bird', 'fish'], 
                   'location': ['land', 'land', 'air', 'water'],
                   'has_fur': [True, True, False, False]
                   })
dfa


# In[105]:


dfb = pd.DataFrame({'animals': ['fish', 'elephant', 'blue whale'], 
                   'avg_weight':[4,12000,300000]
                   })
dfb


# There are a few differences to note here. First, there is one shared column in each DataFrame and that is 'animals'; the rest are unique. Also, while most of the animals are distinct between these two datasets. To that end, there are 3 ways in which we could merge these DataFrames together referring to the uniqueness of the matches between one dataset and the other:
# 1. One-to-one. Each entry in a column of one dataset matches to *at most* one entry in the column of the second dataset (also, the merge keys are unique in both datasets). This is the simplest case to encounter.
# 2. One-to-many. For the column to merge on, there may only be one row with each unique value in that column in one of the datasets, while there may be multiple values in the corresponding column in the other dataset.
# 3. Many-to-many. There may be multiple rows containing the same value in the merge column for each of the datasets.
# 
# Each of these above situations can be handled with the `merge` method. The types of joins are illustrated graphically below:

# ![Types of Joins](img/3.4.15_types_of_joins.png)

# The above examples each work exactly as written. You'll notice two parameters, "how" and "on". The parameter "on" specifies which column to compare in each of the two DataFrames, assuming they are named the same in both (if not, you can use "left_on" and "right_on" to specify them separately). The parameter "how" specifies how the merge is to be performed, but we will discuss that more later in this lesson; for now, we use the "left" join, and just know this means we're always using the left DataFrame as out point of reference for comparing columns. Let's verify that each of the above merges work as expected. First, the one-to-one:

# In[106]:


a = pd.DataFrame(data={
    'name':['Mia','Lucas','Ang','Jia'],
    'course':['math','chem','econ','chem']
})
a


# In[107]:


b = pd.DataFrame(data={
    'name':['Lucas','Ang','Jia','Mia'],
    'grade':['B-','B','A-','B+']
})
b


# In[108]:


merged = pd.merge(a,b,how='left',on='name')
merged


# Next the one-to-many:

# In[109]:


c = pd.DataFrame(data={
    'course':['chem','econ','math'],
    'credits':[4,3,1.5]
})
c


# In[110]:


merged = pd.merge(c,a,how='left',on='course')
merged


# And finally, the many-to-many:

# In[111]:


d = pd.DataFrame(data={
    'course':['chem','chem','econ','math'],
    'topic':['atoms','lab','trade','calc.']
})
d


# In[112]:


merged = pd.merge(a,d,how='left',on='course')
merged


# The above are very clean examples of the three types of joins. Incomplete data are common, however, when either `a` or `b` are missing some of the content that would otherwise allow for a match. In all the above cases, the `merge` method can help us here.
# 
# ## Types of merging
# 
# The `merge` method for `pandas` DataFrames has numerous parameters, but to accomplish the majority of common merges, there are four types of merges to consider: left, right, inner, and outer, which are each illustrated in the figure below, and through which we specify using the "how" parameter.
# 
# Here, the order of entering the parameters is very important. We'll assume that we're using the command `pd.merge(a, b, ...)` with `a` coming before `b` and that we're merging on the data in column "C1". 
# - A **left** merge starts with the contents of `a` (the DataFrame on the "left") and joins the rows of "C1" in `b` that match something in `a`. In the example below, we can see that the entries A and B in C1 match, but there is no C in `b`, therefore, there is a `NaN` in its place. 
# - A **right** merge performs the same operation, but starts with the contents of `b` (the DataFrame on the "right"); in this case we see that there is no match for the value D in column C1 of DataFrame `a`, so that entry has a `NaN` value inserted.
# - An **inner** merge only keeps rows that have content that matches from both `a` and `b`. 
# - An **outer** merge  keeps all value and all rows from both `a` and `b`.

# ![Types of Merges](img/3.4.15_merge_types.png)

# ### Try it yourself
# 
# Go ahead and try the above examples - create the DataFrames and perform the above merges. Make sure your results look the same as the above.

# In[113]:


a = pd.DataFrame(data={
    'C1':['A','B','C'],
    'C2':['x','y','z']
})
a


# In[114]:


b = pd.DataFrame(data={
    'C1':['A','B','D'],
    'C3':[11,12,13]
})
b


# In[115]:


merged = pd.merge(a, b, how="left",  on="C1")
merged


# In[116]:


merged = pd.merge(a, b, how="right",  on="C1")
merged


# In[117]:


merged = pd.merge(a, b, how="inner",  on="C1")
merged


# In[118]:


merged = pd.merge(a, b, how="outer",  on="C1")
merged


# ## Practical Example
# 
# Let's explore a practical example: what if we wanted to know how common homicide was in each state in the United States and identify those places where per capita homicide lowest and highest. To start with, this means we'll need some data, so we'll use data from the [U.S. Centers for Disease Control and Prevention](https://www.cdc.gov/nchs/pressroom/sosmap/homicide_mortality/homicide.htm) for homicide totals by state and data from the [U.S. Census Bureau](https://data.census.gov/cedsci/table?tid=PEPPOP2021.NST_EST2021_POP&hidePreview=false) to get population in 2020. Let's read those files into dataframes and see what we've got!
# 
# *Note: we've removed some extraneous columns to make the example clearer*

# In[119]:


population = pd.read_csv('data/population.csv')
population


# In[120]:


homicides = pd.read_csv('data/homicides.csv')
homicides


# There are two items to note here. The first is that the population data has the full state name listed, while the homicide data only has state abbreviations. The second is that while the homicide data has 50 states, the population data has 57 since there are additional regions listed (e.g. "United States", "Northeast Region", etc.).
# 
# What we'll want to do, is to add in the state names for each state in the homicide data, then merge the two datasets into one. Once we have that combined dataset, we can calculate the per capita homicide rate in each state and sort our data to determine the highest/lowest per capita.
# 
# To add in the state names for each state, let's load in a dataset that contains the 50 states and their abbreviations:

# In[121]:


names = pd.read_csv('data/state_codes.csv')
names


# We see another issue here, though: there are 51 states listed with abbreviations (remember, Python starts counting at 0) since the District of Columbia is included while there are 50 states listed in the `homicides` DataFrame. Let's left-merge the data so we only keep the 50 states for which we have data. Since the column in `homicides` that has the labels is labeled 'STATE' and the column in `names` with the state labels is called 'Code', we'll use the 'left_on' and 'right_on' parameters to specify those columns:

# In[122]:


homicides_with_states = pd.merge(homicides,names,left_on='STATE',right_on='Code',how='left')
homicides_with_states


# Now we have those items combined, but we don't need the "STATE" or "Code" columns, so let's drop them using the `drop` method. We'll do this operation in place so that rather than having to write:
# 
# `homicides3 = homicides_with_states.drop(columns=['STATE','Code'])`
# 
# which leads to a proliferation of variables each time we want to do a new operation (`homicide3`, `homicide4`, etc.); instead we can perform the operation directly on the data using the `inplace=True` keyword.

# In[123]:


homicides_with_states = homicides_with_states.drop(columns=['STATE','Code'])
homicides_with_states


# And just because it's easier to reference cleaned and ordered labels, let's rename 'DEATHS' to 'homicides' using `rename`.

# In[124]:


homicides_with_states = homicides_with_states.rename(columns={'DEATHS':'homicides','State':'state'})
homicides_with_states


# Great - now we're ready to merge in our population data. Let's perform an outer merge so that we keep all our data, then we can check what's missing and remove it as appropriate.

# In[125]:


combined = pd.merge(homicides_with_states,population,how='outer',left_on='state',right_on='NAME')
combined


# We can see from the above that we have a number of `NaN` values. Let's look at rows with any `NaN` values:

# In[126]:


combined[combined.isna().any(axis=1)]


# Let's just break down the above statement for a moment for comprehension. `combined.isna()` returns a True value for each entry in the DataFrame with a `NaN` value. The `.any(axis=1)` looks across axis 1 and if any of the entries in that row (across all columns) has a True value, then that row is represented with a True. Let's look at the steps so it's clear:

# In[127]:


combined.isna()


# In[128]:


combined.isna().any(axis=1)


# So when we put it altogether, it only displaces those rows with `NaN` values:

# In[129]:


combined[combined.isna().any(axis=1)]


# What we can see here is that we don't need any of these regions, as none are U.S. states, so let's drop them using the `dropna` method:

# In[130]:


combined = combined.dropna(axis=0)
combined


# Now that we have our data let's take one more step to clean the formatting of our data. Let's drop the extra column with state names and rename 'POPESTIMATE2020' to 'population':

# In[131]:


combined = combined.drop(columns=['NAME'])
combined = combined.rename(columns={'POPESTIMATE2020':'population'})
combined


# How we're ready to conduct our analysis. Let's create a new column called 'homicide_rate' and it will be the number of homicides divided by the state population. Since this number is typically a small value, this is often reported as the number of homicides per 100,000 people, so we just multiply the result by 100,000.

# In[132]:


combined['homicide_rate'] = combined['homicides'] / combined['population']*100000
combined


# Lastly, let's sort the data by 'homicide_rate' to see what the states are with the highest and lowest rates:

# In[133]:


combined = combined.sort_values(by='homicide_rate')
combined


# We can see that the states of New Hampshire, Maine, Vermont, Idaho, and Massachusetts, each have homicide rates between and 1 and 2.6 people per 100,000. Arkansas, Alabama, Missouri, Louisiana, and Mississippi have far higher rates ranging from 12.3 to 19.5 people per 100,000. The homicide rate is nearly 20 times higher in Mississippi than it is in New Hampshire.
# 
# All of the skills and tools shown here scale up to larger datasets as well. As we can see, data preparation was a significant part of the effort and being able to programmatically complete the process was essential. Data preparation requires careful design to take care of potential imperfections, omissions, or mismatches in the data. Once taken care of, the subsequent analysis can proceed for us to derive insights from our data.

# ## Summary
# 
# In this section, we saw that merging is a key tool for combining datasets and is able to accommodate many of the common types of merges that we would want to execute. Merging data allows us to integrate the information from two DataFrames logically and coherently to prepare it for further analysis and querying, but care must be taken in structuring the merge so that we don't lose data or introduce unwanted `NaN` values. Next, you'll get some practice merging data. Once we have our data combined, in an upcoming lesson, we'll explore how to group our data by its columns.
