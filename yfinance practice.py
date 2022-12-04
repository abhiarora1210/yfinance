#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


get_ipython().system('pip install yfinance')


# In[4]:


import yfinance as yf


# In[6]:


msft = yf.Ticker("MSFT")


# In[7]:


msft.info


# In[8]:


hist = msft.history(period= "max")


# In[9]:


hist


# In[10]:


msft.actions ## dividends, stocksplits


# In[11]:


msft.dividends


# In[12]:


msft.splits


# In[13]:


msft.major_holders


# In[14]:


msft.institutional_holders


# In[15]:


msft.cashflow


# In[16]:


msft.earnings


# In[17]:


msft.sustainability


# In[18]:


msft.recommendations


# In[20]:


msft.recommendations['To Grade'].value_counts()  ## We should Groupby by year to get more accurate answer


# In[22]:


msft.calendar


# In[25]:


msft.isin ##International security identification number


# In[26]:


msft.options


# In[31]:


hist.plot(kind = 'line', figsize = (12,12), subplots = True); ## when used with array columns doesn't show array text


# ## Adavnce Financial data gathering

# In[32]:


# Major finnacial indices


# In[39]:


import requests
import uuid

url = 'https://finance.yahoo.com/world-indices'
cookies = {'euConsentId': str(uuid.uuid4())}

html = requests.get(url, cookies=cookies).content

## If we don't use these above steps it will show error ("Table not found in the next step").


# In[41]:


major_indices = pd.read_html(html)[0]


# In[42]:


major_indices.head()


# In[48]:


ticker_list=major_indices['Symbol'].str.replace("^","").str.lower().to_list()


# In[50]:


len(ticker_list)


# In[68]:


df = yf.download(ticker_list, period="1d",start = "2020-01-01", end = "2022-12-03")


# In[69]:


df.columns


# In[70]:


df.head()


# In[71]:


adj_close = df.dropna(thresh = 10, axis =1)['Adj Close'] ## thresh = 10 means that the column should have atleast 10 non NaN values to not get deleted. axis=1 is used for columns and axis = 0 is used for rows.


# In[72]:


adj_close.head()


# In[73]:


adj_close.describe().T ## We can see that all indices are on different scales, so plotting them together on a single plot won't make sense. Hence, we will be using sub-plots


# In[74]:


adj_close.plot(figsize=(12,12), subplots = True);


# In[77]:


# Will drop XAX due to lack of viable data
adj_close = adj_close.drop("XAX", axis = 1)


# In[78]:


adj_close.plot(figsize=(12,20), subplots = True);


# In[79]:


dji = adj_close['DJI']


# In[82]:


dji.resample('4M').mean()


# In[86]:


dji


# In[87]:


dji.shift(1)


# In[88]:


dji_per_change = dji/(dji.shift(1)-1)


# In[89]:


dji_per_change


# In[90]:


dji_per_change.plot(figsize=(12,12))


# In[92]:


dji_log_returns_shift = np.log(dji / dji.shift(1))


# In[93]:


dji_log_returns_shift.plot(figsize = (12,6))


# In[95]:


dji.hist(bins = 50, figsize = (12,6)) ## Heavily skewed data


# In[96]:


dji_log_returns_shift.hist(bins=50,figsize=(12,6))


# In[97]:


dji_per_change.hist(bins=50, figsize=(12,6))


# In[ ]:




