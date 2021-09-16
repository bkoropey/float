#!/usr/bin/env python
# coding: utf-8

# In[12]:


from sklearn.decomposition import PCA


# In[13]:


import pandas as pd


# In[14]:



df = pd.read_excel("C:/Users/KOROPEYB/Desktop/crackers/sandbox/Book2.xlsx", sheet_name= "DataFrame")


# In[15]:


df.head()


# In[17]:


pca_SWRates = PCA(n_components = 2)


# In[18]:


principal_components = pca_SWRates.fit_transform(df)


# In[19]:


pc_df = pd.DataFrame(data = principal_components, columns=['principal component 1', 'principal component 2'])


# In[20]:


pc_df.tail()


# In[21]:


pc_df.head()


# In[22]:



print('explained variation per principal component: {}'.format(pc_df.explained_variance_ratio_))


# In[23]:



print('explained variation per principal component: {}'.format(pca_SWRates.explained_variance_ratio_))


# In[ ]:




