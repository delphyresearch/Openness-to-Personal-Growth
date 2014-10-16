#Code for transforming the raw CSV dump from >psiturk:download_datafiles
#THis works better as an Ipython Notebook, I've converted this to a script


#Import the neccessary packages

import pandas as pd
import json as js
import yaml as yml # this will come in handy when parsing some wierd characters in the json string
import numpy as np

#Just to double check
import os
#os.getcwd()


# In[3]:

#Data Cleaning
#GET THE DATUMS
def load_data():
    df = pd.read_csv('trialdata.csv')
    df.columns = ['uniqueId','asked_question_number','stuff1','jsonstring']
    print df.head()
    return df



def transform(df):
    """ Unpacks the first level of the json string"""
    for i,row in df.iterrows():
       # print row.index

        jstrng = row['jsonstring']
        #print jstrng
        curr_dict = yml.load(jstrng)
        curr_keys = curr_dict.keys()
        df.append(curr_keys)
        for key in curr_keys:
            
            df.loc[i,key]=str(curr_dict[key])
            

        #delete extraneous rows
        
    out = df[df['asked_question_number']>2]
    outt = out[out['asked_question_number']<131]    
        
    return outt


#the data in the jsonstring is now in the dataframe proper
#next, time to make an 'ITEM_ID' column and a REVERSAL? column
#Add a label for which scale the score comes from
#then, condense to a single row whose columns are the ITEM_ID's, whose row labels are the User_id's, and whose values are the properly reversed stuff
def make_item_id(df):
    "Makes an item_id column, a 'reversed?' column, and a column for determining which scale was used."
    df.append(['ITEM_ID','REVERSED?','SCALE?'])
    for i,row in df.iterrows():
            #print row.columns.values.tolist()
            uiid = row['id']
            reversal=-1
            itemId=-1
            scale=-1 #this refers to psychometric scale

     
            scale=uiid[0:3]
            itemId = uiid[-4:-1]
            firstdigit = itemId[0]
            if firstdigit not in set(['0','1','2','3','4','5','6','7','8','9']):
                itemId =itemId[1:]
            seconddigit = itemId[0]
            if seconddigit not in set(['0','1','2','3','4','5','6','7','8','9']):
                itemId =itemId[1:]
            if str(itemId) == '0L':
                pass
            sign = uiid[-1:]
            if sign=='+':
                reversal=True
            else:
                reversal=False
            df.loc[i,'ITEM_ID']= itemId
            df.loc[i,'UNREVERSED?']=reversal
            df.loc[i,'SCALE?']=scale 
    return df




def bigfivefrequency(userid,reverse_items,df):
    """splits the now labeled data into two- one part for the big five assessment, another for the humility questionnaire.
       returns two one-row dataframes. reverse_items should be true, else you'll just get raw answers
    """
    #print "HEADLE"
   # print df.head()
   # print "\n"
    BffDf = pd.DataFrame([userid])
    OpgDf = pd.DataFrame([userid])
    
    for i,row in df.iterrows():
        scale = df.ix[i,'SCALE?']
        if scale == 'BF-':
           # print df.ix[i,'ITEM_ID']
       
            itemId = int(df.ix[i,'ITEM_ID'])

            BffDf.append([itemId])
            rawanswer = float(df.ix[i,'answer'])


            if reverse_items and not df.ix[i,'UNREVERSED?']: #if the item is marked for reversal....
                adjustedanswer = 100-rawanswer #reverse it

            else:
                adjustedanswer = rawanswer
            BffDf[itemId] = adjustedanswer
           # BffDf.reindex_axis(sorted(BffDf.columns), axis=1)
        else:
            if scale != 'BF-' and scale != -1.0: #the item must therefore be a humility item
                if df.ix[i,'ITEM_ID']>0:
                    try:
                        itemId = int(df.ix[i,'ITEM_ID'])
                    except:
                        continue

                    OpgDf.append([itemId])
                    rawanswer = float(df.ix[i,'answer'])


                    if reverse_items and not df.ix[i,'UNREVERSED?']: #if the item is marked for reversal....
                        adjustedanswer = 100-rawanswer #reverse it
                    else:
                        adjustedanswer = rawanswer
                    OpgDf[itemId] = adjustedanswer
                    #TODO=
                    #do the same thing, but for the humility dataframe (eventually just to CSV file)

    BffDf.sort(axis=1,inplace=True,ascending=True)
    OpgDf.sort(axis=1,inplace=True,ascending=True)

    return BffDf,OpgDf
            
            
        


def make_and_concat(df):

    "The 'governer' of these data chopping programs. controls the data / IO flow."
   
   
    ids = df.uniqueId.unique()
    masterbff = []
    masteropg = []
    
    for uid in ids:

        dff = df[df['uniqueId']==str(uid)]
        dfff = transform(dff)
        dfffff = make_item_id(dfff)


        print uid
        currentbff,currentopg = bigfivefrequency(uid,True,dfffff)
        masterbff.append(currentbff)
        masteropg.append(currentopg)

    BFF= pd.concat(masterbff)
    OPG = pd.concat(masteropg)
    BFF.to_csv('BFF.csv')
    OPG.to_csv('OPG.csv')
    return masterbff,masteropg
    




