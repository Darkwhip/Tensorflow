# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:09:00 2020

@author: Filippe
"""

def divisibles(t):
    n=[]
    for i in range(1, t):
        if t % i == 0:
            n.append(i)
    return(n)

def unPermutator(n):
    a=[]
    for i in range(len(n)):
        g=n[i]
        for j in range(i+1, len(n)):
            if n[j].count(g[0])>0 and n[j].count(g[1])>0 and n[j].count(g[2])>0:
                if a.count(j)==0:
                    a.append(j)
    a.sort()
    for j in range(len(a)):
        del n[a[j]]
        for i in range(len(a)):
            a[i]=a[i]-1
    return n
        
            
            

t=int(input("Insert number to find a size that fits: "))
n=divisibles(t)
n.pop(0)
m=[]
for i in range(len(n)):
    for j in range(len(n)):
        for k in range(len(n)):
            if n[i]*n[j]*n[k]==t:
                m.append((n[i], n[j], n[k]))
m.sort()
m=unPermutator(m)
print("Heres the solutions we found: ", m)