
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



# In[2]:

pd.set_option('display.max_columns', None)


# In[3]:

engine = sa.create_engine('mysql://.../personality')
con = engine.raw_connection()
df = sql.read_frame("SELECT * FROM BFASOPG_STUDY_II", con)
df = df.convert_objects(convert_numeric=True)
con.close()


# In[4]:

dff = df
df.tail()


# In[5]:

len(df)


# In[5]:




# In[6]:

def takestring(row):
    #print json.loads(row['datastring'])
    try:
        d = json.loads(row['datastring'])
    except:
        print row
    else:
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


# In[7]:

df=df[df['status']==4]
df = df.apply(takestring,axis=1)
df = df.convert_objects(convert_numeric=True)


# In[11]:

df.head()


# In[14]:

def split_and_reverse(df):
    ls_col = df.columns.values.tolist()
    ls_col.sort()
   # print ls_col
    r_ls_col = ls_col[:-17] #the restricted list of columns #MAKE SURE THIS PARAM IS RIGHT
    bff_cols = ['workerid']
    opg_cols = ['workerid']
    bff_cols.extend(r_ls_col[:-26])
    opg_cols.extend(r_ls_col[-26:])
    Neuroticism = ['BFAS-1+','BFAS-2+','BFAS-3+','BFAS-4+','BFAS-5+','BFAS-6+','BFAS-F7-','BFAS-8-','BFAS-9-','BFAS-10-','BFAS-11+','BFAS-12+','BFAS-13+','BFAS-14+','BFAS-15+','BFAS-16+','BFAS-17-','BFAS-18-','BFAS-19-','BFAS-20-']
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
            BffDf.loc[label] = df['workerid']
            
    print OpgDf['OPG_16+'].loc[1]
    print type(OpgDf['OPG_16+'].loc[1])
    
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
    


# In[15]:

master_bff,master_opg = split_and_reverse(df)


# In[16]:

master_bff.head()


# In[17]:

master_opg.head()


# In[18]:

master_bff.to_csv('Master_preprocessed_BFAS.csv')
master_opg.to_csv('Master_preprocessed_BFASOPG.csv')


# In[19]:

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
df_questionnaire = extract_questionnare(dff)
df_questionnaire_complete = df_questionnaire[df_questionnaire['status']==4]
age = df_questionnaire_complete.age.values.tolist()
df_questionnaire_complete.engagement.value_counts()


# In[54]:

a = df_questionnaire_complete.age.values.astype(np.float)


# In[55]:

a.mean()


# In[56]:

a.std()


# In[57]:

df_questionnaire_complete.comments.values


# In[58]:

a


# In[ ]:



