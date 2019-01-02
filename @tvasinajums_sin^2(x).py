# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from numpy import sin, linspace

def f(x):
    return sin(x)*sin(x)

x = linspace(0, 4, 10)
print(x)
y = f(x)
print(y

# pirmais atvasinajums
derivative = [] 
deltax = x[1] - x[0]
N = len(x)

for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    derivative.append(temp)

#otrais atvasinajums
derivative_through_array = [] 

for i in range(N - 1):
    temp = (derivative[i + 1] - derivative[i]) / deltax
    derivative_through_array.append(temp)

legend = []


plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("$sin^2(x)$ funkcija un tas atvasinājumi")

plt.plot(x, y, "k")
legend.append("$sin^2(x) funkcija$")
plt.plot(x, y, "ro")
legend.append("$sin^2(x) tikai daži punkti$")

plt.plot(x, derivative, "y")
legend.append("$sin^2(x)$ 1.k. atvasinājums")
plt.plot(x, derivative, "go")
legend.append("$sin^2(x)$ 1.k. atvas.(punkti)")

plt.plot(x[0:len(x) - 1], derivative_through_array, "m")
legend.append("$sin^2(x)$ 2.k. atvasinājums")
plt.plot(x[0:len(x) - 1], derivative_through_array, "bo")
legend.append("$sin^2(x)$ 2.k. atvas.(punkti)")
#Leģendas vieta attēlā
plt.legend(legend, loc=3) 


plt.show()
