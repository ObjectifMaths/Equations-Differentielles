import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')


# on pose z=y' et Y=(y,z)
# y=Y[0] et z=Y[1]
f=lambda Y,t: ( Y[1] ,6*Y[0]/(t**2-1) )



# trace les axes
ec=.1
xx,XX= -1+ec, 1-ec
yy,YY=plt.ylim(-4,4) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
#plt.axes().set_aspect('equal')
 
CI=[(0,1,0),(0,-1,-1)] # conditions initiales
col=['b', 'r'] # couleur des courbes
# avec odeint
for (x0,y0,y1), col in zip(CI,col):
    T1=np.linspace(x0,XX)
    T2=np.linspace(x0,xx)
    Z1=spig.odeint(f,(y0,y1), T1)
    Z2=spig.odeint(f,(y0,y1), T2)
    plt.plot(T1,Z1[:,0], col+'-', label=r"$y({0})={1}$ et $y'({0})={2}$".format(x0,y0,y1))
    plt.plot(T2,Z2[:,0], col+'-')
    plt.plot(x0,y0,col+'o') # mise en evidence de la position initiale
    dx=.5
    plt.plot([x0-dx,x0+dx], [y0-y1*dx,y0+y1*dx],col+'-') # trace la tangente à la position initiale

plt.title(r"$ (t^2-1)y''-6y=0$ sur $\rbrack {-1},1\lbrack$",fontsize=20)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

