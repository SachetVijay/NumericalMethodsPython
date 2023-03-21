import numpy as np
import matplotlib.pyplot as mpl

def neville(x,A,B,i,m):
    if m == 0:
        return B[i]

    p=neville(x,A,B,i,m-1)
    pn=neville(x,A,B,i+1,m-1)
    return ((x-A[i+m])*p + ((A[i]-x)*pn))/(A[i]-A[i+m])
    
A=[-1.0, -0.5, 0.0, 0.5, 1.0]
B=[0.0385, 0.1379, 1.0, 0.1379, 0.0385]

print("For Data Points X : [-1.0, -0.5, 0.0, 0.5, 1.0] ") 


print("For Data Points Y : [0.0385, 0.1379, 1.0, 0.1379, 0.0385] ")


x = np.arange(-1,1,0.01)
y = neville(x,A,B,0,4)

mpl.scatter(A,B,color="red")
mpl.plot(x,y,color="green")
c =[]
for i in range(len(x)):
    c.append(1/(1+25*x[i]*x[i]))

mpl.plot(x,c,color="blue")
mpl.show()

