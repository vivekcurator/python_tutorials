#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:12:43 2022

@author: viveksaini
"""
# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.


n = int(input("Enter a number: "))
if (n % 2) == 0:  
    print("Even")
else:
    print("Odd")
    
    
