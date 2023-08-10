#!/usr/bin/env python
# coding: utf-8

# # Project: gathering, inspecting, and cleaning the data
# 
# In this step of the project, we'll gather the data that we need
# 
# 1. Carbon dioxide emissions by country
# 2. Income (as measured by GDP per capita) by country
# 3. Population by country (so we can convert CO2 emissions into per capita emissions)
# 4. List of territories by continent (since we want to be able to group the countries by region of the world)
# 
# As we load each dataset we will explore it and perform some pre-processing steps to prepare the data for merging it together for our plots. We'll be on the lookout for any inconsistencies in the data (numbers and text mixed up in the data), missing data which may dictate which years we will be able to plot in our final plot.

# ## Data Sources
# 
# Let's start by loading our four data sources. The first three sources are provided on the GapMinder website, but each has a slightly different source.
# 
# 1. [**Carbon dioxide emissions**](https://www.gapminder.org/tools/#$model$markers$spreadsheet$encoding$number$data$concept=co2_emissions_tonnes_per_person&space@=country&=time;;&scale$domain:null&type:null&zoomed:null;;&label$data$concept=name;;&frame$value=2018&data$concept=time;;;;;;&chart-type=spreadsheet&url=v1) (tonnes per person). These data are corbon dioxide emissions from the burning of fossil fuels in the units of metric tonnes pf CO2 per person. These data are sourced from the [Carbon Dioxide Information Analysis Center](https://cdiac.ess-dive.lbl.gov/) at Lawrence Berkeley National Laboratory. If you download these data as a CSV you will get the file 'co2_emissions_tonnes_per_person.csv', which we have included in the `data/` folder.
# 2. [**Income per person**](https://www.gapminder.org/tools/#$model$markers$spreadsheet$encoding$number$data$concept=income_per_person_gdppercapita_ppp_inflation_adjusted&space@=country&=time;;&scale$domain:null&type:null&zoomed:null;;&label$data$concept=name;;&frame$value=2018&data$concept=time;;;;;;&chart-type=spreadsheet&url=v1) (gross domestic product per capita, in international dollars, inflation-adjusted to 2011 prices). These data are sourced from the Gapminder based on World Bank, A. Maddison, M. Lindgren, International Monetary Fund, and others:  [link to more information on the data source](https://www.gapminder.org/data/documentation/gd001/). If you download these data as a CSV you will get the file 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv', which we have included in the `data/` folder.
# 3. [**Population**](https://www.gapminder.org/tools/#$model$markers$spreadsheet$encoding$number$data$concept=population_total&space@=country&=time;;&scale$domain:null&type:null&zoomed:null;;&label$data$concept=name;;&frame$value=2018&data$concept=time;;;;;;&chart-type=spreadsheet&url=v1). These data are sourced from Gapminder based on Maddison and the United Nations: [link to more information on the data source](http://gapm.io/dpop). If you download these data as a CSV you will get the file 'population_total.csv', which we have included in the `data/` folder.
# 4. [**Territories by continent**](https://unstats.un.org/unsd/methodology/m49/overview#). These data are sourced from the United Nations. These data are provided in the file 'united_nations_continents.csv' which we have included in the `data/` folder.

# At each of the above links you could have clicked the "CSV" button to grab the data, but we have done that and provided all of the data in the `data/` folder so you can get started exploring these data right away, but we have not changed the content of each dataset at all. 
# 
# ## Data Exploration
# 
# Before you begin using any dataset, you should get to know it a bit to understand its content, check for missing or anomalous values, and determine whether any additional processing is needed before you analyze it further. We'll walk through each of these four datasets, starting with carbon dioxide emissions.
# 
# ### Dataset 1 of 4: Carbon dioxide emissions data
# 
# Let's start by loading our data into a `pandas` `DataFrame` and take a look at the first 10 rows of content:

# In[1]:


import pandas as pd
co2_all = pd.read_csv('data/co2_emissions_tonnes_per_person.csv')
co2_all.head(10)


# Let's also use the `pandas` `describe()` method to summarize the contents:

# In[2]:


co2_all.describe()


# Looking at the data we learn a few things. First, the dataset contains data on CO2 starting in 1799 and going through 2017. For the plot we will be creating, we only need to plot one year of data, likely the most recent year. Since we only have data up to 2017, we'll need to use that as the common year. Going forward, we'll only concern ourselves with data from 2017.
# 
# Second, we see that many of those early years have `NaN` values, which indicates there is no data present. We can see in the "count" row of the description above that in 1799 and 1800, only 5 entries are non-empty, and this number is 194 from 2008 forward. Let's see how many countries we have in total, by using the `shape` attribute of `co2_all`:

# In[3]:


co2_all.shape


# We have 194 rows and 194 non-empty values in the later years that are included, so we have one value for each country on this list in 2017. We'll want to use the latest data that we have to make the plot as relevant as possible, so the last thing to do is to just extract the 2017 data. We'll need the 2017 column for the data as well as the corresponding country/territory so we can combine the data later with income and population:

# In[4]:


co2 = co2_all[['country','2017']]
co2


# One last step: since we'll eventually be merging our columns together, let's rename the '2017' column so that it is more self-explanatory and call it 'co2' using the `rename()` method:

# In[5]:


co2 = co2.rename(columns={'2017':'co2'})
co2


# The CO2 emissions data is ready for use! Let's move on to exploring income per person.
# 
# ### Dataset 2 of 4: Income per person
# 
# Again, let's start by loading and viewing the first 10 rows of our data:

# In[6]:


income_all = pd.read_csv('data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
income_all.head(10)


# As we look over the dataset here, we can see we have data that goes from 1799 through 2049. So clearly the later years are projections rather than measured data (unless the data providers have a time traveler on staff!).
# 
# We know that we're only concerned with the year 2017 from our discussion of CO2 data, so let's extract the year 2017 and the country:

# In[7]:


income_2017 = income_all[['country','2017']]
income_2017


# 
# But notice something odd here... Some of the values have the letter 'k' at the end of a number. While 'k' is the SI shorthand for a thousand units (representing "kilo"). But what is it doing in our dataset? Let's take a look at the data types in our data. We'd expect those to be numbers: floats or integers or something similar.

# In[8]:


income_2017.dtypes


# OK, the data from 2017 are objects, not floats or integers, just like the column for 'country'. Let's take a look at one of the entries in 2017 and see what's going on with the data there.

# In[9]:


first_entry = income_2017['2017'][0]
first_entry


# In[10]:


type(first_entry)


# It's a string! It's not a number. The authors of the data represented the number 12,000 as the string '12k' instead. We need to correct this since all data that we plot will need to be numerical.
# 
# For each value, we'll need to read in the string - if there are no letters in the entry, we just need to convert it to a number. If there is a letter k in it, we need to remove that letter and THEN convert the rest into a number and multiply it by 1,000. Let's create a function that does that:

# **EXERCISE: Write a function that takes a string as input and outputs the correct numerical representation of the number as a float. That is, if the input is '20' then the output should be the number 20.0; if the input is '20k' then the output should be the number 20000.0**

# In[1]:


# BREAK HERE AND DIRECT STUDENTS TO GRADED LAB


# In[11]:


def string2num(string):
    if 'k' in string:
        number = float(string[:-1])*1000
    else:
        number = float(string)
    return number
        
print(string2num('2'))
print(string2num('2k'))


# Now let's apply our function to our data for each entry in 2017. But before we do, let's make a copy of our data so we don't edit the original (`deep = True` ensures all the data are a copy rather than a view):

# In[12]:


income = income_2017.copy(deep=True)


# We can use the `pandas` method `apply()` to apply our `string2num` function to *each entry* in our '2017' column:

# In[13]:


income['2017'] = income_2017['2017'].apply(string2num)
income


# While it looks like we have successfully converted the strings to floats, let's look at our data types again to ensure we fixed the issue:

# In[14]:


income.dtypes


# Great! We have a column of floats now, so it looks like our fix worked. Let's make one more check to see whether there are any `NaN` values introduced - we want to avoid introducing anything like that into the mix:

# In[15]:


income['2017'].isna().values.any()


# No `NaN` values - so we're all set! 
# 
# And as our last step, let's also rename the column header from '2017' to 'income', similar to what we did with `co2` above, so that its content is clear and it will be ready to be merged together after we've loaded each of our four datasets.

# In[16]:


income = income.rename(columns={'2017':'income'})
income


# 
# With both CO2 and income data prepared, population is next!
# 
# ### Dataset 3 of 4: Population
# 
# As is our standard practice at this point, let's load in and view the first 10 entries in our dataset:

# In[17]:


pop_all = pd.read_csv('data/population_total.csv')
pop_all.head(10)


# These data go well into the future, all the way out to 2099. Let's begin by grabbing the 2017 data and dive a bit deeper.

# In[18]:


pop_2017 = pop_all[['country','2017']]
pop_2017


# It looks like we have suffixes of 'k' and 'M' (representing millions). We will have to apply a similar function to what we used for income here to prepare these data. But we have to ask the question: are 'k' and 'M' the *only* suffixes included in the data or are there others? Let's write a function to figure that out.
# 
# **EXERCISE: Create a function that takes in a `numpy` array (into which we will pass the 2017 population values of `pop_2017['2017'].values`) and searches through them to find any alphabetic letters that are present.** Hint: we recommend looking into the string method `isalpha()` and the `numpy` method `unique()` to help with this exercise.
# 
# For example, if your array of strings contained the following:
# |string list|
# |-|
# | '13k' |
# | '546' |
# | '9M' |
# | '12M' |
# | '900k' |
# 
# Desited output: ['k', 'M']

# In[ ]:


# BREAK HERE AND DIRECT STUDENTS TO GRADED LAB


# In[19]:


# SOLUTION
import numpy as np

def getcharacters(string_list):
    characters = []

    for value in string_list:
        for character in value:
            if character.isalpha():
                characters.append(character)
    return np.unique(characters)


# Let's apply the function we created to our dataset to see what string values are present:

# In[ ]:


unique_characters = getcharacters(pop_2017['2017'].values)
unique_characters


# Great! we now know that we need to handle thousands ('k'), millions ('M'), and billions ('B'). 
# 
# **EXERCISE: adjust your `string2num()` function that we created earlier to accommodate replacing the 'k', 'M' and 'B' characters**

# In[ ]:


# BREAK HERE AND DIRECT STUDENTS TO GRADED LAB


# In[20]:


def string2num(string):
    if 'k' in string:
        number = float(string[:-1])*1000
    elif 'M' in string:
        number = float(string[:-1])*1e6
    elif 'B' in string:
        number = float(string[:-1])*1e9
    else:
        number = float(string)
    return number
        
print(string2num('2'))
print(string2num('2k'))
print(string2num('2M'))
print(string2num('2B'))


# Just like we did for the case of income, let's apply our updated `string2num()` function to our population dataset. Since we're modifying our data, let's be sure to make a copy of it first.

# In[21]:


pop = pop_2017.copy(deep=True)

pop['2017'] = pop_2017['2017'].apply(string2num)
pop


# This looks good, let's double check our data types again to make sure everything was converted over to floats and make sure there were no `NaN` values introduced during processing:

# In[22]:


pop.dtypes


# In[23]:


pop.isna().values.any()


# Lastly, let's rename the column header from '2017' to 'population' so that its column label is clear and descriptive for when we merge these data frames later.

# In[24]:


pop = pop.rename(columns={"2017": "population"})
pop


# With that done, we now have prepared our data for `co2`, `income`, and `pop`. All we need now is a way to identify the corresponding continent / region of the world for for each country, and for that, we can look at our UN data.
# 
# ### Dataset 4 of 4: Continents / global regions
# 
# Once again, let's start by loading in and inspecting the next and final dataset we'll be incorporating: the UN data on continents.

# In[25]:


undata = pd.read_csv('data/united_nations_continents.csv')
undata.head(10)


# Well that was unexpected! Whenever we see an error like this, it's good to look directly at our data to see if we missed something about the data that prevented it from loading. Let's take a look into the first few lines of the 'united_nations_continents.csv' file and see if anything odd is going on there:

# ```text
# Global Code;Global Name;Region Code;Region Name;Sub-region Code;Sub-region Name;Intermediate Region Code;Intermediate Region Name;Country or Area;M49 Code;ISO-alpha2 Code;ISO-alpha3 Code;Least Developed Countries (LDC);Land Locked Developing Countries (LLDC);Small Island Developing States (SIDS)
# 001;World;002;Africa;015;Northern Africa;;;Algeria;012;DZ;DZA;;;
# 001;World;002;Africa;015;Northern Africa;;;Egypt;818;EG;EGY;;;
# 001;World;002;Africa;015;Northern Africa;;;Libya;434;LY;LBY;;;
# 001;World;002;Africa;015;Northern Africa;;;Morocco;504;MA;MAR;;;
# 001;World;002;Africa;015;Northern Africa;;;Sudan;729;SD;SDN;x;;
# ````

# There is definitely something odd going on here! A CSV file stands for "comma separated values" however, this file is not comma separated, it's semicolon separated! To address this, we will need to adjust our data loading code to accommodate. We can do this with the `sep` keyword for the `read_csv()` method to let it know the separator is a semicolon and otherwise proceed as it would with the comma.

# In[26]:


undata = pd.read_csv('data/united_nations_continents.csv', sep=';')
undata.head(10)


# While there's a lot of information here, what we need are two columns: 'Region Name' and 'Country or Area'. Let's extract just those from the data:

# In[27]:


continent = undata[['Region Name','Country or Area']]
continent.head(10)


# For ease of reference, let's rename the columns 'Region Name' and 'Country or Area' to 'continent' and 'country' respectively:

# In[28]:


continent = continent.rename(columns={"Region Name": "continent", "Country or Area": "country"})
continent


# Let's also sort `continent` by 'country':

# In[29]:


continent = continent.sort_values(by=['country'])
continent


# Now we have each of the pieces of the puzzle that we need: `co2`, `income`, `pop` and `continents`. Getting the data ready for use requires significant effort, but it's best if it can be done in a way that is easily reproducible. Imagine that we received an update to the data for 2023 and the first time through we had done all of the steps above manually in the original CSV files. We would then have to go through that process all over again. However, because we automated each process, we can easily rerun the above steps on new data, so our investment in time would pay off going forward.
# 
# Now that we have each of the four data sources separately, in the next lesson we will merge these into one dataset that we can then plot.

# In[31]:


### Not for inclusion - just to save contents from this notebook
import pickle

pickle_path = 'data/pickle/'

to_pickle = ['co2','income','pop','continent']
for item in to_pickle:
    eval(f'{item}.to_pickle(\'{pickle_path}{item}.pkl\')')

