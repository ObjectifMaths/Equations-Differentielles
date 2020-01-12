import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')



sol=lambda t,K,L: (K*np.log(abs(t))+L)*t+t**3/4


# trace les axes
ec=.01
xx,XX= -3+ec, 3-ec
yy,YY=plt.ylim(-3,3) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
#plt.axes().set_aspect('equal')

LineStyle=['-', '--'] # style de ligne
ctes=[(1,0),(0,1)] # conditions initiales
col=[(.5,.5,.5), (.8,.7,0)] # couleur des courbes définies avec les valeurs (red,green, blue)


# avec l'expression des solutions
T1=np.linspace(ec,XX) # sur $\RR_+^*$
T2=np.linspace(-ec,xx) # sur $\RR_-^*$ 
for (K,L), col,LS in zip(ctes,col,LineStyle):
    Z1=sol(T1,K,L)
    Z2=sol(T2,K,L)
    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"$\lambda={}$ et $\mu={}$".format(K,L))
    plt.plot(T2,Z2,color=col,linestyle=LS)


plt.title(r"$ t^2y''-ty'+y=t^3$",fontsize=20)
plt.xlabel(r"$ y(t) = (\lambda \ln \abs t + \mu)\cdot t  + \frac{t^3}{4}  $",fontsize=15)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

