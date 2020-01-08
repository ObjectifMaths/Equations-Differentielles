import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
plt.rc('text', usetex=True) # pour la compilation de xlabel
plt.rc('text.latex', preamble=r'\newcommand{\abs}[1]{\left\vert #1 \right\vert}')



f=lambda y,x: ((5-4*x)-abs(y))/x
sol3=lambda x : (10-4*np.log(2*x))*x-5   # sur $\lbrack 0, \frac 12\lbrack$
sol4=lambda x : -(2*x-1)*(x-2)/x   # sur $\rbrack \frac 12 , 2 \lbrack$
sol5=lambda x : (5/2-4*np.log(x/2))*x-5   # sur $\lbrack2,+\infty \lbrack$



# trace les axes

xx,XX= -1,6
yy,YY=plt.ylim(-6,2) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')
 
x1,y1=1,1 # conditions initiales

# avec odeint
ec=.05 # pour éviter la singularité en $0$
T1=np.linspace(x1,XX)
T2=np.linspace(x1,ec)
Z1=spig.odeint(f,y1,T1)
Z2=spig.odeint(f,y1,T2)
plt.plot(T1,Z1, 'b-', label ="avec odeint")
plt.plot(T1,Z1, 'b-', T2,Z2, 'b-', T2[0],Z2[0], 'bo')

# avec expression des solutions
T3=np.linspace(ec,1/2, 10)
T4=np.linspace(1/2,2,15)
T5=np.linspace(2,5, 30)
plt.plot(T3, sol3(T3), 'ro', markersize=3, markevery=5)
plt.plot(T4, sol4(T4), 'ro', markersize=3 , markevery=5)
plt.plot(T5, sol5(T5), 'ro',markersize=3, markevery=5, label="avec l'expression des solutions")


plt.title(r"$  xy' + \abs y  = 5-4x\quad y(1)=1$",fontsize=20)
plt.grid()
plt.legend()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()

