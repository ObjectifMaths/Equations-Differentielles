from Euler import Euler
import matplotlib.pyplot as plt
import numpy as np

# équation y'=2ty-2t**2+1 avec y(0)=0
f=lambda y,t: 2*t*y-2*t**2+1

# solution approchée
T=np.linspace(0,2,10)
Y=Euler(f, 0, T)
plt.plot(T,Y,'r-', label=u"approchée")

# solution exacte
phi=lambda t: t
plt.plot(T,phi(np.array(T)), 'bo', label="exacte")

plt.title("$y'=3y+2t-3t^2 \qquad y(0)=0$")

# trace les axes
xx,XX=-.25,2.25
yy,YY=-1,2
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.xlabel(u"Avec la méthode d'Euler",fontsize=20)
plt.axes().set_aspect('equal')

# trace le champ de vecteurs
dx,dy=.3,.3
L=.05
x,y=xx+dx,yy
while y<YY:
    u=L/np.sqrt(1+f(y,x)**2)
    v=u*f(y,x)
    plt.plot([x-u,x+u],[y-v,y+v], 'k-')
    x+=dx
    if x>=XX:
        x=xx
        y+=dy
plt.legend()
plt.show()



