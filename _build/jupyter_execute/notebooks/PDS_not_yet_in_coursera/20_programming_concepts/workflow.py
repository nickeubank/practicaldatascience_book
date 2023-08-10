#!/usr/bin/env python
# coding: utf-8

# # Workflow Management
# 
# A key part of being a successful data scientist is keep track of all the data that goes into a project, the various manipulations that are performed on that data, and final results. In this tutorial, I outline some principles and pratices that I have found exceedingly useful in managing my workflows over the years. Workflow management can be very personal, so feel free to take from this what you will. 

# ## File Numbering
# 
# A key feature of data science workflows is that they are often sequential: code for importing data is meant to be run before code for cleaning data, and code for cleaning is meant to be run before analysis. With that in mind, I am an advocate of pre-fixing all files with a number. For example, a small project might have three files of the following structure:
# 
# ```
# 10_import_data.py
# 20_clean_data.py
# 30_analyze_data.py
# ```
# 
# Why 10, 20, 30 and not 1, 2, 3? Because another key feature of data science is that projects never quite end up looking the way we expect them to when we start, and numbering by tens makes it easy to add files between existing files without having to re-number everything. 
# 
# For example, suppose I realize that before cleaning my data, I need to export some summary statistics about cleanliness issues. With this file structure, I can easily add a new file in the middle of the existing files:
# 
# ```
# 10_import_data.py
# 15_export_cleanliness_report.py
# 20_clean_data.py
# 30_analyze_data.py
# ```
# 

# ## Use lots of small files
# 
# OK, you might ask, but why do I need lots of files at all? Why not just one big "project" file? The answer is twofold. 
# 
# The first is that it's easier to debug small files. The only way to *really* know if your code works is to run it from start to finish in a clean session of whatever program you're using (R, Stata, Python, Julia). That way you know that if the code works, it works because everything you need is in the file, and that the code isn't running because you manually created an important variable that's not in the code, but is already in memory. But if you're entire project is in one many-thousand-line file, running that file takes forever. Moreover, when a problem occurs in that giant file, it could have lots of sources. Working with smaller files (a couple hundred lines at most) makes it much easier to test the file quickly, and makes it easier to find the source of problems when they occur. Moreover, small files with descriptive titles make it easier to navigate your project. That means if at some point you realize there's a problem with your data imports (wait, why am I missing three days of data??), it's very clear where you need to make changes.
# 
# The second reason is perhaps even more important. In my experience, we aren't really smart enough to work with files that do more than one or two things. Your computer is more than happy to save thousands of lines of code in a single file called `my_data_science_project.py`. The problem is that it's very hard for *you* to look at a file with thousands of lines of code and answer the question "is the code in this file accomplishing what I want this file to accomplish?". If, by contrast, you have a smaller file that does one thing in much less code, it's easier to evaluate that small chunk of code and decide if it accomplishes the goal set-out by the file's title (importing your data). 

# ## Carefully manage your source data
# 
# **Every** data science project should have a folder called something like `source_data` (or, if you're also numbering folders, `00_source_data`). This is the folder where you keep the input data for your project, the data you got from somewhere else you wish to analyze. This may be the raw results from a survey, data you downloaded from a government source, or data provided to you from another department. 
# 
# **YOU SHOULD NEVER, EVER, EVER MODIFY THE FILES IN THIS FOLDER**
# 
# Files in this folder are sacrosanct. You can *read* them into your programs (obviously, you have to), but you should never *re-save* them. After you read them in, if you need to save anything, *you save it somewhere else*. 
# 
# The reason is that you never want to risk corrupting your source data. If you have raw survey data, you never want to, say, modify those results directly, because what if you make a mistake? Your survey data is now corrupted, and (a) there's no record of that corruption, and (b) if you didn't keep backups of your raw data (which you should!) you've lost irreplaceable data. 

# ## Folder Strutures
# 
# With that mind, I usually work with the following top-level folder structure in my projects:
# 
# 
# - `00_source_data`: Raw inputs to this project, taken from other sources. Data in this folder should never be modified by code in this project.
# - `10_code`: All code for analysis
# - `20_intermediate_files`: data files created by code in this repository (presumably code that processes data found in `00_source_data`)
# - `30_results`: tables, figures, maps, etc. that will later be used in papers
# - `40_docs`: Paper write-ups
# 
# 
# One nice thing about this structure is it makes easy to test the reproducibility of your project: if you've done everything right, then you should be able to:
# 
# 1. Delete everything your `20_intermediate_files` folder and everything in your `30_results` folder, 
# 2. Re-run all the code in your `10_code` (which starts by reading in data from `00_source_data`)
# 
# And have all the results you want for your paper re-appear in your `30_results` folder. And if not all your results reappear (i.e. aren't generated when you run your code), you know that you have some files in there that aren't actually being created by code you currently have in the project (meaning those results aren't reproducible). 
# 
# 

# In[ ]:




