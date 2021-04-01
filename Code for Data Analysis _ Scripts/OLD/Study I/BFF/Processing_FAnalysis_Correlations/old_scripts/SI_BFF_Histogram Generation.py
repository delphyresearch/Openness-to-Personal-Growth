
# coding: utf-8

# In[1]:

#HISTOGRAM GENERATION
#Code for Label Checking
import prettyplotlib as ppl
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[2]:

opg=pd.read_csv('reversed_and_ordered_opg_all.csv')
bff=pd.read_csv('reversed_and_ordered_bff_all.csv')


# In[8]:

opg.head()


# In[23]:

opg_col = ['PBR_1+',
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
 'IE_26-']


# In[24]:

for col in opg_col:
    print col
    ppl.hist(opg[col],bins=20)
    ppl.plt.savefig('OPG'+col+'.png')
    ppl.plt.close()


# In[30]:

bff_cols = ['BF-F1+',
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


# In[31]:

for col in bff_cols:
    print col
    ppl.hist(bff[col],bins=20)
    ppl.plt.savefig('BFF'+col+'.png')
    ppl.plt.close()


# In[ ]:



