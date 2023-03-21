#Error Analysis

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.integrate import odeint, solve_ivp
from mpl_toolkits.mplot3d import Axes3D
import statistics as st

#Define the Henon-Heiles Hamiltonian function
def hamiltonian(q1, q2, p1, p2) :
    return 0.5*(p1**2 + p2**2) + 0.5*(q1**2 + q2**2) + q1**2*q2 - (1/3)*q2**3

# Define the system of differential equations
def henon_heiles(t, z):
    q1, q2, p1, p2 = z
    dq1 = p1
    dq2 = p2
    dp1 = -q1 - 2*q1*q2
    dp2 = -q2 - q1**2 + q2**2
    return [dq1, dq2, dp1, dp2]

E= 1/12

for i in range (1,5):
    if i == 1:
        E=1/6
    if i == 2:
        E=1/8
    if i == 3:
        E=1/12  
    if i == 4:
        E=1/24  
    q1_00=0
    q2_00= 0.1
    p2_00= 0.1
    p1_00= np.sqrt(2*E-q2_00**2+2/3*q2_00**3-p2_00**2)

    #Set time
    endtime= 4000
    t_span = (0, endtime)

    z0 = [q1_00, q2_00, p1_00, p2_00] #IC
    sol0 = solve_ivp(henon_heiles, t_span, z0, rtol= 10**(-12), method='DOP853' ) #Up to here is correct

    #Poincare section 0
    q10=sol0.y[0]
    q20=sol0.y[1]
    p10=sol0.y[2]
    p20=sol0.y[3]

    h0= hamiltonian(q10, q20, p10, p20)

    Error= np.abs(h0-E)/E
    std= st.stdev(Error)
    mean= st.mean(Error)
    print(str(E), 'standard deviation', std)
    print(str(E), 'mean', mean)
    t_eval = np.linspace(0, endtime, len(Error))
    plt.plot(t_eval, Error, lw=0.5, label='E= '+str(E))


plt.xlabel('t')
plt.ylabel('Error')
plt.legend()

plt.show()