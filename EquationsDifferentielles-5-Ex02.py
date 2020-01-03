import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

f=lambda y,t: y/t+t


pen=['g', 'r', 'b']
init=[.8, 1.2, 1.6]

for y0, col in zip(init,pen):

    # à droite de t0
    T=np.linspace(1,2)
    Z=spig.odeint(f,y0,T)
    plt.plot(T,Z,col+'-')
    plt.plot(T[0],y0,col+'o')
    xx,XX=min(T), max(T)

    # à gauche de t0
    T=np.linspace(1,-2)
    Z=spig.odeint(f,y0,T)
    plt.plot(T,Z,col+'-')


plt.title("$ ty'-y=t^2 \quad y({})={} $".format(T[0],y0),fontsize=20)
plt.ylim(-1,2.5) # limite l'axe des ordonnées

# trace les axes
xx,XX= min(min(T),xx), max(max(T),XX)
yy,YY=plt.ylim()
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')

plt.grid()
plt.savefig("EquationsDifferentielles-5-Ex02.pdf")
#plt.show()


