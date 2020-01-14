import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')
plt.rc('text.latex', preamble=r'\renewcommand{\sinh}{\mathrm{sh}}')


# équation différentielle sous la forme y'=f(y,x)
f= lambda y,t:  t**3+1-t**2*y  
sol= lambda t,k: k*np.exp(-t**3/3) +t


# trace les axes
xx,XX= -6, 3
yy,YY=plt.ylim(-3,7) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')



# avec odeint 
LineStyle=['-', '--', ':'] # style de ligne
CI=[(1,-1),(-3,0)] # conditions initiales
couleurs=[(.8,.25,.15), (.2,.7,.2)] # couleur des courbes définies avec les valeurs (red,green, blue)
for (x0,y0), col,LS in zip(CI,couleurs,LineStyle):
    T1=np.linspace(x0,XX)
    T2=np.linspace(x0,xx)
    Z1=spig.odeint(f,y0,T1)
    Z2=spig.odeint(f,y0,T2)
    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"avec odeint $y({})={}$".format(x0,y0))
    plt.plot(T2,Z2,color=col,linestyle=LS)
    plt.plot(x0,y0,color=col,marker='o') # mise en evidence de la condition initiale

# avec l'expression des solutions
LineStyle=['-', '--', ':'] # style de ligne
cteK=[-1,0,1] # conditions initiales
couleurs=[(.5,.7,.9),(.4,.45,.35),(.9,.5,.7)] # couleur des courbes définies avec les valeurs (red,green, blue)
T=np.linspace(xx,XX)
for k,LS,col in zip(cteK,LineStyle,couleurs):
    Z=sol(T,k)
    plt.plot(T,Z, color=col, linestyle=LS, label="$K={}$".format(k))
    
plt.title(r"$ y'+t^2y=  t^3 +1 $",fontsize=20)
plt.xlabel(r"$y(t)= K\cdot \exp\left(-\frac{t^3}{3}\right) + t $")
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

