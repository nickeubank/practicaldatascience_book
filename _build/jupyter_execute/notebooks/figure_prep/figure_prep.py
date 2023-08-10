#!/usr/bin/env python
# coding: utf-8

# Figures built on the graphical ideas of https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

# # CONCAT

# In[6]:


import pandas as pd

a_d = {'C1': ['A','B','C'], 'C2': [2.1,4.3,-6.5], 'C3':[23,14,64]}
b_d = {'C1': ['D','E','F'], 'C2': [5.2, 0.5, 7.6], 'C3':[1,144,39]}
c_d = {'C1': ['D','E','F'], 'C2': [5.2, 0.5, 7.6]}
a = pd.DataFrame(a_d)
b = pd.DataFrame(b_d)
c = pd.DataFrame(c_d)


# In[7]:


a


# In[8]:


b


# In[9]:


c


# In[10]:


d = pd.concat([a,b])
d


# In[11]:


d.reset_index(inplace=True)
d


# In[13]:


e = pd.concat([a,c])
e


# 
