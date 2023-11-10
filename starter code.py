#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from pathlib import Path


# In[4]:


shopping_trends = Path("shopping_trends_updated.csv")


# In[5]:


shopping_trends = pd.read_csv(shopping_trends)


# In[6]:


shopping_trends.head()


# In[7]:


shopping_trends.info()


# In[ ]:




