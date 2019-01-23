
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_excel('http://taanila.fi/data1.xlsx', sheetname='Data')
df.head()


# In[3]:


df.tail(10)


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.columns=['nro', 'sukupuoli', 'ikä', 'perhe', 'koulutus', 'palveluv', 'palkka',
       'johto', 'työtov', 'työymp', 'palkkat', 'työteht', 'työterv', 'lomaosa',
       'kuntosa', 'hieroja']


# In[7]:


df.columns


# In[8]:


df.rename(columns={'sukupuoli':'sukup','työtov':'toveri'}, inplace=True)


# In[9]:


df.columns


# In[10]:


df.count()


# In[11]:


for var in df:
    print(var, pd.unique(df[var]))


# In[12]:


df['sukup_teksti']=df['sukup'].replace({1:'Mies', 2: 'Nainen'})
df.head(6)


# In[13]:


#bins=[18,28,38,48,58,68]
#df['ikäluokka'] = pd.cut(df['ikä'], bins=bins)
#df.head()


# In[14]:


df['tyytyväisyys'] = df[['johto', 'toveri', 'työymp', 'palkkat', 'työteht']].mean(axis=1)
df.head(6)


# In[15]:


df['käyttö'] = df[['työterv', 'lomaosa', 'kuntosa', 'hieroja']].sum(axis=1)
df.head()


# In[16]:


df[4:6]


# In[17]:


df[df['palkka']>4000]


# In[18]:


df[(df['sukup']==2) & (df['palkkat']<3)]


# In[19]:


df[(df['työterv'].notnull())&(df['lomaosa'].notnull())]


# In[20]:


df[['tyytyväisyys', 'käyttö']][df['käyttö']>=3]


# In[21]:


df[['palkka','palkkat']].sort_values(by='palkka', ascending=False).head()


# In[22]:


df.drop(['nro', 'ikä', 'palveluv', 'palkka'], axis=1).head()


# In[23]:


writer=pd.ExcelWriter('valmisteltu.xlsx', engine='xlsxwriter')
df.to_excel(writer)
writer.save()

