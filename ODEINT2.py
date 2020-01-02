import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

# résolution de $y''=\cos(y')-\sin(y)+t$, $y(0)= 1 $ et $y'(0)=-2  $  
# $z=y'$
# $Y =(y,z)$
# $Y'=(z,cos(z)-sin(y)+t)$

# Y[0] représente y, Y[1] représente y'=z
f=lambda Y,t: (Y[1], np.cos(Y[1]) - np.sin(Y[0])+t )

y0=(1,-2)
T=np.linspace(0,3.5,50)

Z=spig.odeint(f,y0,T)
plt.plot(T, Z[:,0], 'g-')
plt.title("$ y''=\cos(y')- \sin(y )+t  \quad  y(0)  =  1  \quad y'(0)=-2$")

# trace les axes
xx,XX=-.25,4
yy,YY=-2.25,2.5
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.xlabel(u"Avec la fonction odeint",fontsize=20)

plt.axes().set_aspect('equal')

plt.grid()
plt.show()


