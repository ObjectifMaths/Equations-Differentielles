import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel

f=lambda y,x: (x+3*y)/abs(x) 
solp= lambda x,k: K*x**3-x/2 # solution sur R+
solm= lambda x,k: K/x**3-x/4 # solution sur R-



# trace les axes

xx,XX= -5,5
yy,YY=plt.ylim(-4,4) # limite l'axe des ordonnées

plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')
 

pen=['g','r', 'b' ]
cteK=[1,-1, -2]

# avec l'expression des solutions sur R-
ec=.05 # pour éviter le pôle en 0
T=np.linspace(xx, -ec)
for K,col in zip(cteK,pen):
   Z=solm(T,K)
   plt.plot(T,Z, col+'-', label="K={}".format(K))

# avec l'expression des solutions sur R+
T=np.linspace(XX,0)
for K,col in zip(cteK,pen):
   Z=solp(T,K)
   plt.plot(T,Z, col+'-')
   
# avec odeint
y0, y1=2,1
T1=np.linspace(XX,0)
Z1=spig.odeint(f,y0,T1) # solution sur R+
T2=np.linspace(xx,0)
Z2=spig.odeint(f,y1,T2) # solution sur R-
plt.plot(T1,Z1, 'y-', T2, Z2, 'c-', label="avec odeint")
plt.plot (T1[0],Z1[0], 'yo', T2[0],Z2[0], 'co') # met en évidence la condition initiale
#
plt.xlabel(r"$x \mapsto \left\{\begin{array}{ccc}  \frac{K}{x^3} - \frac {x}{4}  & \textrm{si} & x <0 \\ Kx^3-\frac {x}{2} & \textrm{si} & x >0   \end{array}  \right.$")
plt.title(r"$\vert x \vert \cdot y'- 3y=x$",fontsize=20)
plt.grid()
plt.legend()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

