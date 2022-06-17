#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('cars_data.csv')
data.head()


# # TO FIND NULL VALUES

# In[3]:


data.isnull()


# # FINDIND COUNT OF MALE AND FEMALE CONTINUING WITH BAR GRAPH

# In[4]:


data['Buyer Gender'].value_counts()


# In[5]:


plotdata = pd.DataFrame({
    "Female":[5052],
    "Male":[4948]
    }, 
    index=["Female-Male"]
)
plotdata.plot(kind="bar")
plt.title("Sales")
plt.xlabel("Gender")
plt.ylabel("Count")


# # TOP 5 CARS BASED ON SALE PRICE

# In[6]:


data.nlargest(5, ['Sale Price'])


# # LEAST 5 CARS BASED ON RESELL PRICE

# In[7]:


data.nsmallest(5, ['Resell Price'])


# In[ ]:




