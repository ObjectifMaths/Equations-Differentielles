import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')



sol=lambda t,K,L: K*(3/4*(t**3-t)*np.log(abs((t+1)/(t-1)))-3*t**2/2+1)+ L*(t**3-t)



# trace les axes
ec=.1
xx,XX= -1+ec, 1-ec
yy,YY=plt.ylim(-3,3) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
#plt.axes().set_aspect('equal')

LineStyle=['-', '--'] # style de ligne
ctes=[(1,0),(0,1)] # conditions initiales
col=[(.5,.5,.5), (.8,.7,0)] # couleur des courbes définies avec les valeurs (red,green, blue)
# avec l'expression des solutions
T=np.linspace(xx,XX)
for (K,L), col,LS in zip(ctes,col,LineStyle):
    print(K,L,col,LS)
    Z=sol(T,K,L)
    plt.plot(T,Z,color=col,linestyle=LS, label=r"$\lambda={}$ et $\mu={}$".format(K,L))


plt.title(r"$ (t^2-1)y''-6y=0$ sur $\rbrack {-1},1\lbrack$",fontsize=20)
plt.xlabel(r"$ y(t) = \lambda\left( \frac 34 \cdot (t^3-t)\cdot  \ln\abs{ \frac{t+1}{t-1}}  - \frac 32\cdot t^2+1   \right) + \mu (t^3-t)$",fontsize=15)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

