import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')
plt.rc('text.latex', preamble=r'\renewcommand{\sinh}{\mathrm{sh}}')


# équation différentielle sous la forme y'=f(y,x)
f= lambda y,t:  (t*y-t**2)/(t+1)  
sol= lambda t,k: (k*np.exp(t) + (t**2+2*t+2))/(t+1)


# trace les axes
xx,XX= -6, 3
yy,YY=plt.ylim(-3,7) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')



# avec l'expression des solutions
LineStyle=['-.', '--', ':'] # style de ligne
cteK=[-1,0,1] # conditions initiales
couleurs=[(.5,.7,.9),(.4,.45,.35),(.9,.5,.7)] # couleur des courbes définies avec les valeurs (red,green, blue)
ec=.01 # pour éviter la singularité en $-1$
T1=np.linspace(xx,-1-ec) 
T2=np.linspace(XX,-1+ec)
for k,LS,col in zip(cteK,LineStyle,couleurs):
    Z1=sol(T1,k)
    Z2=sol(T2,k)
    plt.plot(T1,Z1, color=col, linestyle=LS, label="$K={}$".format(k))
    plt.plot(T2,Z2, color=col, linestyle=LS)


# la solution définie sur R tout entier
T=np.linspace(xx,XX) # en espérant que $-1$ ne soit pas dans la liste...
plt.plot(T,sol(T,-np.exp(1)), color='red', linestyle='-', label="$K=-e$")
    
plt.title(r"$t\cdot y-(1+t)\cdot y'=t^2 $",fontsize=20)
plt.xlabel(r"$y(t)= \frac{K\cdot  \exp (t) + t^2+2t+2}{t+1}  $")
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

