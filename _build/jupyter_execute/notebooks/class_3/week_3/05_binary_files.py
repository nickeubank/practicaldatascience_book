#!/usr/bin/env python
# coding: utf-8

# # Ways To Store and Read Data: Binary Files
# 
# In our last reading we talked about plaintext files: files that store data in a human-readable format. In this reading, we will talk about the second type of file you are likely to come across in your career—binary files.

# Binary files differ from plaintext files in that the way that the 1s and 0s in the file are meant to be interpreted is not dictated by common text encodings—like ASCII or Unicode—where for example the number 1 is always represented by `00110001`, 2 by `00110010`, 3 by `001100011`, etc.
# 
# Instead, binary data files can only be interpreted by software specifically written to interpret the formatted binary file you're working with, like Microsoft Excel. As a result, if you try and open them in a normal text editor—which will try and interpret the 1s and 0s as Unicode, you'll see jibberish. 
# 
# To illustrate, let's save a version of our small world dataset to a binary `.dta` format, then try and open it in our VS Code text editor:
# 

# In[2]:


import pandas as pd
world = pd.read_csv("data/world-very-small.csv")
world.to_stata("data/world-very-small.dta")


# Now if I try and open that `.dta` file, the first thing that will happen as I will see is this warning:
# 
# ![binary world warning](img/world_v_small_warning.png)
# 
# And if I ask it to open the file anyway, all I see is this:
# 
# ![binary world in binary](img/world_v_small_in_binary.png)
# 
# But that's not because the file is corrupt—indeed, if I asked pandas to open that file with the proper function, we get back our usual table:

# In[3]:


pd.read_stata("data/world-very-small.dta")


# ## Common Binary Formats
# 
# Many binary formats were created by a proprietary, closed source program like Microsoft Excel or Stata, but there are also a range of open-source binary file standards. Here is a list (though definitely not an exhaustive one!) of binary formats you may encounter as a data scientist, along with how to read and write data of these types in pandas. As we mentioned in the previous reading, don't try to memorize these—you can always google them later—just read them over in an effort to get a sense of what the landscape of binary file formats looks like.
# 
# **Formats Created By Proprietary Software:**
# 
# - `.xls`, `.xlsx`: Excel spreadsheets. Excel can open and save `.csv` files, but by default it stores data in `.xlsx` formats that can also store formatting information, functions, etc. 
#     - Read with `pd.read_excel` and write with `df.to_excel`.
# - `.dta`: Binary data files created by the program [Stata](https://en.wikipedia.org/wiki/Stata). 
#     - Read with `pd.read_stata` and write with `df.to_stata`.
# - `.sav`: Binary data files created by the program [SPSS](https://en.wikipedia.org/wiki/SPSS). 
#     - Read with `pd.read_spss`.
# 
# **Open Standards:**
# 
# - [Parquet](https://en.wikipedia.org/wiki/Apache_Parquet): Created by the Apache Foundation, Parquet is increasingly my *personal* favorite file format. It was originally designed to aid with distributed computer (e.g. using lots of computers to process very large datasets), but also works great with smaller data. 
#     - Read with `pd.read_parquet` and write with `df.to_parquet`.
# - [Pickle](https://docs.python.org/3/library/pickle.html): Pickle is a format for saving Python objects. It is not only Python specific, but there are also a few different versions of pickle that have been released over the years, and pickle files are often not backwards compatible. Moreover, you should never open a pickle file you don't trust as they are a great vector for malware.
#     - Read with `pd.read_pickle` and write with `df.to_pickle`.
# - [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format): A slightly older binary format that I think was first popularized by astronomers looking to store lots of image data. Kinda hard to work with though, not recommended.
#     - Read with `pd.read_hdf5`. Writing to HDF5 gets complicated fast. :)

# ## A Note on Databases
# 
# Databases—like MySQL, Postgres, MongoDB, etc.—*are* a potential source of data, but they aren't (usually) individual files; rather, databases are programs that collectively manage a collection of datasets in one place, and manage access to those datasets. 
# 
# Python and pandas do have LOTS of tools for interacting with databases, and if that interests you, you can read about the pandas SQL database utilities [here](https://pandas.pydata.org/docs/user_guide/io.html#sql-queries). But databases are a discipline unto themselves, so we won't try and get into them in any depth here!

# ## So What File Format Should I Use?
# 
# All this raises the obvious question: what format should YOU use when saving your own data?
# 
# Every commonly used file type has its place, so really the answer will always depend on what tradeoffs your willing to accept. But here's some of the pros and cons of using plaintext versus binary files:
# 
# **Plaintext:**
# 
# *Pros:*
# 
# - Near universal compatibility.
# 
# That's kind of the only thing, actually, but it's not a small thing by any means!
# 
# *Cons:*
# 
# - Can be much larger when working with large datasets (though many programs can read zipped or compressed CSVs, which helps a lot).
# - Don't store data type information, so if you want to store data in unusual formats (like 32 bit floats instead of 64 bit floats), that information may be lost.
# - Slower to read and write. 
# 
# **Binary Formats:**
# 
# *Pros:*
# 
# - Faster to read and write.
# - Some (e.g., parquet or HDF5) offer built in compression and error checking.
# - Data types are stored.
# 
# *Cons:*
# 
# - To open them, you have to have the right version of the right software. 
# 
# **So In Conclusion:**
# 
# Personally, I use binary formats for all my own projects because I appreciate the speed and compression, and I appreciate the fact that all my data types are preserved. But if I were disseminating anything widely, I'd probably use a plaintext format.

# ## Exercises
# 
# Your colleague is not nearly as sophisticated a data scientist as you, and only knows how to open Stata `.dta` files. However, he was recently sent a JSON file called `world-very-small.json` he can't open. Can you help him out? 
# 
# 1. Using pandas, read in `world-very-small.json`.
# 2. Check that it looks like the `world-very-small` data we've been using extensively recently.
# 3. Now write the data to a `.dta` file.
# 4. Test that you've done so successfully by reading the `.dta` file you created back in using `pd.read_stata()`.
