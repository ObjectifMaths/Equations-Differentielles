import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel

# équation différentielle sous la forme y'=f(y,x)
f= lambda y,x: 1/x+2*np.log(x)-2*y
sol = lambda x,k: k*np.exp(-2*x)+np.log(x)

# trace les axes
xx,XX= -1, 5
yy,YY=plt.ylim(-3,7) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')


ec=.01 # pour éviter la singularité en $0$
# avec odeint sur R+*
LineStyle=[':', ':', ':'] # style de ligne
CI=[(1,1),(2,-2)] # conditions initiales
col=[(.8,.25,.15), (.2,.7,.2)] # couleur des courbes définies avec les valeurs (red,green, blue)
for (x0,y0), col,LS in zip(CI,col,LineStyle):
    T1=np.linspace(x0,XX)
    T2=np.linspace(x0,ec)
    Z1=spig.odeint(f,y0,T1)
    Z2=spig.odeint(f,y0,T2)
    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"avec odeint $y({})={}$".format(x0,y0))
    plt.plot(T2,Z2,color=col,linestyle=LS)
    plt.plot(x0,y0,color=col,marker='o') # mise en evidence de la condition initiale

# avec l'expression des solutions
T=np.linspace(XX,ec)
LineStyle=['-', '-', '-'] # style de ligne
cteK=[-1,0,5]
Col=[(.2,.5,.7),(.4,.2,.8),(.6,.4,.2)]
for k,col, LS in zip(cteK,Col,LineStyle):
    Z=sol(T,k)
    plt.plot(T,Z,color=col, linestyle=LS, label=r"$K={}$".format(k))

    
plt.title(r"$ y'+2y=\frac 1x+2\ln x  $",fontsize=20)
plt.xlabel(r"$y(x)= K\cdot \exp(-2x) + \ln x  $")
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

