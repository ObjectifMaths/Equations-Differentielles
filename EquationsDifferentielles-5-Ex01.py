import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: 2/t*y-1
y0=1.2

# à droite de y0
T=np.linspace(1,2)
Z=spig.odeint(f,y0,T)
plt.plot(T,Z,'g-')
plt.plot(T[0],y0,'go')
xx,XX=min(T), max(T)

# à gauche de y0
T=np.linspace(1,-2)
Z=spig.odeint(f,y0,T)
plt.plot(T,Z,'g-')


plt.title("$ ty'-2y=-t \quad y({})={} $".format(T[0],y0),fontsize=20)
plt.ylim(-1,2.5) # limite l'axe des ordonnées

# trace les axes
xx,XX= min(min(T),xx), max(max(T),XX)
yy,YY=plt.ylim()
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

plt.grid()
plt.savefig("EquationsDifferentielles-5-Ex01.pdf")
plt.show()


