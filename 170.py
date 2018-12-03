#Fails: 170.py
# Autors: Anna Bogačova
# Apliecibas numurs: 181REB372
# Datums: 03/12/2018
# Sagatave funkcijas saknes meklesanai ar dihatonijas metodi

# -*- coding: utf-8 -*-
from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

# Definejam argumenta x robežas:
a = 1.1
b = 3.2

# Aprekinajam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

# Parbaudam, vai dotajā intervalā ir saknes:
if (funa * funb > 0.0):
    print ("Dotajā intervālā [%s, %s] sakņu nav")%(a,b)
    sleep(1); exit() # Ziņo uz ekrana, gaida 1 sec. un darbu pabeidz
else:
    print ("Dotajā intervālā sakne(s) ir!")

# Definejam precizitati, ar kadu meklesim sakni:
detlax = 0.01
k = 0

# Sašaurinam saknes meklēšanas robežas:
while (fabs(b-a) > detlax ):
    k = k+1
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x

print ("Sakne ir: ", x)
print ("f(x)= ", f(x))
print ("k= ", k)

