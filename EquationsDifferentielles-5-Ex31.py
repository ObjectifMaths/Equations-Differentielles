import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')



f= lambda y,x: (x-2*x*y)/(x**2+1) # l'équatino différentielle sous la forme y'=f(y,x)
sol=lambda x,K: (x**2/2+K)/(x**2+1)# expression des solutions


# trace les axes
xx,XX= -4.5, 4.5
yy,YY=plt.ylim(-3,3) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

# avec l'expression des solutions
LineStyle=['-', '--'] # style de ligne
ctes=[2,-1] # constantes d'intégrations
col=[(.75,.25,.75), (.25,.25,.25),] # couleur des courbes définies avec les valeurs (red,green, blue)
T=np.linspace(xx,XX)
for K, col,LS in zip(ctes,col,LineStyle):
    Z=sol(T,K)
    plt.plot(T,Z,color=col,linestyle=LS, label=r"$K={}$".format(K))

# avec odeint
LineStyle=[':', '-.'] # style de ligne
CI=[(0,1),(0,-2)] # conditions initiales
col=[(0,.75,.75), (.2,0.5,.75),] # couleur des courbes définies avec les valeurs (red,green, blue)
T1=np.linspace(0,XX)
T2=np.linspace(0,xx)
for (x0,y0), col,LS in zip(CI,col,LineStyle):
    Z1=spig.odeint(f,y0,T1)
    Z2=spig.odeint(f,y0,T2)

    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"avec odeint $y({})={}$".format(x0,y0))
    plt.plot(T2,Z2,color=col,linestyle=LS)
    plt.plot(x0,y0,color=col,marker='o') # mise en evidence de la condition initiale
    
plt.title(r"$ (x^2+1)y'+2xy=x$",fontsize=20)
plt.xlabel(r"$ y(x) = \frac{x^2/2+K}{x^2+1}$",fontsize=15)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

