# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:20:57 2023

@author: ajmek
"""

import random

x = 100000
print('N = ', x)
i = 0
totalRolls = [0] * 12
for i in range(x):
    oneDie = random.randint(1,6)
    twoDie = random.randint(1,6)
    total = oneDie + twoDie
    totalRolls[total - 1] += 1
    i += 1
for i, j in enumerate(totalRolls):
    if(i == 0):
        continue
    rollProb = float(j) / x
    print(i + 1, ":", '{: .2%}'.format(rollProb))
    
    
        
    
    
        
    