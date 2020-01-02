import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig


f=lambda y,t: t+np.sin(y)**2
y0=1
T=np.linspace(0,2,10)

Z=spig.odeint(f,y0,T)
plt.plot(T,Z,'g-')
plt.title("$ y'=x+\sin^2y  \quad  y(0)  =  1 $")
plt.xlabel("Avec spig.odeint",fontsize=20)


# trace les axes
xx,XX=-.25,2.25
yy,YY=-.25,4
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.xlabel(u"Avec la fonction odeint",fontsize=20)
plt.axes().set_aspect('equal')

plt.grid()
plt.show()


