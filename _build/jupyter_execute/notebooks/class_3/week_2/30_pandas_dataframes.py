#!/usr/bin/env python
# coding: utf-8

# # Working with tabular data through Dataframes
# 
# Previously, we learned about Series: an ordered collection of observations, analogous to a `numpy` vector but with superpowers. 
# 
# In this tutorial, we'll learn about DataFrames, a method of holding *tabular* data in which each row is an observation, and each column is a variable. (OK, there are some different forms of tabular data, but that's the most common format you'll encounter). 
# 
# To illustrate, here's a small `pandas` DataFrame (created by importing data from a spreadsheet you can find [here](https://github.com/nickeubank/practicaldatascience/blob/master/Example_Data/world-very-small.csv)):

# In[70]:


import pandas as pd

smallworld = pd.read_csv(
    "https://raw.githubusercontent.com/nickeubank/"
    "practicaldatascience/master/Example_Data/world-very-small.csv"
)
smallworld


# As you can see, each of the 6 rows in the DataFrame `world` is a different country, and each column contains different information about that country—the country's name, its region, its income level (GDP per Capita in 2008), and how close it was to an idealized liberal democracy in 2008 (it's polity IV score). 

# ## What is a DataFrame?

# 
# Where a Series was a one-dimensional collection of data, a DataFrame is fundamentally two-dimensional. As a result, it has many of the same types of features as a Series, just generalized to two dimensions. Here we show the breakdown of key aspects of a DataFrame that we'll discuss throughout this lesson.

# 
# <img src="img/3.2.30-pandas_dataframe_anatomy.png">

# 
# ### Index and Columns
# 
# For example, like a Series, a DataFrame has an index that labels every row: in this case, it's the usual default index that labels each row with its initial row number. Unlike a Series, however, DataFrames have a second set of labels: column names!

# In[71]:


# Here are the row labels
# (Note that a "range index" is just
# another way of labeling each row with its row number)
smallworld.index


# In[72]:


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

# In[73]:


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

# In[74]:


world = pd.read_csv(
    "https://raw.githubusercontent.com/nickeubank/"
    "practicaldatascience/master/Example_Data/world-small.csv"
)
world


# As you can see, `pandas` prints out a bunch of the rows, but not all the rows (note the `...` in the middle) in an effort to not take over your monitor. This DataFrame could theoretically be printed out in its entirety (as noted at the bottom of the output, it only has 145 rows), but in the real world, we often work with datasets with hundreds of thousands or millions of rows where printing just isn't possible. So here are some methods for "getting to know your data":

# Let's look at the first 5 rows using `.head()`:

# In[75]:


world.head(5)


# And look at the last 5 rows with `.tail()`:

# In[76]:


world.tail(5)


# View a random subset of rows (here, 5). This is valuable because the first rows of a dataset aren't always representative of the dataset. Often datasets are ordered (this dataset is sorted alphabetically by country), and seeing the first or last few entries can sometimes be misleading. Random sampling can reduce this effect.

# In[77]:


world.sample(5)


# We can use `len()` to get the number of rows:

# In[78]:


len(world)


# Or `len()` and `.columns` to get the number of columns:

# In[79]:


len(world.columns)


# We can also check the data type of each column with `.dtypes` (note the `s`):

# In[80]:


world.dtypes


# Or a slightly more nicely formatted summary with `.info()`:

# In[81]:


world.info()


# We can also summary statistics for each numeric column (objects are ignored) with `.describe()`:

# In[82]:


world.describe()


# Finally, we can list out all the column names. Note that when a table has a lot of columns, the output of `.columns` will be truncated. When that happens, this little hack will ensure you get to see all the columns:

# In[83]:


for c in world.columns:
    print(c)


# ## Subsetting a DataFrame
# 
# As with Series, one of the most important skills for working with DataFrames is knowing how to subset them. Thankfully, subsetting DataFrames is just like subsetting Series but in two dimensions.
# 
# ### .iloc
# 
# To subset a DataFrame using `iloc`, we now have to pass two arguments into `iloc` separated by a comma (the first entry subsets rows, the second columns, just like in `numpy`). 
# 
# For example, if we wanted the entry in the fourth row of the first column, we would use: 

# In[84]:


world.iloc[3, 0]


# And like with Series and `numpy`, `iloc` supports slices. Here are the first two rows of the first three columns:

# In[85]:


world.iloc[0:2, 0:3]


# If you want to get a subset on one dimension, but *all* the entries on the other, just pass `:` for the dimension on which you want all the data (just like in `numpy`). Here are the first two rows and all the columns:

# In[86]:


world.iloc[0:2, :]


# If you ONLY pass one set of arguments, though, those will be applied to the first dimension (rows), just like in `numpy`. Thus `.iloc[0:2]` is the same as `.iloc[0:2, :]`. 

# In[87]:


world.iloc[0:2]


# ### loc
# 
# `.loc` generalized from Series to DataFrames using the same tricks as `.iloc`: if you pass two arguments, the first will subset rows (though for `.loc`, the subsetting is on index values, not row numbers), and the second will subset columns (again, on column names, not column order). 

# In[88]:


# Index value 1, column country
world.loc[1, "country"]


# And just like in Series, if you pass a range to `.loc`, the end points will be included (unlike with most Python functions)

# In[89]:


world.loc[0:1, "country"]


# Finally, as with `.iloc`, if you pass a single argument to `.loc`, it will subset on the first dimension (rows):

# In[90]:


world.loc[0:3]


# ### Logical Tests

# Subsetting with logical tests also works in a familiar manner for DataFrames: 
# 
# - If you pass a single boolean array to `.loc`, it will subset on rows. 
# - If the Boolean array has an Index (i.e. if it's a Series), then alignment will take place on index values.
# - If the Boolean array does NOT have an index (i.e. it's a list of Booleans), then alignment will take place on row order. 
# - To subset columns based on a test, you have to use `.loc[:, YOUR_TEST_HERE]`. 

# To illustrate, let's start by shuffling our DataFrame so that index values and row numbers aren't the same:

# In[91]:


world = world.sort_values("gdppcap08")
world.head()


# In[92]:


# Test with an index -> subset rows, align on index
relatively_democratic = world.loc[world["polityIV"] > 10]
relatively_democratic.head()


# And if we want to subset columns on a Boolean (admittedly a silly example, but you get the idea):

# In[93]:


relatively_democratic = relatively_democratic.loc[
    :, (world.columns == "country") | (world.columns == "gdppcap08")
]
relatively_democratic


# ### A Reminder on Combining Logical Tests
# 
# [As with numpy](https://www.practicaldatascience.org/html/30_subsetting_vectors.html#Subsetting-With-Logical-Operations), when combining logical tests, you have to wrap each test in parentheses. If you don't, and just pass `world.columns == "country" | world.columns == "gdppcap08"`, you will get a *very* confusing Error:

# ```python
# 
# relatively_democratic.loc[
#     :, world.columns == "country" | world.columns == "gdppcap08"
# ]
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# File ~/opt/miniconda3/lib/python3.10/site-packages/pandas/core/ops/array_ops.py:311, in na_logical_op(x, y, op)
#     302 try:
#     303     # For exposition, write:
#     304     #  yarr = isinstance(y, np.ndarray)
#    (...)
#     309     # Then Cases where this goes through without raising include:
#     310     #  (xint or xbool) and (yint or bool)
# --> 311     result = op(x, y)
#     312 except TypeError:
# 
# File ~/opt/miniconda3/lib/python3.10/site-packages/pandas/core/roperator.py:58, in ror_(left, right)
#      57 def ror_(left, right):
# ---> 58     return operator.or_(right, left)
# 
# TypeError: unsupported operand type(s) for |: 'str' and 'str'
# 
# ...
# 
#     339 return result.reshape(x.shape)
# 
# TypeError: Cannot perform 'ror_' with a dtyped [object] array and scalar of type [bool]
# ```
# 

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
# - If your entry is a Boolean array, *and* of exactly the same length as the number of rows in your data, it will subset rows.
#     - Note this means that `[]` does not do the same thing we saw `.loc` do above where, if passed a short Boolean array, it will assume any row without an entry in the Boolean array should be dropped.

# In[94]:


# Select one column
world["country"].head()


# In[95]:


# Select multiple columns
world[["country", "gdppcap08"]].head()


# In[96]:


# Boolean test
world[world["gdppcap08"] > 10000].head()


# In[97]:


# Slice of rows
world[0:3]


# ## DataFrames: Collections of Series

# While it is natural to think of a DataFrame as a single table (like a numpy matrix), in reality, **a DataFrame** is just a collection of Series.  
# 
# To see this, let's pull out an individual column using square bracket notation, and check its type:

# In[102]:


type(world["country"])


# Tada! 
# 
# And that means that you can always pull out a column from a DataFrame and manipulate it using the tools you've already learned from the Series tutorial. And because you know how to extract the `numpy` array that underlies a Series, that means you also always know how to move from DataFrames to `numpy` arrays if you need to:

# In[104]:


# Get numpy array under one column
type(world["country"].values)


# 
# ### Selecting Series versus Selecting DataFrames
# 
# There is one point of nuance worth exploring: when you extract a single column from a DataFrame, you have the choice of either extracting a Series, or extracting a DataFrame with a single column. What determines this is whether you use one pair of square brackets, or two. 
# 
# If you use a single set of square brackets (or pass just the name of a column to `loc`, you get back a Series. But if you pass a *list* with the column name, you get back a DataFrame:

# In[ ]:


type(world["country"])


# In[ ]:


type(world[["country"]])


# This also holds for rows, by the way. If you ask for a single row, you will actually get back a (newly construted) Series:

# In[ ]:


type(world.iloc[3])


# (Obviously, if you ask for more than one row, or more than one column, you will always get back a DataFrame, since the object you're requesting is intrinsically 2-dimensional and can't be represented as a Series. )

# ## Summary
# 
# We have explored how DataFrames are versatile tools for loading in (and writing out) data of diverse file types and for selecting subsets of those data (filtering) for further analysis. These techniques are at the core of how we typically work with tabular datasets in data science. Int he exercises that follow, you'll have a chance to get experience using those tools. And in the next week, we will dive deeply into how to work with DataFrames and use them to ready data for further analysis.
