import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: (2*t/np.sqrt(1+t**2)-y)/t
sol=lambda t,k: (k+2*np.sqrt(1+t**2))/t



# trace les axes

xx,XX= -4,4
plt.ylim(-4,4) # limite l'axe des ordonnées
yy,YY=plt.ylim()

plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')



pen=['g','r', 'c', 'b' ]
cteK=[1,-1, 2, -2]

ec=.01
T1=np.linspace(ec, XX)
T2=np.linspace(xx, -ec)
for K,col in zip(cteK,pen):
   Z1=sol(T1,K)
   plt.plot(T1,Z1, col+'-', label="K={}".format(K))
   Z2=sol(T2,K)
   plt.plot(T2,Z2, col+'-')
      

plt.title(r"$t^2(1+t^2)y'(t)-(1+t)y(t)=t^4-t$",fontsize=20)
plt.xlabel(r"$t\mapsto \frac{K+2\sqrt{1+t^2}}{t}$")
plt.grid()
plt.legend()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()


