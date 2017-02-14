
# coding: utf-8

# In[1]:

import pandas as pd
import numpy
import matplotlib
from  matplotlib import pyplot as plt
import scipy.stats.stats as sss
get_ipython().magic(u'matplotlib inline')


# In[2]:

pd.set_option('display.max_columns', None)


# In[3]:

bff = pd.read_csv('./Master_preprocessed_BFF.csv')
opg = pd.read_csv('./Master_preprocessed_BFFOPG.csv')
bff = bff.convert_objects(convert_numeric=True) 
opg = opg.convert_objects(convert_numeric=True)


# In[4]:

bff.head()


# In[5]:

opg.head()


# In[6]:

correct_order_opg = ['workerid','PBR_1+',
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
 'IE_23-','IE_24+','IE_25-','IE_26-',
]


# In[7]:

opg = opg[correct_order_opg]


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
 'BF-F17-',
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
 'BF-F28-',
 'BF-F29+',
 'BF-F30+',
 'BF-F31+',
 'BF-F32+',
 'BF-F33+',
 'BF-F34-',
 'BF-F35-',
 'BF-F36-',
 'BF-F37-',
 'BF-F38-',
 'BF-F39-',
 'BF-F40+',
 'BF-F41+',
 'BF-F42+',
 'BF-F43+',
 'BF-F44-',
 'BF-F45-',
 'BF-F46-',
 'BF-F47-',
 'BF-F48-',
 'BF-F49-',
 'BF-F50+',
 'BF-F51-',
 'BF-F52+',
 'BF-F53+',
 'BF-F54+',
 'BF-F55+',
 'BF-F56-',
 'BF-F57-',
 'BF-F58+',
 'BF-F59+',
 'BF-F60-',
 'BF-F61+',
 'BF-F62+',
 'BF-F63+',
 'BF-F64+',
 'BF-F65+',
 'BF-F66+',
 'BF-F67-',
 'BF-F68-',
 'BF-F69+',
 'BF-F70-',
 'BF-F71+',
 'BF-F72+',
 'BF-F73+',
 'BF-F74+',
 'BF-F75+',
 'BF-F76+',
 'BF-F77+',
 'BF-F78-',
 'BF-F79-',
 'BF-F80-',
 'BF-F81-',
 'BF-F82+',
 'BF-F83-',
 'BF-F84+',
 'BF-F85+',
 'BF-F86+',
 'BF-F87+',
 'BF-F88+',
 'BF-F89+',
 'BF-F90-',
 'BF-F91-',
 'BF-F92+',
 'BF-F93+',
 'BF-F94+',
 'BF-F95+',
 'BF-F96+',
 'BF-F97+',
 'BF-F98+',
 'BF-F99+',
 'BF-F100+',
 'BF-F101+',
 'BF-F102+']


# In[9]:

bff = bff[correct_order_bff]


# In[10]:

cbff = bff.corr()
cbff.to_csv('STUDY_I_BFF_CORR_TABLE.csv')


# In[10]:

#bff.to_csv('master_ordered_and_preprocessed_bff.csv')
#opg.to_csv('master_ordered_and_preprocessed_bffopg.csv')
#bff = pd.read_csv('master_ordered_and_preprocessed_bff.csv')
#opg = pd.read_csv('master_ordered_and_preprocessed_bffopg.csv')


# In[11]:

#bff = bff[bff.columns.values.tolist()[1:]


# In[12]:

opg.head()


# In[13]:

#Histograms
import prettyplotlib as ppl
#for i in bff.columns.values.tolist():
    print i
    ppl.hist(bff[i],bins=20)
    ppl.plt.savefig(i+'.png')
    ppl.plt.close()


# In[14]:

opg_subset =  [
 'PBR_1+',
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


# In[15]:

opg=opg[opg_subset]


# In[16]:

opg.head()


# In[17]:

opg['mean'] = opg.mean(axis=1)


# In[18]:

bff['gfp'] = bff.mean(axis=1)


# In[ ]:




# In[19]:

opg.head()


# In[20]:

bff.head()


# In[21]:

len(bff)


# In[ ]:




# In[ ]:




# In[ ]:




# In[22]:

############################
clnbff = bff


# In[23]:

#INFO FROM FACTOR ANALYSIS (FA(BFF,7,minres,oblimn))
# reverse all the items that negatively loaded on to their factors...
clnbff['BF-F33+'] =  pd.Series(100 - clnbff['BF-F33+'])
clnbff['BF-F32+'] = pd.Series( 100 - clnbff['BF-F32+'])
clnbff['BF-F101+'] =  pd.Series(100 - clnbff['BF-F101+'])
clnbff['BF-F52+'] =  pd.Series(100 - clnbff['BF-F52+'])
clnbff['BF-F54+'] =  pd.Series(100 - clnbff['BF-F54+'])
clnbff['BF-F95+'] =  pd.Series(100 - clnbff['BF-F95+'])
clnbff['BF-F37-'] =  pd.Series(100 - clnbff['BF-F37-'])
clnbff['BF-F34-'] =  pd.Series(100 - clnbff['BF-F34-'])
clnbff['BF-F35-'] =  pd.Series(100 - clnbff['BF-F35-'])
clnbff['BF-F39-'] =  pd.Series(100 - clnbff['BF-F39-'])


# In[24]:

Agreeableness_indexes = [23,
22,
21,
27,
24,
26,
30,
28,
25,
65,
63,
64,
67,
31,
17,
66,
61,
62,
19]



agree = []
for i in sorted(Agreeableness_indexes):
    agree.append(correct_order_bff[i-1])
AGREE = bff[agree]


# In[25]:

AGREE.head()


# In[26]:

Volatility_indexes = [5,
1,
4,
2,
7,
8,
9,
3,
14,
6,
38,
36]


# In[27]:

Withdrawal_indexes = [15,#last two are reversed....
11,
10,
12,
80,
18,
78,
13,
79,
16,
20,
81,
70,
91,
83,
33,
32
]


# In[ ]:




# In[28]:

rneuro = []
Volatility_indexes.extend(Withdrawal_indexes)

for i in sorted(Volatility_indexes):
    rneuro.append(correct_order_bff[i-1])

#reverse the last twoo


# In[29]:

NEUROTIC = bff[rneuro]
NEUROTIC['BF-F32+'] = pd.Series(100-NEUROTIC['BF-F32+'])
NEUROTIC['BF-F33+'] = pd.Series(100-NEUROTIC['BF-F33+'])


# In[30]:

Volatility_indexes


# In[ ]:




# In[31]:

Openness_indexes = [86,
88,
94,
98,
102,
89,
97,
99,
92,
87,
84,
93,
82,
96,
85,
100,
90,
52,54,95]

opn = []
for i in sorted(Openness_indexes):
    opn.append(correct_order_bff[i-1])
OPEN = bff[opn]
OPEN['BF-F52+'] = pd.Series(100-OPEN['BF-F52+'])
OPEN['BF-F54+'] = pd.Series(100-OPEN['BF-F54+'])
OPEN['BF-F95+'] = pd.Series(100-OPEN['BF-F95+'])


# In[32]:

Concientiousness_org_indexes = [49, #last one is reversed
44,
56,
45,
59,
57,
48,
58,
47,
60,
51,
46,
68,
50,
101]


# In[33]:

Concientiousness_indus_indexes = [55,
40,
43,
42,
41,
53]


# In[34]:

conci = []
Concientiousness_indus_indexes.extend(Concientiousness_org_indexes)

for i in sorted(Concientiousness_indus_indexes):
    conci.append(correct_order_bff[i-1])
CONCI = bff[conci]
CONCI['BF-F101+'] = pd.Series(100-CONCI['BF-F101+'])


# In[35]:

CONCI.head()


# In[ ]:




# In[36]:

Extraversion_assert_indexes = [76,
77,
73,
71,
72,
75,
74,
69,
29,
37,
34,35,39]


# In[37]:

ext = []
for i in sorted(Extraversion_assert_indexes):
    ext.append(correct_order_bff[i-1])
EXTRA = bff[ext]
#reverse 37,34,35,39

EXTRA['BF-F37-'] = pd.Series(100-EXTRA['BF-F37-'])
EXTRA['BF-F34-'] = pd.Series(100-EXTRA['BF-F34-'])
EXTRA['BF-F35-'] = pd.Series(100-EXTRA['BF-F35-'])
EXTRA['BF-F39-'] = pd.Series(100-EXTRA['BF-F39-'])


# In[38]:

factor_measures = [AGREE,NEUROTIC,OPEN,EXTRA,CONCI]


# In[39]:

masterls = [Agreeableness_indexes,Volatility_indexes,Openness_indexes,Concientiousness_indus_indexes,Extraversion_assert_indexes]


# In[40]:

mls =[item for sublist in masterls for item in sublist]


# In[41]:

factor_measures[0]


# In[42]:

colls=bff.columns.values.tolist()


# In[43]:

sorted(mls)


# In[44]:

len(mls)


# In[45]:

neo = []
for i in sorted(mls):
    neo.append(correct_order_bff[i-1])


# In[46]:

neo


# In[47]:

clnbff = bff[neo]


# In[48]:

# reverse all the items that negatively loaded on to their factors...
clnbff['BF-F33+'] =  pd.Series(100 - clnbff['BF-F33+'])
clnbff['BF-F32+'] = pd.Series( 100 - clnbff['BF-F32+'])
clnbff['BF-F101+'] =  pd.Series(100 - clnbff['BF-F101+'])
clnbff['BF-F52+'] =  pd.Series(100 - clnbff['BF-F52+'])
clnbff['BF-F54+'] =  pd.Series(100 - clnbff['BF-F54+'])
clnbff['BF-F95+'] =  pd.Series(100 - clnbff['BF-F95+'])
clnbff['BF-F37-'] =  pd.Series(100 - clnbff['BF-F37-'])
clnbff['BF-F34-'] =  pd.Series(100 - clnbff['BF-F34-'])
clnbff['BF-F35-'] =  pd.Series(100 - clnbff['BF-F35-'])
clnbff['BF-F39-'] =  pd.Series(100 - clnbff['BF-F39-'])




# In[49]:

clnbff['gfp'] = clnbff.mean(axis=1)


# In[51]:

fig = plt.figure(figsize=(7.5, 5.5))
plt.scatter(opg.mean(axis=1),clnbff['gfp'],alpha=.5,s=30)
#plt.title('Humility vs GFP, Factor Analyzed, N =  434')
plt.xlabel('H/OPG')
plt.ylabel('BFF GFP Estimate')
plt.xlim((25,100))
plt.ylim((25,100))
plt.savefig('SCIENCE_BFF_HOPG_I.png',format='png', dpi=300
            )
plt.show()


# In[47]:

fig = plt.figure(figsize=(15, 9))
plt.scatter(opg['mean'],clnbff['gfp'],alpha=.5,s=30)
plt.title('Humility vs GFP, Naive, N =  434, no outliers discarded,volatility->stability')
plt.xlabel('Naive Humility Estimate')
plt.ylabel('Naive GFP Estimate')
#plt.savefig('Naive_estimates_bffopg_10_20_Raw_labeled_axes.png',format='png', dpi=500
#            )
plt.show()


# In[ ]:




# In[ ]:




# In[109]:

len(opg)


# In[54]:

print sss.pearsonr(opg['mean'],clnbff['gfp']) #Over all correlation FFPE and H_OPG


# In[111]:

for m in factor_measures:
    #measures = [AGREE,NEUROTIC,OPEN,EXTRA,CONCI]
    print sss.pearsonr(opg['mean'],m.mean(axis=1))
    #[AGREE,NEUROTIC,OPEN,EXTRA,CONCI]


# In[123]:

for m in factor_measures:
    #measures = [AGREE,NEUROTIC,OPEN,EXTRA,CONCI]
    plt.scatter(opg['mean'],m.mean(axis=1))
    plt.show()
    #[AGREE,NEUROTIC,OPEN,EXTRA,CONCI]


# In[55]:


df_loadings = pd.read_csv('./STUDY_I_BFF_7_G_SOLUTION.csv')
dfl = df_loadings
dfl.head()


# In[56]:

clnbff['opg'] = opg['mean']


# In[57]:

bff.tail()


# In[58]:

c = clnbff.corr()


# In[59]:

plt.scatter(c['opg'][:-2],dfl['g'])


# In[62]:

fig = plt.figure(figsize=(11,7))
plt.scatter(c['opg'][:-2],dfl['g'],alpha=.7,s=30)
#plt.title('Humility vs GFP, Factor Analyzed, N =  434')
plt.xlabel('H-OPG - Item correlations')
plt.ylabel('g Loading on item')
plt.xlim(xmin=-.3)
plt.ylim(ymin=-.3)
plt.savefig('g_vs_HOPG_loadings_BFF.eps',format='eps', dpi=500
           )
plt.show()


# In[135]:

f.sort()


# In[136]:

f


# In[137]:

sss.pearsonr(c['opg'][:-2],dfl['g'])


# In[68]:



