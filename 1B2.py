import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *

x = linspace(0, 4, 70)   
ya = sin(x)
yb = x
yc = x - x**3/(3*2*1)
yd = x - x**3/(3*2*1) + x**5/(5*4*3*2*1)
ye = x - x**3/(3*2*1) + x**5/(5*4*3*2*1) - x**7/(7*6*5*4*3*2*1)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcijas')
plt.plot(x, ya)
plt.plot(x, ya, color = "#00FF40")
plt.plot(x, yb, color = "#F5A9F2")
plt.plot(x, yc, color = "#DF3A01")
plt.plot(x, yd, color = "#2EFEF7")
plt.plot(x, ye, color = "#610B38")

plt.show()
