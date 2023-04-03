# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:03:14 2023

@author: ajmek
"""

num = 1
total = 0
evenTotal = 0
oddTotal = 0
while(num <= 20):
    total += num
    print(total)
    if((num % 2) == 0):
        evenTotal += num
    else:
        oddTotal += num
    num += 1
print('The sum of all even numbers in the set is ' + str(evenTotal))
print('The sum of all odd numbers in te set is ' + str(oddTotal))

    