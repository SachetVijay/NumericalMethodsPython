# Q2 Cubic Spline Method
import numpy as np
import matplotlib.pyplot as plt

def neville(x,A,B,i,m):
    if m == 0:
        return B[i]
    p=neville(x,A,B,i,m-1)
    pn=neville(x,A,B,i+1,m-1)
    return ((x-A[i+m])*p + ((A[i]-x)*pn))/(A[i]-A[i+m])

def f(x):
    return 1/(1+25*x**2)
xd = [-1.0, -0.5, 0.0, 0.5, 1.0]
yd = [0.0385, 0.1379, 1.0, 0.1379, 0.0385]
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

x = np.linspace(-1, 1, 1000)
y = np.zeros(1000)
yn = neville(x,xd,yd,0,nd-1)

for i in range(0,1000):
    if x[i] <= xd[1]:
        y[i] = fi(x[i], 0)
    elif x[i] <= xd[2]:
        y[i] = fi(x[i], 1)
    elif x[i] <= xd[3]:
        y[i] = fi(x[i], 2)
    else:
        y[i] = fi(x[i], 3)
plt.plot(x, y)
plt.plot(xd, yd, 'ro')
plt.plot(x, yn)
plt.plot(x, f(x))
plt.legend(['Cubic Spline', 'Data', 'Neville', 'f(x)'])
plt.show()