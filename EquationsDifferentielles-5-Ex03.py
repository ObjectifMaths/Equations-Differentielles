import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: (t**2+3*y)/(t+1)


pend=['g', 'r', 'b']
peng=['y', 'm', 'c']
initd=[-.8, 1.2, 1.6]
initg=[-0.8, 0, 1.6]

for y0, col in zip(initd,pend):
    # à droite de -1
    T=np.linspace(2,-1)
    Z=spig.odeint(f,y0,T)
    plt.plot(T,Z,col+'-')
    plt.plot(T[0],y0,col+'o')
    xx,XX=min(T), max(T)
    
    
for y0, col in zip(initg,peng):
    # à gauche de -1
    T=np.linspace(-3,-1)
    Z=spig.odeint(f,y0,T) 
    plt.plot(T,Z,col+'-')


plt.title(r"$ (t+1)y'-3y=t^2$",fontsize=20)
plt.ylim(-2,2) # limite l'axe des ordonnées

# trace les axes
xx,XX= -3,2
yy,YY=plt.ylim()
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()


