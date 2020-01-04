import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: 2*y+t+np.sin(t)
sol=lambda t,K:K*np.exp(2*t)  -t/2-1/4-2/5*np.sin(t)-1/5*np.cos(t)

pen=['g','r', 'c' ]
cteK=[.1,-.1,-.5]


# trace les axes

xx,XX= -6,4
plt.ylim(-4,4) # limite l'axe des ordonnées
yy,YY=plt.ylim()

plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')


ec=.02

# avec expression des solutions
T=np.linspace(xx,XX)
for K, col in zip(cteK,pen):
    plt.plot(T,sol(T,K),col+'-', label="K={}".format(K))

# avec odeint
y0=0
T1=np.linspace(0,XX) # sur $\RR_+$
Z1=spig.odeint(f,y0,T1)
T2=np.linspace(0,xx) # sur $\RR_-$
Z2=spig.odeint(f,y0,T2)
plt.plot(T1,Z1,'y-', label="avec odeint")
plt.plot( T2,Z2,'y-', T1[0],[y0],'yo')



    

plt.title(r"$y' -2y =t+\sin(t)$",fontsize=20)
plt.xlabel(r"$t\mapsto K\exp(2t)  -\frac {t}{2} -\frac {1}{4} -\frac {2}{5} \sin t - \frac {1}{5}\cos t$")


plt.grid()
plt.legend()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()


