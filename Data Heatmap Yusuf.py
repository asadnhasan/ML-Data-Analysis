#!/usr/bin/env python
# coding: utf-8

# Heat Map Demo for Yusuf 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


# Read data from the CSV file
data = pd.read_csv(r"C:\Users\Syed Asad\OneDrive\Desktop\Python Files\Data Analysis\Yusufmeeting.csv")


# In[13]:


print("Data from CSV:")
print(data.to_string(index=False))


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from the CSV file with the first row as header
data = pd.read_csv(r"C:\Users\Syed Asad\OneDrive\Desktop\Python Files\Data Analysis\Yusufmeeting.csv", header=0)

# Print the data read from the CSV file without index numbers
print("Data from CSV:")
print(data.to_string(index=False))

# Set 'Meeting_Type' column as the index
data.set_index('Meeting_Type', inplace=True)

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data, annot=True, cmap='Reds', fmt='d', linewidths=0.5)
plt.xlabel('Months')
plt.ylabel('Meeting Type')
plt.title('Frequency of Meetings Across Months')
plt.show()


# In[16]:


# Save the heatmap as a PNG image
plt.savefig('heatmap_meetings.png', bbox_inches='tight', dpi=300)


# In[ ]:




