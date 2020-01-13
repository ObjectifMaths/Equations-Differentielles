import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')



sol=lambda x,K: K*np.exp(1/x**2)*x**3+x**3


# trace les axes
xx,XX= -3, 3
yy,YY=plt.ylim(-3,3) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

LineStyle=['-', '--', '-', ':'] # style de ligne
ctes=[-.5,.5,.25,0] # constantes d'intégrations
col=[(.5,.5,.75), (.8,.4,1), (.5,.8,.9),(1,.5,.2)] # couleur des courbes définies avec les valeurs (red,green, blue)


# avec l'expression des solutions
ec=.01 # pour éviter la singularité en $0$
T1=np.linspace(xx,-ec)
T2=np.linspace(ec, XX)
for K, col,LS in zip(ctes,col,LineStyle):
    Z1=sol(T1,K)
    Z2=sol(T2,K)
    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"$K={}$".format(K))
    plt.plot(T2,Z2,color=col,linestyle=LS)
    
plt.title(r"$ x^3y'+(2-3x^2)y=x^3$",fontsize=20)
plt.xlabel(r"$ y(x) = K\cdot  \exp\left(\frac{1}{x^2}\right)\cdot x^3 +x^3  $",fontsize=15)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

