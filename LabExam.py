import numpy as np
x1=8.21
y1=0.00
x2=0.34
y2=6.62
x3=5.96
y3=-1.12

def radius(a,b,x,y):
    return np.sqrt((a-x)**2+(b-y)**2)

arr1=[x2-x1, y2-y1, (x2**2-x1**2)+(y2**2-y1**2)]
arr2=[x2-x3, y2-y3, (x2**2-x3**2)+(y2**2-y3**2)]

arr1[0]= arr1[0] - (arr2[0]*arr1[1]/arr2[1])
arr1[2]= arr1[2] - (arr2[2]*arr1[1]/arr2[1])

a=arr1[2]/arr1[0]
b=(arr2[0]-(arr2[0]*a))/arr2[1]

R= radius(a,b,x1,y1)

print(f"a={a}, b={b}, c={R}")
