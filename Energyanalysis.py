import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.integrate import odeint, solve_ivp
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm


x = np.linspace(-0.9, 0.9, 1500)
y = np.linspace(-0.9, 0.9, 1500)
X, Y = np.meshgrid(x, y)
Z = 1/2*(X**2+Y**2)+X**2*Y-(1/3)*Y**3

fig,ax=plt.subplots(1,1)
#cp = ax.contourf(X, Y, Z, inline=1)
cp= plt.contour(np.transpose(Z),np.linspace(Z.min(),Z.max(),25), inline=1, cmap=cm.coolwarm) 
plt.clabel(cp, inline=1, fontsize=5)
#fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Equipontential lines')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()