import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


def hamiltonian(x, y, px, py): #Henon
    h=0.5*(px**2+py**2)+0.5*(x**2+y**2)+x**2*y-(y**3)/3    
    return (h)


E=0.01
h=0.01
x=0
y= np.random.uniform(-0.05, 0.05)
py= np.random.uniform(-0.05, 0.05)
px= np.sqrt(2*E-y**2+2/3*y**3-py**2)


def f(x,y):
    return -x-2*x*y

def g(x,y):
    return -y-x**2+y**2

xl=[]
xl.append(x)
yl=[]
yl.append(y)
pyl=[]
pyl.append(py)
pxl=[]
pxl.append(px)

for i in range (50000):
    xplus=x+px*h+0.5*h**2*f(x,y)
    yplus=y+py*h+0.5*h**2*g(x,y) 

    pxplus=px+0.5*h*(f(x,y)+f(xplus, yplus))
    pyplus=py+0.5*h*(g(x,y)+g(xplus, yplus))
    
    x=xplus
    xl.append(x)
    y=yplus
    yl.append(y)
    px=pxplus
    pxl.append(px)
    py=pyplus
    pyl.append(py)

plt.plot(xl,yl)
plt.show()
