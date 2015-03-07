
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas.io import sql
import sqlalchemy as sa
import yaml as yml
import json
import demjson
get_ipython().magic(u'matplotlib inline')
pd.set_option('display.max_columns', None)


# In[2]:

engine = sa.create_engine('mysql://(*&^%$%^&*(*&^%$#%^&*(*&^%$)))/personality')
con = engine.raw_connection()
df = sql.read_frame("SELECT * FROM BFASopg union select * from bffopg ", con)
con.close()


# In[3]:

len(df)


# In[4]:

df.tail()


# In[4]:




# In[4]:




# In[5]:

def transform(df):
    for i,row in df.iterrows():
       # print row.index


        jstrng = row['datastring']
        if jstrng =='':
            pass
        else:
            try:
                curr_dict = json.loads(jstrng)
            except:
                continue
            curr_keys = curr_dict.keys()
            df.append(curr_keys)
            for key in curr_keys:
                if key == 'data':
                    for j in curr_dict['data']:
                        jj = j['trialdata']
                        if 'answer' in jj:
                            item_id = jj['id']
                            rawanswer  = jj['answer']
                           # print item_id
                            df.append([item_id])
                            df.loc[i,item_id] = rawanswer

                else:
                #df.ix[i,key]= str(curr_dict[key])
                    df.loc[i,key]=str(curr_dict[key])
                #row[key]=str(curr_dict[key])
            #delete extraneous rows

        #out = df[df['asked_question_number']>2]
        #outt = out[out['asked_question_number']<131]
    return df


# In[6]:

tdf = transform(df)


# In[7]:

len(tdf)


# In[8]:

masterdf = tdf[tdf['status']==4]


# In[9]:

len(masterdf)


# In[10]:

masterdf.head()


# In[11]:

opg_cols = ['workerId',u'PBR_1+',
 u'PBR_2-',
 u'PBR_3+',
 u'PBR_4+',
 u'PBR_5+',
 u'PBR_6-',
 u'PBR_7-',
 u'PBR_8-',
  u'OPG_9+',
 u'OPG_10+',
 u'OPG_11-',
 u'OPG_12+',
 u'OPG_13+',
 u'OPG_14+',
 u'OPG_15+',
 u'OPG_16+',
 u'OPG_17-',
 u'OPG_18-',
 u'IE_19+',
 u'IE_20+',
 u'IE_21+',
 u'IE_22-',
 u'IE_23-',
 u'IE_24+',
 u'IE_25-',
 u'IE_26-']


# In[12]:

masteropg = masterdf[opg_cols]


# In[13]:

m = masteropg.drop_duplicates()


# In[14]:

print len(masteropg)
print len(m)


# In[14]:




# In[15]:

opg = masteropg[masteropg['PBR_1+'].notnull()]


# In[16]:

len(opg)


# In[16]:




# In[17]:

opg = opg.convert_objects(convert_numeric=True)


# In[18]:

opg.tail(10)


# In[19]:

opg = opg.drop_duplicates()


# In[20]:

len(opg)


# In[21]:

#ITEM SPECIFIC ADJUSTMENTS

#Middle Distance
opg['OPG_16+'] = 100-2*abs(opg['OPG_16+']-50)
opg['IE_21+'] = 100-2*abs(opg['IE_21+']-50)

#Stretching, because marking '100%' would mean a '90' without this:
opg['PBR_1+'] = ((opg['PBR_1+']-50)*1.1)+50
opg['PBR_3+'] = ((opg['PBR_3+']-50)*1.1)+50
opg['OPG_15+'] = ((opg['OPG_15+']-50)*1.1)+50

#rounding to within actual limits:
opg['PBR_1+'] = opg['PBR_1+'].apply(lambda x: 100 if x>100 else x)
opg['PBR_3+'] = opg['PBR_3+'].apply(lambda x: 100 if x>100 else x)
opg['OPG_15+'] = opg['OPG_15+'].apply(lambda x: 100 if x>100 else x)
opg['PBR_1+'] = opg['PBR_1+'].apply(lambda x: 0 if x<0 else x)
opg['PBR_3+'] = opg['PBR_3+'].apply(lambda x: 0 if x<0 else x)
opg['OPG_15+'] = opg['OPG_15+'].apply(lambda x: 0 if x<0 else x)


# In[22]:

#Reverse the Reversals
for label in opg:
        if label[-1]=='-':
            opg[label]=100-opg[label]
        elif label[-1]=='+':
            pass


# In[23]:

opg.head()


# In[24]:

opg.to_csv('SI_Master_processed_OPG.csv')


# In[27]:

copg = opg.corr()
copg.to_csv('SI_OPG_CORR_TABLE.csv')


# In[7]:

#### Calculating overlapping respondents


#pd.read_csv()
bfasopg = pd.read_csv('../BFAS ANALYSIS/Master_preprocessed_BFASOPG.csv')
bffopg = pd.read_csv('../BFF_ANALYSIS/data and analysis/Master_preprocessed_BFFOPG.csv')
wbfas = set(bfasopg.workerid.values.tolist())
wbff = set(bffopg.workerid.values.tolist())
rr = list(set.intersection(wbfas,wbff))


# In[8]:

len(rr)


# In[14]:

union = list(set.union(wbfas,wbff))
punion = pd.DataFrame(union)
#Export for comparing to study II

punion.to_csv('unique_studyI_IDS.csv')


# In[12]:

import os
os.getcwd()


# In[14]:




# In[ ]:



