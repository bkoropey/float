#!/usr/bin/env python
# coding: utf-8

# In[1]:



import statsmodels.api as sm


# In[2]:



from sklearn import linear_model 


# In[6]:



import pandas as pd

df = pd.read_excel("C:\\Users\\KOROPEYB\\Desktop\\crackers\\sandbox\\Book2.xlsx", sheet_name = "DataFrame", headers = 7)


# In[7]:


df


# In[8]:



YD1S = df["D1: 8-6 Summer"]


# In[9]:


YD1S


# In[10]:



YD2S = df["D2: 8-8 Summer"]
YD2S


# In[11]:



YD1W = df["D1: 8-6 Winter"]
YD2W = df["D2: 8-8 Winter"]
YD3W = df["D3: All Day Winter"]
YD1W
YD2W
YD3W


# In[12]:


YD1W


# In[13]:


YD2W


# In[14]:


YD3W


# In[18]:



x = df[["D2: 8-8 Summer", "D3: All Day Summer","D1: 8-6 Winter", "D2: 8-8 Winter", "D3: All Day Winter"]]
                    
                    
                    
                    
                    


# In[19]:


x


# In[20]:


model = sm.OLS(YD1S, x).fit()


# In[21]:


model.summary()


# In[22]:


import numpy as np

np.corrcoef(df)


# In[ ]:




