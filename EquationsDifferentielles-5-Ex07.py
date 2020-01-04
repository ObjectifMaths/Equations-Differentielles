import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: (t-1-t*y)/t/(t-1)
sol=lambda t,K:(t-np.log(abs(t))+K)/(t-1) 

pen=['g','r', 'c','b' ]
cteK=[1,2,-2,-1]

ec=.02
for K, col in zip(cteK,pen):
    # sur $\lbrack {-\infty} , 0\rbrack$
    T=np.linspace(-3,0-ec)
    plt.plot(T,sol(T,K),col+'-', label="K={}".format(K))
    # sur $\rbrack \frac 0,1\lbrack  $
    T=np.linspace(0+ec,1-ec)
    plt.plot(T,sol(T,K),col+'-')
    # sur $\rbrack \frac 1,{+\infty}\lbrack  $
    T=np.linspace(1+ec,4)
    plt.plot(T,sol(T,K),col+'-')



# # tracé de la sol déf sur $\rbrack 0,+\infty\lbrack$

# T=np.linspace(ec, 4)
# plt.plot(T, sol(T,-1),'b-',label="K=-1")
    

plt.title(r"$t(t-1)y' + ty =t-1$",fontsize=20)
plt.ylim(-4,4) # limite l'axe des ordonnées
plt.xlabel(r"$t\mapsto \frac{t-\ln\vert t\vert+K}{t-1}$")

# trace les axes
xx,XX= -3,4
yy,YY=plt.ylim()

# tracé des asymptotes
plt.plot([0]*2,plt.ylim(), 'k-')
plt.plot([1]*2,plt.ylim(), 'k-')

plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

plt.grid()
plt.legend()

FichierCourant=os.path.basename(__file__)
plt.savefig(FichierCourant[:-2]+"pdf")
#plt.show()


