#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/tejas/Downloads/age_gender_dataset.csv")

plt.hist(df["Age"])
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/tejas/Downloads/age_gender_dataset.csv")

gender_counts = df["Gender"].value_counts()

plt.bar(gender_counts.index, gender_counts.values)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution")
plt.show()


# In[ ]:




