import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')



sol=lambda x,K: K*(x-2)+(x-2)**3


# trace les axes
xx,XX= -1, 5
yy,YY=plt.ylim(-3,3) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

LineStyle=['-', '--', '-', ':'] # style de ligne
ctes=[-1,1,2,-3] # conditions initiales
col=[(.5,.5,.5), (.8,.7,0), (0,.8,.9),(1,.5,.2)] # couleur des courbes définies avec les valeurs (red,green, blue)


# avec l'expression des solutions
T=np.linspace(xx,XX) 
for K, col,LS in zip(ctes,col,LineStyle):
    Z=sol(T,K)
    plt.plot(T,Z,color=col,linestyle=LS, label=r"$K={}$".format(K))

plt.title(r"$ (x-2)y'-y=2(x-2)^3$",fontsize=20)
plt.xlabel(r"$ y(x) = K\cdot (x-2)+(x-2)^3  $",fontsize=15)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

