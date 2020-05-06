#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:32:42 2020

@author: rahulss
"""

import pandas as pd

def addRate(userID, jobID, rating):
    isThere = False
    

    df1 = pd.read_csv('./ml-jobData-fake/rating.csv')
    dfjson = df1.to_json(r'./ml-jobData-fake/endgameRating.json')

    
    try:
        userFloat = float(userID)
        jobFloat = float(jobID)
        ratingFloat = float(rating)
        print(userFloat,jobFloat,ratingFloat)
        
        if (0 > ratingFloat or ratingFloat > 10):
            invalid = "invalid"
            return invalid
        
    except ValueError:
        error = "error"
        return error
    
    for index, row in df1.iterrows():
        print(row['userID'],row['jobID'])
        if str(row['jobID'])==str(jobID) and str(row['userID'])==str(userID):
           row['rating'] = rating
           isThere = True
   
    
    # Creating the Second Dataframe using dictionary 
 
    if isThere != True: 
        df2 = pd.DataFrame({"userID": [userID],
                            "jobID": [jobID],
                            "rating": [rating]}) 
    
        dff = df1.append(df2, ignore_index = True)
        dff.to_csv(r'./ml-jobData-fake/rating.csv', index = False)      
        added = "added"
        return added
     
    else:

        df1.to_csv(r'./ml-jobData-fake/rating.csv', index = False)
        updated = "updated"
        return updated
