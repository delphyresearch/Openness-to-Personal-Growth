
# coding: utf-8

# In[6]:

import numpy as np
import pandas as pd
from pandas.io import sql
import sqlalchemy as sa
import yaml as yml
import json
import demjson
get_ipython().magic(u'matplotlib inline')

#CHANGE VAIRABLES TO BFAS


# In[7]:

pd.set_option('display.max_columns', None)


# In[8]:

engine = sa.create_engine('mysql://evan:****&&&&&&######/personality')
con = engine.raw_connection()
df = sql.read_frame("SELECT * FROM BFASOPG_STUDY_II", con)
df = df.convert_objects(convert_numeric=True)
con.close()


# In[9]:

dff = df
df.tail()


# In[14]:

len(df)


# In[14]:




# In[15]:

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


# In[16]:

df=df[df['status']==4]
df = df.apply(takestring,axis=1)
df = df.convert_objects(convert_numeric=True)


# In[17]:

df.head()


# In[18]:

corder = [u'BFAS-1+',
            u'BFAS-2+',
            u'BFAS-3+',
            u'BFAS-4+',
            u'BFAS-5+',
            u'BFAS-6+',
            u'BFAS-F7-',
            u'BFAS-8-',
            u'BFAS-9-',
            u'BFAS-10-',
             u'BFAS-11+',
             u'BFAS-12+',
             u'BFAS-13+',
             u'BFAS-14+',
             u'BFAS-15+',
             u'BFAS-16+',
             u'BFAS-17-',
             u'BFAS-18-',
             u'BFAS-19-',
              u'BFAS-20-',
     u'BFAS-21+',
     u'BFAS-22+',
     u'BFAS-23+',
     u'BFAS-24+',
     u'BFAS-25+',
     u'BFAS-26-',
     u'BFAS-27-',
     u'BFAS-28-',
     u'BFAS-29-',
      u'BFAS-30-',
     u'BFAS-31+',
     u'BFAS-32+',
     u'BFAS-33+',
     u'BFAS-34+',
     u'BFAS-35-',
     u'BFAS-36-',
     u'BFAS-37-',
     u'BFAS-38-',
     u'BFAS-39-',
     u'BFAS-40-',
     u'BFAS-41+',
     u'BFAS-42+',
     u'BFAS-43+',
     u'BFAS-44+',
     u'BFAS-45-',
     u'BFAS-46-',
     u'BFAS-47-',
     u'BFAS-48-',
     u'BFAS-49-',
      u'BFAS-50-',
     u'BFAS-51+',
     u'BFAS-52+',
     u'BFAS-53+',
     u'BFAS-54+',
     u'BFAS-55+',
     u'BFAS-56+',
     u'BFAS-57-',
     u'BFAS-58-',
     u'BFAS-59-',
     u'BFAS-60-',
     u'BFAS-61+',
     u'BFAS-62+',
     u'BFAS-63+',
     u'BFAS-64+',
     u'BFAS-65+',
     u'BFAS-66-',
     u'BFAS-67-',
     u'BFAS-68-',
     u'BFAS-69-',
     u'BFAS-70-',
     u'BFAS-71+',
     u'BFAS-72+',
     u'BFAS-73+',
     u'BFAS-74+',
     u'BFAS-75+',
     u'BFAS-76+',
     u'BFAS-77-',
     u'BFAS-78-',
     u'BFAS-79-',
     u'BFAS-80-',
     u'BFAS-81+',
     u'BFAS-82+',
     u'BFAS-F83+',
     u'BFAS-F84+',
     u'BFAS-F85+',
     u'BFAS-F86+',
     u'BFAS-F87-',
     u'BFAS-88-',
     u'BFAS-89-',
     u'BFAS-90-',
     u'BFAS-91+',
     u'BFAS-92+',
    u'BFAS-93+',
     u'BFAS-94+',
     u'BFAS-95+',
     u'BFAS-96+',
     u'BFAS-97-',
     u'BFAS-98-',
     u'BFAS-99-',
      u'BFAS-100-']


# In[9]:

ls_col = df.columns.values.tolist()
ls_col.sort()
   # print ls_col
r_ls_col = ls_col[:-17]


# In[10]:

ls_col


# In[11]:

r_ls_col[-26:]


# In[26]:

def split_and_reverse(df):
    ls_col = df.columns.values.tolist()
    ls_col.sort()
   # print ls_col
    r_ls_col = ls_col[:-17] #the restricted list of columns #MAKE SURE THIS PARAM IS RIGHT
    bfas_cols = ['workerid']
    opg_cols = ['workerid']
    bfas_cols.extend(corder)
    opg_cols.extend(r_ls_col[-26:])
    Neuroticism = ['BFAS-1+','BFAS-2+','BFAS-3+','BFAS-4+','BFAS-5+','BFAS-6+','BFAS-F7-','BFAS-8-','BFAS-9-','BFAS-10-','BFAS-11+','BFAS-12+','BFAS-13+','BFAS-14+','BFAS-15+','BFAS-16+','BFAS-17-','BFAS-18-','BFAS-19-','BFAS-20-']
    print bff_cols[0:10]
    print '\n'
    print opg_cols[0:10]
    print '\n'
    BfasDf = df[bff_cols]
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
            BfasDf[label] = 100- BfasDf[label].astype(float)



        elif label[-1]=='+': #label = workerID
            pass
        else:
            BfasDf.loc[label] = df['workerid']

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
        BfasDf[label] = 100-BfasDf[label].astype(float)

    #BffDf.sort(axis=1,inplace=True,ascending=True)
    #OpgDf.sort(axis=1,inplace=True,ascending=True)

    return BfasDf,OpgDf



# In[27]:

master_bfas,master_opg = split_and_reverse(df)


# In[28]:

master_bfas.head()


# In[29]:

master_opg.head()


# In[30]:

master_bfas.to_csv('Master_preprocessed_BFAS.csv')
master_opg.to_csv('Master_preprocessed_BFASOPG.csv')


# In[4]:

master_bfas = pd.read_csv('Master_preprocessed_BFAS.csv')
master_opg = pd.read_csv('Master_preprocessed_BFASOPG.csv')


# In[10]:

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


# In[21]:

######################################
df_questionnaire_complete[['workerid','age','engagement']].to_csv('WorkerID_Gender_Age_pairing_BFAS_II.csv')


# In[19]:




# In[56]:

a.std()


# In[57]:

df_questionnaire_complete.comments.values


# In[58]:

a


# In[ ]:



