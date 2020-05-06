#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:25:09 2020

@author: rahulss
"""

import os
import sys
import re
import csv

from surprise import Dataset
from surprise import Reader

from collections import defaultdict
import numpy as np

class JobData:
    jobID_to_name = {}
    name_to_jobID = {}
    jobData_path = './ml-jobData-fake/jobData.csv'
    rating_path = './ml-jobData-fake/rating.csv'
    
    def loadMLJobData(self):
        
         # Look for files relative to the directory we are running from
        os.chdir(os.path.dirname(sys.argv[0]))
    
        ratingDataset = 0;
        self.jobID_to_name = {}
        self.name_to_jobID = {}
        
        reader = Reader(line_format='user item rating',sep=',',rating_scale=(1,5),skip_lines=1)
        ratingDataset = Dataset.load_from_file(self.rating_path, reader = reader)
        
        with open(self.jobData_path, newline='', encoding='ISO-8859-1') as csvfile:
            jobReader = csv.reader(csvfile)
            next(jobReader)
            for row in jobReader:
                jobID = int(row[0])
                jobTitle = int(row[1])
                self.jobID_to_name[jobID] = jobTitle
                self.name_to_jobID[jobTitle]
                
        return ratingDataset
    
    def getUserRating(self, user):
        userRatings = []
        hitUser = False
        
        with open(self.rating_path, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userId = int(row[0])
                if(user == userId):
                    jobID, rating =int(row[1]), float(row[2])
                    userRatings.append((jobID, rating))
                    hitUser = True
                if(hitUser and (user != userId)):
                    break
                
        return userRatings
    
    def getPopularityRanks(self):
        ratings = defaultdict(int)
        rankings = defaultdict(int)
        
        with open(self.rating_path, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                jobID = int(row[1])
                ratings[jobID] += 1
        rank = 1
        for jobID, ratingCount in sorted(ratings.items(), key=lambda x:x[1], reverse=True):
            rankings[jobID] = rank
            rank += 1
        return rankings
    
    def getTags(self):
        tags = defaultdict(list)
        tagIDs = {}
        maxTagID = 0
        with open(self.jobData_path, newline='', encoding='ISO-8859-1') as csvfile:
            jobReader = csv.reader(csvfile)
            next(jobReader)
            for row in jobReader:
                jobID = int(row[0])
                tagList = row[3].split('|')
                tagIDList = []
                for tag in tagList:
                    if tag in tagIDs:
                        tagID = tagIDs[tag]
                    else:
                        tagID = maxTagID
                        tagIDs[tag] = tagID
                        maxTagID += 1
                    tagIDList.append(tagID)
                tags[jobID] = tagIDList
                
        # Convert integer-encoded genre lists to bitfields that we can treat as vectors
        for (JobID, tagIDList) in tags.items():
            bitfield = [0] * tagIDList
            for tagID in tagIDList:
                bitfield[tagID] = 1
            tags[jobID] = bitfield
                
        return tags
    
    def getJobTitle(self, jobID):
        if jobID in self.name_to_jobID:
            return self.name_to_jobID[jobID]
        else:
            return ''
        
    def getjobID(self, jobTitle):
        if jobTitle in self.jobID_to_name:
            return self.jobID_to_name[jobTitle]
        else:
            return ''
                    
    
                    
        
    
    
