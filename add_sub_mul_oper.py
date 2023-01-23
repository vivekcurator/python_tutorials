#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:49:12 2023

@author: viveksaini
"""

N1=int(input("Enter the First Number: "))
N2=int(input("Enter the Second Number: "))
N3=int(input("Enter the Third Number: "))
N4=int(input("Enter the Fourth Number: "))

op=input("\nEnter the operator( + , - , * ): ")
 
if op=="+":
    print("\nThe addition is", N1+N2+N3+N4)
elif op=="-":
    print("\nThe subtraction is",N1-N2-N3-N4)
elif op=="*":
    print("\nThe multiplication is",N1*N2*N3*N4)
else:
    print("\ninvalid operator!!!")
    
