#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 00:10:05 2017

@author: syamherle
"""
import time
import os
from algorithm import *
import pandas as pd
from reviewRating import *
from visualizeoutput import *

class ReviewScore:
    
    def __init__(self,path):
        self.path = path
    
    def readFile(self):
        basePath = self.path+'/review/'
        subDir = [folder for folder in os.listdir(basePath) if not folder.startswith(".")]
        df= pd.DataFrame(columns=[])
        for num in range(len(subDir)):
            files =[f for f in os.listdir(basePath+subDir[num])]
            in_files=[]
            
            reviewRating = CalculateReviewScore(os.getcwd()+'/rating/'+subDir[num]+'.txt')
            self.reviewArray = reviewRating.calulateRating()
            for file_num in range(len(files)):
                with open(basePath+subDir[num]+'/'+files[file_num]) as f:
                    lines =[line.strip() for line in f]
                    in_files.append(lines)
            self.documentCosine={}
            for i in range(len(in_files)):
                for j in range(len(in_files)):
                    
                    temp_str1 = "".join(str(x) for x in in_files[i] if x != "")
                    temp_str2 = "".join(str(x) for x in in_files[j] if x != "")
                    cosineval = CosineSimillarity(temp_str1,temp_str2)
                    cosineval.createDict()
                    
                    self.documentCosine[(i,j)] =cosineval.cosineCalculation()
                   
                
            self.avgsum=0.0
            self.avgDocCosine={}
            #calculating average cosines for document
            for i in range(len(in_files)):
                for j in range(len(in_files)):
                    if i != j:
                        self.avgsum += self.documentCosine[(i,j)]
                self.avgDocCosine[i] = self.avgsum/(len(in_files))
                self.avgsum=0.0
                
            
            if len(self.reviewArray) == len(self.avgDocCosine.keys()):
              
                for i in range(len(self.reviewArray)):
                    df = df.append({"id":int(i),"rating score":self.reviewArray[i],"review score":self.avgDocCosine[i]},ignore_index=True)
            df['id'] = df['id'].astype('int64')
            df.to_csv('output.csv',encoding='utf-8')
            print 'Calculation of hotel ',subDir[num],' is completed.'
        plot()
        
def main(path):
    
    review_score = ReviewScore(path)
    review_score.readFile()
if __name__ == "__main__":
    start_time = time.time()
    main(os.getcwd())
    print("--- %s seconds ---" % (time.time() - start_time))
    
    