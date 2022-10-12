# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 03:50:44 2022

@author: abhis
"""

import random

def main():
    
    flips = int(input("Enter the flips you want: "))
    no_of_heads = int(input("Enter the number of heads/tails you want: "))
    num_sets = int(input("Enter the staring sets you like to gene: "))
    epsilon = 0.001 # can also be a variable, takes more time to compute for higher precision
    
    times_simulate = 20  # this can be variable too, but 20 is enough for time being
    
    best_num_sets = precision(epsilon, times_simulate, flips, no_of_heads, num_sets)
    
    print(probability_of_occurence(flips, no_of_heads, best_num_sets), best_num_sets)

def flips(num_flips):
    sets = []
    choices = ['H','T']
    for i in range(num_flips):
        sets.append(random.choice(choices))
    return sets 


def probability_of_occurence(num_flips, occ_of_heads, num_sets):
    wants = 0
    for i in range(num_sets):
        counts =0               # no of sets of flips
        for j in flips(num_flips):
            if j == 'H':
                counts = counts +1
                
        if counts == occ_of_heads:
            wants = wants + 1 
            
    return wants/num_sets

def mean_sdt(lst):
    mean = sum(lst)/len(lst)
    for i in lst:
        sdt= ((i-mean)**2/len(lst))**0.5
    return (mean, sdt) 


def precision(precision, times_simulate, num_flips, occ_of_heads, num_sets):
    sdt = precision
    
    while sdt > precision/2:
        result = []
        for i in range(times_simulate):
            result.append(probability_of_occurence(num_flips, occ_of_heads, num_sets))
        sdt= mean_sdt(result)[1]
        num_sets = num_sets*2
    return num_sets

if "__name__" == main():
    main()