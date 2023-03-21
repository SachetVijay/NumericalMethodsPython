import numpy as np
import matplotlib.pyplot as mpl

def neville(x,A,B,i,m):
    if m == 0:
        return B[i]
        
    p=neville(x,A,B,i,m-1)
    pn=neville(x,A,B,i+1,m-1)
    return ((x-A[i+m])*p + ((A[i]-x)*pn))/(A[i]-A[i+m])
    

A= [8.1, 8.3, 8.6, 8.7]
B= [16.95, 17.57, 18.51, 18.82]

print("For Data Points X : [8.1, 8.3, 8.6, 8.7] ") 


print("For Data Points Y : [16.95, 17.57, 18.51, 18.82] ")


x = np.arange(5,9,0.1)
y = neville(x,A,B,0,3)

mpl.scatter(A,B,color="blue")
mpl.plot(x,y,color="red")
mpl.show()
