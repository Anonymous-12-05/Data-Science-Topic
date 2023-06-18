#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Plotly is an interactive visualisation library
#Cufflinks connects plotply with pandas
#Cufflinks connects plotly to python


# In[2]:


import pandas as pd
import numpy as np
from plotly import __version__


# In[4]:


conda install plotly


# In[7]:


conda install cufflinks


# In[1]:


import cufflinks


# In[3]:


print(__version__)


# In[6]:


import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[7]:


init_notebook_mode(connected=True)


# In[8]:


cf.go_offline()


# In[9]:


#Data
df=pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())


# In[10]:


df.head()


# In[11]:


df2=pd.DataFrame({'Category':['A','B',"C"],'Values':[32,43,50]})


# In[12]:


df2


# In[15]:


df.iplot()


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


df.iplot(kind="scatter",x='A',y='B',mode='markers')


# In[19]:


df2.iplot(kind='bar',x='Category',y='Values')


# In[20]:


df.sum().iplot(kind='bar')


# In[21]:


df.iplot(kind='box')


# In[22]:


df3=pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[500,400,300,200,100]})


# In[23]:


df3


# In[24]:


df3.iplot(kind='surface')


# In[25]:


df[['A','B']].iplot(kind='spread')


# In[26]:


df.iplot(kind='bubble',x='A',y='B',size='C')


# In[27]:


df.scatter_matrix()


# In[ ]:




