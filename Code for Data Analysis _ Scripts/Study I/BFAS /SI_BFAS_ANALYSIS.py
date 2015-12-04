
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

#pd.set_option('display.max_columns', None)


# In[3]:

bfas= pd.read_csv('./Master_preprocessed_BFAS.csv')
opg = pd.read_csv('./Master_preprocessed_BFASOPG.csv')
bfas = bfas.convert_objects(convert_numeric=True) 
opg = opg.convert_objects(convert_numeric=True)
#Scroll down to read in bfas..


# In[4]:

bfas.head()


# In[5]:

bfas['BFAS-32+'].head()


# In[6]:

bfas.tail()


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
 'IE_26-',
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
 'BFAS-90+',
 'BFAS-90-',
 'BFAS-91+',
 'BFAS-92+',
 'BFAS-95+',
 'BFAS-96+',
 'BFAS-97+',
 'BFAS-98-',
 'BFAS-99-',
 'BFAS-100-',
 'BFAS-101-']


# In[10]:

bfas.to_csv("MASTER_last_round_preprocessing-BFAS.csv")
bfas = pd.read_csv("MASTER_last_round_preprocessing-BFAS.csv")


# In[10]:

opg = opg[correct_order_opg]
bfas = bfas[bfas_cols]


# In[11]:

subset = ['PBR_1+', #From Factor analysis - G loadings from a five factor solution of less than 20 are dropped
 'PBR_2-',
 'PBR_3+',
 'PBR_4+',
 'PBR_5+',
 'PBR_7-',
 'OPG_10+',
 'OPG_12+',
 'OPG_13+',
 'OPG_14+',
 'OPG_15+',
 'OPG_16+',
 'IE_19+',
 'IE_20+',
 'IE_21+',
 'IE_22-',
 'IE_24+',
 'IE_25-'
]
opg = opg[subset]


# In[12]:

opg['mean'] = opg.mean(axis=1)


# In[13]:

bfas.columns.values.tolist()


# In[14]:

cbfas = bfas.corr()
cbfas.to_csv('Study_I_BFAS_CORR_TABLE.csv')


# In[15]:

fig = plt.figure(figsize=(7.5, 5.5))
plt.scatter(opg.mean(axis=1),bfas.mean(axis=1),alpha=.5,s=30)
#scored as written
plt.xlabel('H/OPG')
plt.ylabel('BFAS GFPE Estimate')
plt.xlim((25,100))
plt.ylim((25,100))
plt.savefig('SCIENCE_BFAS_HOPG_I.png',format='png', dpi=300
            )
plt.show()


# In[17]:

sss.pearsonr(opg['mean'],bfas.mean(axis=1))


# In[18]:

#bfas.columns.values.tolist()


# In[19]:

#scoring factors as written
stability_columns = bfas_cols[1:][0:20]
openness_columns = bfas_cols[1:][80:]
extro_columns = bfas_cols[1:][60:80]
conci_columns = bfas_cols[1:][40:60]
agree_columns = bfas_cols[1:][20:40]


# In[20]:

df_stable = bfas[stability_columns]
df_open = bfas[openness_columns]
df_extro = bfas[extro_columns]
df_conci = bfas[conci_columns]
df_agree = bfas[agree_columns]


# In[21]:

df_stable['stability'] = df_stable.mean(axis=1)
df_open['openness'] = df_open.mean(axis=1) 
df_extro['extro'] = df_extro.mean(axis=1)
df_conci['conci'] = df_conci.mean(axis=1)
df_agree['agree'] = df_agree.mean(axis=1)


# In[22]:

written_measures = [df_stable['stability'],df_open['openness'],df_extro['extro'],df_conci['conci'],df_agree['agree']]


# In[23]:

for construct in written_measures:
    print sss.pearsonr(opg['mean'],construct)
    
    #AS WRITTEN
    #Stable
    #Open
    #Extro
    #Conci
    #Agree


# In[24]:


  #Histograms
import prettyplotlib as ppl
#for i in bfas.columns.values.tolist()[1:]:
    print i
    ppl.hist(bfas[i],bins=20)
    ppl.plt.savefig(i+'.png')
    ppl.plt.close()


# In[25]:


bfas.head()


# In[ ]:




# In[26]:

Neuro_Ind = [5,
2,
1,
6,
4,
3,
15,
10,
13,
7,
11,
14,
12,
17,
9,
16,
8,
19,
50,
20,
18,
47,
49]


neur = []
for i in sorted(Neuro_Ind):
    neur.append(bfas_cols[i]) #this works because the labels are offset by 1, due to 'workderid'
NEURO = bfas[neur]


# In[ ]:




# In[27]:

Agree_Ind = [26,
23,
28,
27,
22,
21,
24,
25,
29,
30,
37,
40,
63,
92,
62,
35,
68,
67,
69,
97,
100]

agre = []
for i in sorted(Agree_Ind):
     agre.append(bfas_cols[i])
AGREE = bfas[agre]


# In[28]:

extro_assert_Ind = [73,
75,
71,
74,
72,
77,
78,
76,
79,
61,
80,
64,
85,
70,
65,
38,#
32,#
34,#
36,#
33,#
39,
44]#

ext= []
for i in sorted(extro_assert_Ind):
     ext.append(bfas_cols[i])
EXTRA = bfas[ext]
EXTRA['BFAS-38-'] = pd.Series(100-EXTRA['BFAS-38-'])
EXTRA['BFAS-32+'] = pd.Series(100-EXTRA['BFAS-32+'])
EXTRA['BFAS-34+'] = pd.Series(100-EXTRA['BFAS-34+'])
EXTRA['BFAS-36-'] = pd.Series(100-EXTRA['BFAS-36-'])
EXTRA['BFAS-33+'] = pd.Series(100-EXTRA['BFAS-33+'])
EXTRA['BFAS-39-'] = pd.Series(100-EXTRA['BFAS-39-'])


# In[29]:

EXTRA.head()


# In[30]:

bfas_cols[45]


# In[31]:

concientiousness_Ind = [51,
52,
56,
53,
54,
31,
55,
57,
42,
58,
41,
59,
60,
45,
99,
43,
46,
48,
86]# 

conci= []
for i in sorted(concientiousness_Ind):
     conci.append(bfas_cols[i])
CONCI = bfas[conci]

CONCI['BFAS-100-'] = pd.Series(100-CONCI['BFAS-100-'])


# In[32]:

openness_Ind = [87,
83,
88,
81,
82,
96,
89,
84,
93,
91,
90,
66,
94,
95,
98]#


opn= []
for i in sorted(openness_Ind):
     opn.append(bfas_cols[i])
OPEN = bfas[opn]

OPEN['BFAS-66-'] = pd.Series(100-OPEN['BFAS-66-'])


# In[33]:

OPEN.head()


# In[34]:

masterls = [Neuro_Ind,Agree_Ind,extro_assert_Ind,concientiousness_Ind,openness_Ind]


# In[35]:

mls =[item for sublist in masterls for item in sublist]


# In[36]:

sorted(mls)


# In[37]:

factor_measures = [AGREE,NEURO,OPEN,EXTRA,CONCI]


# In[38]:

for m in factor_measures:
    #measures = [AGREE,NEUROTIC,OPEN,EXTRA,CONCI]
    print sss.pearsonr(opg.mean(axis=1),m.mean(axis=1))
    #[AGREE,NEUROTIC,OPEN,EXTRA,CONCI]


# In[39]:

#FFPE

neo = []
for i in sorted(mls):
    neo.append(bfas_cols[i])

bfas_proc = bfas[neo]

bfas_proc['BFAS-66-'] = pd.Series(100-bfas_proc['BFAS-66-'])
bfas_proc['BFAS-100-'] = pd.Series(100-bfas_proc['BFAS-100-'])
bfas_proc['BFAS-38-'] = pd.Series(100-bfas_proc['BFAS-38-'])
bfas_proc['BFAS-32+'] = pd.Series(100-bfas_proc['BFAS-32+'])
bfas_proc['BFAS-34+'] = pd.Series(100-bfas_proc['BFAS-34+'])
bfas_proc['BFAS-36-'] = pd.Series(100-bfas_proc['BFAS-36-'])
bfas_proc['BFAS-33+'] = pd.Series(100-bfas_proc['BFAS-33+'])
bfas_proc['BFAS-39-'] = pd.Series(100-bfas_proc['BFAS-39-'])


# In[40]:

bfas_proc.head()


# In[41]:

bfas_proc['gfp'] = bfas_proc.mean(axis=1)


# In[62]:

fig = plt.figure(figsize=(11,7))#(figsize=(15, 9))
plt.scatter(opg.mean(axis=1),bfas_proc['gfp'],alpha=.7,s=30)
#plt.title('Relationship of H/OPG vs GFP')
plt.xlabel('H/OPG')
plt.ylabel('BFAS-GFP Estimate')
plt.savefig('LabledBFASGFPSI_IV.eps',format='eps', dpi=500
           )
plt.show()


# In[43]:

print sss.pearsonr(opg.mean(axis=1),bfas_proc['gfp'])


# In[29]:




# In[64]:

#Connections with G
df_loadings = pd.read_csv('./STUDY_I_BFAS_5_G_SOLUTION.csv')


# In[65]:

df_loadings.tail()


# In[66]:

bfas.head()


# In[67]:

bbfas = bfas
bbfas['opg'] = opg.mean(axis=1)


# In[68]:

bbcfas = bfas_proc
bbcfas['opg'] = opg.mean(axis=1)


# In[64]:

bbfas.head()


# In[69]:

bbcfas.head()


# In[70]:

c = bbfas.corr()
d = bbcfas.corr()


# In[71]:

print "as written:",sss.pearsonr(c['opg'][:-1],df_loadings['g'])
print "as FA:",sss.pearsonr(d['opg'][:-2],df_loadings['g'])


# In[85]:

fig = plt.figure(figsize=(11,7))
plt.scatter(c['opg'][:-1],df_loadings['g'],alpha=.7,s=30) #Don't need the correlation of opg with itself...


plt.xlabel('BFAS Item - H-OPG correlation')
plt.ylabel('g loading on item')
plt.savefig('g_vs_HOPG_loadings_BFAS_as_writtenI.eps',format='eps', dpi=500
           )
plt.show()


# In[77]:

len(df_loadings['g'])


# In[79]:

d.tail()


# In[80]:

fig = plt.figure(figsize=(11,7))
plt.scatter(d['opg'][:-2],df_loadings['g'],alpha=.7,s=30) #Don't need the correlation of opg with itself...

plt.title('Prediction of G loadings from H-OPG correlations_BFAS')
plt.xlabel('BFAS Item - H-OPG correlation')
plt.ylabel('Item G loading')
#plt.savefig('G_vs_HOPG_loadings_BFAS.png',format='png', dpi=500
#            )
plt.show()


# In[82]:

print sss.pearsonr(d['opg'][:-2],df_loadings['g'])
print sss.pearsonr(c['opg'][:-1],df_loadings['g'])


# In[30]:

fig = plt.figure(figsize=(7.5, 5.5))
plt.scatter(c['opg'][:-1],df_loadings['g'],alpha=.5,s=30)
#plt.title('Humility vs GFP, Factor Analyzed, N =  434')
plt.xlabel('H-OPG - Item correlations')
plt.ylabel('General Factor - Item loadings')
plt.xlim(xmin=-.1)
plt.ylim(ymin=-.1)
plt.savefig('Figure4_GLoadings_vs_HOPG_Correlations_Study_I.eps',format='eps', dpi=450
           )
plt.show()


# In[31]:

sss.pearsonr(c['opg'][:-1],df_loadings['g'])


# In[40]:

c.tail()

