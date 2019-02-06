
# coding: utf-8

# In[1]:


# tuodaan kirjastot
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[3]:


# luodaan omaa dataa
raw_data = {'Alue':['Helsinki', 'Turku', 'Tampere', 'Oulu'],
            'Myynti':[13221847,852669,10322199,568230]}
# luodaan oma dataframe
myynnit = pd.DataFrame(raw_data)
myynnit


# In[5]:


myynnit.index=myynnit['Alue']
myynnit


# In[6]:


# plotataan data, sulkuihin voi laittaa lisäparamentrejä halutessaan
myynnit.plot.barh()
# huom asteikko automaattisesti meni tässä 10^7 


# In[7]:


# mitä taulukkotyylejä käytössä?
plt.style.available


# In[9]:


# valitaan ggplot ja katsotaan
plt.style.use('ggplot')
myynnit.plot.barh()


# In[11]:


# luodaan ax-olio ja sortataan arvot, ei tarvita legediä
ax = myynnit.sort_values(by='Myynti').plot.barh(title='Myynti vuonna 2017',
                                               legend=False)
# nimetään nyt ax:n x-akseli ja jätetään y tyhjäksi
ax.set(xlabel='Miljoonaa euroa',ylabel='')
# korjataan mittakaava eli tics kuntoon
# huom vals on vain muuttjan nimi ei muuta, haetaan ticksit
vals=ax.get_xticks()
# kerrotaan kuinka monta desimaaia. huom sulkuhäkkyrät, x/10^6 = myyntiluvut/miljoonalla koska niin me otsikoitiin
ax.set_xticklabels(['{:.1f}'.format(x/1000000) for x in vals])


# In[12]:


# summataan myynnit ja lasketaan prosentuaalinen myynti
myynnityht = myynnit['Myynti'].sum()
myynnit['%']=myynnit['Myynti']/myynnityht*100
myynnit


# In[18]:


# luodaan ax olio, järjestetään ne prosenttien mukaan, luodaan taulukko ja otsikoidaan se
ax= myynnit.sort_values(by='%')['%'].plot.barh(title='Osuus kokonaismyynnistä vuonna 2017', legend=False, width=0.4, color='C0')
# huom width viittaa pylvään suhteelliseen paksuuteen


# In[19]:


# nimetään akselit, huom sulkihirviö taas :D
ax.set(xlabel='%', ylabel='')
vals = ax.get_xticks()
ax.set_xticklabels(['{:.0f} %'.format(x) for x in vals])
# huom ei printannu kuvioo joten sun pitää laittaa se edellien kuvion luonti ennen näit samaan koodiin :D uusi yritys


# In[22]:


# uudestaan :D 
ax= myynnit.sort_values(by='%')['%'].plot.barh(title='Osuus kokonaismyynnistä vuonna 2017', legend=False, width=0.4, color='C0')
ax.set(xlabel='%', ylabel='')
vals = ax.get_xticks()
ax.set_xticklabels(['{:.0f} %'.format(x) for x in vals])
# sit get current figure ja tallennetaan kuvio, voit valii formaatin, tallentaa samaan kansioon missä koodikin
plt.gcf().savefig('pythonin-kuva.png')


# In[ ]:


# mitäs nyt?

