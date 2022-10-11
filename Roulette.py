# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 02:48:18 2022

@author: abhis
"""

## A comparison between winning odds in a fair roulette, European roulette, and an American roulette


import random
random.seed(0)

def main():
    
    result= []
    
    trials = int(input('Enter the number of trials: '))
    
    bet_amount = int(input("Enter the betting amount: "))
        
    pocket = int(input("Enter the pocket you want to play: "))
        
    spins = int(input("Enter the number of spin you like to play: "))
    
    for i in [Fairroullete, EuRoullete, AmericanRoulette]:
       
        game = i()
        
        #result.append(( game, play(game, bet_amount, pocket, spins)))
        print(game, mean_and_sdt(trialsplay(game, bet_amount, pocket, spins, trials)))
        
    

class Fairroullete():
    def __init__(self):
        self.pockets = []
        
        for i in range(1, 37):
            self.pockets.append(i)
            
        self.ball =None  ## Intializing the ball to be none 
        
        self.pocketodds = len(self.pockets)-1
        
        
    def spin(self):
        self.ball = random.choice(self.pockets)
        #return self.ball  ## check the validity of this code
    
    
    def betball(self, pocket, amt):
        if str(pocket)==str(self.ball):
            return amt*self.pocketodds
        else:
            return -amt
        
    def __str__(self):
        return "Fair Roulette"
    
    
class EuRoullete(Fairroullete):
    def __init__(self):
        Fairroullete.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return "European Roulette"
    
class AmericanRoulette(EuRoullete):
    def __init__(self):
        EuRoullete.__init__(self)
        self.pockets.append('00')
        
    def __str__(self):
        return 'American Roulette'
    

def play(game, bet_amount, pocket, spins):
    #game = Fairroullete()
    
    wins = 0
    #bets = bet_amount*spins
    
    for i in range(spins):
        game.spin()
        wins= wins + game.betball(pocket, bet_amount)
    return (wins/spins)*100

#def trialsplay(game, bet_amount, pockets, spins, trials):
    #pay = 0
    #for i in range(trials):
        #pay = pay + play(game, bet_amount, pockets, spins)
    #return pay
    
##Incorporated to do mean and the std

def trialsplay(game, bet_amount, pockets, spins, trials):
    pay = []
    for i in range(trials):
        pay.append(play(game, bet_amount, pockets, spins))
    return pay    
    
def mean_and_sdt(lst):
    s = 0
    sum_diff = 0
    for i in lst:
        s = s+i
    mean = s/len(lst)
    for i in lst:
        sum_diff = sum_diff + (i-mean)**2
    sdt = (sum_diff/len(lst))**0.5
    return (mean, sdt)

main()
    
    
    