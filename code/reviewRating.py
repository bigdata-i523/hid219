#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:53:26 2017

@author: syamherle
"""

class CalculateReviewScore:
    def __init__(self,path):
        self.filePath = path
        self.calulateRating()
    def calulateRating(self):
        ratingArray=[]
        returnArray=[]
        sumAvg =0.0
        with open(self.filePath) as f:
            ratingArray.extend([int(line.strip().split(':')[-1]) for line in f])
    
        
        for i in range(len(ratingArray)):
            
            sumAvg=0.0
            for j in range(len(ratingArray)):
                if i!=j:
                    
                    sumAvg += abs(float((ratingArray[i]-ratingArray[j])/5.0))
            
            returnArray.append(1-(sumAvg/(len(ratingArray))))
       
        return returnArray