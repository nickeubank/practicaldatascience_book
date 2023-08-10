#!/usr/bin/env python
# coding: utf-8

# # Writing Good Jupyter Notebooks
# 
# Unlike `.py` files, the purpose of a Jupyter Notebook is not just for getting something done, or for communicating with a computer; rather, Jupyter notebooks are for communicating *with people*, and the way we write them should reflect that fact. (If you're curious, I think the origin of Jupyter Notebooks lies in the idea of [literate programming](https://en.wikipedia.org/wiki/Literate_programming), which was all about this idea.)
# 
# In this class, you will generally be writing notebooks as a way of doing class exercises, which means the organization of your work will naturally be constrained by the structure of the exercises you are doing. As such, you don't need to worry too much about how you organize the content of your notebook—in other words, how you would compose the presentation of results—something you may find yourself doing in the workplace some day! Nevertheless, here are several principles to follow when working in Jupyter notebook, as well as a few examples of what I think are relatively good notebooks. Note that with each principle I'm including notes on how one *could* achieve the principle, but I also don't want to be dogmatic—if you find alternate ways to achieve the goals laid a below, by all means please do so!
# 

# 
# ## Use Markdown
# 
# My number one rule for writing good notebooks is to use Markdown. If you aren't familiar with Markdown syntax yet, you should definitely familiarize yourself with it ([here's one cheatsheet](https://en.wikipedia.org/wiki/Markdown#Examples) and here's [another cheatsheet](https://www.markdownguide.org/basic-syntax/)) as it has become the near lingua franca of the internet—it's not only supported by R Markdown and Jupyter Notebooks, but also platforms like Github, Wikipedia, Wordpress, and many many more.
# 
# Markdown (and formatting in general) is *especially* import for exercises because your exercises contain lots of different types of information: the exercise number, the prompt to which you're responding, your answers, etc. So using markdown to visually distinguish these different types of content quickly is really helpful (*especially* for the TAs and me who are trying to quickly skim LOTS of assignments—the easier you can make it for us to identify where your answers are, the happier it will make us!).
# 
# One particularly useful Markdown trick? Quote blocks! Start a line with `> `, and what follows will be put in a quote block. Good for distinguishing your answers from exercise prompts (honestly, you can quote block the prompt *or* your answer—I've seen both, and both look quite good!)

# 
# ## Interpret Your Numbers
# 
# Data science isn't about writing code that passes a test suite or that runs without raising exceptions; data science is about *interpreting* data to help improve our understanding of the world around us. To that end, any time you are sharing a result, you **absolutely must** interpret it for the reader. That means no answering a question with Python printing out a number—you should also tell the reader what, in substantive terms, that number means. For example, if you're asked what share of US households are living below the poverty line, don't answer `0.183`. First, it's not clear if that's the share / proportion (18.3%), or the percentage of households (0.18%). Second, one should always include units when presenting numbers (in this case "US Households"), since the share of households living below the poverty line worldwide is different from the share of households living below the poverty line in the US is different from the share of _people_ living below the poverty line in the US. 
# 
# I recognize that when an exercise prompt is pretty clear this may feel unnecessary / pedantic, but it's a good practice to get used to for the real world. Get your units wrong and... [bad things can happen.](https://www.wired.com/2010/11/1110mars-climate-observer-report/)
# 
# My personal suggestion for how to do this is to present answers with an f-strings (not familiar with f-strings? Best Python feature in years. [Learn all the tricks here!](https://www.youtube.com/watch?v=BxUxX1Ku1EQ)). These will not only allow you to combine interpretation / units with your result, but you can also format it (so it doesn't have 20 decimal places), and you have an output that will automatically update if you change code further up in the notebook. For example:
# 

# In[2]:


below_poverty = 0.183
print(f"The share of US Households earning less than $20,000 in 2008 was {below_poverty:.2f}")


# ## Format Your Code
# 
# While VS Code does *not* implement "Format on Save" for Jupyter Notebook, you *can* still use Black to format your code. Just right-click in a Jupyter Notebook cell and select either "Format Cell" or "Format Notebook". It can take a couple moments, so be patient, but it works!
# 
# As you've seen me say in videos (and as we will talk about more later this semester), well formatted code is not just about making your code pretty—humans are visual creatures, so the more consistently your code is formatted, the more easily your visual pattern-recognition systems will be able to notice problems. So please format your code!
# 
# That goes for long strings, too, by the way. Black won't split a string into multiple lines, but Python will let you split a string across multiple lines in a couple ways:

# In[3]:


# With a backslash at the end of the line
x = "Hello Everyone! My name is "     "Nick"
x


# In[5]:


# Or just by ending your string and
# starting anew on the next line 
# inside parens 
# (often useful for file paths).
x = ("Hello Everyone! My name is "
     "Nick")
x


# ## Other Odds and Ends
# 
# - **Comment Your Code:** As you can see from the example above, even in notebooks (where a lot of what you want to communicate will end up in markdown cells), you can/should still comment your code!
# - **Restart and Re-Run Your Notebook:** No one should be submitting notebooks with cell execution counters (those little numbers to the left of your code cells) that are in the high double digits or, god forbid, triple digits. Before submitting your notebook (and honestly any time you've been monkeying around a lot while you're working) **you should Restart your notebook and click `Run All`.**
# - **Don't leave in spaghetti output:** Sometimes when we're writing our code will do things like print out 40 lines of a DataFrame, or all the column names in a massive dataset. That's fine while you're working, but don't leave that output there for your reader—no one wants to flip through three pages of column names to get back to actual content they care about!

# ## Some Examples
# 
# I don't want to give away solutions to this or other MIDS classes, so I don't have a *ton* of notebooks to share, but here are a couple good example notebooks (all shared with permission):
# 
# - [A Deep Learning assignment from former MIDSter Nate Warren.](https://github.com/nickeubank/practicaldatascience/raw/master/Example_Data/example_notebooks/ExampleNotebook_NW.ipynb.zip) Note use of quote blocks to differentiate answers from prompts.
# - [A notebook from a GIS module in this class we won't be doing this year from MIDSters Erika Fox and Raza Lamb.](https://github.com/nickeubank/practicaldatascience/raw/master/Example_Data/example_notebooks/ExampleNotebook_FoxLamb.pdf)
# 
# 

# ## Homework Grading
# 
# Moving forward, here is an approximate rubric for homeworks:
# 
# **A (0.95):**
# 
# *All* of the following is true:
# 
# - There are no significant errors in the code/analysis.
# - The document is well-formatted and everything the authors are doing are coherently communicated.
# - Numbers are presented in context, and with interpretation where appropriate.
# - All code is well-formatted.
# 
# **B (0.85):**
# 
# *One* of the following is true:
# 
# - There are *some* significant errors in the code/analysis,
# - The document is not well-formatted / some of what the authors are doing is not coherently communicated,
# - Some numbers are presented without context, or without interpretation where interpretation would have been appropriate.
# - The code has significant formatting errors.
# 
# **C (0.75):**
# 
# *Two* of the conditions for a B assignment are true.
# 
# (Grades above an A (e.g. above 0.95), or below a C are possible where deemed appropriate by graders.)
