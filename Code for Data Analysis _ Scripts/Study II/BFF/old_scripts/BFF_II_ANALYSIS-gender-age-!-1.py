
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
demo = pd.read_csv('./WorkerID_Gender_Age_pairing_BFF_II.csv')
bff = bff.convert_objects(convert_numeric=True) 
opg = opg.convert_objects(convert_numeric=True)


# In[5]:

bff.head()


# In[6]:

opg.head()


# In[7]:

demo = demo[['workerid','age','engagement']]


# In[8]:

opg = pd.merge(opg,demo,how='outer',)


# In[9]:

bff = pd.merge(bff,demo,how='outer',)


# In[10]:

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
 'IE_26-',
 'Extra_27-',
 'Extra_28+'

]


# In[11]:

correct_order_bff = [
'age','engagement',
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


# In[12]:

opg = opg[correct_order_opg]


# In[13]:

bff = bff[correct_order_bff]


# In[14]:

opg.to_csv('Ordered_II_BFF_OPG.csv')
bff.to_csv('Ordered_II_BFF.csv')


# In[15]:

cbff = bff.corr()
cbff.to_csv("STUDYII_BFF_COR_TABLE.csv")


# In[14]:

opg.head()


# In[15]:

opg_subset =  [
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
 'Extra_27-',
 'Extra_28+'
]

opg_no_extra = [
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
 'OPG_12+',
 'OPG_13+',
 'OPG_15+',
 'OPG_17-',
 'IE_19+',
 'IE_20+',
 'IE_21+',
 'IE_22-',
 'IE_24+',
 'IE_25-',]


# In[16]:

opg1=opg[opg_subset]
opg2 = opg[opg_no_extra]


# In[17]:

opg1.head()


# In[ ]:




# In[18]:

###################################
#Need to exlude age from the ffpe calculation.
bff['age'] = bff['age'].astype(str)
opg1['age'] = opg1['age'].astype(str)
opg2['age'] = opg2['age'].astype(str)

opg1['mean']=opg1.mean(axis=1,numeric_only=True)
opg2['mean']=opg2.mean(axis=1,numeric_only=True)
bff['gfp'] = bff[correct_order_bff].mean(axis=1,numeric_only=True)


# In[19]:

plt.scatter(opg2['mean'],bff['gfp'])


# In[20]:

mbff = bff[bff['engagement']=='Male']
fbff = bff[bff['engagement']=='Female']
mopg1 = opg1[opg1['engagement']=='Male']
fopg1 = opg1[opg1['engagement']=='Female']
mopg2 = opg2[opg2['engagement']=='Male']
fopg2 = opg2[opg2['engagement']=='Female']


# In[21]:

plt.scatter(mopg2['mean'],mbff['gfp'],)


# In[22]:

plt.scatter(fopg2['mean'],fbff['gfp'],)


# In[23]:

print 'total, scored as written:'
print sss.pearsonr(bff['gfp'],opg2['mean'])
print 'male:'
print sss.pearsonr(mbff['gfp'],mopg2['mean'])
print 'female:'
print sss.pearsonr(fbff['gfp'],fopg2['mean'])


# In[24]:

print 'm',len(mopg2)
print 'f',len(fopg2)


# In[25]:

############Factor Level Analysis


# In[26]:

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
    print correct_order_bff[i+1] #this is due to the extra 'gender' and agelabe;
    Neuro.append(correct_order_bff[i+1])

#reverse #64
NEUROTIC = bff[Neuro]
NEUROTIC['BF-F65+'] = pd.Series(100-NEUROTIC['BF-F65+'])


# In[27]:

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
    agree.append(correct_order_bff[i+1])
AGREE = bff[agree]
AGREE['BF-F46-'] = pd.Series(100-AGREE['BF-F46-'])


# In[28]:

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
    opn.append(correct_order_bff[i+1])
OPEN = bff[opn]


# In[29]:

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
    ext.append(correct_order_bff[i+1])
EXTRA = bff[ext]
#reverse 44,48,49 (by label, not by index)


EXTRA['BF-F44-'] = pd.Series(100-EXTRA['BF-F44-'])
EXTRA['BF-F48-'] = pd.Series(100-EXTRA['BF-F48-'])
EXTRA['BF-F49-'] = pd.Series(100-EXTRA['BF-F49-'])


# In[30]:

method_indices = [
54,
66,
6,
53,
51,
63,
40
]


# In[31]:

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
    conci.append(correct_order_bff[i+1])
CONCI = bff[conci]
CONCI['BF-F74+'] = pd.Series(100-CONCI['BF-F74+'])


# In[ ]:




# In[32]:

masterls = [Neurotic_indices,Agreeable_indices,Open_indices,Extra_indices,conci_distracted]


# In[33]:

masterls


# In[34]:

method_indices


# In[35]:

mls =[item for sublist in masterls for item in sublist]


# In[36]:

len(mls)


# In[37]:

sorted(mls)


# In[38]:

neo = []
for i in sorted(mls):
    neo.append(correct_order_bff[i+1])


# In[39]:

a = ['age','engagement'] + neo


# In[40]:

#a


# In[41]:

clnbff = bff[a]
#c


# In[42]:

#Reverse the Reversals for the overall correlation


# In[43]:

clnbff['BF-F65+'] =  pd.Series(100 - clnbff['BF-F65+'])
clnbff['BF-F46-'] = pd.Series( 100 - clnbff['BF-F46-'])
clnbff['BF-F44-'] =  pd.Series(100 - clnbff['BF-F44-'])
clnbff['BF-F48-'] =  pd.Series(100 - clnbff['BF-F48-'])
clnbff['BF-F49-'] =  pd.Series(100 - clnbff['BF-F49-'])
clnbff['BF-F74+'] =  pd.Series(100 - clnbff['BF-F74+'])


# In[44]:

clnbff.columns.values


# In[45]:

###################################
#Need to exlude age from the ffpe calculation.
clnbff['age'] = clnbff['age'].astype(str)
opg1['age'] = opg1['age'].astype(str)
opg2['age'] = opg2['age'].astype(str)

clnbff['gfp'] = clnbff.mean(axis=1,numeric_only=True)
opg1['mean']=opg1.mean(axis=1,numeric_only=True)
opg2['mean']=opg2.mean(axis=1,numeric_only=True)


# In[46]:

clnbff['age'] = clnbff['age'].astype(float)
opg1['age'] = opg1['age'].astype(float)
opg2['age'] = opg2['age'].astype(float)


# In[47]:

ccbff =clnbff.drop(['age','engagement'],axis=1)
copg1 = opg1.drop(['age','engagement'],axis=1)
copg2 = opg2.drop(['age','engagement'],axis=1)


# In[48]:

##############################DESCRIPTIVE STATISTICS
bffstds = clnbff.std(axis=0)
bffmeans = clnbff.mean(axis=0)
hopgstds = copg1.std(axis=0)
hopgmeans = copg1.mean(axis=0)




# In[53]:

bffstds.to_csv("studyII_bffstds.csv")
bffmeans.to_csv("studyII_bffmeans.csv")
hopgstds.to_csv("studyII_final_hopgstds.csv")
hopgmeans.to_csv("studyII_final_hopgmeans.csv")


# In[70]:

fig = plt.figure(figsize=(7.5, 5.5))
plt.scatter(opg1['mean'],ccbff['gfp'],alpha=.5,s=30)
#scored as written
#plt.plot([30, 90], [30, 90], color='k', linestyle='-', linewidth=1)
plt.plot(opg1['mean'], np.poly1d(np.polyfit(opg1['mean'],ccbff['gfp'], 1))(opg1['mean']), color = 'k', linewidth=1,alpha=.95)
plt.xlabel('H/OPG')
plt.ylabel('BFF GFP Estimate Study II')
plt.xlim((20,100))
plt.ylim((20,100))
plt.savefig('SCIENCE_BFF_HOPG_II_LINE.png',format='png', dpi=300
            )
plt.show()


# In[62]:

fig = plt.figure(figsize=(7.5, 5.5))
plt.scatter(opg1['mean'],ccbff['gfp'],alpha=.5,s=30)
#scored as written
#plt.plot([30, 90], [30, 90], color='k', linestyle='-', linewidth=1)
#plt.plot(opg1['mean'], np.poly1d(np.polyfit(opg1['mean'],ccbff['gfp'], 1))(opg1['mean']), color = 'k', linewidth=,alpha=.8)
plt.xlabel('H/OPG')
plt.ylabel('BFF GFP Estimate Study II')
plt.xlim((20,100))
plt.ylim((20,100))
#plt.savefig('SCIENCE_BFF_HOPG_II.png',format='png', dpi=300
#            )
plt.show()


# In[50]:

fig = plt.figure(figsize=(7.5, 5.5))
plt.scatter(copg1['mean'],ccbff['gfp'],alpha=.5,s=30)
#scored as written
plt.xlabel('H/OPG')
plt.ylabel('BFF FFPE Estimate Study II')
plt.xlim((20,100))
plt.ylim((20,100))
#plt.savefig('SCIENCE_BFF_HOPG_II.png',format='png', dpi=300
#            )
plt.show()


# In[49]:

sss.pearsonr(ccbff['gfp'],copg1['mean'])


# In[50]:

len(copg1)


# In[51]:

sss.pearsonr(ccbff['gfp'],copg2['mean'])


# In[54]:

#for each factor:
constructs = [AGREE,NEUROTIC,OPEN,CONCI,EXTRA]
for construct in constructs:
    print sss.pearsonr(copg1['mean'],construct.mean(axis=1))


# In[63]:

copg1.head()


# In[64]:

copg2.head()


# In[62]:

mbff = clnbff[clnbff['engagement']=='Male']
fbff = clnbff[clnbff['engagement']=='Female']
mopg2 = opg2[opg2['engagement']=='Male']
fopg2 = opg2[opg2['engagement']=='Female']
mopg1 = opg1[opg1['engagement']=='Male']
fopg1 = opg1[opg1['engagement']=='Female']


# In[62]:




# In[63]:

plt.scatter(opg1['mean'],clnbff['gfp'])


# In[64]:

plt.scatter(mopg1['mean'],mbff['gfp'])


# In[65]:

plt.scatter(fopg1['mean'],fbff['gfp'])


# In[52]:

print 'total, scored as written:'
print sss.pearsonr(clnbff['gfp'],opg2['mean'])
print 'male:'
print sss.pearsonr(mbff['gfp'],mopg2['mean'])
print 'female:'
print sss.pearsonr(fbff['gfp'],fopg2['mean'])

#Not significant. Not large enough sample size anyways.


# In[53]:

print 'total, scored as written:'
print sss.pearsonr(clnbff['gfp'],opg1['mean'])
print 'male:'
print sss.pearsonr(mbff['gfp'],mopg1['mean'])
print 'female:'
print sss.pearsonr(fbff['gfp'],fopg1['mean'])


# In[67]:

print len(mbff)
print len(fbff)


# In[55]:

clnbff.age.max()


# In[68]:

#######################BY AGE
########BY AGE

def age_stuff(start,stop,step):
    A = []
    for age in range(start,stop,step):
        print age
        print 'SAMPLE SIZE:'
        print len(clnbff[
            (clnbff['age']<age) & (clnbff['age']>(age-step))])
        A.append(sss.pearsonr(clnbff[(clnbff['age']<age) & (clnbff['age']>(age-step))]['gfp'],opg2[(opg2['age']<age) & (opg2['age']>(age-step))]['mean']))
        plt.figure()
        plt.scatter(clnbff[(clnbff['age']<age) & (clnbff['age']>(age-step))]['gfp'],opg2[(opg2['age']<age) & (opg2['age']>(age-step))]['mean'])
        plt.title(age)
    return A


# In[60]:

print sss.pearsonr(clnbff[(clnbff['age']<29) 
                    & (clnbff['age']>(17))]['gfp'],opg2[(opg2['age']<29) & (opg2['age']>(17))]['mean'])
print len(
    
    clnbff[(clnbff['age']<28) 
                    & (clnbff['age']>(17))]['gfp'])




# In[61]:

print sss.pearsonr(clnbff[(clnbff['age']<39) 
                    & (clnbff['age']>(27))]['gfp'],opg2[(opg2['age']<39) & (opg2['age']>(27))]['mean'])
print len(
    
    clnbff[(clnbff['age']<39) 
                    & (clnbff['age']>(27))]['gfp'])


# In[62]:

print sss.pearsonr(clnbff[(clnbff['age']<49) 
                    & (clnbff['age']>(37))]['gfp'],opg2[(opg2['age']<49) & (opg2['age']>(37))]['mean'])
print len(
    
    clnbff[(clnbff['age']<49) 
                    & (clnbff['age']>(37))]['gfp'])


# In[63]:

print sss.pearsonr(clnbff[(clnbff['age']<59) 
                    & (clnbff['age']>(47))]['gfp'],opg2[(opg2['age']<59) & (opg2['age']>(47))]['mean'])
print len(
    
    clnbff[(clnbff['age']<59) 
                    & (clnbff['age']>(47))]['gfp'])


# In[71]:

print sss.pearsonr(clnbff[(clnbff['age']>58)]['gfp'],opg2[(opg2['age']>58)]['mean'])
print len(
  clnbff[clnbff['age']>58])
                   
#Given these small samples, sizes, let's combine with above


# In[72]:

print sss.pearsonr(clnbff[(clnbff['age']>(47))]['gfp'],opg2[(opg2['age']>47)]['mean'])
print len(
    clnbff[(clnbff['age']>(47))]['gfp'])


# In[53]:

fig = plt.figure(figsize=(15, 9))
plt.scatter(opg1['mean'],clnbff['gfp'],alpha=.5,s=30)
plt.title('Humility vs GFP, Naive, N =  434, no outliers discarded,volatility->stability')
plt.xlabel('Naive Humility Estimate')
plt.ylabel('Naive GFP Estimate')
#plt.savefig('Naive_estimates_bffopg_10_20_Raw_labeled_axes.png',format='png', dpi=500
#            )
plt.show()


# In[70]:

print sss.pearsonr(opg1['mean'],clnbff['gfp'])
print sss.pearsonr(opg2['mean'],clnbff['gfp'])


# In[71]:

factor_measures = [AGREE,NEUROTIC,OPEN,EXTRA,CONCI]


# In[72]:

for m in factor_measures:
    #measures = [AGREE,NEUROTIC,OPEN,EXTRA,CONCI]
    print sss.pearsonr(opg1['mean'],m.mean(axis=1))
    #[AGREE,NEUROTIC,OPEN,EXTRA,CONCI]


# In[58]:

bff.head()


# In[59]:

clnbff.head()


# In[57]:

bff['meanopg']=opg1['mean']


# In[42]:

import os
os.getcwd()


# In[55]:

dfl = pd.read_csv('./BFF_II_OMEGA_FA_6_LOADING_FIGSHARE.csv')
dfl.convert_objects(convert_numeric=True)


# In[56]:

dfl.head()


# In[57]:

dfl.tail(9)


# In[57]:




# In[58]:

ccbff.head()


# In[59]:

ccc = ccbff.drop(['gfp'],axis=1)


# In[60]:

ccc['meanopg1'] = opg1['mean']
ccc['meanopg2'] = opg2['mean']


# In[61]:

cc = ccc.corr()


# In[62]:

cc.tail()


# In[63]:

len(cc)


# In[64]:

cc


# In[65]:

cc['meanopg1'][:-2]


# In[66]:

print len(dfl['g'])
print len(cc['meanopg1'][:-2])


# In[67]:

z = cc['meanopg1'][:-2]


# In[68]:

z.sort()
z


# In[69]:

fig = plt.figure(figsize=(15, 9))
plt.scatter(cc['meanopg1'][:-2],dfl['g'],alpha=.5,s=30)
plt.title('Humilty loadings vs g, STUDY II BFF')
plt.xlabel('Humility')
plt.ylabel('G')
#plt.savefig('Naive_estimates_bffopg_10_20_Raw_labeled_axes.png',format='png', dpi=500
#            )
plt.show()


# In[72]:

fig = plt.figure(figsize=(15, 9))
plt.scatter(cc['meanopg2'][:-2],dfl['g'],alpha=.5,s=30)
plt.title('Humilty loadings vs g, STUDY II BFF')
plt.xlabel('Humility')
plt.ylabel('G')
#plt.savefig('Naive_estimates_bffopg_10_20_Raw_labeled_axes.png',format='png', dpi=500
#            )
plt.show()


# In[71]:

print sss.pearsonr(cc['meanopg1'][:-2],dfl['g'])#2.1
print sss.pearsonr(cc['meanopg2'][:-2],dfl['g'])#2.0


# In[75]:

fig = plt.figure(figsize=(7.5, 5.5))
plt.scatter(cc['meanopg2'][:-2],dfl['g'],s=30)
#scored as written
plt.xlabel('H-OPG - item correlations')
plt.ylabel('BFF item general factor loadings ')
plt.xlim(xmin=-.3)
plt.ylim(ymin=-.3)
plt.savefig('BFF_HOPG_Gloadings_II.eps',format='eps', dpi=450
            )
plt.show()


# In[ ]:



