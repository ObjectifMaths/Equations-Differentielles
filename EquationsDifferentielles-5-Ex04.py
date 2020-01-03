import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: ((2*t-1)*np.exp(t)-(t-1)*y)/t


pen=['g', 'b', 'r', 'c']
init=[7.6, -1, 5,1]


for y0, col in zip(init,pen):
    T=np.linspace(2,-2,100)
    Z=spig.odeint(f,y0,T)
    plt.plot(T,Z,col+'-')
    plt.plot(T[0],y0,col+'o')
    xx,XX=min(T), max(T)
    
    


plt.title(r"$ty'+(t-1)y=(2t-1)\exp(t)$",fontsize=20)
plt.ylim(-10,8) # limite l'axe des ordonnées

# trace les axes
xx,XX= -3,2
yy,YY=plt.ylim()
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
#plt.axes().set_aspect('equal')

plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()


