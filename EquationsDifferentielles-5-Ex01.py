import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: 2/t*y-1

CI=[(1,1.2,'g'), (1.5,1,'r')]
xx, XX=-2,2

for (t0,y0,col) in CI:
    T=np.linspace(t0,XX) # à droite de t0
    Z=spig.odeint(f,y0,T)
    plt.plot(T,Z,col+'-')
    plt.plot(T[0],y0,col+'o', label="y({})={}".format(t0,y0))
    
    T=np.linspace(t0,xx) # à gauche de t0
    Z=spig.odeint(f,y0,T)
    plt.plot(T,Z,col+'-')
    


plt.title("$ ty'-2y=-t$",fontsize=20)


# trace les axes
yy,YY=plt.ylim(-1,2.5) # limite l'axe des ordonnées
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

plt.grid()
plt.legend()
plt.savefig("EquationsDifferentielles-5-Ex01.pdf")
#plt.show()


