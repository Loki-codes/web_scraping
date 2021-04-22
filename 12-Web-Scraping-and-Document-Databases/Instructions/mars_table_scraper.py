#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[41]:


def scrape_table():
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
#     pull data into a pd table
    df1 = tables[0]
#     drop headers and unneeded columns
    df1 = df1.drop(2, axis=1)
    df1 = df1.drop(0, axis=0)
    df1 = df1.rename(columns={0: "titles", 1: "Data"})
#     send table html out to a file. 
    df1.to_html('./mars_table.html',header=True, index=False)
 


# In[ ]:





# In[ ]:




