#!/usr/bin/env python
# coding: utf-8

# In[29]:


### Not for inclusion - just to load contents from previous notebook
import pandas as pd
pickle_path = 'data/pickle/'

to_pickle = ['co2','income','pop','continent']
for item in to_pickle:
    exec(f'{item}=pd.read_pickle(\"{pickle_path}{item}.pkl\")')


# # Project: Data merging
# 
# Recall our goal is to produce a plot that explores the relationship between carbon dioxide emissions, income, and population for each country/territory. In this step of the project, we'll merge our four data sources together on:
# 
# 1. Carbon dioxide emissions by country
# 2. Income (as measured by GDP per capita) by country
# 3. Population by country (so we can convert CO2 emissions into per capita emissions)
# 4. List of territories by continent (since we want to be able to group the countries by region of the world)
# 
# In the last lesson, we loaded the data we needed for reach of those as: `co2`, `income`, `pop` and `continents` and created a series of steps that we could reuse if we need to process a different year of data. Now, we need to merge these into one `DataFrame` so that we can plot it. To refresh our memories, let's take a look at our four datasets that we need to merge together and think about how we will merge them:

# In[30]:


co2


# In[31]:


income


# In[32]:


pop


# In[33]:


continent


# The first observation when looking across these four datasets is that they each have a different number of rows! 194, 195, 197, and 249, respectively. This means they don't all contain the same countries. But we need to combine them to plot them.
# 
# Think about what type of merge would be appropriate here? Left, right, inner, or outer? We only want to save the rows that are matching, so an inner merge seems like the right approach. Let's start by merging co2 and income based on the 'country' column:

# In[34]:


data = pd.merge(co2,income,how='inner',on='country')
data


# Excellent - we have 193 rows, which is as expected given the smallest size among the two dataframes being merged. Next lets add in population:

# In[35]:


data = pd.merge(data,pop,how='inner',on='country')
data


# And again we have 193 merged columns - looks like we have everything except for the continent labels added in. Adding in the continent labels is a little bit trickier, however, because if we look at the lists of the country/territory names in our `data` and `continent` frames, we can see that some of the names that are the same are simply written a bit differently. For example the following pairs represent the same territory:
# 
# - 'Brunei', 'Brunei Darussalam'
# - 'Bolivia', 'Bolivia (Plurinational State of)'
# - 'Venezuela','Venezuela (Bolivarian Republic of)'
# - 'St. Vincent and the Grenadines', 'Saint Vincent and the Grenadines'
# - 'Cote d'Ivoire', 'Côte d’Ivoire'
# 
# This means that these will not be merged together using the `merge()` method because their values are not identical.
# 
# We will create a method for idnetifying matching pairs of all names that we can confidently match, and will manually label the continent for the remaining territories. Looking at the data, it looks like we have 4 general categories:
# 1. **Exact matches**. Character-for-character equality. E.g., 'Burundi' <-> 'Burundi'
# 2. **Subset matches**. The "shorthand" name is a subset of the full name. E.g., 'Bolivia' <-> 'Bolivia (Plurinational State of)'
# 3. **Near matches**. The names are VERY similar, but a few characters may be different. E.g., 'Cape Verde' <-> 'Cabo Verde'
# 4. **Unmatched examples**. Cases that do not have corresponding pairs. E.g. 'Holy See'
# 
# Since the lists to be merged are of length 193 and 249, respectively, then a simple approach to merging them is to manually correct the names of countries/territories in the `continents` frame to match the rest. This approach is fine, however, this is not practical for larger lists which will commonly be encountered. Instead, we will find a way to minimize the need for manual intervention and identify the nearest match from one list to the other by considering the four possible cases above. As with many aspects of data science, we cannot always eliminate the need for some manual effort in preparing the data, but we will reduce it greatly.
# 
# **EXERCISE: Create a function that takes as input two arrays of strings and returns a list the most likely matches**
# 

# In[ ]:


def get_matches(list1,list2):
    pass
    # Returns a list of tuples of matches:
    #   [ (match_string_1, match_string_2, similarity_score)]


# As a recommended approach, use the list of 4 categories above and test for each. What is important here is that order matters. If you perform a match, the matched strings should be removed from further consideration going forward so you don't create duplicate matches. Additionally, match those quantities that the most likely matches first (e.g. exact matches before subset matches, before near matches). Since the lengths of the territory lists are 193 and 249, at most there will be 193 matches.
# 
# You're encouraged to read about and use the `difflib` package and the `SequenceMatcher` object and `get_close_matches` function. `SequenceMatcher` provides a similarity score for comparing two strings and takes on values between 0 and 1 where 1 is an exact match and 0 is no match at all. The `get_close_matches` function provides a list of the closest matches to the input string based on the `SequenceMatcher` similarity score.
# 
# Therefore, pseudocode for this function should be:
# 1. Identify any exact matches and remove them from the list of strings to match
# 2. Identify subset matches and remove them from the list of strings to match
# 3. One at a time, create near matches based on the similarity score of each possible match
# 4. Repeat (3) until all 193 of the territories have been matched
# 5. Return the list of tuples with each match and its corresponding similarity score (set all exact matches and subset matches to a similarity score of 1)

# In[ ]:


# BREAK HERE AND DIRECT STUDENTS TO GRADED LAB


# In[36]:


from difflib import SequenceMatcher, get_close_matches

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def closest(a,B):
    return get_close_matches(a,list(B),n=1,cutoff=0)

long = list(continent['country'].values)
short = list(data['country'].values)
long_strings = long.copy()
short_strings = short.copy()

# First pass, match those with exact subsets
matches = []
for ss in short:
    candidates = []
    for ls in long:
        if ss in ls:
            candidates.append(ls)
    if len(candidates) > 0:
        selected = closest(ss,candidates)[0]
        sim = similar(ss,selected)
        long_strings.remove(selected)
        short_strings.remove(ss)
        matches.append([ss, selected, 1])

# Second pass, match what remains using proximity
slength = len(short_strings)
while slength > 0:
    matching_options = []
    similarity = []
    for ss in short_strings:
        selected = closest(ss,long_strings)[0]
        similarity.append(similar(ss,selected))
        matching_options.append([ss,selected])
    x = 1
    max_index = similarity.index(max(similarity))
    sim = max(similarity)
    long_strings.remove(matching_options[max_index][1])
    short_strings.remove(matching_options[max_index][0])
    matches.append([matching_options[max_index][0], matching_options[max_index][1],sim])
    slength = len(short_strings)
    
for e in matches:
    print(f'SS = {e[0]}, LS = {e[1]}, Sim = {e[2]}')


# In[37]:


for match in matches:
    if match[2] > 0.5:
        continent = continent.replace(match[1], match[0])


# In[38]:


data = pd.merge(data,continent,how='left',on='country')
data


# In[39]:


data[data.isnull().any(axis=1)]


# In[48]:


continent['continent'].unique()


# In[51]:


data.at[35, 'continent'] = 'Africa'
data.at[72, 'continent'] = 'Asia'
data.at[90, 'continent'] = 'Asia'
data.at[94, 'continent'] = 'Asia'
data.at[140, 'continent'] = 'Asia'
data.at[177, 'continent'] = 'Asia'
data


# In[53]:


data.isnull().any()


# In[55]:


data[data.isna().any(axis=1)]


# In[52]:


data[data.isnull().any(axis=1)]


# Wonderful! We have our dataset successfully merged. 
# 

# ## Changing the data from being divided into continents to 4 global regions
# 
# We just have one final data processing step before we create our plot. If you look at the chart on GapMinder's website, instead of using 7 continent categories, they use four categories for the world grouping Asia and Oceania into Asia. Let's do the same here by replacing any instances of "Oceania" with "Asia". Here we can use the `replace()` method.

# In[57]:


data['continent'].unique()


# In[56]:


data['continent'] = data['continent'].replace("Oceania","Asia")
data['continent'].unique()


# Phew! We have done a LOT of data processing to get ready to make our plot, which we'll do in the next lesson. Our data are the fuel for all the analyses we do in data science and often its takes some effort to prepare them for use. Having a clean dataset like we do now is entirely worth it as we can now explore these data by plotting them!

# In[58]:


### Not for inclusion - just to save contents from this notebook
import pickle

pickle_path = 'data/pickle/'

data.to_pickle(f'{pickle_path}data.pkl')

