#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


my_list=[1,2,3]


# In[5]:


np.array(my_list)


# In[6]:


my_mat=[[1,2,3],[4,5,6],[7,8,9]]


# In[7]:


np.array(my_mat)


# In[9]:


np.arange(0,11,2)


# In[10]:


np.zeros(3)


# In[42]:


np.ones((2,3))


# In[16]:


np.linspace(0,5,3)


# In[17]:


np.eye(4)


# In[18]:


np.random.rand(5)


# In[19]:


np.random.rand(4,3)


# In[21]:


np.random.randn(2,2)


# In[23]:


np.random.randint(1,100,10)


# In[24]:


arr=np.arange(25)


# In[25]:


ranarr=np.random.randint(0,50,10)


# In[28]:


arr.reshape(5,5)


# In[30]:


ranarr.max()


# In[31]:


ranarr.min()


# In[32]:


ranarr.argmax()


# In[36]:


arr.shape


# In[35]:


arr=arr.reshape(5,5)


# In[37]:


arr.dtype


# In[2]:


import numpy as np
arr=np.arange(0,11)


# In[4]:


arr[8]


# In[5]:


arr[0:5]


# In[6]:


arr[0:6]=100


# In[7]:


arr


# In[8]:


arr=np.arange(0,11)


# In[9]:


arr


# In[10]:


slice_of_arr=arr[0:6]


# In[11]:


slice_of_arr[:]=99


# In[12]:


slice_of_arr


# In[13]:


arr


# In[14]:


arr_copy=arr.copy()


# In[15]:


arr_copy[:]=100


# In[16]:


arr_copy


# In[17]:


arr


# In[18]:


arr_2d=np.array([[5,10,15],[20,25,30],[35,40,45]])


# In[19]:


arr_2d


# In[20]:


arr_2d[0][0]


# In[21]:


arr_2d[2,1]


# In[22]:


arr_2d[:2,1:]


# In[23]:


arr=np.arange(1,11)


# In[24]:


arr


# In[26]:


bool_arr=arr>5


# In[27]:


arr[bool_arr]


# In[28]:


arr=np.arange(0,11)


# In[29]:


arr+arr


# In[30]:


arr+2


# In[31]:


arr**2


# In[32]:


arr/arr


# In[33]:


arr/0


# In[34]:


inf


# In[35]:


np.sqrt(arr)


# In[36]:


np.exp(arr)


# In[37]:


np.max(arr)


# In[38]:


np.sin(arr)


# In[39]:


np.log(arr)


# In[40]:


arr=np.ones(10)


# In[41]:


arr


# In[44]:


arr*5


# In[47]:


np.arange(10,50,2)


# In[48]:


np.arange(0,9).reshape(3,3)


# In[49]:


np.eye(3)


# In[54]:


np.random.randn(25)


# In[62]:


arr=np.arange(1,101).reshape(10,10)/100


# In[59]:


np.linspace(0,1,20)


# In[69]:


arr.sum(axis=0)


# In[ ]:




