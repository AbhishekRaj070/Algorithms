# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 05:02:33 2022

@author: abhis
"""
## Algorithm to generate Gaussian distribution

import matplotlib.pyplot as plt
import random
import math as m
import statistics as s

def main():
    
    mu = int(input('Enter the value of mean: '))
    sigma = int(input('Enter the value of std. dev.: '))
    
    extent = int(input("Enter the extent you want your gaussian in: "))
    
    y=[]
    x=[]
    i=-extent
    while i <=extent:
        y.append(gaussian(i,mu,sigma))
        x.append(i)
        i=i+0.05
        
    plt.plot(x,y)
        

def gaussian(x, mu, sigma):
    
    y1 = 1/(sigma*(2*m.pi)**0.5)
    y2 = m.exp(-((x-mu)**2)/(2*sigma**2))
    y=y1*y2
    return y


## to test the emperical case that 67% of data between first standard deviation
## 95% data between second standard deviation & 99% in third standard deviation


def test_Emperical(num_trials):
    import scipy.integrate
    
    for i in range(num_trials):
        mu = random.randint(-10,10)
        sigma = random.randint(1,10)
        print('mu:', mu, 'sigma:',sigma)
    
        for j in [1, 1.96, 3]:
            area = scipy.integrate.quad(gaussian, mu-sigma*j, mu+ sigma*j,(mu,sigma))[0]
            
            print(j,area)
            
if "__name__" == main():
    main()
