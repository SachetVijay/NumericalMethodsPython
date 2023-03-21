import numpy as np
import matplotlib.pyplot as plt

xd = [1.0, 2.0, 3.0, 4.0, 5.0]
yd = [0.0, 1.0, 0.0, 1.0, 0.0]
h = abs(xd[1]-xd[0]);
nd = len(xd)
k = np.zeros(nd)
ki = np.zeros(nd-2)
for i in range(1,nd-1):
    ki[i-1] = 6*(yd[i+1]-2*yd[i]+yd[i-1])/(h**2)
k[3] = (4*ki[2]-ki[1])/15
k[2] = (ki[1]-k[3])/4
k[1] = (ki[0]-k[2])/4

def fi(x, i):
    return (k[i]*((x-xd[i+1])**3/(xd[i]-

xd[i+1]) - (x - xd[i+1]) * (xd[i]- xd[i+1]))/6 - k[i+1]*((x-
xd[i])**3/(xd[i] - xd[i+1]) -(x-xd[i])*(xd[i]-xd[i+1]))/6 + (yd[i]*(x-
xd[i+1]) -yd[i+1]*(x-xd[i]))/(xd[i]-xd[i+1]))



x = np.linspace(0, 6, 100)
y = np.zeros(100)
for i in range(0,100):
    if x[i] <= xd[1]:
        y[i] = fi(x[i], 0)
    elif x[i] <= xd[2]:
        y[i] = fi(x[i], 1)
    elif x[i] <= xd[3]:
        y[i] = fi(x[i], 2)
    else:
        y[i] = fi(x[i], 3)
print(y)
plt.plot(x, y)
plt.plot(xd, yd, 'ro')
plt.plot(1.5, fi(1.5, 0), 'bo')
print(fi(1.5, 0))
plt.show()