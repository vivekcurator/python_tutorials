#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:23:16 2022

@author: viveksaini
"""

n = 4
m = 4
for i in range(0, n):
    for j in range(0, m):
        if(i==0 or i==n-1 or j==0 or j==m-1):
            print("*", end=' ')
        else:
            print(' ',end=' ')
    print("\r")
    
    
    
    
    
