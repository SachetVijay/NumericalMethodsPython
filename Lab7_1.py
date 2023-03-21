import math
import matplotlib.pyplot as plt

def f(x):
  return 2.0*(x**2)*math.cos(x**2)
def trapezoidal(x0,xn,n):
    h =(xn-x0)/n

    inti=f(x0)+f(xn)

    for i in range(1,n):
        k=x0+i*h
        inti=inti+2*f(k)

    inti=inti*h/2

    return inti

lower_limit = 0
upper_limit = math.sqrt(math.pi)
sub_interval = int(input("Enter number of panels: "))
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print( "Integration result by Trapezoidal method is: %0.6f " % (result) )