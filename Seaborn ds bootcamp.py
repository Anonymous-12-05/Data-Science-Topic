#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Seaborn is a statistical plotting library
#It has beautiful default syles
#It is designed to work verl well with pandas dataframe objects


# In[39]:


import seaborn as sns
import matplotlib as plt


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


tips=sns.load_dataset('tips')


# In[6]:


tips.head()


# In[14]:


sns.distplot(tips['total_bill'])


# In[19]:


sns.jointplot(x='total_bill',y='tip',data=tips)


# In[22]:


sns.pairplot(tips,hue="sex",palette='coolwarm')


# In[23]:


sns.rugplot(tips["total_bill"])


# In[27]:


sns.distplot(tips['total_bill'])


# In[25]:


#Categorical data


# In[32]:


import numpy as np


# In[33]:


sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# In[34]:


sns.countplot(x='sex',data=tips)


# In[37]:


sns.boxplot(x="day",y='total_bill',data=tips)


# In[39]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)


# In[43]:


sns.stripplot(x="day",y="total_bill",data=tips,jitter=True,hue="sex",split=True)


# In[45]:


sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x="day",y="total_bill",data=tips,color="black")


# In[46]:


sns.factorplot(x="day",y="total_bill",data=tips,kind='bar')


# In[47]:


#Matrix plots


# In[48]:


flights=sns.load_dataset('flights')


# In[49]:


tips.head()


# In[50]:


flights.head()


# In[54]:


tc= tips.corr()
tc


# In[57]:


sns.heatmap(tc,annot=True,cmap='coolwarm')


# In[60]:


fp=flights.pivot_table(index="month",columns="year",values="passengers")


# In[63]:


sns.heatmap(fp,cmap='magma',linecolor="white",linewidth=1)


# In[65]:


sns.clustermap(fp,cmap="coolwarm",standard_scale=1)


# In[1]:


#Grid


# In[4]:


iris=sns.load_dataset('iris')
iris.head()


# In[6]:


iris['species'].unique()


# In[8]:


sns.pairplot(iris)


# In[20]:


g=sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(sns.stripplot)
g.map_lower(sns.kdeplot)


# In[23]:


tips=sns.load_dataset('tips')
tips.head()


# In[28]:


g=sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.distplot,'total_bill')


# In[26]:


#Regression Plots


# In[32]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')


# In[33]:


#Style and color


# In[44]:


#plt.figure(figsize=(12,3))
#sns.set_style('ticks')
sns.set_context('poster')
sns.countplot(x='sex',data=tips)
#sns.despine()


# In[ ]:





# In[ ]:




