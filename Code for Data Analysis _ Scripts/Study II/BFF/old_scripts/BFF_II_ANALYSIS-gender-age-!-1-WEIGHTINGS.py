
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
bfas = bfas.convert_objects(convert_numeric=True) 
opg = opg.convert_objects(convert_numeric=True)


# In[4]:

bfas.head()


# In[5]:

opg.head()


# In[6]:

correct_order_opg = ['workerid',
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


# In[7]:

bfas_cols = [
 'workerid',
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


# In[8]:

opg = opg[correct_order_opg]
bfas = bfas[bfas_cols]


# In[9]:

bfas.head()


# In[10]:

bfas = bfas.drop(419,axis=0)


# In[11]:

bcorr = bfas.corr()


# In[15]:

bcorr.to_csv('BFAS_II_CORR_TABLE.csv')


# In[12]:

opg.head()


# In[13]:

dropped_opg2 = [#from the g-loadings of the schmid-lieman solution, gloadings >.2
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


# In[14]:

#Histograms
import prettyplotlib as ppl
#for i in bfas.columns.values.tolist()[1:]:
    print i
    ppl.hist(bfas[i],bins=15)
    ppl.plt.savefig(i+'.png')
    ppl.plt.close()


# In[15]:

#Histograms
import prettyplotlib as ppl
#for i in opg.columns.values.tolist()[1:]:
    print i
    ppl.hist(opg[i],bins=15)
    ppl.plt.savefig(i+'.png')
    ppl.plt.close()


# In[14]:

bfas.head()


# In[15]:

bfas


# In[16]:

bfas['ffpe'] = bfas.mean(axis=1)
opg['mean']=opg.mean(axis=1)


# In[17]:

plt.scatter(bfas['ffpe'],opg['mean'])


# In[19]:

fig = plt.figure(figsize=(7.5, 5.5))
plt.scatter(opg.mean(axis=1),bfas.mean(axis=1),alpha=.5,s=30)
#scored as written
plt.xlabel('H/OPG')
plt.ylabel('Study II BFAS GFP Estimate')
plt.xlim((25,100))
plt.ylim((25,100))
plt.savefig('SCIENCE_BFAS_HOPG_II.png',format='png', dpi=300
            )
plt.show()


# In[20]:

sss.pearsonr(bfas['ffpe'],opg['mean'])


# In[22]:

len(bfas)


# In[23]:

####The theory should hold for individual factors, too
stability_columns = bfas_cols[1:][0:20]
openness_columns = bfas_cols[1:][80:-1]
extro_columns = bfas_cols[1:][60:80]
conci_columns = bfas_cols[1:][40:60]
agree_columns = bfas_cols[1:][20:40]


# In[24]:

df_stable = bfas[stability_columns]
df_open = bfas[openness_columns]
df_extro = bfas[extro_columns]
df_conci = bfas[conci_columns]
df_agree = bfas[agree_columns]


# In[25]:

df_stable['stability'] = df_stable.mean(axis=1)
df_open['openness'] = df_open.mean(axis=1) 
df_extro['extro'] = df_extro.mean(axis=1)
df_conci['conci'] = df_conci.mean(axis=1)
df_agree['agree'] = df_agree.mean(axis=1)


# In[26]:

measures = [df_stable['stability'],df_open['openness'],df_extro['extro'],df_conci['conci'],df_agree['agree']]


# In[27]:

for construct in measures:
    print sss.pearsonr(opg['mean'],construct)


# In[28]:

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


# In[29]:

factor_stable = bfas[neurols]
factor_open= bfas[openls]
factor_extro = bfas[extrols]
factor_conci = bfas[concils]
factor_agree = bfas[agreels]


# In[30]:

lss = neurols 
lss.extend(openls)
lss.extend(extrols)
lss.extend(concils)
lss.extend(agreels)
lss.sort()
print (len(lss))
lss


# In[31]:

factor_extro.head()
factor_stable.head()


# In[32]:

factor_extro['BFAS-34+'] = pd.Series(100-factor_extro['BFAS-34+'])
factor_extro['BFAS-33+'] = pd.Series(100-factor_extro['BFAS-33+'])
factor_extro['BFAS-39-'] = pd.Series(100-factor_extro['BFAS-39-'])
factor_stable['BFAS-98-'] = pd.Series(100-factor_stable['BFAS-98-'])


# In[33]:

factor_extro.head()


# In[34]:

factor_stable['m'] = factor_stable.mean(axis=1)
factor_open['m'] = factor_open.mean(axis=1)
factor_extro['m'] = factor_extro.mean(axis=1)
factor_conci['m'] = factor_conci.mean(axis=1)
factor_agree['m'] = factor_agree.mean(axis=1)


# In[35]:

factor_measures=[factor_stable['m'],factor_open['m'],factor_extro['m'],factor_conci['m'],factor_agree['m']]


# In[36]:

for construct in factor_measures:
    print sss.pearsonr(opg['mean'],construct)


# In[37]:

#Mean of means, and all that.

ffpe = .2 * (factor_stable['m'] + factor_open['m'] + factor_extro['m'] + factor_conci['m'] + factor_agree['m'])




# In[70]:

sss.pearsonr(opg['mean'],ffpe) #FFPE AS FACTOR ANALYZED.


# In[71]:

fig = plt.figure(figsize=(7, 5))
plt.scatter(opg['mean'],ffpe, alpha=.5,s=30)
plt.title('H-OPG vs. BFAS FFPE')
plt.xlabel("Respondent's H-OPG estimate")
plt.ylabel("Respondent's five factor estimate")
plt.savefig('HOPG_VS_BFAS_FFPE.eps',format='eps', 
         )
plt.show()


# In[72]:

measures = [df_stable['stability'].tolist(),df_open['openness'].tolist(),df_extro['extro'].tolist(),df_conci['conci'].tolist(),df_agree['agree'].tolist()]


# In[73]:

for construct in measures: #AS WRITTEN
    print sss.pearsonr(opg['mean'],construct)


# In[75]:

for construct in factor_measures: #As factor analyzed
    print sss.pearsonr(opg['mean'],construct)


# In[39]:

for construct in measures:
    print sss.pearsonr(opg['mean'],construct)


# In[40]:

import os
os.getcwd()


# In[56]:

gload = pd.read_csv('BFAS_II_OMEGA_FA_6_LOADING_FIGSHARE.csv')
#gload = pd.read_csv('BFAS_II_OMEGA_FA_6_LOADING_FIGSHARE.csv')


# In[57]:

gload.head()


# In[58]:

gload.tail()


# In[60]:

bbbfas = bfas


# In[61]:

bbbfas.head()


# In[63]:

bbbfas = bbbfas.drop(['workerid','ffpe','hopg'],axis=1)


# In[64]:

bbbfas['hopg'] = opg['mean']


# In[67]:

c = bbbfas.corr()


# In[68]:

c.head()


# In[69]:

c.tail()


# In[48]:

gload['opgcorr']= c['hopg'][:-2]


# In[71]:

print len(c['hopg'][:-1])
print len(gload['g'])


# In[72]:

gload.head()


# In[80]:

print sss.pearsonr(c['hopg'][:-1],gload['g'])


# In[81]:

plt.scatter(c['hopg'][:-1],gload['g'])


# In[88]:

fig = plt.figure(figsize=(7.5, 5.5))
plt.scatter(c['hopg'][:-1],gload['g'],s=30)
#scored as written
plt.xlabel('H-OPG item loadings')
plt.ylabel('BFAS item general factor loadings ')
plt.xlim(xmin=-.2)
plt.ylim(ymin=-.2)
plt.savefig('BFAS_HOPG_Gloadings_II.eps',format='eps', dpi=450
            )
plt.show()


# In[84]:

plt.scatter(c['hopg'][:-1],gload['g'])


# In[ ]:



