#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Geographical Plotting is usually challenging to  due the various formats 
#the data can come in.


# In[10]:


#Choropleth maps
import plotly as py


# In[18]:



from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import plotly.graph_objs as go


# In[12]:


#conda install chart-studio


# In[14]:


init_notebook_mode(connected=True)


# In[15]:


data=dict(type='choropleth',locations=['AZ','CA','NY'],locationmode='USA-states',colorscale='Portland',text=['text 1','text 2','text 3'],z=[1.0,2.0,3.0],colorbar={'title':'Colorbar Title Goes Here'})


# In[16]:


data


# In[19]:


layout=dict(geo={'scope':'usa'})


# In[21]:


choromap=go.Figure(data=[data],layout=layout)


# In[22]:


iplot(choromap)


# In[24]:


import pandas as pd
df=pd.read_csv('2011_US_AGRI_Exports.csv')


# In[25]:


df


# In[34]:


data=dict(type='choropleth',
          colorscale='ylorbr',
         locations=df['code'],
         locationmode='USA-states',
          z=df['total exports'],
         text=df['text'],
          marker=dict(line=dict(color='rgb(255,255,255)',width=2)),
         colorbar={'title':'Millions USD'})#ylorbr


# In[35]:


layout=dict(title='2011 US Agriculture Exports by State',
            geo=dict(scope='usa',showlakes=True,lakecolor='rgb(85,173,240)'))


# In[36]:


choromap2=go.Figure(data=[data],layout=layout)


# In[37]:


iplot(choromap2)


# In[38]:


df=pd.read_csv('2014_World_GDP.csv')


# In[40]:


data=dict(type='choropleth',
         locations=df['CODE'],
          z=df['GDP (BILLIONS)'],
         text=df['COUNTRY'],
         colorbar={'title':'GDP in Billions USD'})


# In[44]:


layout=dict(title='2014 Global GDP',
            geo=dict(showframe=False,projection={'type':'mercator'}))


# In[45]:


cm3=go.Figure(data=[data],layout=layout)


# In[46]:


iplot(cm3)


# In[ ]:




