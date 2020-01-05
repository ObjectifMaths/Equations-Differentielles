import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel

f=lambda y,t: (1-(t+1)*y)/t
sol=lambda t,k: (K+np.exp(-t))/t




# trace les axes

xx,XX= -3,3
yy,YY=plt.ylim(-4,4) # limite l'axe des ordonnées

plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')
 

pen=['g','r', 'b' ]
cteK=[1,-1, -2]

# avec l'expression des solutions 
ec=.05 # pour éviter le pôle en 0
T1=np.linspace(xx,-ec)
T2=np.linspace(ec,XX)
for K,col in zip(cteK,pen):
   Z1=sol(T1,K)
   Z2=sol(T2,K)
   plt.plot(T1,Z1, col+'-', label="K={}".format(K))
   plt.plot(T2,Z2, col+'-')
      
# avec odeint
y0, y1 = 1, -1
T1=np.linspace(XX,ec)
Z1=spig.odeint(f,y0,T1) # solution sur R+
T2=np.linspace(xx,-ec)
Z2=spig.odeint(f,y1,T2) # solution sur R-
plt.plot(T1,Z1, 'y-', T2, Z2, 'c-', label="avec odeint")
plt.plot (T1[0],Z1[0], 'yo', T2[0],Z2[0], 'co') # met en évidence la condition initiale

plt.xlabel(r"$x \mapsto \frac{K+exp(-t)}{t} $")
plt.title(r"$ty'+(t+1)y=1$",fontsize=20)
plt.grid()
plt.legend()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

