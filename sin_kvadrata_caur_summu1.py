# -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
    k = 0
    a = (-1)**2*x**2*2**1/(2)
    S = a
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 500:
       k = k+1
       R = (-1)*x*x/((2*k)*(2*k-1))
       a = a*R
       S = S+a
       if k==499:

           print("Izdruka no liet.f. a499 = %6.2f S499 = %6.2f"%(a,S))
    print ("Izdruka no liet.f. a500 = %6.2f S500 = %6.2f"%(a,S))      

    print("Izdruka no liet.f. Beigas!")    
    return S

x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y= sin(x)*sin(x)
print("standarta sin**2(%.2f) = %6.2f"%(x,y))

c = u"\u221E"
yy = mans_sinuss(x)
print("mans sin**2(%.2f) = %6.2f"%(x,yy))
print("             500")
print("            ____")
print("            \           k    2*k   2*k-1")
print("             \      (-1)  * x   * 2")
print("sin^2(%.2f))=>    _________________          , kur -%s <x< %s "%(x,c,c))
print("             /")
print("            /____      (2*k)!")
print("             k=1")
print(" ")
print(" ")
print("                                                   2")
print("                                             (-1)*x")
print("rekurences reizinātajs                    _____________")
print("                                           2*k*(2*k-1)")


