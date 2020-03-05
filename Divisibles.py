# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:00:39 2020

@author: Filippe
"""

n=[]
t=int(input("Insert number to find divisibles: "))
for i in range(1, t):
    if t % i == 0:
        n.append(i)
print("Divisibles of ", t, ":")
print(n)
