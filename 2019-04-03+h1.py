
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')
sns.set()


# In[3]:


iris=sns.load_dataset('iris')
iris.head()


# In[4]:


X=iris.drop('species', axis=1)


# In[5]:


from sklearn.cluster import KMeans
malli = KMeans(n_clusters=3)
malli.fit(X)


# In[6]:


malli.cluster_centers_


# In[16]:


pd.crosstab(X['K'], 'lkm')


# In[18]:


X.groupby('K').describe().T


# In[19]:


X.groupby('K').describe().T


# In[20]:


sns.pairplot(X, hue='K')


# In[21]:


pd.crosstab(X['K'], iris['species'])

