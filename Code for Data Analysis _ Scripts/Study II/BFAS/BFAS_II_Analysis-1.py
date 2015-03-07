
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
import matplotlib
from  matplotlib import pyplot as plt
import scipy.stats.stats as sss
get_ipython().magic(u'matplotlib inline')
import pystan
from __future__ import division


# In[4]:

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 30)


# In[5]:

bfas= pd.read_csv('./Master_preprocessed_BFAS.csv')
opg = pd.read_csv('./Master_preprocessed_BFASOPG.csv')
bfas = bfas.convert_objects(convert_numeric=True) 
opg = opg.convert_objects(convert_numeric=True)


# In[6]:

bfas.head()


# In[7]:

opg.head()


# In[8]:

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


# In[9]:

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


# In[10]:

opg = opg[correct_order_opg]
bfas = bfas[bfas_cols]


# In[11]:

bfas.head()


# In[12]:

bfas = bfas.drop(419,axis=0)


# In[12]:




# In[12]:




# In[12]:




# In[12]:




# In[12]:




# In[13]:

dropped_opg2 = [#from the g-loadings of the schmid-lieman transformed 6 factor solution, all items with loadings >.25
 'PBR_1+',
 'PBR_2-',
 'PBR_3+',
 'PBR_4+',
 'PBR_5+',
 'PBR_6-',
 'PBR_7-',
 'PBR_8-',
 #'OPG_9+',
 'OPG_10+',
 'OPG_12+',
 'OPG_13+',
 #'OPG_14+',
 'OPG_15+',
 #'OPG_17-',
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


# In[16]:

bfas.head()


# In[17]:

bfas['gfp'] = bfas[bfas_cols[1:-1]].mean(axis=1)


# In[18]:

opg['mean'] = opg[dropped_opg2].mean(axis=1)


# In[19]:

opg.head()


# In[20]:

fig = plt.figure(figsize=(15, 9))
#AS WRITTEN
plt.scatter(opg['mean'],bfas['gfp'],alpha=.5,s=30)
plt.title('STUDY II: Naive GFP/MEAN OPG and BFAS,  N =  420')
plt.xlabel('Naive Humility')
plt.ylabel('Naive BFAS GFP')
#plt.savefig('WeightedOPG_naiveGFP_10_21_Raw.png',format='png', 
 #         )
plt.show()


# In[21]:

print sss.pearsonr(bfas['gfp'].tolist(),opg['mean'].tolist())

print len(bfas['gfp'])
print len(opg['mean'])
#Hot Damn.


# In[21]:




# In[21]:




# In[22]:

####The theory should hold for individual factors, too
stability_columns = bfas_cols[1:][0:20]
openness_columns = bfas_cols[1:][80:-1]
extro_columns = bfas_cols[1:][60:80]
conci_columns = bfas_cols[1:][40:60]
agree_columns = bfas_cols[1:][20:40]


# In[23]:

df_stable = bfas[stability_columns]
df_open = bfas[openness_columns]
df_extro = bfas[extro_columns]
df_conci = bfas[conci_columns]
df_agree = bfas[agree_columns]


# In[24]:

df_stable['stability'] = df_stable.mean(axis=1)
df_open['openness'] = df_open.mean(axis=1) 
df_extro['extro'] = df_extro.mean(axis=1)
df_conci['conci'] = df_conci.mean(axis=1)
df_agree['agree'] = df_agree.mean(axis=1)


# In[25]:

measures = [df_stable['stability'],df_open['openness'],df_extro['extro'],df_conci['conci'],df_agree['agree']]


# In[26]:

for construct in measures:
    print sss.pearsonr(opg['mean'],construct)


# In[27]:

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


# In[28]:

factor_stable = bfas[neurols]
factor_open= bfas[openls]
factor_extro = bfas[extrols]
factor_conci = bfas[concils]
factor_agree = bfas[agreels]


# In[29]:

lss = neurols 
lss.extend(openls)
lss.extend(extrols)
lss.extend(concils)
lss.extend(agreels)
lss.sort()
print (len(lss))
lss


# In[30]:

factor_extro.head()
factor_stable.head()


# In[31]:

factor_extro['BFAS-34+'] = pd.Series(100-factor_extro['BFAS-34+'])
factor_extro['BFAS-33+'] = pd.Series(100-factor_extro['BFAS-33+'])
factor_extro['BFAS-39-'] = pd.Series(100-factor_extro['BFAS-39-'])
factor_stable['BFAS-98-'] = pd.Series(100-factor_stable['BFAS-98-'])


# In[32]:

factor_extro.head()


# In[33]:

factor_stable['m'] = factor_stable.mean(axis=1)
factor_open['m'] = factor_open.mean(axis=1)
factor_extro['m'] = factor_extro.mean(axis=1)
factor_conci['m'] = factor_conci.mean(axis=1)
factor_agree['m'] = factor_agree.mean(axis=1)


# In[34]:

factor_measures=[factor_stable['m'],factor_open['m'],factor_extro['m'],factor_conci['m'],factor_agree['m']]


# In[35]:

for construct in factor_measures:
    print sss.pearsonr(opg['mean'],construct)


# In[36]:

#Mean of means, and all that.

ffpe = .2 * (factor_stable['m'] + factor_open['m'] + factor_extro['m'] + factor_conci['m'] + factor_agree['m'])




# In[37]:

sss.pearsonr(opg['mean'],ffpe) #FFPE AS FACTOR ANALYZED.


# In[38]:

fig = plt.figure(figsize=(7, 5))
plt.scatter(opg['mean'],ffpe, alpha=.5,s=30)
plt.title('H-OPG vs. BFAS FFPE')
plt.xlabel("Respondent's H-OPG estimate")
plt.ylabel("Respondent's five factor estimate")
plt.savefig('HOPG_VS_BFAS_FFPE.eps',format='eps', 
         )
plt.show()


# In[39]:

measures = [df_stable['stability'].tolist(),df_open['openness'].tolist(),df_extro['extro'].tolist(),df_conci['conci'].tolist(),df_agree['agree'].tolist()]


# In[40]:

for construct in measures:
    print sss.pearsonr(opg['mean'],construct)


# In[41]:

fig = plt.figure(figsize=(30, 20))
colors = ['g','r','c','m','b']
for i,construct in enumerate(factor_measures):
    #fig = plt.figure(figsize=(15, 9))
    plt.scatter(opg['mean'],construct,alpha=.38,s=33,c=colors[i])
plt.title('five dimensions')
plt.xlabel('Naive Humility')
plt.ylabel('Naive five factors')
plt.savefig('Each_factor_and_OPG_BFAS.png',format='png', 
         )
plt.show()


# In[41]:




# In[41]:




# In[44]:

for construct in factor_measures:
    print sss.pearsonr(opg['mean'],construct)


# In[45]:

fig = plt.figure(figsize=(30, 20))
colors = ['g','r','c','m','b']
for i,construct in enumerate(measures):
    #fig = plt.figure(figsize=(15, 9))
    plt.scatter(opg['mean'],construct,alpha=.38,s=33,c=colors[i])
plt.title('five dimensions')
plt.xlabel('Naive Humility')
plt.ylabel('Naive five factors')
plt.savefig('Each_factor_and_OPG_BFAS.png',format='png', 
         )
plt.show()


# In[46]:

for construct in measures:
    print sss.pearsonr(opg['mean'],construct)


# In[47]:

import os
os.getcwd()


# In[48]:

gload = pd.read_csv('STUDYII_BFAS_6_G.csv')


# In[49]:

gload.head()


# In[50]:

gload.tail()


# In[51]:

bfas['hopg'] = opg['mean']


# In[52]:

c = bfas.corr()


# In[53]:

c.head()


# In[54]:

c.tail()


# In[55]:

gload['opgcorr']= c['hopg'][:-2]


# In[56]:

print len(c['hopg'][:-2])
print len(gload['g'])
print len(gload['opgcorr'])


# In[57]:

gload.head()


# In[58]:

print sss.pearsonr(c['hopg'][:-2],gload['g'])


# In[59]:

plt.scatter(c['hopg'][:-2],gload['g'])


# In[59]:




# In[ ]:



