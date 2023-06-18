#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Pandas for data visualisation


# In[9]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df1=pd.read_csv('df1.csv',index_col=0)


# In[5]:


df1.head()


# In[6]:


df2=pd.read_csv('df2.csv')


# In[7]:


df2.head()


# In[10]:


df1['A'].hist()


# In[12]:


df1['A'].plot(kind='hist')


# In[14]:


df2.plot.area()


# In[16]:


df2.plot.bar(stacked=True)


# In[17]:


df1['A'].hist(bins=50)


# In[22]:


df1.plot.line(x='A',y='B',figsize=(12,3))


# In[23]:


df1.plot.scatter(x='A',y='B')


# In[24]:


df=pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])


# In[26]:


df.plot.hexbin(x='a',y='b',gridsize=25)


# In[ ]:




