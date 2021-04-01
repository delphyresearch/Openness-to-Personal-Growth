
# coding: utf-8

# In[35]:

#Data analysis from second round of data collection - 435 people on the BFF/OPG


# In[1]:

import numpy as np
import pandas as pd
from pandas.io import sql
import sqlalchemy as sa
import yaml as yml
import json
import demjson
get_ipython().magic(u'matplotlib inline')


# In[2]:

pd.set_option('display.max_columns', None)


# In[2]:

engine = sa.create_engine('mysql://evan:=========/  /=====/personality')
con = engine.raw_connection()
df = sql.read_frame("SELECT * FROM bffopg", con)
con.close()


# In[3]:

df.head()


# In[4]:

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


# In[5]:

def takestring(row):
    d = json.loads(row['datastring'])

   # print jj
    j= d['data']
    for a in j:
        b = a['trialdata']
        if 'answer' in b:
            item_id = b['id']
            rawanswer = b['answer']
            row[item_id] = rawanswer
    #print row
    return pd.Series(row)


# In[6]:

#df.apply(takestring,axis=1)
df=df[df['status']==4]


# In[7]:

len(df)


# In[8]:

tdf = df.apply(takestring,axis=1)


# In[9]:


tdf.head()



# In[10]:

tdf = tdf.convert_objects(convert_numeric=True)


# In[11]:

#tdf.to_csv('Master_extracted_BFFOPG.csv')


# In[40]:

#tdf = pd.read_csv('Master_extracted_BFFOPG.csv')


# In[11]:

d = tdf.columns.tolist()


# In[12]:

dd = d[:-17]


# In[13]:

dd[-26:]



# In[14]:

dd[:-26]


# In[14]:




# In[14]:




# In[14]:




# In[14]:




# In[14]:




# In[14]:




# In[15]:




# In[16]:

def split_and_reverse(df):
    ls_col = df.columns.values.tolist()
    ls_col.sort()
    print ls_col
    r_ls_col = ls_col[:-17] #the restricted list of columns
    bff_cols = ['workerid']
    opg_cols = ['workerid']
    bff_cols.extend(r_ls_col[:-26])
    opg_cols.extend(r_ls_col[-26:])
    Neuroticism = ['BF-F1+','BF-F2+','BF-F3+','BF-F4+','BF-F5+','BF-F6-','BF-F7+','BF-F8+','BF-F9+','BF-F10+','BF-F11+','BF-F12+','BF-F13+','BF-F14+','BF-F15+','BF-F16+','BF-F17-','BF-F18+','BF-F19-','BF-F20+']
    print bff_cols[0:10]
    print '\n'
    print opg_cols[0:10]
    print '\n'
    BffDf = df[bff_cols]
    OpgDf = df[opg_cols]

   # df['ref'] = pd.Series([100.0 for x in range(len(BffDf['workerId']))])
   # print df['ref'].tail()



    for label in bff_cols:
        #print label
        if label[-1]=='-': #if item is reversed:
             #print BffDf[label].head()
             #print '\n'
             #print len(BffDf[label])
             #a = ref.sub(BffDf[label])
             #print a.head()
            BffDf[label] = 100- BffDf[label].astype(float)


        elif label[-1]=='+': #label = workerID
            pass
        else:
            BffDf[label] = df['workerid']


    OpgDf['OPG_16+'] = 100-2*abs(OpgDf['OPG_16+']-50)
    OpgDf['IE_21+'] = 100-2*abs(OpgDf['IE_21+']-50)

    OpgDf['PBR_1+'] = ((OpgDf['PBR_1+']-50)*1.1)+50
    OpgDf['PBR_3+'] = ((OpgDf['PBR_3+']-50)*1.1)+50
    OpgDf['OPG_15+'] = ((OpgDf['OPG_15+']-50)*1.1)+50

    OpgDf['PBR_1+'] = OpgDf['PBR_1+'].apply(lambda x: 100 if x>100 else x)
    OpgDf['PBR_3+'] = OpgDf['PBR_3+'].apply(lambda x: 100 if x>100 else x)
    OpgDf['OPG_15+'] = OpgDf['OPG_15+'].apply(lambda x: 100 if x>100 else x)

    OpgDf['PBR_1+'] = OpgDf['PBR_1+'].apply(lambda x: 0 if x<0 else x)
    OpgDf['PBR_3+'] = OpgDf['PBR_3+'].apply(lambda x: 0 if x<0 else x)
    OpgDf['OPG_15+'] = OpgDf['OPG_15+'].apply(lambda x: 0 if x<0 else x)

    for label in OpgDf:
        if label[-1]=='-':
            OpgDf[label]=100-OpgDf[label].astype(float)
        elif label[-1]=='+':
            pass
        else:
            OpgDf[label] = df['workerid']

    ##Now, change neuroticism to stability
    for label in Neuroticism:
        BffDf[label] = 100-BffDf[label].astype(float)

    BffDf.sort(axis=1,inplace=True,ascending=True)
    OpgDf.sort(axis=1,inplace=True,ascending=True)

    return BffDf,OpgDf





# In[17]:

a = tdf.columns.values.tolist()


# In[18]:

a[1:-17][:-26
         ]


# In[19]:

master_bff,master_opg = split_and_reverse(tdf)



# In[20]:

master_opg.tail()


# In[21]:

master_bff.tail()


# In[22]:

print len(master_opg)
print len(master_bff)


# In[23]:




# In[23]:

master_bff.to_csv('Master_preprocessed_BFF.csv')
master_opg.to_csv('Master_preprocessed_BFFOPG.csv')


# In[24]:

def extract_questionnare(df):
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
            #curr_keys = curr_dict.keys()
            #df.append(curr_keys)

            question_dict = curr_dict['questiondata']
            question_keys = question_dict.keys()
            if question_dict=={}:
                continue
            else:
                #print question_dict
                #print question_keys
                df.append(question_keys)
                for key in question_keys:
                    df.append([key])
                    df.loc[i,key] = question_dict[key]

                #else:
                #df.ix[i,key]= str(curr_dict[key])
                 #   df.loc[i,key]=str(curr_dict[key])
                #row[key]=str(curr_dict[key])
            #delete extraneous rows

        #out = df[df['asked_question_number']>2]
        #outt = out[out['asked_question_number']<131]
    return df
df_questionnaire = extract_questionnare(df)
df_questionnaire_complete = df_questionnaire[df_questionnaire['status']==4]
age = df_questionnaire_complete.age.values.tolist()
df_questionnaire_complete.engagement.value_counts()


# In[25]:

df_questionnaire = extract_questionnare(df)


# In[26]:

df_questionnaire_complete = df_questionnaire[df_questionnaire['status']==4]


# In[32]:

age = df_questionnaire_complete.age.values.astype(np.float)


# In[33]:

df_questionnaire_complete.engagement.value_counts()


# In[34]:




# In[35]:

import numpy as np


# In[36]:

from matplotlib import pyplot as plt


# In[37]:

#df_questionnaire_complete.to_csv('questionnaire_extracted_df.csv')


# In[38]:

np.array(age).std()


# In[39]:

np.array(age).mean()


# In[40]:

comments = df_questionnaire_complete[df_questionnaire_complete.comments != ''].comments


# In[41]:

comments.values


# In[ ]:



