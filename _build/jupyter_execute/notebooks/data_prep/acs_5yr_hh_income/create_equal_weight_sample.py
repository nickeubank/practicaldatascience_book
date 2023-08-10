#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("./acs_5yr_hh_income.csv.gz")
df.head(30)


# In[62]:


df.HHINCOME.describe()


# In[3]:


hh = df.drop_duplicates(["SAMPLE", "SERIAL"])


# In[40]:


hh.head(20)


# In[41]:


len(hh)


# In[42]:


len(hh[hh.HHINCOME ==9999999 ])


# In[43]:


hh[hh.HHINCOME.isnull()]


# In[44]:


hh.HHINCOME.isnull().sum()


# In[51]:


flat = hh.sample(n=1_000_000, weights=df["HHWT"])
len(flat)


# In[52]:


flat.HHINCOME.isnull().sum()


# In[53]:


flat = flat[flat.HHINCOME!=9999999]


# In[54]:


len(flat)


# In[55]:


flat.HHINCOME.describe()


# In[56]:


flat.HHINCOME.isnull().sum()


# In[57]:


flat.HHINCOME.to_csv(
    "../../class_2/week_2/data/us_household_incomes.txt", header=False, index=False
)


# In[58]:


import numpy as np


# In[60]:


v= np.loadtxt("../../class_2/week_2/data/us_household_incomes.txt")
v


# In[61]:


v.shape


# In[69]:


np.percentile(v, 50)


# In[67]:


v = np.sort(v)


# In[ ]:




