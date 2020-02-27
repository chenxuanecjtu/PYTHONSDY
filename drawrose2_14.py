#drawrose

import matplotlib

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
#ax=fig.gca(projection='3d')
ax = Axes3D(fig)

#[x,t]=np.meshgrid(np.array(range(25))/24.0,np.arange(0,575.5,0.5)/575*17*np.pi-2*np.pi)
x=np.array(range(25))/24.0
t=np.arange(0,575.5,0.5)/575*17*np.pi-2*np.pi

x,t=np.meshgrid(x,t)

p=(np.pi/2)*np.exp(-t/(8*np.pi))
u=1-(1-np.mod(3.6*t,2*np.pi)/np.pi)**4/2
y=2*(x**2-x)**2*np.sin(p)
r=u*(x*np.sin(p)+y*np.cos(p))

xx=r*np.cos(t)
yy=r*np.sin(t)
zz=u*(x*np.cos(p)-y*np.sin(p))
surf=ax.plot_surface(xx*10,yy*10,zz*10,rstride=5,cstride=5, cmap="Reds",linewidth=0,antialiased=True)

for i in range(0,20):
	x1 = np.linspace(-0.8,0.8,2)
	y1 = np.linspace(0.8,-0.8,2)
	x1,y1=np.meshgrid(x1,y1)
	z1=x1+y1-i
	surf=ax.plot_surface(x1,y1,z1,rstride=5,cstride=5, cmap="Dark2",linewidth=10,antialiased=True)
	x1 = np.linspace(0.8,-0.8,2)
	y1 = np.linspace(-0.8,0.8,2)
	x1,y1=np.meshgrid(x1,y1)
	z1=1.6-x1-y1-i
	surf1=ax.plot_surface(x1,y1,z1,rstride=5,cstride=5, cmap="Dark2",linewidth=10,antialiased=True)
	
#surf=ax.plot_surface(xx,yy,zz,rstride=7,cstride=7, cmap="Reds",linewidth=0,antialiased=True)
#rstride cstride xy sm


plt.axis('off')
plt.title("2020214  to ctz ",color="pink")
plt.xticks([])
plt.yticks([])

ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([0.3, 0.3, 1, 1]))

plt.show()
