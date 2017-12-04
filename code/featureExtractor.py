#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:33:56 2017

@author: syamherle
"""
import os
import shutil 
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SQLContext

class Preprocess:
    def __init__(self,path):
        conf = SparkConf().setAppName("App")
        conf = (conf.setMaster('local[*]')
            .set('spark.executor.memory', '4G')
            .set('spark.driver.memory', '45G')
            .set('spark.driver.maxResultSize', '10G'))
        self.sc = SparkContext(conf=conf)
    
        self.sqlContext = SQLContext(self.sc)
        self.path = path
    def readFile(self):
        self.businessDf = self.sqlContext.read.json(self.path+'/dataset/business.json')
        self.reviewDf = self.sqlContext.read.json(self.path+'/dataset/review.json')
        self.businessDf.na.drop()
        self.reviewDf.na.drop()
    def createBusinessFeature(self):
        self.businessDict ={}
        for row in self.businessDf.collect():
            self.businessDict[row['business_id']] = row['name']
    def createReviwFeatures(self):
        self.reviewDict = {}
        for row in self.reviewDf.collect():
            self.businessName = self.businessDict[row["business_id"]]
            try:
                self.reviewDict[self.businessName] += 1
            except:
                self.reviewDict[self.businessName] = 1
            self.dumpData(row)
    def formatString(self,str):
        str = str.replace('/',':')
        return str
    def dumpData(self,row):
        
        
        if not os.path.exists('reviews_model'):
        	os.makedirs('reviews_model')
        
        if not os.path.exists('ratings_model'):
        	os.makedirs('ratings_model')   
        
        review_file = self.businessName + '_' + str(self.reviewDict[self.businessName]) + '.txt'
    	
        
    
        if not os.path.exists('reviews_model/' + self.formatString(self.businessName)):
            os.makedirs('reviews_model/' + self.formatString(self.businessName))
    	
        reviewOutput = open('reviews_model/' + self.formatString(self.businessName) + '/' + self.formatString(review_file), 'w')
        reviewOutput.write(row['text'].encode('utf8'))
        reviewOutput.close()
    
        ratingWriteBuffer = open('ratings_model/' + self.formatString(self.businessName) + '.txt', 'a')
        ratingstring = self.businessName + '_' + str(self.reviewDict[self.businessName]) + ':' + str(row["stars"]) + '\n' 
        
        ratingWriteBuffer.write(ratingstring.encode('utf8'))
        ratingWriteBuffer.close()
        self.sc.stop()
            
        
################################################
# Booting up spark
################################################
def main():
    try:
        shutil.rmtree('reviews_model')
    except:
        pass
    
    try:
        shutil.rmtree('ratings_model')
    except:
        pass
    os.system('clear')
    
    path = os.getcwd()
    process=Preprocess(path)
    process.readFile()
    process.createBusinessFeature()
    process.createReviwFeatures()
    
if __name__ == "__main__":
    main()
