
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


# In[24]:

bfas= pd.read_csv('./Master_preprocessed_BFAS.csv')
opg = pd.read_csv('./Master_preprocessed_BFASOPG.csv')
demo = pd.read_csv('./WorkerID_Gender_Age_pairing_BFAS_II.csv')
bfas = bfas.convert_objects(convert_numeric=True)
opg = opg.convert_objects(convert_numeric=True)


# In[25]:

bfas.head()


# In[26]:

opg.head()


# In[27]:

################################################
demo = demo[['workerid','age','engagement']]



# In[28]:

##################################################

#Join Age, Gender by workerid

opg = pd.merge(opg,demo,how='outer',)


# In[29]:

####################################

bfas = pd.merge(bfas,demo,how='outer',)


# In[29]:




# In[30]:

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


# In[31]:

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


# In[32]:

opg = opg[correct_order_opg]
bfas = bfas[bfas_cols]


# In[36]:




# In[37]:

bfas = bfas.drop(419,axis=0)


# In[12]:

bcorr = bfas.corr()


# In[15]:

bcorr.to_csv('BFAS_II_CORR_TABLE.csv')


# In[31]:

opg.head()


# In[38]:

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


# In[13]:

#Histograms
import prettyplotlib as ppl
#for i in bfas.columns.values.tolist()[1:]:
    print i
    ppl.hist(bfas[i],bins=15)
    ppl.plt.savefig(i+'.png')
    ppl.plt.close()


# In[14]:

#Histograms
import prettyplotlib as ppl
#for i in opg.columns.values.tolist()[1:]:
    print i
    ppl.hist(opg[i],bins=15)
    ppl.plt.savefig(i+'.png')
    ppl.plt.close()


# In[42]:

bfas.head()


# In[45]:

bfas


# In[50]:

###################################
#Need to exlude age from the ffpe calculation.
bfas['age'] = bfas['age'].astype(str)
opg['age'] = opg['age'].astype(str)
bfas['ffpe'] = bfas.mean(axis=1,numeric_only=True)
opg['mean']=opg.mean(axis=1,numeric_only=True)


# In[51]:

bfas['age'] = bfas['age'].astype(float)
opg['age'] = opg['age'].astype(float)


# In[52]:

plt.scatter(bfas['ffpe'],opg['mean'])


# In[55]:

##########################

mbfas = bfas[bfas['engagement']=='Male']
fbgas = bfas[bfas['engagement']=='Female']
mopg = opg[opg['engagement']=='Male']
fopg = opg[opg['engagement']=='Female']


# In[56]:

##############################
plt.scatter(mbfas['ffpe'],mopg['mean'])


# In[57]:

plt.scatter(fbgas['ffpe'],fopg['mean'])


# In[58]:

print 'total, scored as written:'
print sss.pearsonr(bfas['ffpe'],opg['mean'])
print 'male:'
print sss.pearsonr(mbfas['ffpe'],mopg['mean'])
print 'female:'
print sss.pearsonr(fbgas['ffpe'],fopg['mean'])

#according to vassar stats, the male-female correlation difference


# In[59]:

len(mbfas)


# In[60]:

len(fbgas)


# In[102]:

bfas.age.max()


# In[111]:

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



# In[112]:

age_stuff(28,75,10)


# In[113]:

age_stuff(33,75,15)


# In[114]:

age_stuff(38,90,20)


# In[55]:

####The theory should hold for individual factors, too
stability_columns = bfas_cols[1:][0:20]
openness_columns = bfas_cols[1:][80:-1]
extro_columns = bfas_cols[1:][60:80]
conci_columns = bfas_cols[1:][40:60]
agree_columns = bfas_cols[1:][20:40]


# In[56]:

df_stable = bfas[stability_columns]
df_open = bfas[openness_columns]
df_extro = bfas[extro_columns]
df_conci = bfas[conci_columns]
df_agree = bfas[agree_columns]


# In[57]:

df_stable['stability'] = df_stable.mean(axis=1)
df_open['openness'] = df_open.mean(axis=1)
df_extro['extro'] = df_extro.mean(axis=1)
df_conci['conci'] = df_conci.mean(axis=1)
df_agree['agree'] = df_agree.mean(axis=1)


# In[58]:

measures = [df_stable['stability'],df_open['openness'],df_extro['extro'],df_conci['conci'],df_agree['agree']]


# In[59]:

for construct in measures:
    print sss.pearsonr(opg['mean'],construct)


# In[60]:

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


# In[61]:

factor_stable = bfas[neurols]
factor_open= bfas[openls]
factor_extro = bfas[extrols]
factor_conci = bfas[concils]
factor_agree = bfas[agreels]


# In[62]:

lss = neurols
lss.extend(openls)
lss.extend(extrols)
lss.extend(concils)
lss.extend(agreels)
lss.sort()
print (len(lss))
lss


# In[63]:

factor_extro.head()
factor_stable.head()


# In[64]:

factor_extro['BFAS-34+'] = pd.Series(100-factor_extro['BFAS-34+'])
factor_extro['BFAS-33+'] = pd.Series(100-factor_extro['BFAS-33+'])
factor_extro['BFAS-39-'] = pd.Series(100-factor_extro['BFAS-39-'])
factor_stable['BFAS-98-'] = pd.Series(100-factor_stable['BFAS-98-'])


# In[65]:

factor_extro.head()


# In[66]:

factor_stable['m'] = factor_stable.mean(axis=1)
factor_open['m'] = factor_open.mean(axis=1)
factor_extro['m'] = factor_extro.mean(axis=1)
factor_conci['m'] = factor_conci.mean(axis=1)
factor_agree['m'] = factor_agree.mean(axis=1)


# In[67]:

factor_measures=[factor_stable['m'],factor_open['m'],factor_extro['m'],factor_conci['m'],factor_agree['m']]


# In[68]:

for construct in factor_measures:
    print sss.pearsonr(opg['mean'],construct)


# In[69]:

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


# In[86]:

for construct in measures:
    print sss.pearsonr(opg['mean'],construct)


# In[87]:

import os
os.getcwd()


# In[76]:

gload = pd.read_csv('BFAS_II_OMEGA_FA_6_LOADING_FIGSHARE.csv')


# In[77]:

gload.head()


# In[78]:

gload.tail()


# In[79]:

bfas['hopg'] = opg['mean']


# In[80]:

c = bfas.corr()


# In[81]:

c.head()


# In[82]:

c.tail()


# In[83]:

gload['opgcorr']= c['hopg'][:-2]


# In[84]:

print len(c['hopg'][:-2])
print len(gload['g'])
print len(gload['opgcorr'])


# In[85]:

gload.head()


# In[86]:

print sss.pearsonr(c['hopg'][:-2],gload['g'])


# In[87]:

plt.scatter(c['hopg'][:-2],gload['g'])


# In[59]:




# In[ ]:



