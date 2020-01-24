import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')
plt.rc('text.latex', preamble=r'\renewcommand{\sinh}{\mathrm{sh}}')


# équation différentielle sous la forme y'=f(y,x)
f= lambda y,t: (y+np.log(t))/t 
sol=lambda t,k: k*t-1-np.log(t)

# trace les axes
xx,XX= -1, 4
yy,YY=plt.ylim(-2,2) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')



# avec odeint
ec=.1
LineStyle=['-', '--'] # style de ligne
CI=[(1,1),(1,-1)] # conditions initiales
couleurs=[(.8,.25,.15), (.2,.7,.2)] # couleur des courbes définies avec les valeurs (red,green, blue)
for (x0,y0), col,LS in zip(CI,couleurs,LineStyle):
    T1=np.linspace(x0,XX)
    T2=np.linspace(x0,ec)
    Z1=spig.odeint(f,y0,T1)
    Z2=spig.odeint(f,y0,T2)
    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"avec odeint $y({})={}$".format(x0,y0))
    plt.plot(T2,Z2,color=col,linestyle=LS)
    plt.plot(x0,y0,color=col,marker='o') # mise en evidence de la condition initial

# avec l'expression des solutions
ec=.1
LineStyle=['-', ':'] # style de ligne
cteK=[1,2]
couleurs=[(.5,.5,.75), (.32,.87,.82)] # couleur des courbes définies avec les valeurs (red,green, blue)
for k, col,LS in zip(cteK,couleurs,LineStyle):
    T1=np.linspace(ec,XX)
    Z1=sol(T1,k)
    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"avec $k={}$".format(k))


plt.title(r"$ ty'-y= \ln(t) $",fontsize=20)
plt.xlabel(r"$y(t) = k\cdot t-1-\ln(t)$")
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

