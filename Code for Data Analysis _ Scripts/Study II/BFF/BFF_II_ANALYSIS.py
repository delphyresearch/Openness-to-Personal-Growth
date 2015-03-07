
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib
from  matplotlib import pyplot as plt
import scipy.stats.stats as sss

get_ipython().magic(u'matplotlib inline')
#import pystan
from __future__ import division


# In[2]:

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 30)


# In[3]:

import os
os.getcwd()


# In[4]:

bff= pd.read_csv('./BFF_II_Pre.csv')
opg = pd.read_csv('./OPG_II_Pre.csv')
bff = bff.convert_objects(convert_numeric=True) 
opg = opg.convert_objects(convert_numeric=True)


# In[5]:

bff.head()


# In[6]:

opg.head()


# In[7]:

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
 'Extra_27-',
 'Extra_28+'

]


# In[8]:

correct_order_bff = [
 'BF-F1+',
 'BF-F2+',
 'BF-F3+',
 'BF-F4+',
 'BF-F5+',
 'BF-F6-',
 'BF-F7+',
 'BF-F8+',
 'BF-F9+',
 'BF-F10+',
 'BF-F11+',
 'BF-F12+',
 'BF-F13+',
 'BF-F14+',
 'BF-F15+',
 'BF-F16+',
 'BF-F17+',
 'BF-F18+',
 'BF-F19-',
 'BF-F20+',
 'BF-F21+',
 'BF-F22+',
 'BF-F23+',
 'BF-F24+',
 'BF-F25+',
 'BF-F26+',
 'BF-F27+',
 'BF-F28+',
 'BF-F29+',
 'BF-F30+',
 'BF-F31+',
 'BF-F32+',
 'BF-F33+',
 'BF-F34-',
 'BF-F35+',
 'BF-F36+',
 'BF-F37+',
 'BF-F38+',
 'BF-F39+',
 'BF-F40+',
 'BF-F41+',
 'BF-F42-',
 'BF-F43+',
 'BF-F44-',
 'BF-F45+',
 'BF-F46-',
 'BF-F47-',
 'BF-F48-',
 'BF-F49-',
 'BF-F50+',
 'BF-F51+',
 'BF-F52+',
 'BF-F53+',
 'BF-F54+',
 'BF-F55-',
 'BF-F56-',
 'BF-F57-',
 'BF-F58-',
 'BF-F59-',
 'BF-F60-',
 'BF-F61+',
 #'BF-F62+',#Skipped this in the labeling process
 'BF-F63-',
 'BF-F64+',
 'BF-F65+',
 'BF-F66-',
 'BF-F67+',
 'BF-F68-',
 'BF-F69-',
 'BF-F70+',
 'BF-F71+',
 'BF-F72-',
 'BF-F73+',
 'BF-F74+',
 'BF-F75+',
 'BF-F76+',
 'BF-F77+',
 'BF-F78+',
 'BF-F79+',
 'BF-F80+',
 'BF-F81+',
 'BF-F82+',
 'BF-F83+',
 'BF-F84+',
 'BF-F85+',
 'BF-F86+',
 'BF-F87+',
 'BF-F88+',
 'BF-F89+',
 'BF-F90+',
 'BF-F91+',
 'BF-F92+',
 'BF-F93+',
 'BF-F94+',
 'BF-F95-',
 'BF-F96+',
 'BF-F97+',
 'BF-F98+',
 'BF-F99+',
 'BF-F100+',
 'BF-F101+',
 'BF-F102+',
 'BF-F103+',
 'BF-F104+',
 'BF-F105+']


# In[9]:

opg = opg[correct_order_opg]


# In[10]:

bff = bff[correct_order_bff]


# In[11]:

opg.to_csv('Ordered_II_BFF_OPG.csv')
bff.to_csv('Ordered_II_BFF.csv')


# In[12]:

opg.head()


# In[13]:

opg_subset =  [
 'PBR_1+',
 'PBR_2-',
 'PBR_3+',
 'PBR_4+',
 'PBR_5+',
 'PBR_6-',
 'PBR_7-',
 'PBR_8-',
# 'OPG_9+',
 'OPG_10+',
 'OPG_12+',
 'OPG_13+',
 'OPG_15+',
 #'OPG_17-',
 'IE_19+',
 'IE_20+',
 'IE_21+',
 'IE_22-',
 'IE_24+',
 'IE_25-',
 'Extra_27-',
 'Extra_28+'
]

opg_no_extra = [
 'PBR_1+',
 'PBR_2-',
 'PBR_3+',
 'PBR_4+',
 'PBR_5+',
 'PBR_6-',
 'PBR_7-',
 'PBR_8-',
# 'OPG_9+',
 'OPG_10+',
 'OPG_12+',
 'OPG_13+',
 'OPG_15+',
 #'OPG_17-',
 'IE_19+',
 'IE_20+',
 'IE_21+',
 'IE_22-',
 'IE_24+',
 'IE_25-',]


# In[14]:

opg1=opg[opg_subset]
opg2 = opg[opg_no_extra]


# In[15]:

opg1.head()


# In[16]:

bff['gfp'] = bff[correct_order_bff].mean(axis=1)


# In[17]:

opg1['mean'] = opg1.mean(axis=1)
opg2['mean'] = opg2.mean(axis=1)


# In[18]:

import os
os.getcwd()


# In[19]:

############Factor Level Analysis


# In[20]:

Neurotic_indices = [2,
4,
5,
7,
9,
15,
8,
1,
11,
16,
12,
17,
3,
13,
18,
14,
47,
10,
20,
26,
64,
19
]
Neuro = []


for i in Neurotic_indices:
    Neuro.append(correct_order_bff[i-1])

#reverse #64
NEUROTIC = bff[Neuro]
NEUROTIC['BF-F65+'] = pd.Series(100-NEUROTIC['BF-F65+'])


# In[21]:

Agreeable_indices = [
27,
30,
29,
32,
28,
33,
31,
36,
34,
39,
50,
41,
45,
37,
43,
38,

46
]


agree = []
for i in sorted(Agreeable_indices):
    agree.append(correct_order_bff[i-1])
AGREE = bff[agree]
AGREE['BF-F46-'] = pd.Series(100-AGREE['BF-F46-'])


# In[22]:

Open_indices = [
92,
90,
97,
104,
100,
93,
91,
89,
88,
101,
95,
96,
102,
103,
76,
94,
98,
99
]

opn = []
for i in sorted(Open_indices):
    opn.append(correct_order_bff[i-1])
OPEN = bff[opn]


# In[23]:

Extra_indices = [
75,
79,
78,
82,
85,
83,
81,
74,
80,
84,
87,
77,
42,
35,
72,
86,
44,48,49,61]

ext = []
for i in sorted(Extra_indices):
    ext.append(correct_order_bff[i-1])
EXTRA = bff[ext]
#reverse 44,48,49 (by label, not by index)


EXTRA['BF-F44-'] = pd.Series(100-EXTRA['BF-F44-'])
EXTRA['BF-F48-'] = pd.Series(100-EXTRA['BF-F48-'])
EXTRA['BF-F49-'] = pd.Series(100-EXTRA['BF-F49-'])


# In[24]:

method_indices = [
54,
66,
6,
53,
51,
63,
40
]


# In[25]:

conci_distracted = [
55,
60,
67,
56,
59,
58,
65,
68,
70,
69,
71,
57,
62,
52,
23,
24,
25,
22,
73,
21
]

conci = []
conci_distracted.extend(method_indices)
for i in sorted(conci_distracted):
    conci.append(correct_order_bff[i-1])
CONCI = bff[conci]
CONCI['BF-F74+'] = pd.Series(100-CONCI['BF-F74+'])


# In[25]:




# In[26]:

masterls = [Neurotic_indices,Agreeable_indices,Open_indices,Extra_indices,conci_distracted]


# In[27]:

masterls


# In[28]:

method_indices


# In[29]:

mls =[item for sublist in masterls for item in sublist]


# In[30]:

len(mls)


# In[31]:

sorted(mls)


# In[32]:

neo = []
for i in sorted(mls):
    neo.append(correct_order_bff[i-1])


# In[33]:

clnbff = bff[neo]


# In[34]:

#Reverse the Reversals for the overall correlation

rlist= [64,46,22,44,48,49,73]


# In[35]:

clnbff['BF-F65+'] =  pd.Series(100 - clnbff['BF-F65+'])
clnbff['BF-F46-'] = pd.Series( 100 - clnbff['BF-F46-'])
clnbff['BF-F22+'] =  pd.Series(100 - clnbff['BF-F22+'])
clnbff['BF-F44-'] =  pd.Series(100 - clnbff['BF-F44-'])
clnbff['BF-F54+'] =  pd.Series(100 - clnbff['BF-F54+'])
clnbff['BF-F48-'] =  pd.Series(100 - clnbff['BF-F48-'])
clnbff['BF-F49-'] =  pd.Series(100 - clnbff['BF-F49-'])
clnbff['BF-F74+'] =  pd.Series(100 - clnbff['BF-F74+'])


# In[36]:

clnbff['gfp'] = clnbff.mean(axis=1)


# In[37]:

fig = plt.figure(figsize=(15, 9))
plt.scatter(opg1['mean'],clnbff['gfp'],alpha=.5,s=30)
plt.title('Humility vs GFP, Naive, N =  434, no outliers discarded,volatility->stability')
plt.xlabel('Naive Humility Estimate')
plt.ylabel('Naive GFP Estimate')
#plt.savefig('Naive_estimates_bffopg_10_20_Raw_labeled_axes.png',format='png', dpi=500
#            )
plt.show()


# In[38]:

print sss.pearsonr(opg1['mean'],clnbff['gfp'])
print sss.pearsonr(opg2['mean'],clnbff['gfp'])


# In[39]:

factor_measures = [AGREE,NEUROTIC,OPEN,EXTRA,CONCI]


# In[40]:

for m in factor_measures:
    #measures = [AGREE,NEUROTIC,OPEN,EXTRA,CONCI]
    print sss.pearsonr(opg1['mean'],m.mean(axis=1))
    #[AGREE,NEUROTIC,OPEN,EXTRA,CONCI]


# In[41]:

bff['meanopg']=opg1['mean']


# In[54]:

import os
os.getcwd()


# In[84]:

dfl = pd.read_csv('./BFF/STUDY_II_BFF_7_G_LOADS7.csv')
dfl.convert_objects(convert_numeric=True)


# In[85]:

dfl.head()


# In[97]:

dfl.tail(9)


# In[87]:

bff['meanopg1'] = opg1['mean']
bff['meanopg2'] = opg2['mean']


# In[88]:

cc = bff.corr()


# In[89]:

cc.tail()


# In[90]:

len(cc)


# In[91]:

cc


# In[98]:

print len(dfl['g'][:-8])
print len(cc['meanopg1'][:-4])


# In[101]:

fig = plt.figure(figsize=(15, 9))
plt.scatter(cc['meanopg1'][:-4],dfl['g'][:-8],alpha=.5,s=30)
plt.title('Humilty loadings vs g, STUDY II BFF')
plt.xlabel('Humility')
plt.ylabel('G')
#plt.savefig('Naive_estimates_bffopg_10_20_Raw_labeled_axes.png',format='png', dpi=500
#            )
plt.show()


# In[103]:

fig = plt.figure(figsize=(15, 9))
plt.scatter(cc['meanopg2'][:-4],dfl['g'][:-8],alpha=.5,s=30)
plt.title('Humilty loadings vs g, STUDY II BFF')
plt.xlabel('Humility')
plt.ylabel('G')
#plt.savefig('Naive_estimates_bffopg_10_20_Raw_labeled_axes.png',format='png', dpi=500
#            )
plt.show()


# In[104]:

print sss.pearsonr(cc['meanopg1'][:-4],dfl['g'][:-8])
print sss.pearsonr(cc['meanopg2'][:-4],dfl['g'][:-8])


# In[105]:




# In[ ]:



