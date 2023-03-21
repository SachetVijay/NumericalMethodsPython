import numpy as np
import matplotlib.pyplot as plt

n = int(input('Enter the number of points :'))
arrX = np.zeros(n)
arrY = np.zeros(n)

for i in range (n):
    arrX[i] = float(input('Enter points x'+str(i)+': '))
    arrY[i] = float(input('Enter points y'+str(i)+': '))

x = float(input('Enter x  '))

def cardinal(x):
    x = float(x)
    li = 1.0
    for j in range(n):
        if arrX[i] != arrX[j]:
            li = li * (x - arrX[j])/(arrX[i] - arrX[j])
    return li      

pn = np.zeros(n)
ans = 0.0
for i in range (n):
    pn[i] = arrY[i] * cardinal(x)
    ans += pn[i]
 
print(ans)



z=0.1
for k in range (n):
    pltx=[]
    plty=[]
    while z<3:
        pltx.append(z)
        plty.append(cardinal(z))
        z=z+0.1
        plt.plot(pltx,plty)
    plt.show()    


