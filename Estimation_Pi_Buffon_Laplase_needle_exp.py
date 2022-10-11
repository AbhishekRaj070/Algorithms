# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:48:01 2022

@author: abhis
"""
import random
import numpy as np


def main():
    
    precision = float(input('Enter the expected precision: '))
    
    numtrials = int(input("Enter the no. of times to run the Buffon_Laplase: "))
    
    numneedles = int(input('Enter the no of needles to throw: '))
    
    print(precision_check(precision, numtrials, numneedles))

def Buffon_Laplase(numneedles):
    incircle = 0
    for i in range(numneedles):
        x= random.random()
        y= random.random()
        if x**2 + y**2 <= 1:
            incircle = incircle+1
            
    return 4*incircle/numneedles

def getestimates(numtrials, numneedles):
    result = []
    for i in range(numtrials):
        result.append(Buffon_Laplase(numneedles))
    st = np.std(result)
    mean = sum(result)/len(result)
    return (mean,st)

def precision_check(precision, numtrials, numneedles):
    std = precision
    while std >= precision/2:
        numneedles = numneedles*2
        mean, std = getestimates(numtrials, numneedles)
        print()
        print(mean, std)


if "__name__" == main():
    main()
