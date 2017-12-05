#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:33:07 2017

@author: syamherle
"""
import math
class CosineSimillarity:
    def __init__(self,t1,t2):
        
        self.arrOne = t1.split(" ")
        self.arrTwo = t2.split(" ")
        self.freqDict={}
        
    def createDict(self):
        self.uniqueWords =set()
       
        for i in self.arrOne:
            if i != "":
                try:
                    self.freqDict[i] = (self.freqDict[i][0]+1,self.freqDict[i][1])
                except:
                    self.freqDict[i] = (1,0)
                    self.uniqueWords.add(i)
        for i in self.arrTwo:
            if i != "":
                try:
                    self.freqDict[i] = (self.freqDict[i][0],self.freqDict[i][1]+1) 
                except:
                    self.freqDict[i] = (0,1)
                    self.uniqueWords.add(i)
            
    def cosineCalculation(self):
        
        prod_val,val_one,val_two =0.0,0.0,0.0
        for i in self.uniqueWords:
            prod_val += float(self.freqDict[i][0]) * float(self.freqDict[i][1])
            val_one += math.pow(self.freqDict[i][0],2)
            val_two += math.pow(self.freqDict[i][1],2)
         
        return (prod_val)/(math.sqrt(val_one)*math.sqrt(val_two))
            
        
        
                
                
            