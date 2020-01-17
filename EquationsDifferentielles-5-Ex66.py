import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')



sol=lambda x,K: K*(np.cos(x)+np.sin(x))    # expression des solutions

# trace les axes
xx,XX= -5, 5
yy,YY=plt.ylim(-3,4) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

# avec l'expression des solutions
LineStyle=['-', '-'] # style de ligne
ctes=[2,-1] # constantes d'intégrations
col=[(.75,.25,.75), (.25,.25,.25),] # couleur des courbes définies avec les valeurs (red,green, blue)
ec=.01 # pour éviter la singularité en $1$
T=np.linspace(xx,XX,200)
for K, col,LS in zip(ctes,col,LineStyle):
    Z=sol(T,K)
    plt.plot(T,Z,color=col,linestyle=LS, label=r"$a={}$".format(K))

    
plt.title(r"$ y'(x)=y(-x) $",fontsize=20)
plt.xlabel(r"$ y(x) = a\cdot (\cos(x) + \sin(x) ) $",fontsize=15)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

