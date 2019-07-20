#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns


# In[5]:


df=pd.read_csv("all.csv", header=None,
               names=["rating", 'review_count', 'isbn', 'booktype','author_url', 'year', 'genre_urls', 'dir','rating_count', 'name'],
)
df.head()


# In[6]:


df.dtypes


# In[7]:


df.shape


# In[8]:


df.shape[0], df.shape[1]


# In[9]:


df.columns


# In[10]:


type(df.rating), type(df)


# In[11]:


df.rating < 3


# In[12]:


np.sum(df.rating < 3)


# In[14]:


print(1*True, 1*False)


# In[15]:


np.sum(df.rating < 3)/df.shape[0]


# In[16]:


np.sum(df.rating < 3)/float(df.shape[0])


# In[17]:


np.mean(df.rating < 3.0)


# In[18]:


(df.rating < 3).mean()


# In[19]:


df.query("rating > 4.5")


# In[20]:


df[df.year < 0]


# In[21]:


df[(df.year < 0) & (df.rating > 4)]


# In[22]:


df.dtypes


# In[23]:


df['rating_count']=df.rating_count.astype(int)
df['review_count']=df.review_count.astype(int)
df['year']=df.year.astype(int)


# In[24]:


df[df.year.isnull()]


# In[25]:


df = df[df.year.notnull()]
df.shape


# In[26]:


df['rating_count']=df.rating_count.astype(int)
df['review_count']=df.review_count.astype(int)
df['year']=df.year.astype(int)


# In[27]:


df.dtypes


# In[28]:


df.rating.hist();


# In[31]:


sns.set_context("notebook")
meanrat=df.rating.mean()
print(meanrat, np.mean(df.rating), df.rating.median())
with sns.axes_style("whitegrid"):
    df.rating.hist(bins=30, alpha=0.4);
    plt.axvline(meanrat, 0, 0.75, color='r', label='Mean')
    plt.xlabel("average rating of book")
    plt.ylabel("Counts")
    plt.title("Ratings Histogram")
    plt.legend()


# In[32]:


df.review_count.hist(bins=np.arange(0, 40000, 400))


# In[33]:


df.review_count.hist(bins=100)
plt.xscale("log");


# In[34]:


plt.scatter(df.year, df.rating, lw=0, alpha=.08)
plt.xlim([1900,2010])
plt.xlabel("Year")
plt.ylabel("Rating")


# In[35]:


alist=[1,2,3,4,5]


# In[36]:


asquaredlist=[i*i for i in alist]
asquaredlist


# In[37]:


plt.scatter(alist, asquaredlist);


# In[39]:


print(type(alist))


# In[40]:


plt.hist(df.rating_count.values, bins=100, alpha=0.5);


# In[42]:


print(type(df.rating_count), type(df.rating_count.values))


# In[43]:


alist + alist


# In[44]:


np.array(alist)


# In[45]:


np.array(alist)+np.array(alist)


# In[46]:


np.array(alist)**2


# In[47]:


newlist=[]
for item in alist:
    newlist.append(item+item)
newlist


# In[48]:


a=np.array([1,2,3,4,5])
print(type(a))
b=np.array([1,2,3,4,5])

print(a*b)


# In[49]:


a+1


# In[ ]:




