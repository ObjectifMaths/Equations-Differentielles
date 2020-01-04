import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: (t**4-t+(t+1)*y)/t**2/(1+t**2)


pen=['g','r', 'c' ]
init=[1,-1, 2]


# trace les axes

xx,XX= -.1,4
plt.ylim(-4,4) # limite l'axe des ordonnées
yy,YY=plt.ylim()

plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')


ec=.01

# avec odeint
T=np.linspace(XX, ec) 
for y0, col in zip(init,pen):
   Z=spig.odeint(f,y0,T)
   plt.plot(T,Z,col+'-', label="avec odeint")
   plt.plot(T[0], y0, col+'o')
   

plt.title(r"$t^2(1+t^2)y'(t)-(1+t)y(t)=t^4-t$",fontsize=20)

plt.grid()
#plt.legend()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()


