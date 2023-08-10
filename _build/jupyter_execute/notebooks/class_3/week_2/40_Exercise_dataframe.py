#!/usr/bin/env python
# coding: utf-8

# # Estimating Labor Market Returns to Education
# 
# In this exercise, we're going to use data from the [American Communities Survey (ACS)](https://usa.ipums.org/usa/acs.shtml) to study the relationship betwen educational attainment and wages. The ACS is a survey conducted by the United States Census Bureau (though it is not "The Census," which is a counting of every person in the United States that takes place every 10 years) to measure numerous features of the US population. The data we will be working with includes about 100 variables from the 2017 ACS survey, and is a 10% sample of the ACS (which itself is a 1% sample of the US population, so we're working with about a 0.1% sample of the United States). 
# 
# This data comes from [IPUMS](https://usa.ipums.org/usa/), which provides a very useful tool for getting subsets of major survey datasets, not just from the US, but [from government statistical agencies the world over](https://international.ipums.org/international-action/sample_details).
# 
# This is *real* data, meaning that you are being provided the data as it is provided by IPUMS. Documentation for all variables used in this data can be found [here](https://usa.ipums.org/usa-action/variables/group) (you can either search by variable name to figure out the meaning of a variable in this data, or search for something you want to see if a variable with the right name is in this data). 
# 
# Within this data is information on both the educational background and current earnings of a representative sample of Americans. We will now use this data to estimate the labor-market returns to graduating high school and college, and to learn something about the meaning of an educational degree. 

# **1)** Data for these [exercises can be found here](https://github.com/nickeubank/MIDS_Data/tree/master/US_AmericanCommunitySurvey). First, download `US_ACS_2017_10pct_sample.dta`. 

# **2)** Now import `US_ACS_2017_10pct_sample.dta` into a pandas DataFrame. This can be done with the command `pd.read_stata`, which will read in files created in the program Stata (and which uses the file suffix `.dta`). This is a format commonly used by social scientists.

# ## Getting to Know Your Data
# 
# When you get a new dataset like this, it's good to start by trying to get a feel for its contents and organization. Toy datasets you sometimes get in classes are often very small, and easy to look at, but this is a pretty large dataset, so you can't just open it up and get a good sense of it. Here are some ways to get to know your data. 

# **3)** How many rows are in your data?

# **4)** How many columns are in your data?

# **5)** Let's see what variables are in this dataset. First, try to see them all using the command:
# 
# ```
# acs.columns
# ```
# 

# As you will see, `python` doesn't like to print out all the different variables. To get everything printed out, we can loop over all the columns and print them one at a time with the command:
# 
# ```
# for c in acs.columns: print(c)
# ```
# 
# Try it. 

# **4)** That's a *lot* of variables, and definitely more than we need. In general, life is easier when working with these kinds of huge datasets if you can narrow down the number of variables a little. In this exercise, we will be looking at the relationship between education and wages, we need variables for: 
# 
# - Age
# - Income
# - Education
# - Employment status (is the person actually working)
# 
# These quantities of interest correspond to the following variables in our data: `age`, `inctot`, `educ`, and `empstat`. 
# 
# Subset your data to just those variables. 

# **5)** Now that we have a more manageable number of variables, it's often very useful to look at a handful of rows of your data. The easiest way to do this is probably the `.head()` method (which will show you the first five rows), or the `tail()` method, which will show you the last five rows. 
# 
# But to get a good sense of your data, it's often better to use the `sample()` command, which returns a random set of rows. As the first and last rows are sometimes not representative, a random set of rows can be very helpful. Try looking at a random sample of 20 rows (note: you don't have to run `.sample()` ten times to get ten rows. Look at the `.sample` help file if you're stuck. 

# **6)** Do you see any immediate problems? What issues do you see?

# **7)** One problem is that many people seem to have incomes of $9,999,999. Moreover, people with those incomes seem to be very young children. 
# 
# What you are seeing is one method (a relatively old one) for representing missing data. In this case, the value 9999999 is used to denote observations for which there is no data (Or more specifically, in this case observations where the person is too young to work, so their income value is missing). 
# 
# So let's begin by dropping anyone who has `inctot` equal to 9999999. 

# **8)** OK, the other potential problem is that our data includes lots of people who are unemployed and people who are not in the labor force (this means they not only don't have a job, but also aren't looking for a job). For this analysis, we want to focus on the wages of people who are currently employed. So subset the dataset for the people for whom `empstat` is equal to "employed". 
# 
# Note that our decision to only look at people who are employed impacts how we should interpret the relationship we estimate between education and income. Because we are only looking at employed people, we will be estimating the relationship between education and income *for people who are employed*. That means that if education affects the *likelihood* someone is employed, we won't capture that in this analysis.

# **9)** Now let's turn to education. The `educ` variable seems to have a lot of discrete values. Let's see what values exist, and their distribution, using the `value_counts()` method. This is an *extremely* useful tool you'll use a lot! Try the following code (modified for the name of your dataset, of course):
# 
# ```
# acs['educ'].value_counts()
# ```

# **10)** There are a lot of values in here, so let's just check a couple. What is the average value of `inctot` for people whose highest grade level is "grade 12" (in the US, that is someone who has graduated high school)?

# **11)** What is the average income of someone who graduated college ("4 years of college")? What does that suggest is the value of getting a college degree after graduating high school?

# **12)** What is the average income for someone who has not finished high school? What does that suggest is the value of a high school diploma?

# **13)** Complete the following table:
# 
# - Average income for someone who has not finished high school: _________
# - Average income for someone who only completed 9th grade: _________
# - Average income for someone who only completed 10th grade: _________
# - Average income for someone who only completed 11th grade: _________
# - Average income for someone who finished high school (12th grade) but never started college: _________
# - Average income for someone who completed 4 year of college (in the US, this means graduating college): _________

# **14)** Why do you think there is no benefit from moving from grade 9 to grade 10, or grade 10 to grade 11, but there is a huge benefit to moving from grade 11 to graduating high school (grade 12)?

# ## Take-aways
# 
# Congratulations! You just discovered "the sheepskin effect!": people with degrees tend to earn substantially more than people who have *almost* as much education, but don't have an actual degree. 
# 
# In economics, this is viewed as evidence that the reason employers pay people with high school degrees more than those without degree is *not* that they think those who graduated high school have learned specific, useful skills. If that were the case, we would expect employee earnings to rise with every year of high school, since in each year of high school we learn more. 
# 
# Instead, this suggests employees pay high school graduates more because they think *the kind of people* who can finish high school are the *kind of people* who are likely to succeed at their jobs. Finishing high school, in other words, isn't about accumulating specific knowledge; it's about showing that you *are the kind of person* who can rise to the challenge of finishing high school, also suggesting you are also the kind of person who can succeed as an employee. 
# 
# (Obviously, this does not tell us whether that is an *accurate* inference, just that that seems to be how employeers think.) 
# 
# In other words, in the eyes of employers, a high school degree is a *signal* about the kind of person you are, not certification that you've learned a specific set of skills (an idea that earned [Michael Spence](https://en.wikipedia.org/wiki/Michael_Spence) a Nobel Prize in Economics). 
