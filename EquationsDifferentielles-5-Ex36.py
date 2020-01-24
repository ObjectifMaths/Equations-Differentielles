import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')
plt.rc('text.latex', preamble=r'\renewcommand{\sinh}{\mathrm{sh}}')


# équation différentielle sous la forme y'=f(y,x)
f= lambda y,t:  (t**3 *np.exp((t**2-1)/t)+y) /t**2  



# trace les axes
xx,XX= -6, 3
yy,YY=plt.ylim(-3,7) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')
 

ec=.1 # pour éviter la singularité en $0$
# avec odeint sur R+*
LineStylep=['-', '--'] # style de ligne
CIp=[(1,1),(1,-2)] # conditions initiales
colp=[(.8,.25,.15), (.2,.7,.2)] # couleur des courbes définies avec les valeurs (red,green, blue)
for (x0,y0), col,LS in zip(CIp,colp,LineStylep):
    T1=np.linspace(x0,XX)
    T2=np.linspace(x0,ec)
    Z1=spig.odeint(f,y0,T1)
    Z2=spig.odeint(f,y0,T2)
    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"avec odeint $y({})={}$".format(x0,y0))
    plt.plot(T2,Z2,color=col,linestyle=LS)
    plt.plot(x0,y0,color=col,marker='o') # mise en evidence de la condition initiale


# avec odeint sur R+*
LineStylem=['-', '--', ':'] # style de ligne
CIm=[(-1,-1),(-1,2)] # conditions initiales
colm=[(.7,.45,.65), (.7,.1,.8)] # couleur des courbes définies avec les valeurs (red,green, blue)
for (x0,y0), col,LS in zip(CIm,colm,LineStylem):
    T1=np.linspace(x0,xx)
    T2=np.linspace(x0,-ec)
    Z1=spig.odeint(f,y0,T1)
    Z2=spig.odeint(f,y0,T2)
    plt.plot(T1,Z1,color=col,linestyle=LS, label=r"avec odeint $y({})={}$".format(x0,y0))
    plt.plot(T2,Z2,color=col,linestyle=LS)
    plt.plot(x0,y0,color=col,marker='o') # mise en evidence de la condition initiale

   
plt.title(r"$ t^2y'- y=  t^3\cdot \exp\left(\frac{t^2-1}{t}\right)  $",fontsize=20)
plt.legend()
plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

