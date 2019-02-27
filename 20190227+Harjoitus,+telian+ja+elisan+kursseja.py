
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.style.use('seaborn-whitegrid')


# In[2]:


elisa=pd.read_csv('http://taanila.fi/elisa.csv',sep=';',decimal=',')
elisa.head()


# In[3]:


telia=pd.read_csv('http://taanila.fi/telia.csv',sep=';',decimal=',')
elisa.head()


# In[4]:


elisa.index=pd.to_datetime(elisa['Date'],dayfirst=True)
#to datetime on pandaksen komento missä tunnistetaan päivämäärädataa
elisa.head()


# In[5]:


telia.index=pd.to_datetime(telia['Date'],dayfirst=True)
#to datetime on pandaksen komento missä tunnistetaan päivämäärädataa
telia.head()


# In[6]:


elisa.sort_index(inplace=True)
# sorttaus sorttaa ja inplace tallentaa
elisa.head()


# In[7]:


elisa['Closing price'].plot()
#plottaus on grafiikkakomento, plotin oletus on _käppyrä_


# In[8]:


telia['Closing price'].plot()


# In[9]:


elisa['Closing price']['2019-01'].plot()


# In[10]:


telia['Closing price']['2019-02'].plot()


# In[11]:


figl,ax1=plt.subplots(figsize=(10,6))
color='C0'
ax1.set_ylabel('Elisa',color=color)
ax1.plot(elisa['Closing price'],color=color)

# tehdään toinen ax olio
# tehdään se aikaisemman perusteella

ax2=ax1.twinx()
color='C1'
ax2.set_ylabel('Telia', color=color)
ax2.plot(telia['Closing price'],color=color)


# In[12]:


elisa['Closing price'].plot()
#liukuva keskiarvo edellisiltä sadalta päivältä
elisa['Closing price'].rolling(100).mean().plot()


# In[13]:


elisa['Elisa_change']=elisa['Closing price'].pct_change()
# lasketaan prosentuaalinen muutos
elisa.head()


# In[14]:


telia['Telia_change']=telia['Closing price'].pct_change()
# lasketaan prosentuaalinen muutos
telia.head()


# In[15]:


muutokset=pd.concat([elisa['Elisa_change'],telia['Telia_change']],axis=1)
# concat yhdistää eri aineistoja, 
# axis=0 aineistot päällekkäin, axis=1 aineistot vierekkäin 
# pandas btw osaa yhistää ite samat päivämäärät yhteen eli kolot ei haittaa
muutokset.head()


# In[16]:


ax3=muutokset['2019-01':].plot()
# huom jos haluu kaikki ni ei tarvii eritellä, oiskohan 'pvm': et siitä eteenpäi?
ax3.set_ylabel('Muutos')
vals=ax3.get_yticks()
ax3.set_yticklabels(['{:.0f} %'.format(y*100) for y in vals])
# laitetaan akselit ja yksiköt kuntoon


# In[17]:


muutokset.describe()


# In[18]:


muutokset[(muutokset['ELisa_change']<-0.05)|(muutokset['Elisa_change']>0.05)]


# In[ ]:


muutokset.corr()


# In[19]:


korrelaatio=muutokset['Elisa_change'].rolling(100,
                                            min_periods=30).corr(muutokset['Telia_change'])
korrelaatio.plot()


# In[22]:


(muutokset['Elisa_change'].rolling(252).std()*(252**0.5)).plot()


# In[23]:


muutokset['Weekday']=muutokset.index.weekday
muutokset.head()
# huom 0=maanantai 1=tiistai


# In[24]:


muutokset.groupby('Weekday')['Elisa_change'].describe()


# In[25]:


muutokset.groupby('Weekday')['Telia_change'].describe()

