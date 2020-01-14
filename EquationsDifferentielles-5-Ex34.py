import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')



f= lambda y,t:  (1+4*t**2*y)/(t**3-1)  # l'équation différentielle sous la forme y'=f(y,x)
sol=lambda t,K: K*(abs(t**3-1))**(4/3) + 3*t**4/4 -t    # expression des solutions


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
T=np.linspace(-2,2,200)
for K, col,LS in zip(ctes,col,LineStyle):
    Z=sol(T,K)
    plt.plot(T,Z,color=col,linestyle=LS, label=r"$K={}$".format(K))

# avec odeint sur $\rbrack1,+\infty\lbrack$
LineStyle=['-', '-'] # style de ligne
CI=[1,-2] # conditions initiales
col=[(0,.75,.75), (.2,0.5,.75),] # couleur des courbes définies avec les valeurs (red,green, blue)
T1=np.linspace(XX, 1+ec)
T2=np.linspace(xx, 1-ec)
for y0, col,LS in zip(CI,col,LineStyle):
    Z1=spig.odeint(f,y0,T1)
    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"avec odeint $y({})={}$".format(XX,y0))
    plt.plot(XX,y0,color=col,marker='o') # mise en evidence de la condition initiale

# avec odeint sur $\rbrack -\infty ,1\lbrack$
LineStyle=['-', '-'] # style de ligne
CI=[1,-2] # conditions initiales
col=[(.75,.5,.25), (.25,0.75,.25),] # couleur des courbes définies avec les valeurs (red,green, blue)
ec=.05 # pour éviter la singularité en $1$
for y0, col,LS in zip(CI,col,LineStyle):
    Z2=spig.odeint(f,y0,T2)
    plt.plot(T2,Z2,color=col,linestyle=LS, label=r"avec odeint $y({})={}$".format(xx,y0))
    plt.plot(xx,y0,color=col,marker='o') # mise en evidence de la condition initiale


    
plt.title(r"$  (t^3-1)y'-4t^2 y=1 $",fontsize=20)
plt.xlabel(r"$ y(t) = K\cdot (t^3-1)^{4/3} + \frac {3}{4}\cdot t^4-t $",fontsize=15)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

