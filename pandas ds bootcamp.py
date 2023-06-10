#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Pandas is an open source library built on top of NumPy
It allows for fast analysis and data cleaning and preparation
It excels in performance and productivity
It also has built in visualisation features
It can also work with data from a variety of sources.
'''


# In[2]:


import pandas


# In[3]:


'''Series'''


# In[4]:


import numpy as np
import pandas as pd


# In[5]:


labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}


# In[6]:


pd.Series(data=my_data)


# In[7]:


pd.Series(data=my_data,index=labels)


# In[8]:


pd.Series(arr)


# In[9]:


pd.Series(d)


# In[10]:


pd.Series(data=[sum,print,int])


# In[11]:


ser1=pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])


# In[12]:


ser1


# In[22]:


ser2=pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])


# In[23]:


ser2


# In[15]:


ser1['USA']


# In[17]:


ser1[0]


# In[18]:


ser3=pd.Series(data=labels)


# In[20]:


ser3


# In[24]:


ser1+ser2


# In[25]:


#dataframes


# In[26]:


from numpy.random import randn


# In[28]:


np.random.seed(101)


# In[29]:


df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[30]:


df
#w,x,y,z is a series


# In[32]:


df['W']


# In[33]:


type(df['W'])


# In[34]:


df.W


# In[35]:


df[['W','Z']]


# In[36]:


df['new']=df['W']+df['Y']


# In[37]:


df


# In[39]:


df.drop('new',axis=1)


# In[40]:


df


# In[41]:


df.drop('new',axis=1,inplace=True)


# In[42]:


df


# In[43]:


df.drop('E',axis=0)


# In[45]:


df.shape


# In[46]:


#ROWS


# In[47]:


df.loc['A']


# In[48]:


df.iloc[0]


# In[49]:


df.loc['B','Y']


# In[50]:


df.loc[['A','B'],['W','Y']]


# In[51]:


# Dataframes Part 2 


# In[53]:


booldf=df>0


# In[54]:


booldf


# In[55]:


df[booldf]


# In[56]:


df[df>0]


# In[57]:


df


# In[58]:


df['W']>0


# In[62]:


resultdf=df[df['W']>0]


# In[60]:


df[df['Z']<0]


# In[63]:


resultdf['X']


# In[64]:


df[df['W']>0]['X']


# In[65]:


df[(df['W']>0) and (df['Y']>1)]


# In[68]:


df[(df['W']>0) & (df['Y']>1)]


# In[69]:


df


# In[72]:


df.reset_index()


# In[73]:


newind='CA NY WY OR CO'.split()


# In[74]:


newind


# In[75]:


df['States']=newind


# In[76]:


df


# In[77]:


df.set_index('States')


# In[78]:


#dataframes part 3


# In[82]:


#index levels
outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)


# In[85]:


df=pd.DataFrame(randn(6,2),hier_index,['A','B'])


# In[86]:


df


# In[87]:


df.loc['G1']


# In[88]:


df.loc['G1'].loc[1]


# In[90]:


df.index.names=['Groups','Num']


# In[91]:


df


# In[92]:


df.shape


# In[93]:


df.loc['G2']


# In[94]:


df.loc['G2'].loc[2]['B']


# In[98]:


df.xs(1,level='Num')


# In[99]:


#Missing Data


# In[100]:


d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}


# In[101]:


df=pd.DataFrame(d)


# In[102]:


df


# In[104]:


df.dropna(axis=1)


# In[105]:


df.dropna()


# In[106]:


df.dropna(thresh=2) #HAs atleast 2 non null values


# In[107]:


df.fillna(value="FILL")


# In[109]:


df['A'].fillna(df['A'].mean())


# In[110]:


#Groupby


# In[111]:


data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
      'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
      'Sales':[200,120,340,124,243,350]}


# In[112]:


df=pd.DataFrame(data)


# In[113]:


df


# In[115]:


bycomp=df.groupby('Company')


# In[116]:


bycomp.mean()


# In[118]:


bycomp.count()


# In[119]:


df.groupby('Company').describe()


# In[120]:


df.groupby('Company').describe().transpose()


# In[121]:


#merging concatenation,joining
#pd.concat([df1,df2,df3])


# In[122]:


#pd.concat([df1,df2,df3],axis=1)
#pd.merge(leftdf,rightdf,how="inner",on="keyseries")

#leftdf.join(rightdf)
#leftdf.join(rightdf,how='outer')


# In[123]:


#operations


# In[125]:


#df['A'].unique()
#df['col2'].value_counts()
#df['col1'].apply(user_defined_function)
#df.sort_values(by='col2')
#df.isnull()
#df.pivot_table(values='D',index=['A,'B],coloumns=['C '])


# In[126]:


#Data input nd output


# In[127]:


pwd


# In[130]:


#df=pd.read_csv('example.csv')
df.to_csv('My_output',index=False)


# In[133]:


df=pd.read_csv('My_output')


# In[134]:


df


# In[138]:


pd.read_excel('Excel_sample2.xlsx')
#df.to_excel('Excel_Sample2.xlsx',sheet_name='Newsheet')


# In[139]:


#data=pd.read_html('Html Link')
from sqlalchemy import create_engine


# In[140]:


engine=create_engine('sqlite:///:memory:')


# In[141]:


df.to_sql('my_table',engine)


# In[142]:


sqldf=pd.read_sql('my_table',con=engine)


# In[143]:


sqldf


# In[ ]:




