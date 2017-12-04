#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:31:57 2017

@author: syamherle
"""

import pandas as pd
import matplotlib.pyplot as plt
def plot():
    data =pd.read_csv('output.csv',sep=',')
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = data['rating score']
    y = data['review score']
    ax.scatter(x,y)
    plt.title('opinion spammer')
    plt.ylabel('Review score')
    plt.xlabel('Rating Score')
    plt.savefig('outputFig')
    
def main():
    plot()

if __name__ == "__main__":
    main()
