#!/usr/bin/env python
# coding: utf-8

# # Working with tabular data through Dataframes
# 
# Previously, we learned about Series: an ordered collection of observations, analogous to a `numpy` vector but with super-powers. 
# 
# In this tutorial, we'll learn about DataFrames, a method of holding *tabular* data in which each row is an observation, and each column is a variable. (OK, there are some different forms of tabular data, but that's the most common format you'll encounter). 
# 
# To illustrate, here's a small `pandas` dataframe (created by importing data from a spreadsheet you can find [here](https://github.com/nickeubank/practicaldatascience/blob/master/Example_Data/world-very-small.csv)):

# In[1]:


import pandas as pd

smallworld = pd.read_csv(
    "https://raw.githubusercontent.com/nickeubank/"
    "practicaldatascience/master/Example_Data/world-very-small.csv"
)
smallworld


# As you can see, each of the 6 rows in the DataFrame `world` is a different country, and each column contains different information about that country (the country's name, its region, it's income level (GDP per Capita in 2008), and how close it was to an idealized liberal democracy in 2008 (it's polity IV score). 

# ## What is a DataFrame?

# 
# Where a Series was a one-dimensional collection of data, a DataFrame is fundamentally two dimensional. As a result, it has many of the same types of features as a Series, but generalized to two dimension. Here we show the breakdown of key aspects of a DataFrame that we'll discuss throughout this lesson.

# 
# ![dataframe](images/3.2.30-pandas_dataframe_anatomy.png)

# 
# ### Index and Columns
# 
# For example, like a Series, a DataFrame has an index that labels every row: in this case, it's the usual default index that labels each row with its initial row number. Unlike a Series, however, DataFrames have a second set of labels: column names!

# In[2]:


# Here are the row labels
# (Note that a "range index" is just
# another way of labeling each row with its row number)
smallworld.index


# In[3]:


# And here is our column index.
# Note that while we don't call it "index",
# the column names are of type Index.
# They really are the same as row indices,
# just for columns

smallworld.columns


# ### Constructing DataFrames
# 
# As with Series, there are many ways to construct a DataFrame. Honestly, by far the most common is that you'll read in a dataset from a file. Pandas offers lots of tools for doing this depending on the format of the data you're importing. We'll discuss this more in future lessons, but here are just a few methods to know about: 
# 
# - `pd.read_csv`: Read in a comma-separated-value file
# - `pd.read_excel`: Read in an Excel (`.xls` and `.xlsx`) spreadsheet
# - `pd.read_stata`: Read Stata (`.dta`) datasets
# - `pd.read_hdf`: Read HDF (`.hdf`) datasets
# - `pd.read_sql`: Read from a SQL database
# 
# Similarly, if we have an existing DataFrame (let's call it `df`) we want to output to a file or database, we can use complimentary methods of `df` to do so such as:
# 
# - `df.to_csv`: Write to a comma-separated-value file
# - `df.to_excel`: Write to an Excel (`.xls` and `.xlsx`) spreadsheet
# - `df.to_stata`: Write to a stata (`.dta`) dataset
# - `df.to_hdf`: Write to an HDF (`.hdf`) dataset
# - `df.to_sql`: Write to a SQL database
# 
# You can find a full list of [IO methods here](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)!

# But you can also construct DataFrames by hand. The easiest (and most common) way is by passing in a Dictionary, where the keys will become column names and the values are column values:

# In[4]:


df = pd.DataFrame(
    {
        "animals": ["dog", "cat", "bird", "fish"],
        "can_swim": [True, False, False, True],
        "has_fur": [True, True, False, False],
    }
)
df


# ## Getting To Know Your DataFrame

# While our toy `smallworld` dataset is small enough to easy print out and visualize, most datasets worth working with are too big to just look at. In those situations, we need tools to summarize the contents of our DataFrame. 
# 
# Let's load up a version of the `smallworld` dataset we looked at above that actually has all the countries in the world (instead of just 6). You can find the original dataset [here](https://github.com/nickeubank/practicaldatascience/blob/master/Example_Data/world-small.csv).

# In[5]:


world = pd.read_csv(
    "https://raw.githubusercontent.com/nickeubank/"
    "practicaldatascience/master/Example_Data/world-small.csv"
)
world


# As you can see, `pandas` prints out a bunch of the rows, but not all the rows (note the `...` in the middle) in an effort to not take over your computer. This DataFrame could theoretically be printed out in its entirety (as noted at the bottom of the output, it only has 145 rows), but in the real world we often work with datasets with hundreds of thousands or millions of rows where printing just isn't possible. So here are some methods for "getting to know your data":

# Look at the first 5 rows:

# In[6]:


world.head(5)


# Look at the last 5 rows:

# In[7]:


world.tail(5)


# View a random subset of rows (here, 5). This is valuable because the first rows of a dataset aren't always representative of the dataset. Often datasets are ordered (as this one is alphabetically by country), and seeing the first or last few entries can sometimes be misleading. Random sampling can reduce this effect.

# In[8]:


world.sample(5)


# Get the number of rows:

# In[9]:


len(world)


# Get the number of columns:

# In[10]:


len(world.columns)


# Learn the data type of each column:

# In[11]:


world.dtypes


# Get summary statistics for each numeric column (objects are ignored):

# In[12]:


world.describe()


# List out all the columns (if there are a lot, you can't just see them in the table, and if you just do `world.columns`, often pandas will compress that too. This will show you all columns:

# In[13]:


for c in world.columns:
    print(c)


# ## Subsetting a DataFrame
# 
# As with Series, one of the most important skills for working with DataFrames is knowing how to subset them. Thankfully, DataFrames works kind of like a two-dimensional generalization of Series when it comes to the use of `iloc` and `loc`. 
# 
# iloc
# 
# To subset a DataFrame using `iloc`, we now have to pass two arguments into `iloc` seperated by a comma. For example, if we wanted the entry in the fourth row of the first column, we would use: 

# In[14]:


world.iloc[3, 0]


# Similarly, `iloc` still supports slices. Here are the first two rows of the first three columns:

# In[15]:


world.iloc[0:2, 0:3]


# If you want to get a subset on one dimension, but *all* the entries on the other, just pass a `:` for the dimension on which you want all the data (just like in numpy). Here are the first two rows and all the columns:

# In[16]:


world.iloc[0:2, :]


# If you ONLY pass one set of arguments, though, those will be applied to the first dimension (rows), just like in `numpy`. Thus `.iloc[0:2]` is the same as `.iloc[0:2, :]`. 

# In[17]:


world.iloc[0:2]


# ### loc
# 
# The generalization of `.loc` from Series to DataFrames works the same as `iloc`. If you pass two arguments, the first will subset rows (though for `.loc`, the subsetting is on index values, not row numbers), and the second will subset columns (again, on column names, not column order). 

# In[18]:


# Index value 1, column country
world.loc[1, "country"]


# And just like in Series, if you pass a range to `.loc`, the end points will be included (unlike with most Python functions)

# In[19]:


world.loc[0:1, "country"]


# Finally, as with `.iloc`, if you pass a single argument to `.loc`, it will subset on the first dimension (rows):

# In[20]:


world.loc[0:3]


# ### Logical Tests

# Subsetting with logical tests also works in a familiar manner for DataFrames: 
# 
# - If you pass a single boolean array to `.loc`, it will subset on rows. 
# - If the boolean array has an Index (i.e. if it's a Series), then alignment will take place on index values
# - If the boolean array does NOT have an idex (i.e. it's a list of booleans), then alignment will take place on row order. 
# - To subset columns based on a test, you have to use `.loc[:, YOUR_TEST_HERE]`. 

# To illustrate, let's start by shuffling our DataFrame so that index values and row numbers aren't the same:

# In[21]:


world = world.sort_values("gdppcap08")
world.head()


# In[22]:


# Test with an index -> subset rows, align on index
relatively_democratic = world.loc[world["polityIV"] > 10]
relatively_democratic.head()


# And if we want to subset columns on a Boolean (admittedly a silly example, but you get the idea):

# In[23]:


relatively_democratic = relatively_democratic.loc[
    :, (world.columns == "country") | (world.columns == "gdppcap08")
]
relatively_democratic


# ### `[]` Square brackets
# 
# As with Series, single square brackets in `pandas` change their behavior depending on the values you pass them. Again, it is worth emphasizing that there is *nothing* that one can do with square brackets that you can't do with `.loc` and `.iloc`, so if they seem to strange, you don't have to use them. 
# 
# With that said, as summarized below, `[]` is actually much safer on DataFrames than on Series. 
# 
# The rules of `[]` in DataFrames are:
# 
# - If your entry is a *single* column name, or a list of column names, it will return those columns. 
# - If your entry is a slice, it will work like `iloc` and select rows based on row order. 
# - If your entry is a boolean array, *and* of exactly the same length as the number of rows in your data, it will subset rows.
#     - Note this means that `[]` does not do the same thing we saw `.loc` do above where, if passed a short boolean array, it will assume any row without an entry in the boolean array should be dropped.

# In[24]:


# Select one column
world["country"].head()


# In[25]:


# Select multiple columns
world[["country", "gdppcap08"]].head()


# In[26]:


# Boolean test
world[world["gdppcap08"] > 10000].head()


# In[27]:


# Slice of rows
world[0:3]


# **My advice on using `[]` on DataFrames:** in short, `[]` is much safer on DataFrames because the situation where `[]` *might* subset on index labels (if your index labels are integers) or it *might* subset on row order (if your index labels are not integers) doesn't exist. Moreover, selecting a single column is *extremely* common, and this is a case where I use single square brackets all the time. 
# 
# In a Series, if I pass `0`, it's always unclear whether that's going to get me the first row (row-order-based) or the row with index value 0 (if I have integer index-values). On a DataFrame, a single entry or list of entries will *only* attempt to match columns based on column *labels*, and if that fails, it throws an exception rather than defaulting to acting like `.iloc`:

# ```python
# world[0]
# 
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# File ~/opt/miniconda3/lib/python3.10/site-packages/pandas/core/indexes/base.py:3621, in Index.get_loc(self, key, method, tolerance)
#    3620 try:
# -> 3621     return self._engine.get_loc(casted_key)
#    3622 except KeyError as err:
# 
# ...
# 
# File ~/opt/miniconda3/lib/python3.10/site-packages/pandas/core/indexes/base.py:3623, in Index.get_loc(self, key, method, tolerance)
#    3621     return self._engine.get_loc(casted_key)
#    3622 except KeyError as err:
# -> 3623     raise KeyError(key) from err
#    3624 except TypeError:
#    3625     # If we have a listlike key, _check_indexing_error will raise
#    3626     #  InvalidIndexError. Otherwise we fall through and re-raise
#    3627     #  the TypeError.
#    3628     self._check_indexing_error(key)
# 
# KeyError: 0
# 

# Similarly, boolean subsetting always acts like you're using `.loc` (aligning on index values where it can, row order if it can't), and slices in `[]` *always* get behavior like `.iloc`, making behavior much more predictable. 

# ## Getting Columns with Dot-Notation
# 
# In addition to passing the name of a column into `.loc` or to `[]`, columns can also *sometimes* be access using dot-notation: 

# In[28]:


world.country.head()


# This method of getting columns is very easy and intuitive (given how often we use dot-notation in Python more broadly), but it has a couple significant pit-falls:
# 
# - Only works for column names without spaces or punctuation
# - You can't pass a variable to dot-notation, you have to write out the column explicity (so you can't write generalized code).
# - Only works if the column name isn't the same as an existing method (i.e. df.count will call the `count` method, even if you have a column named "count")
# - Causes big problems if you try to put it on the left side of the equals sign. 
# 
# Of these, the reasons for the first and second aren't complicated, but the third and fourth concerns bear exploring. 
# 
# Suppose we added a column to our data called `rank` that gave each country's GDP rank (this code is a little convoluted because there is an easier way to do this, but this works):

# In[29]:


world = world.sort_values("gdppcap08")
world["rank"] = range(0, len(world))
world.head()


# But if we try and access the rack column with dot-notation, we don't get that column, we get the method `rank`:

# In[30]:


world.rank


# Now if you hit this problem on the right side an assignment operator, you'll get an exception and will know you have a problem. Suppose you want to move up everyone's rank by 1:

# In[31]:


world.rank = world["rank"] + 1


# In[32]:


world.head()


# It fails silently because what you've actually done is over-written the *method* rank with the column `rank` plus 1. Now now only has your `rank` column not changed (see it still starts with 0), but now you've broken the `rank` method:

# ```python
# world.rank()
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-34-685de3d339fd> in <module>
# ----> 1 world.rank()
# 
# TypeError: 'Series' object is not callable
# ```

# When you try to assign values using dot-notation, you also get into trouble if you try to create a *new* column. For example: 

# In[33]:


world.rank_doubled = range(0, 2 * len(world), 2)
world.head()


# See now `rank_doubled` wasn't added to your DataFrame? It just disappears. `pandas` does now raise a warning, but warnings don't stop your code from running, so if you don't see it, you can corrupt your data. 

# **My advice on dot-notation:** 
# 
# - Never, just *never* use dot-notation on the left-side of the assignment operator. It's just begging for trouble. 
# - Try not to use it on the right side of the assignment operator. It's safer than using it on the left side of the assignment operator, but none of us will ever memorize all the names of methods in `pandas`, and if your column happens to have the same name as a method, you may not notice the error. 

# ## DataFrames: Collection of Series

# While it is natural to think of a DataFrame as a single table (like a numpy matrix), in reality **a DataFrame is just a collection of Series**.  
# 
# To see this, let's pull out individual columns using square bracket notation, and check it's type:

# In[34]:


type(world["country"])


# Tada! 
# 
# And that means that you can always pull out a column from a DataFrame and manipulate it using the tools you've already learned from the Series tutorial. And because you know how to extract the `numpy` array that underlies a Series, that means you also always know how to move from DataFrames to `numpy` arrays if you need to. 
# 
# ### Selecting Series versus Selecting DataFrames
# 
# There is one point of nuance worth exploring: when you extract a single column from a DataFrame, you have the choice of either extracting a Series, or extracting a DataFrame with a single column. What determines this is whether you use one pair of square brackets, or two. 
# 
# If you use a single set of square brackets (or pass just the name of a column to `loc`, you get back a Series. But if you pass a *list* with the column name, you get back a DataFrame:

# In[35]:


type(world["country"])


# In[36]:


type(world[["country"]])


# This also holds for rows, by the way. If you ask for a single row, you will actually get back a (newly construted) Series:

# In[37]:


type(world.iloc[3])


# (Obviously, if you ask for more than one row, or more than one column, you will always get back a DataFrame, since the object you're requesting is intrinsically 2-dimensional and can't be represented as a Series. )

# ## Summary
# 
# We have explored how DataFrames are versatile tools for loading in (and writing out) data of diverse file types and for selecting subsets of those data (filtering) for further analysis. These techniques are at the core of how we typically work with tabular datasets in data science. Int he exercises that follow, you'll have a chance to get experience using those tools. And in the next week, we will dive deeply into how to work with DataFrames and use them to ready data for further analysis.
