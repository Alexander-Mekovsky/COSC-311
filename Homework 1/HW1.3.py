# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:27:08 2023

@author: ajmek
"""

L = input('Input side length. Any length less than 2 will be rejected and asked to input again ')
L = int(L)
while(L < 2):
    L = input('Input less than 2. Please try again ')
    L = int(L)
    """
for i in range(L):
    print(' ' * (L - i - 1) + '*' * (L + i * 2))
for i in range(L - 1):
    print('*' * (L + ((L - 1) * 2)))
for i in range(L - 1):
    print(' ' * (i + 1) + '*' * (((L - i + 1) * 2) - 1))
    """
    
for i in range(L):
    print(' ' * (L - i - 1) + '*' * (L + (i * 2)) + ' ' * (L - i - 1))
for i in range(L - 2):
    print('*' * ((L * 2) + (L - 2)))
for i in range(L):
    print(' ' * (i) + '*' * (((L * 2) + (L - 2)) - (i * 2)) + ' ' * (i))