# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig
from Euler import Euler

#f=lambda y,t: t+np.sin(y)**2
f=lambda y,t: 3*y+2*t-3*t**2

T=np.linspace(0,2,20)
y0=0

#par la méthode d'Euler
Y=Euler(f, y0, T)
plt.plot(T,Y,'r-', label=u"par Euler")

# par la fonction odeint
Z=spig.odeint(f,y0,T)
plt.plot(T,Z,'g-', label=u"par odeint")

# solutino exacte
phi=lambda t: t**2
plt.plot(T,phi(np.array(T)), 'bo', label="exacte")

# trace les axes
xx,XX=-.25,2.25
yy,YY=-.25,4
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.axes().set_aspect('equal')


plt.title("$ y'= 3y+2t-3t^2  \quad  y(0)  =  0 $")
plt.xlabel("Comparaison Euler et spig.odeint",fontsize=20)
plt.legend()
plt.show()


