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

print(delta)
print(summe)
print(omega)
print(k)
print(phi)
