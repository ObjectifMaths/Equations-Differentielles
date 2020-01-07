import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel

f=lambda y,x: (x**2+(x-2)*y)/x/(x+1)
sol=lambda x,k: (x+1)**3/x**2*(k+np.log(abs(x+1)))+ (18*x**2+27*x+11)/6/x**2


# trace les axes

xx,XX= -6,6
yy,YY=plt.ylim(-4,4) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')
 

pen=['g','r', 'b', 'c']
cteK=[1,-1, -2, -11/6]
etiqK=[r"$1$", r"$-1$", r"$-2$", r"$-\frac {11}{6}$"]

# avec l'expression des solutions 
ec=.05 # pour éviter les singularités en $-1$ et en $0$
T1=np.linspace(xx,-1-ec)
T2=np.linspace(-1+ec,-ec)
T3=np.linspace(XX,ec)
for K,col,L in zip(cteK,pen,etiqK):
   Z1=sol(T1,K)
   Z2=sol(T2,K)
   Z3=sol(T2,K)
   plt.plot(T1,Z1, col+'-', label="K={}".format(L))
   plt.plot(T2,Z2, col+'-',T3,Z3, col+'-')
      
# avec odeint
y0, y1,y2 = 0, -1,1
Z1=spig.odeint(f,y0,T1) # $\rbrack {-\infty},-1\lbrack$
T2_1=np.linspace(-.5,-ec)
T2_2=np.linspace(-.5,-1+ec)
Z2_1=spig.odeint(f,y1,T2_1) # solution sur $\rbrack -1,0\lbrack$
Z2_2=spig.odeint(f,y1,T2_2) # solution sur $\rbrack -1,0\lbrack$

Z3=spig.odeint(f,y2,T3) # solution sur $\rbrack 0, {+\infty}\lbrack$

plt.plot(T1,Z1, 'y-', T2_1, Z2_1, 'k-', T2_2, Z2_2, 'k-', T3,Z3,'m-', label="avec odeint")
plt.plot (T1[0],Z1[0], 'yo', T2_1[0],Z2_1[0], 'ko', T3[0],Z3[0], 'mo') # met en évidence la condition initiale

plt.xlabel(r"$x\mapsto  \frac{(x+1)^3}{x^2}\cdot (K+\ln\vert x+1\vert)  + \frac{18x^2+27x+11}{6x^2} $")
plt.title(r"$ x(x+1)y'-(x-2)y=x^2 $",fontsize=20)
plt.grid()
plt.legend()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

