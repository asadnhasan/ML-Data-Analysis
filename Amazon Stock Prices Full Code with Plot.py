#!/usr/bin/env python
# coding: utf-8

# ## This is a tutorial Jupyter Notebook for pulling the stock prices of Amazon(AMZN) via yfinance from 1-JAN-2023 to 18-JUL-2023.
# 
# Also, there is a Scatter and Bar Plot with the Tutorial Youtube Video
# 
# All Rights Reserved with Syed Asad Husain Zaidi

# In[4]:


import yfinance as yf
import datetime

# Set the stock symbol (AMZN for Amazon)
stock_symbol = 'AMZN'

# Set the start and end dates for the historical data
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 7, 18)

# Fetch the historical stock data for Amazon from Yahoo Finance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Print the data
print(stock_data)



# In[8]:


import yfinance as yf
import datetime
import matplotlib.pyplot as plt

# Set the stock symbol (AMZN for Amazon)
stock_symbol = 'AMZN'

# Set the start and end dates for the historical data
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 7, 18)

# Fetch the historical stock data for Amazon from Yahoo Finance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Plot the 'Close' prices over time
plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['Close'], label='Close Price', color='red')
plt.title('Historical Stock Data for Amazon')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()



# In[9]:


get_ipython().run_line_magic('system', 'pwd')


# In[10]:


import os

current_directory = os.getcwd()
print(current_directory)


# In[11]:


import yfinance as yf
import datetime
import matplotlib.pyplot as plt

# Set the stock symbol (AMZN for Amazon)
stock_symbol = 'AMZN'

# Set the start and end dates for the historical data
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 7, 18)

# Fetch the historical stock data for Amazon from Yahoo Finance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Create the bar chart for the 'Close' prices over time
plt.figure(figsize=(10, 6))
plt.bar(stock_data.index, stock_data['Close'], color='blue', alpha=0.7)
plt.title('Historical Stock Data for Amazon')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[13]:


get_ipython().run_cell_magic('HTML', '', '<iframe width="560" height="315" src="https://www.youtube.com/embed/EEEZX_0FMEc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>\n')


# In[ ]:




