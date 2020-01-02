from Euler import Euler
import matplotlib.pyplot as plt
import numpy as np

# équation y'=y+t avec y(0)=0
f=lambda y,t: y+t

# solution approchée avec la méthode d'Euler
T=np.linspace(0,2,10)
Y=Euler(f, 0, T)
plt.plot(T,Y,'r-', label=u"approchée")

# solution exacte
phi=lambda t: np.exp(t)-t-1
plt.plot(T,phi(np.array(T)), 'bo', label="exacte")

plt.title("$y'=y+t \qquad y(0)=0$")

# trace les axes
xx,XX=-.25,2.25
yy,YY=-1,4.5
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')
plt.xlabel(u"Avec la méthode d'Euler",fontsize=20)

# repère orthonormé
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

# affiche la légende
plt.legend()

#affiche le graphique
plt.show()



