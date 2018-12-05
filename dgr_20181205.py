#print(vars())
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
#print(vars())

from numpy import sin, linspace
#print(vars())

def f(x):
    return sin(x)

x= linspace(0,4,11)
#print(vars())

y=f(x)

legend = []
#print(legend)

from matplotlib import pyplot as plt
#print(plt.plot.__doc__) - ka vispar var uzdot robežas
plt.axis([0, 4,-1, 1])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $sin(x)$ un tās atvasinājumi")
plt.plot(x,y,"k")
legend.append("$sin(x)$ - default - viss ir savienots ar taisnam līnijam")
#print(legend)
plt.plot(x,y,"ro")
legend.append("$sin(x)$ - tikai daži punkti")
#print(legend)

N = len(x)
deltax = x[1] - x[0]
derivative = []

for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    derivative.append(temp)

plt.plot(x, derivative, "y")
legend.append("$sin(x)$ atvsinājums - viss ir savienots ar taisnam līnijam")
plt.plot(x, derivative, "go")
legend.append("$sin(x)$ atvasinājums - daži punkti")

#b punkta sakums

derivative_through_array = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    derivative_through_array.append(temp)

plt.plot(x[0:N-1], derivative_through_array, "m")
legend.append("$sin(x)$ atvsinājums, izmantojot masīva vērtības, - viss ir savienots ar taisnam līnijām")
plt.plot(x[0:N-1], derivative_through_array, "bo")
legend.append("$sin(x)$ atvsinājums, izmantojot masīva vērtības, - daži punkti")



plt.plot(0.680,0.620,"ch",markersize = 9)    
#print(plt.legend.__doc__)
#plt.legend(legend, loc ="upper left")
plt.legend(legend, loc = 3, fancybox=True, framealpha=0.5, facecolor="pink")
plt.show()
