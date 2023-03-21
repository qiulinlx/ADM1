import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.integrate import odeint, solve_ivp
from mpl_toolkits.mplot3d import Axes3D

# Define the Henon-Heiles Hamiltonian function
def hamiltonian(q, p):
    return 0.5*(p[0]**2 + p[1]**2) + 0.5*(q[0]**2 + q[1]**2) + q[0]**2*q[1] - (1/3)*q[1]**3

# Define the system of differential equations
def henon_heiles(t, z):
    q1, q2, p1, p2 = z
    dq1 = p1
    dq2 = p2
    dp1 = -q1 - 2*q1*q2
    dp2 = -q2 - q1**2 + q2**2
    return [dq1, dq2, dp1, dp2]

# Set initial conditions
E=0.01
q1_01 = 0
q2_01 = -0.05
p2_01 = 0.05
p1_01 = np.sqrt(2*E-q2_01**2+2/3*q2_01**3-p2_01**2)

#Set time
endtime= 400
t_span = (0, endtime)
t_eval = np.linspace(0, endtime, 2000)

z1 = [q1_01, q2_01, p1_01, p2_01] #IC
sol1 = solve_ivp(henon_heiles, t_span, z1, rtol= 10**(-12), t_eval=t_eval, method='DOP853')

#Poincare section 1
q11=sol1.y[0]
q21=sol1.y[1]
p11=sol1.y[2]
p21=sol1.y[3]

y1=[]
yv1=[]

for i in range(len(p11)):
    if (( 0 < p11[i] )) and ((-0.001 < q11[i] < 0.001)):
        y1.append(q21[i])
        yv1.append(p21[i])


z1 = [q1_01, q2_01, p1_01, p2_01] #IC
sol1 = solve_ivp(henon_heiles, t_span, z1, t_eval=t_eval, method='DOP853')


#Plot the trajectory in 3D phase space
end= len(sol1.y[0])
ts= np.linspace(0, endtime ,end)

fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.set_ylim([0, 10])
ax.plot3D(sol1.y[0], ts, sol1.y[1], 'turquoise')
#ax.plot3D(sol0.y[0], ts, sol0.y[1], 'grey')

ax.set_xlabel('x')
ax.set_ylabel('time')
ax.set_zlabel('y')
ax.set_title('Henon-Heiles Hamiltonian')
plt.show()

fig=plt.figure()
plt.plot(sol1.y[0], sol1.y[1], color='turquoise')
plt.show()