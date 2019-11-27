# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:44:58 2019

@author: ABC
"""
#%%#
#1.Aufgabe b)
import math

def entropie(p): #Formel zur berechnung von Entropie
 
    if p > 1.0 or p <= 0.0: #Nur 
        
        return 
    
    else:
    
        return - p * math.log2(p) - (1-p) * math.log2(1 - p)  

delta = entropie(0.2)
summe = entropie(0.125)
omega = entropie(0.2)
k = entropie(0.345)
phi = entropie(0.13)

entropieH = delta+summe+omega+k+phi

print(delta)
print(summe)
print(omega)
print(k)
print(phi)
print(entropieH)

    
 #%%#
#1.Aufgabe c) und d) 
import math

def entropie(tabelle): #Formel zur berechnung von Entropie
    entropieH = 0
    
    for val in tabelle:
        
        p= tabelle[val]
        
        if p > 1.0 or p <= 0.0: #Nur 
            return 
        
        else:
            entropieH = entropieH + (- p * math.log2(p) - (1-p) * math.log2(1 - p))
            
    print("Die Entropie H der Zeichen Z ist:",entropieH)
    return 
        

tabelle = {
        "delta":0.2,
        "summe":0.125,
        "omega":0.2,
        "k":0.345,
        "phi":0.13,
        }
entropie(tabelle)
#%%#
 
