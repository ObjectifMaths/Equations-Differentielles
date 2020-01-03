import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: (np.sin(t)*y-np.sin(2*t))/np.cos(t)


pen=['g','r', ]
init=[1.5,-.5,]


for y0, col in zip(init,pen):
    # sur $\lbrack 0 , \frac \pi2\lbrack$
    ec=.1
    T=np.linspace(0,np.pi/2-ec)
    Z=spig.odeint(f,y0,T)
    plt.plot(T,Z,col+'-')
    plt.plot(T[0],y0,col+'o')
    # sur $\rbrack \frac \pi2,0\lbrack  $
    T=np.linspace(0,-np.pi/2+ec)
    Z=spig.odeint(f,y0,T)
    plt.plot(T,Z,col+'-')

# tracé de la sol déf sur R
T=np.linspace(-np.pi, np.pi)
plt.plot(T,np.cos(T),'b-')
    

plt.title(r"$\cos(t) y'-\sin(t) y=-\sin 2t$",fontsize=20)
plt.ylim(-2,5) # limite l'axe des ordonnées


# trace les axes
xx,XX= -3,2
yy,YY=plt.ylim()

# tracé des asymptotes
plt.plot([-np.pi/2]*2,plt.ylim(), 'k-')
plt.plot([+np.pi/2]*2,plt.ylim(), 'k-')

plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

plt.grid()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()


