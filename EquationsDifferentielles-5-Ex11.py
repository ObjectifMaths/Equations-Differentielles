import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: 1+t*y/(t**2+1)
sol=lambda t,k: (k+np.arcsinh(t))*np.sqrt(t**2+1)



# trace les axes

xx,XX= -3,3
yy,YY=plt.ylim(-4,4) # limite l'axe des ordonnées

plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')



pen=['g','r', 'b' ]
cteK=[1,-1, -2]

# avec l'expression des solutions
T=np.linspace(xx, XX)
for K,col in zip(cteK,pen):
   Z=sol(T,K)
   plt.plot(T,Z, col+'-', label="K={}".format(K))

# avec odeint
y0=2
col='y'
T1=np.linspace(0,XX)
T2=np.linspace(0,xx)
Z1=spig.odeint(f,y0,T1) # solution sur R+
Z2=spig.odeint(f,y0,T2) # solution sur R-
plt.plot(T1,Z1, col+'-', label="avec odeint")
plt.plot(T2, Z2, col+'-')
plt.plot (T1[0],y0, col+'o') # met en évidence la condition initiale
# les 3 plt.plot sont séparés pour que la légende n'apparaisse pas trois fois


plt.title(r"$(t^2+1)y'(t)-ty(t)=t^2+1$",fontsize=20)
plt.xlabel(r"$t\mapsto  (K+ \mathrm{argsh} (t)) \cdot  \sqrt{t^2+1}$")
plt.grid()
plt.legend()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()


