import  math

from    scipy  import   integrate

def f(x):
    return  2.0*(x**2)*math.cos(x**2)
I   =   integrate.romberg(f,0,math.sqrt(math.pi), show = True)