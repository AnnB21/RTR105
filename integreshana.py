# -*- coding: utf-8 -*-
from numpy import random,sin 
from matplotlib import pyplot as plt

N = 10000

a = 0
b = 5


x= random.uniform(a, b, N)
y = random.uniform(a, b, N)

plt.grid()
plt.xlabel('x')
plt.ylabel('y')

plt.title('Funkcija sin^2 x un tās integrālis (laukums starp funkciju un x ass)')
#plt.plot(x, y, 'ko')

N1 = 1

for i in range(N):
    if y[i] < (sin(x[i])*sin(x[i]))/ 2:
        plt.plot(x[i], y[i], 'go')
        N1 = N1 + 1
    else:
        plt.plot(x[i], y[i], 'ro')
        
plt.show()

S = (b - a) * (b - a)
S_nez = float(S * N1 / N)
print("Laukuma skaitliskā vertība:")
print(S_nez)
