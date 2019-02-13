
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')

#valitaan gg plot tyyli

plt.style.use('ggplot')


# In[2]:


#ladataan valmmis titanic-aineisto kirjoastosta load komennolla
titanic=sns.load_dataset('titanic')
titanic.head()


# In[3]:


# tehdään suoraan kuvio datast count plot komennolla
ax=sns.countplot(x='class',data=titanic, color='C0')
# määritellään y axkselin otsikko
ax.set_ylabel('lukumäärä')


# In[5]:


# mikäs on hue paramentri?
ax=sns.countplot(x='class', hue='who', data=titanic)


# In[6]:


sns.countplot(y='class', hue='who', data=titanic)


# In[13]:


# factor plot?? col = kolumni
sns.factorplot(x='class',hue='who', data=titanic, col='survived', kind='count')


# In[14]:


sns.barplot(x='class', y='survived', hue='sex', data=titanic)


# In[16]:


tips=sns.load_dataset('tips')
tips.head()


# In[17]:


sns.countplot(x='day',hue='sex',data=tips)


# In[18]:


sns.barplot(x='day', y='tip',hue='sex', data=tips)


# In[21]:


tips['tip%']=tips['tip']/(tips['total_bill']-tips['tip'])
sns.barplot(x='day',y='tip%', data=tips)


# In[22]:


df=pd.read_excel('http://taanila.fi/data1.xlsx', sheetname='Data')
df.head()


# In[27]:


# voi luoda ax olion seabornil
ax=sns.barplot(data=df, orient='h', color='C0',
           order=['työtov', 'työteht', 'työymp', 'johto', 'palkkat'])
ax.set_xlim(1,5)
ax.set_title('Tyytyväisyyskeskiarvoja')
ax.set_xlabel('1=Erittäin tyytymätön, 5=Erittäin tyytyväinen')

