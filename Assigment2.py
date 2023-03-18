import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import time 

 # record start time
start = time.time()

def hamiltonian(x, y, px, py):
    h=0.5*(px**2+py**2)+1/24*(np.exp(2*y+2*np.sqrt(3)*x)+np.exp(2*y-2*np.sqrt(3)*x)+np.exp(-4*y))-1/8
    return (h)

def motion(t, z):
    x, y, px, py = z
    dxdt = px
    dydt = py
    dpxdt = -1/12*(np.sqrt(3)*np.exp(2*y+2*np.sqrt(3)*x)-np.sqrt(3)*np.exp(2*y-2*np.sqrt(3)*x))
    dpydt = -1/12*(np.exp(2*y+2*np.sqrt(3)*x)+np.exp(2*y-2*np.sqrt(3)*x)-2*np.exp(-4*y))
    return [dxdt, dydt, dpxdt, dpydt]

def Henon(x,w):
    t, y, dx, dy = w
    dt = 1/dx
    dq2=dy/dx
    dp1= -1/12*(np.sqrt(3)*np.exp(2*y+2*np.sqrt(3)*x)-np.sqrt(3)*np.exp(2*y-2*np.sqrt(3)*x))/dx
    dp2= -1/12*(np.exp(2*y+2*np.sqrt(3)*x)+np.exp(2*y-2*np.sqrt(3)*x)-2*np.exp(-4*y))/dx
    return [dt, dq2, dp1, dp2]

endtime= 2000
t_span = (0, endtime)
t_eval=np.arange(0, endtime, 0.01) 


H= 1
for i in range (30):
    x0= 0
    y0= np.random.uniform(-0.5, 0.5)
    py0=np.random.uniform(0, 1)
    #y0= np.random.uniform(-1, 2)
    #py0=np.random.uniform(0, 3)
    #y0= np.random.uniform(-1.5, 2.5)
    #py0=np.random.uniform(0, 12)
    #y0= np.random.uniform(-1.8, 2.8)
    #py0=np.random.uniform(0, 20)
    px0= np.sqrt(2*H-py0**2-1/12*(2*np.exp(2*y0)+np.exp(-4*y0))+1/4)

    z0 = [x0, y0, px0, py0] #IC
    sol0 = solve_ivp(motion, t_span, z0, rtol= 10**(-8), t_eval=t_eval ) #Up to here is correct

    #Poincare section 0
    q10=sol0.y[0]
    q20=sol0.y[1]
    p10=sol0.y[2]
    p20=sol0.y[3]



    y0=[]
    yv0=[]

    for i in range(len(p10)):
        if (( 0 < p10[i] )) and ( q10[i-1] < 0) and (q10[i]>0):
                xi= np.longdouble(q10[i-1])
                ti=np.longdouble(t_eval[i-1])
                x_span= (0, -xi)
                w= [ti,  np.longdouble(q20[i-1]),  np.longdouble(p10[i-1]),  np.longdouble(p20[i-1]) ]
                sol= solve_ivp(Henon, x_span, y0= w, rtol= 10**(-8) )
                y= sol.y[1]
                yv= sol.y[3]

                y0.append(y[-1])
                yv0.append(yv[-1])
                
                plt.scatter(y0, yv0, marker='.', s=2) #--------------------------------------------------------------
    del(y0)
    del(yv0)
    del(q10, q20, p10, p20)     

plt.xlabel('Position qy')       
plt.ylabel('Momentum py')
plt.savefig('PoincareSection100.png', dpi=800)

# record end time
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

#22:18