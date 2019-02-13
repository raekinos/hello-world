
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[6]:


df = pd.read_excel('http://taanila.fi/data1.xlsx', sheetname='Data')
df.head()


# In[7]:


koulutus=['Peruskoulu', '2.aste', 'Korkeakoulu', 'Ylempi korkeakoulu']
perhe=['Perheetön', 'Perheellinen']
sukup=['Mies', 'Nainen']


# In[8]:


#lasketaan tunnuslukuja
df.describe()


# In[9]:


#jos haluaa valita muuttujat
df[['ikä', 'palveluv', 'palkka']].describe()


# In[14]:


df[['ikä', 'palveluv', 'palkka']].describe().style.format('{:.2f}')


# In[16]:


df1=df.pivot_table(values='palkka', index=['sukup', 'perhe'], columns='koulutus')
df1.style.format('{:.0f}')


# In[17]:


#muokataan indeksiä, eli se hakee ne oikeet nimet.. selvitä mikä tää levels meinaa oikeest
#huom style format ei tallennu
df1.index=df1.index.set_levels(sukup, level=0)
df1.style.format('{:.0f}')


# In[19]:


# mikä on hierarkinen indeksi?
df1.index=df1.index.set_levels(perhe, level=1)
df1.columns=koulutus
# miks toi on tollee?
df1.style.format('{:.0f}')


# In[21]:


df2=df.pivot_table(values='palkka', index='koulutus',
                  aggfunc=[np.min,np.median,np.mean,np.max])
df2.index=koulutus
df2.columns=['pienin','mediaani','keskiarvo','suurin']
df2.style.format('{:.0f}')


# In[25]:


#boxplotti, eli ppirtää describen kaavioon
ax=df.boxplot('palkka',by='koulutus')
#sivotaan otsikot pois
plt.title('')
plt.suptitle('')
#miksi suptitle??
plt.xlabel('Koulutus')
plt.ylabel('Palkka')
ax.set_xticklabels(koulutus)


# In[26]:


df[['ikä','palveluv', 'palkka']].corr()


# In[32]:


#korrelaatio koko data
df[['sukup', 'ikä', 'perhe', 'koulutus', 'palveluv', 'palkka', 'työtov', 'työymp', 'palkkat', 'työteht']].corr().style.format('{:.2f}')


# In[30]:


df.plot.scatter('ikä', 'palkka')

