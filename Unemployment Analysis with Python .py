#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import get
from warnings import warn
from time import sleep
from random import randint
import numpy as np, pandas as pd
import seaborn as sns
import re
from matplotlib import pyplot as plt
from warnings import filterwarnings


# In[2]:


df= pd.read_csv(r"C:\Users\Darasandhya\OneDrive\Desktop\intershiponline\Unemployment_Rate_upto_11_2020.csv")


# In[3]:


df.head()


# In[6]:


df.isnull().sum()


# In[12]:


df= pd.read_csv(r"C:\Users\Darasandhya\OneDrive\Desktop\intershiponline\Unemployment_Rate_upto_11_2020.csv",skiprows=0)
df.info()


# In[16]:


df.head()


# In[29]:


df.isnull()


# In[30]:


df.groupby('Region')[' Estimated Unemployment Rate (%)'].agg({'min','max','mean','median'})


# In[32]:


sns.boxplot(df[' Estimated Unemployment Rate (%)'],df['Region'])


# In[33]:


sns.violinplot(df[' Estimated Unemployment Rate (%)'],df['Region'])


# In[37]:


pd.crosstab(df[' Estimated Unemployment Rate (%)'],df['Region']).sum().plot.bar()


# In[38]:


sns.scatterplot(data=df,y=' Estimated Unemployment Rate (%)',x='Region',color='red')
plt.xticks(rotation =90)
plt.show()


# In[39]:


df[' Estimated Unemployment Rate (%)'].plot(kind='hist', bins=10)


# In[40]:


sns.distplot(df[' Estimated Unemployment Rate (%)']);


# In[42]:


sns.countplot(df[' Estimated Unemployment Rate (%)']);


# In[44]:


sns.jointplot(data = df, x=' Estimated Unemployment Rate (%)',y='Region')


# In[45]:


sns.barplot(df[' Estimated Unemployment Rate (%)'],df['Region']);


# In[46]:


df.groupby(['Region']).sum().plot(kind='pie', y=' Estimated Unemployment Rate (%)')


# In[ ]:





# In[ ]:





# In[ ]:




