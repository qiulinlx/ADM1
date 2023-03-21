import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint, solve_ivp
from matplotlib.patches import Rectangle

y=np.linspace(0,1.75, 10000)

E=0.5*y**2-1/3*y**3

plt.plot(y,E, color='black', linewidth=2)
plt.axhline(y=0.125)
plt.xlabel('y')
plt.fill_between(y, E, 1, color='lightsteelblue')
plt.fill_between(y, E, 0, color='salmon')
plt.fill_between(y, -0.25, E, color='lightgrey')

plt.ylabel('Energy')
plt.show()

dy=np.sqrt( 2*E+y**2-2/3*y**3)
