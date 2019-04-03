
# coding: utf-8

# In[4]:


import pandas as pd
import scipy.stats as stats
df=pd.read_excel('http://taanila.fi/data1.xlsx', sheetname='Data')
df.head()


# In[5]:


# ikä ja palkka, onko merkitsevää riippuvuutta?
stats.pearsonr(df['ikä'], df['palkka'])


# In[7]:


stats.spearmanr(df['ikä'], df['palkka'])


# In[8]:


# entä onko riippuvuutta sp ja perhesude?
stats.chi2_contingency(pd.crosstab(df['sukup'], df['perhe']))


# In[9]:


'eli sp ja perheen välillä on riippuvuutta p=0,047'


# In[10]:


# no entä m/f palkkaero? suodatetaan miesten ja naisten palkat erikseen
a=df['palkka'][df['sukup']==1] # mieheet
b=df['palkka'][df['sukup']==2] # naisten
print(a.mean())
print(b.mean())
stats.ttest_ind(a, b, equal_var=False)


# In[11]:


a=df['palkka'][df['sukup']==1] # mieheet
b=df['palkka'][df['sukup']==2] # naisten
print(a.median())
print(b.median())
stats.ttest_ind(a, b, equal_var=False)


# In[13]:


#Miesten ja naisten palkka ka on ero (2-suuntainen p=0,003)


# In[15]:


stats.mannwhitneyu(a,b)

