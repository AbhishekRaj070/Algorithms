# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 05:52:37 2022

@author: abhis
"""

## class to define cow object that needs to be transported includes, names, weights

def main():
    
    filename = r'C:\Users\abhis\OneDrive\Desktop\MIT\6002_Intro_to computational_thinking\Assignment\#1\ps1_cow_data.txt'
    cows_object = aliencows(filename)
    max_cost = int(input("Enter Maximum cost: "))
    keyfunction = cows.getweight
    greedy_algorithm = greedy(cows_object, max_cost, keyfunction)
    print(greedy_algorithm)



def loadcows(filename): #
    d={}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            d[line.strip().split(',')[0]]=int(line.strip().split(',')[1])
    return d 

class cows(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def getname(self):
        return self.name
    
    def getweight(self):
        return self.weight
    
    def __str__(self):
        return f"{self.name},{self.weight}"
    
    
    
def aliencows(filename): # takes about the list of element name ans weight
    name =  list(loadcows(filename).keys()) 
    weight= list(loadcows(filename).values())
    result = []
    for i in range(len(name)):
        result.append(cows(name[i], weight[i]))
    return result    
    
    
def greedy(items, maxcost, keyfunction):
    itemscopy =sorted(items, key = keyfunction, reverse = True)
    
    answer=[]

    while len(itemscopy)!=0:
        result=[]
        k=[]
        totalweight = 0
        for i in itemscopy:

            if (totalweight + i.getweight())<=maxcost:
                result.append(i.getname())
                k.append(i)###
                totalweight = totalweight + i.getweight()

                #itemscopy.remove(i)
        for j in k:
            itemscopy.remove(j)
        
        answer.append(result) 
    
    return answer


main()