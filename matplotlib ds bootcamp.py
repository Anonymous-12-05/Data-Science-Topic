#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Matplotlib is the most popular plotting library for python
#It gives you control over every aspect of a figure
#It was designed to have a similar feel to Matlab's graphical plotting


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import numpy as np
x=np.linspace(0,5,11)
y=x**2


# In[9]:


x


# In[10]:


y


# In[18]:


#Functional 
plt.plot(x,y)
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("Title")
plt.show()


# In[19]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[20]:


#Object oriented method


# In[25]:


fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel("X label")
axes.set_ylabel("Y label")
axes.set_title("title")


# In[28]:


fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes2.plot(y,x)


# In[7]:


fig,axes=plt.subplots(nrows=1,ncols=2)
#axes.plot(x,y)
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()


# In[8]:


#Figure Size and DPI


# In[12]:


fig=plt.figure(figsize=(8,2))
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[13]:


fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)


# In[14]:


fig.savefig('my_pic.png')


# In[16]:


fig=plt.figure(figsize=(8,2))
ax=fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label="Square")
ax.plot(x,x**3,label="Cube")
ax.legend(loc=0)


# In[17]:


#Plot appearance


# In[33]:


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y,color='orange',linewidth=3,linestyle='-')
ax.set_xlim([0,1])
ax.set_ylim([0,2])


# In[ ]:




