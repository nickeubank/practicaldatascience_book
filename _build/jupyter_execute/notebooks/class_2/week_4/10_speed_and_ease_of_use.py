#!/usr/bin/env python
# coding: utf-8

# # The Python Ease of Use / Speed Tradeoff
# 
# As a Data Scientist working in Python, *most* of the time the libraries you want to use have already been carefully engineered to deliver excellent performance, meaning you *usually* don't have to worry about code speed. However, understanding why programs like Python can sometimes be slow is still important to avoid accidentally writing code that runs so slowly you can't get your work done and for troubleshooting code that you need to execute faster. 
# 
# Two primary factors determine the speed of a program: 
# 
# - The number of computations the computer has to complete (i.e. adding, multiplying, etc.)
# - The amount it has to access and move data around since accessing memory is **slow**). 

# 
# This is a bit abstract, so let's look at some real code and discuss what your computer is actually doing when it runs Python code. In particular, let's focus on what happens in a loop like this:

# In[ ]:


summation = 0
for i in range(1000):
    summation = summation + i


# 
# 
# Now, you might think that all Python has to do to run this loop is add a bunch of numbers. But unfortunately, that's not the case. 
# 
# At each step of this loop, Python has to do the following: 
# 
# 1. Dereference `summation` (by "dereference" we mean find the place in memory that is associated with the variable `summation` and read the data there)
# 2. Determine the data type of `summation` (in this case, it's an integer). 
# 3. Dereference `i`
# 4. Determine the data type of `i` (in this case, it's an integer). 
# 5. Look up how it should interpret `+` given that `summation` is an integer and `i` is an integer. 
#     - Remember: if `summation` and `i` were strings, it wouldn't be doing addition, it would be concatenating! And because integers and floating point numbers are different things from the perspective of a computer, if `i` were an integer and `summation` were a floating point number, `+` would require (a) converting `i` to a floating point number, then (b) adding the floating point version of `i` to `summation`. 
# 6. Compile low-level binary code (referred to as "machine code") that can be read by the computer's processor to tell it to execute an addition of two integers AND to also check and make sure that the operation won't cause an integer overflow. That's another operation!).
# 7. Run that code. 
# 
# As you can see, there's a *lot* going on in that simple line of code, and that process has to repeat *every step of the loop*.
# 
# Now, you might ask, is all of that necessary? 
# 
# The answer is both yes and no. There are languages that don't require all those steps (like C and C++, the standard-bearers for speed), but if Python didn't do all those things when it ran, you wouldn't be able to use Python the way you do. 
# 
# Python is designed to be easy for you, the programmer. Unlike in some languages (like C), in Python, you don't have to declare that `i` is an integer explicitly in your code, and you are allowed to change `i` from an integer to a floating point number whenever you want. That makes Python what's called a **dynamically typed** language, and it makes it very easy to use. If you wrote this in C, every time you made a new variable you'd have to declare its type. But the fact it's dynamically typed means the language is never quite sure of the type of a variable until it explicitly checks that type because it could change at any time. 
# 
# Moreover, Python is a language you can use *interactively*. You can't open a terminal and write and execute C code one line at a time. For languages like C (what are called "compiled languages"), you write all of your code, then hit compile, and your computer reads all your code and compiles low-level binary code for that entire program at once. Then the only way to use your C code is to run that compiled program. But the advantage of that is that step 6 (compiling your code) is done once in advance, and you don't have to do that every time you run your code. But to make Python interactive, it was decided that Python should evaluate each line of code when it reaches that code. That massively increases its flexibility and allows you to program interactively, but for loops like this, it means to do 1,000 additions, it also has to compile low-level machine code 1,000 times.

# ## Rules for Going Fast in Python
# 
# So now that you have some sense of why Python can be slow, let's talk about how to keep your Python code fast.
# 
# ### Rule 1: Use other people's optimized functions
# 
# Let's start with the dirty secret of Python: when you use a library in Python, the code you're running was almost never actually written in Python. Instead, the functions you're calling have a "thin" layer of Python at the top (which is what you're interacting with), but when it comes to doing serious computations, the functions are actually calling tools written in C, which is *blazing* fast. In fact, Python has been described as a glue language, able to get some of the speed benefits of compiled languages like C/C++ while retaining the convenient syntax and interactivity of python through those packages.
# 
# Thus the first rule of speed in Python: when you need speed, use tools that other people have written and distributed in libraries with active communities (like `pandas`, `sci-py`, `statsmodels`, etc.). Because what you're really doing is using C, and C is 10x or 100x times faster than Python.
# 
# ### Rule 2: Vectorize, Don't write loops
# 
# When you use "vectorized" code, you get *huge* performance gains, and is the subject of the next section.

# ## Recap
# - Python has major benefits it is an interpreted language and dynamically typed that is easy to read and write and express programs clearly in a few lines of code
# - The price Python pays for its benefits is its performance, which is generally slower than compiled languages using native Python
# - Python is a glue language that can provide an interface between compiled languages like C/C++ and the convenient Python syntax providing speed and code clarity
# - Increase speed in your programs by using well-tested Python libraries rather than writing your own code because they will likely have been optimized for speed
