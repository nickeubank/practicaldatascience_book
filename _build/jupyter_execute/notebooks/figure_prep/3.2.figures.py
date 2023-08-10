#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

a = pd.DataFrame({'C1':['A','B','C'],
                  'C2':['x','y','z']})
b = pd.DataFrame({'C1':['A','B','D'],
                  'C3':[11,12,13]})


# In[2]:


a


# In[3]:


b


# In[6]:


left = pd.merge(a, b, how="left", on="C1")
left

