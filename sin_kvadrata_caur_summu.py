# -*- coding: utf-8 -*-
from math import *
# (1.) * (2) = (2.) - float * int = float
# (1.) * (2.)= (2.) - float * float = float
# Python 2.x
# x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")
# Python 2.x
# x = float(raw_input("Lietotāj, lūdzu, ievadi argumentu (x): "))
# Python 3.x
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = sin(x)*sin(x)
print("sin**2(%.2f) = %.2f"%(x,y))
a0 = (-1)**2*x**2*2**1/(2*1)
S0 = a0
print("a0 = %.2f S0 = %.2f"%(a0,S0))
a1 = (-1)**3*x**4*2**3/(4*3*2*1)
S1 = a0 + a1
print("a1 = %.2f S1 = %.2f"%(a1,S1))
a2 = (-1)**4*x**6*2**5/(6*5*4*3*2*1)
S2 = a0 + a1 + a2
print("a2 = %.2f S2 = %.2f"%(a2,S2))
a3 = (-1)**5*x**8*2**7/(8*7*6*5*4*3*2*1)
S3 = a0 + a1 + a2 + a3
print("a3 = %.2f S3 = %.2f"%(a3,S3))
