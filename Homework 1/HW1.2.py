# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:11:30 2023

@author: ajmek
"""
def weatherFunc():
    print('Use this program to determine if you should play tennis given the current weather')
    outlook = input('How is the outlook for today? Type "Sunny", "Overcast", or "Rain" ')
    if(outlook == 'Overcast'):
        print('Yes')
    elif(outlook == 'Sunny'):
        humidity = input('How is the humidity for today? Type "Normal" or "High" ')
        if(humidity == 'Normal'):
            print('Yes')
        else:
            print('No')
    else:
        rain = input('How is the rain for today? Type "Weak" or "Strong" ')
        if(rain == 'Weak'):
            print('Yes')
        else:
            print('No')

weatherFunc()