
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib
from  matplotlib import pyplot as plt
import scipy.stats.stats as sss
get_ipython().magic(u'matplotlib inline')
import pystan
from __future__ import division


# In[2]:

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 30)


# In[3]:

bfas= pd.read_csv('./Master_preprocessed_BFAS.csv')
opg = pd.read_csv('./Master_preprocessed_BFASOPG.csv')
demo = pd.read_csv('./WorkerID_Gender_Age_pairing_BFAS_II.csv')
bfas = bfas.convert_objects(convert_numeric=True) 
opg = opg.convert_objects(convert_numeric=True)


# In[4]:

bfas.head()


# In[5]:

opg.head()


# In[6]:

################################################
demo = demo[['workerid','age','engagement']]



# In[7]:

##################################################

#Join Age, Gender by workerid

opg = pd.merge(opg,demo,how='outer',)


# In[8]:

####################################

bfas = pd.merge(bfas,demo,how='outer',)


# In[ ]:




# In[9]:

correct_order_opg = ['workerid','age','engagement',
 'PBR_1+',
 'PBR_2-',
 'PBR_3+',
 'PBR_4+',
 'PBR_5+',
 'PBR_6-',
 'PBR_7-',
 'PBR_8-',
 'OPG_9+',
 'OPG_10+',
 'OPG_11-',
 'OPG_12+',
 'OPG_13+',
 'OPG_14+',
 'OPG_15+',
 'OPG_16+',
 'OPG_17-',
 'OPG_18-',
 'IE_19+',
 'IE_20+',
 'IE_21+',
 'IE_22-',
 'IE_23-',
 'IE_24+',
 'IE_25-',
 'IE_26-'
]


# In[10]:

bfas_cols = [
 'workerid',
'age','engagement',
 'BFAS-1+',
 'BFAS-2+',
 'BFAS-3+',
 'BFAS-4+',
 'BFAS-5+',
 'BFAS-6+',
 'BFAS-F7-',
 'BFAS-8-',
 'BFAS-9-',
 'BFAS-10-',
 'BFAS-11+',
 'BFAS-12+',
 'BFAS-13+',
 'BFAS-14+',
 'BFAS-15+',
 'BFAS-16+',
 'BFAS-17-',
 'BFAS-18-',
 'BFAS-19-',
 'BFAS-20-',
 'BFAS-21+',
 'BFAS-22+',
 'BFAS-23+',
 'BFAS-24+',
 'BFAS-25+',
 'BFAS-26-',
 'BFAS-27-',
 'BFAS-28-',
 'BFAS-29-',
 'BFAS-30-',
 'BFAS-31+',
 'BFAS-32+',
 'BFAS-33+',
 'BFAS-34+',
 'BFAS-35-',
 'BFAS-36-',
 'BFAS-37-',
 'BFAS-38-',
 'BFAS-39-',
 'BFAS-40-',
 'BFAS-41+',
 'BFAS-42+',
 'BFAS-43+',
 'BFAS-44+',
 'BFAS-45-',
 'BFAS-46-',
 'BFAS-47-',
 'BFAS-48-',
 'BFAS-49-',
 'BFAS-50-',
 'BFAS-51+',
 'BFAS-52+',
 'BFAS-53+',
 'BFAS-54+',
 'BFAS-55+',
 'BFAS-56+',
 'BFAS-57-',
 'BFAS-58-',
 'BFAS-59-',
 'BFAS-60-',
 'BFAS-61+',
 'BFAS-62+',
 'BFAS-63+',
 'BFAS-64+',
 'BFAS-65+',
 'BFAS-66-',
 'BFAS-67-',
 'BFAS-68-',
 'BFAS-69-',
 'BFAS-70-',
 'BFAS-71+',
 'BFAS-72+',
 'BFAS-73+',
 'BFAS-74+',
 'BFAS-75+',
 'BFAS-76+',
 'BFAS-77-',
 'BFAS-78-',
 'BFAS-79-',
 'BFAS-80-',
 'BFAS-81+',
 'BFAS-82+',
 'BFAS-F83+',
 'BFAS-F84+',
 'BFAS-F85+',
 'BFAS-F86+',
 'BFAS-F87-',
 'BFAS-88-',
 'BFAS-89-',
 'BFAS-90-',
 'BFAS-91+',
 'BFAS-92+',
 'BFAS-93+',
 'BFAS-94+',
 'BFAS-95+',
 'BFAS-96+',
 'BFAS-97-',
 'BFAS-98-',
 'BFAS-99-',
 'BFAS-100-']


# In[11]:

opg = opg[correct_order_opg]
bfas = bfas[bfas_cols]


# In[ ]:




# In[12]:

bfas = bfas.drop(419,axis=0)


# In[13]:

bcorr = bfas.corr()


# In[14]:

bcorr.to_csv('BFAS_II_CORR_TABLE.csv')


# In[14]:

opg.head()


# In[15]:

dropped_opg2 = [#from the g-loadings of the schmid-lieman solution, gloadings >.2
 'age','engagement',
 'PBR_1+',
 'PBR_2-',
 'PBR_3+',
 'PBR_4+',
 'PBR_5+',
 'PBR_6-',
 'PBR_7-',
 'PBR_8-',
 'OPG_9+',
 'OPG_10+',
 'OPG_11-',
 'OPG_12+',
 'OPG_13+',
 'OPG_15+',
 'OPG_17-',
 'IE_19+',
 'IE_20+',
 'IE_21+',
 'IE_22-',
 'IE_24+',
 'IE_25-',
]
opg = opg[dropped_opg2]


# In[16]:

#Histograms
import prettyplotlib as ppl
#for i in bfas.columns.values.tolist()[1:]:
    print i
    ppl.hist(bfas[i],bins=15)
    ppl.plt.savefig(i+'.png')
    ppl.plt.close()


# In[17]:

#Histograms
import prettyplotlib as ppl
#for i in opg.columns.values.tolist()[1:]:
    print i
    ppl.hist(opg[i],bins=15)
    ppl.plt.savefig(i+'.png')
    ppl.plt.close()


# In[18]:

bfas.head()


# In[19]:

bfas


# In[20]:

###################################
#Need to exlude age from the ffpe calculation.
bfas['age'] = bfas['age'].astype(str)
opg['age'] = opg['age'].astype(str)
bfas['ffpe'] = bfas.mean(axis=1,numeric_only=True)
opg['mean']=opg.mean(axis=1,numeric_only=True)


# In[21]:

bfas['age'] = bfas['age'].astype(float)
opg['age'] = opg['age'].astype(float)


# In[22]:

plt.scatter(bfas['ffpe'],opg['mean'])


# In[23]:

##########################

mbfas = bfas[bfas['engagement']=='Male']
fbgas = bfas[bfas['engagement']=='Female']
mopg = opg[opg['engagement']=='Male']
fopg = opg[opg['engagement']=='Female']


# In[24]:

##############################
plt.scatter(mbfas['ffpe'],mopg['mean'])


# In[25]:

plt.scatter(fbgas['ffpe'],fopg['mean'])


# In[26]:

print 'total, scored as written:'
print sss.pearsonr(bfas['ffpe'],opg['mean'])
print 'male:'
print sss.pearsonr(mbfas['ffpe'],mopg['mean'])
print 'female:'
print sss.pearsonr(fbgas['ffpe'],fopg['mean'])

#according to vassar stats, the male-female correlation difference


# In[27]:

len(mbfas)


# In[28]:

len(fbgas)


# In[29]:

bfas.age.max()


# In[31]:

print sss.pearsonr(bfas[(bfas['age']<29) 
                    & (bfas['age']>(17))]['ffpe'],opg[(opg['age']<29) & (opg['age']>(17))]['mean'])
print len(
    
    bfas[(bfas['age']<28) 
                    & (bfas['age']>(17))]['ffpe'])


# In[33]:

print sss.pearsonr(bfas[(bfas['age']<39) & (bfas['age']>(27))]['ffpe'],
                   opg[(opg['age']<39) & (opg['age']>(27))]['mean'])
print len(
    
    bfas[(bfas['age']<39) 
                    & (bfas['age']>(27))]['ffpe'])


# In[39]:




# In[40]:

print sss.pearsonr(bfas[(bfas['age']<49) & (bfas['age']>(37))]['ffpe'],
                   opg[(opg['age']<49) & (opg['age']>(37))]['mean'])
print len(
    bfas[(bfas['age']>49) 
                   ]['ffpe'])


# In[42]:

print sss.pearsonr(bfas[(bfas['age']>48)]['ffpe'],
                   opg[(opg['age']>48)]['mean'])
print len(
    bfas[(bfas['age']>48) 
                    ]['ffpe'])


# In[31]:

def age_stuff(start,stop,step):
    A = []
    for age in range(start,stop,step):
        print age
        print 'SAMPLE SIZE:'
        print len(bfas[
            (bfas['age']<age) & (bfas['age']>(age-step))])
        plt.figure()
        plt.scatter(bfas[(bfas['age']<age) & (bfas['age']>(age-step))]['ffpe'],opg[(opg['age']<age) & (opg['age']>(age-step))]['mean'])
        plt.title(age)
        A.append(sss.pearsonr(bfas[(bfas['age']<age) & (bfas['age']>(age-step))]['ffpe'],opg[(opg['age']<age) & (opg['age']>(age-step))]['mean']))
    return A



# In[32]:

age_stuff(28,75,10)


# In[33]:

age_stuff(33,75,15)


# In[34]:

age_stuff(38,90,20)


# In[24]:

####The theory should hold for individual factors, too
stability_columns = bfas_cols[3:][0:20]
openness_columns = bfas_cols[3:][80:-1]
extro_columns = bfas_cols[3:][60:80]
conci_columns = bfas_cols[3:][40:60]
agree_columns = bfas_cols[3:][20:40]


# In[25]:

stability_columns


# In[26]:

df_stable = bfas[stability_columns]
df_open = bfas[openness_columns]
df_extro = bfas[extro_columns]
df_conci = bfas[conci_columns]
df_agree = bfas[agree_columns]


# In[27]:

df_stable['stability'] = df_stable.mean(axis=1)
df_open['openness'] = df_open.mean(axis=1) 
df_extro['extro'] = df_extro.mean(axis=1)
df_conci['conci'] = df_conci.mean(axis=1)
df_agree['agree'] = df_agree.mean(axis=1)


# In[28]:

measures = [df_stable['stability'],df_open['openness'],df_extro['extro'],df_conci['conci'],df_agree['agree']]


# In[32]:

for construct in measures:
    print sss.pearsonr(opg['mean'],construct)


# In[34]:

bfas[2]


# In[ ]:




# In[39]:

####THAT WAS 'AS PRESCRIBED'

#AS FOR "FACTORS AS FACTOR ANALYZED:"

neurols = [
2,
6,
7,
5,
1,
9,
4,
3,
8,
10,
15,
12,
13,
17,
19,
16,
11,
18,
14,
35,
38,
98] #reversed



agreels = [
26,
27,
28,
23,
24,
25,
22,
29,
21,
40,
30,
67,
36,
66,
68,
63,
62,
69,
100,
37,
97]

extrols = [
73,
71,
74,
75,
76,
78,
77,
72,
61,
64,
79,
20,
65,
70,
80,
34,#
33,#
39#
]

concils = [
52,
51,
53,
56,
59,
54,
42,
58,
57,
55,
41,
45,
46,
60,
47,
49,
43,
50,
31,
48,
44
]

openls = [ #combing the two last factors identified -- both were aspects of Openness
87,
89,
83,
81,
90,
82,
88,
84,
85,
86,
93,
99,
95,
96,
32,
94,
92,
91
]


# In[40]:

#need to account for the two added age/gender columns

nls = [x+2 for x in neurols]
ols = [x+2 for x in openls]
els = [x+2 for x in extrols]
cls = [x+2 for x in concils]
als = [x+2 for x in agreels]


# In[41]:

factor_stable = bfas[nls]
factor_open= bfas[ols]
factor_extro = bfas[els]
factor_conci = bfas[cls]
factor_agree = bfas[als]


# In[42]:

lss = neurols 
lss.extend(openls)
lss.extend(extrols)
lss.extend(concils)
lss.extend(agreels)
lss.sort()
print (len(lss))
lss


# In[43]:

factor_extro.head()
factor_stable.head()


# In[44]:

factor_extro['BFAS-34+'] = pd.Series(100-factor_extro['BFAS-34+'])
factor_extro['BFAS-33+'] = pd.Series(100-factor_extro['BFAS-33+'])
factor_extro['BFAS-39-'] = pd.Series(100-factor_extro['BFAS-39-'])
factor_stable['BFAS-98-'] = pd.Series(100-factor_stable['BFAS-98-'])


# In[45]:

factor_extro.head()


# In[46]:

factor_stable['m'] = factor_stable.mean(axis=1)
factor_open['m'] = factor_open.mean(axis=1)
factor_extro['m'] = factor_extro.mean(axis=1)
factor_conci['m'] = factor_conci.mean(axis=1)
factor_agree['m'] = factor_agree.mean(axis=1)


# In[47]:

factor_measures=[factor_stable['m'],factor_open['m'],factor_extro['m'],factor_conci['m'],factor_agree['m']]


# In[48]:

for construct in factor_measures:
    print sss.pearsonr(opg['mean'],construct)


# In[51]:

#Mean of means, and all that.

gfp = .2 * (factor_stable['m'] + factor_open['m'] + factor_extro['m'] + factor_conci['m'] + factor_agree['m'])




# In[52]:

sss.pearsonr(opg['mean'],gfp) #gfp AS FACTOR ANALYZED.


# In[54]:

fig = plt.figure(figsize=(11, 7))
plt.scatter(opg['mean'],ffpe, alpha=.7,s=30)
#plt.title('H-OPG vs. BFAS FFPE')
plt.xlabel("H/OPG Score")
plt.ylabel("BFAS - GFP estimate")
plt.savefig('HOPG_VS_BFAS_GFP_SII.eps',format='eps',dpi=500 
         )
plt.show()


# In[55]:

measures = [df_stable['stability'].tolist(),df_open['openness'].tolist(),df_extro['extro'].tolist(),df_conci['conci'].tolist(),df_agree['agree'].tolist()]


# In[56]:

for construct in measures: #AS WRITTEN
    print sss.pearsonr(opg['mean'],construct)


# In[57]:

for construct in factor_measures: #As factor analyzed
    print sss.pearsonr(opg['mean'],construct)


# In[86]:

for construct in measures:
    print sss.pearsonr(opg['mean'],construct)


# In[87]:

import os
os.getcwd()


# In[58]:

gload = pd.read_csv('BFAS_II_OMEGA_FA_6_LOADING_FIGSHARE.csv')


# In[59]:

gload.head()


# In[60]:

gload.tail()


# In[72]:

bfas.head()


# In[61]:

bfas['hopg'] = opg['mean']


# In[62]:

c = bfas.corr()


# In[63]:

c.head()


# In[73]:

c.tail()


# In[64]:

c.tail()


# In[77]:

c['hopg'][1:-2]


# In[78]:

gload['opgcorr']= c['hopg'][1:-2]


# In[79]:

print len(c['hopg'][:-2])
print len(gload['g'])
print len(gload['opgcorr'])


# In[80]:

gload.head()


# In[81]:

print sss.pearsonr(c['hopg'][1:-2],gload['g'])
#as written


# In[82]:

plt.scatter(c['hopg'][1:-2],gload['g'])


# In[84]:


fig = plt.figure(figsize=(11, 7))
plt.scatter(c['hopg'][1:-2],gload['g'],alpha=.7,s=30)
#plt.title('Humility vs GFP, Factor Analyzed, N =  434')
plt.xlabel('H-OPG - Item correlations')
plt.ylabel('g loading on BFAS Item')
plt.xlim(xmin=-.1)
plt.ylim(ymin=-.1)
plt.savefig('Figure_8_BFAS_GLoadings_vs_HOPG_Correlations_Study_II_U.eps',format='eps', dpi=500
          )
plt.show()


# In[41]:




# In[ ]:



