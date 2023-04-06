import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


def hamiltonian(x, y, px, py): #Henon
    h=0.5*(px**2+py**2)+0.5*(x**2+y**2)+x**2*y-(y**3)/3    
    return (h)


E=1/6
h=0.01
x=0
y= np.random.uniform(-0.05, 0.05)
py= np.random.uniform(-0.05, 0.05)
px= np.sqrt(2*E-y**2+2/3*y**3-py**2)

tau=0.01 
c1=0.5-np.sqrt(3)/6
c2= np.sqrt(3)/3
d1=0.5


def f(x,y):
    return -x-2*x*y

def g(x,y):
    return -y-x**2+y**2


def eA(c, x, y, px, py):
    x=x+tau*c*px
    y=y+tau*c*py
    px=px
    py=py
    return (x,y,px,py)

def eB(d, x, y, px, py):
    x=x
    y=y
    px=px+tau*d*f(x,y)
    py=py+tau*d*g(x,y)
    return (x,y,px,py)

def Saba2(w, x, y, px, py):
    z=eA(c1,x,y, px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]

    z=eB(d1, x,y,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]

    z=eA(c2, x,y,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]

    z= eB(d1, x,y,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]

    z=eA(c1,x,y,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]
    
    return (x,y,px,py)
    
xl=[]
xl.append(x)
yl=[]
yl.append(y)
pyl=[]
pyl.append(py)
pxl=[]
pxl.append(px)

error=[]

w1= -0.11776799841*10**-1
w2=  0.23557321336
w3=0.7845136104776
w0=1-2*(w1+w2+w3)

for i in range (1000):
    z=Saba2(w3, x,y ,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]

    z=Saba2(w2, x,y ,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]

    z=Saba2(w1, x,y ,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]

    z=Saba2(w0, x,y ,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]
    
    z=Saba2(w1, x,y ,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]
    
    z=Saba2(w2, x,y ,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]

    z=Saba2(w3, x,y ,px,py)
    x=z[0]
    y=z[1]
    px=z[2]
    py=z[3]

    e=hamiltonian(x, y, px, py)
    ee= np.log((E-e)/E)
    error.append(ee)
    xl.append(x)
    yl.append(y)
    pxl.append(px)
    pyl.append(py)

t=range(len(error))

#plt.plot(xl,yl)
plt.plot(t, error)
plt.show()
