import sys
sys.path.append("/usr/lib/python2.7/dist-packages/numpy/")
sys.path.append("/usr/lib/python2.7/dist-packages/matplotlib/")


from numpy import *
x = linspace(0, 7, 11)
y = sin(x)*sin(x)
ya = x**2
yb= ya -x**4/(1*2*3*4)
yc= yb - x**6/(1*2*3*4*5*6)
yd= yc-x**8/(1*2*3*4*5*6*7*8)
ye= yd-x**10/(1*2*3*4*5*6*7*8*9*10)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $sin^2(x)$")

plt.plot(x, y)
plt.plot(x,yb)
plt.plot(x,yc)
plt.plot(x,yd)
plt.plot(x,ye)
plt.show()
