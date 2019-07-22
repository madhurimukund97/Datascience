#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")


# In[3]:


req


# In[4]:


dir(req)


# In[5]:


page = req.text
page


# In[6]:


from bs4 import BeautifulSoup


# In[7]:


soup = BeautifulSoup(page, 'html.parser')
soup


# In[8]:


soup.title


# In[9]:


"title" in dir(soup)


# In[10]:


soup.table["class"]


# In[11]:


[t["class"] for t in soup.find_all("table") if t.get("class")]


# In[13]:


table_html = str(soup.find_all("table", "wikitable")[2])


# In[14]:


from IPython.core.display import HTML

HTML(table_html)


# In[15]:


rows = [row for row in soup.find_all("table", "wikitable")[2].find_all("tr")]
rows


# In[16]:


rem_nl = lambda s: s.replace("\n", "")


# In[17]:


def print_siblings(name, *siblings):
    print(name, "has the following siblings:")
    for sibling in siblings:
        print(sibling)
    print()
        
print_siblings("John", "Ashley", "Lauren", "Arthur")
print_siblings("Mike", "John")
print_siblings("Terry")


# In[18]:


columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
columns


# In[19]:


indexes = [rem_nl(row.find("th").get_text()) for row in rows[1:]]
indexes


# In[20]:


HTML(table_html)


# In[21]:


to_num = lambda s: s[-1] == "%" and int(s[:-1]) or None


# In[22]:


values = [to_num(rem_nl(value.get_text())) for row in rows[1:] for value in row.find_all("td")]
values


# In[23]:


stacked_values = zip(*[values[i::3] for i in range(len(columns))])
list(stacked_values)


# In[24]:


import pandas as pd


# In[27]:


stacked_values = zip(*[values[i::3] for i in range(len(columns))])


# In[28]:


df = pd.DataFrame(stacked_values, columns=columns, index=indexes)
df


# In[31]:


columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()] 
stacked_values = zip(*[values[i::3] for i in range(len(columns))])


# In[32]:


data_dicts = [{col: val for col, val in zip(columns, col_values)} for col_values in stacked_values]
data_dicts


# In[33]:


df.dtypes


# In[34]:


df.dropna()


# In[35]:


df.dropna(axis=1)


# In[36]:


df.dropna()


# In[37]:


df_clean = df.fillna(0).astype(int)
df_clean


# In[38]:


df_clean.dtypes


# In[39]:


df_clean.describe()


# In[40]:


import numpy as np


# In[41]:


df_clean.values


# In[42]:


type(df_clean.values)


# In[43]:


np.mean(df_clean.Undergrad)


# In[44]:


np.std(df_clean)


# In[45]:


df_clean["Undergrad"]


# In[46]:


df_clean.Undergrad


# In[48]:


df_clean.loc["Asian/Pacific Islander"]


# In[49]:


df_clean.loc["Asian/Pacific Islander","Graduate"]


# In[50]:


seq_table = df_clean.stack().reset_index()
seq_table.columns = ["race", "source", "percentage"]
seq_table


# In[51]:


grouped_data = seq_table.groupby("race")
grouped_data.groups


# In[52]:


type(grouped_data)


# In[53]:


mean_table = grouped_data.mean()
mean_table


# In[54]:


for name, group in seq_table.groupby("source", sort=True):
  print(name)
  print(group)


# In[55]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[56]:


mean_table.plot(kind="bar")


# In[ ]:




