
# coding: utf-8

# In[31]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[32]:


# read the excel file into a pandas DataFrame
df = pd.read_excel('datasets/4-43.xlsx', 'Sheet1')
df


# In[33]:


# set the DataFrame to be indexed by the year
df.set_index('year', inplace=True)
df


# In[41]:


# plot the time series and moving average with window size '3'
win_size = 3
df.sales.plot(label='time series')
df.sales.rolling(win_size).mean().plot(label='moving average')
plt.legend()


# In[46]:


# plot time series and exponentially weighted moving average 
alpha = 0.2 # smoothing parameter
c = 1/alpha-1
df.sales.plot(label='time series')
df.sales.ewm(com=c).mean().plot(label='ewma')
plt.legend()

