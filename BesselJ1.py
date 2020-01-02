import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spig

def f(Y,x,a):
   return (Y[1],(a**2/x**2-1)*Y[0]-1/x*Y[1])

x0=0.1
Y0=(.0499375260,.497504163)
x1=4
X=np.linspace(x0,x1,20)
Y=spig.odeint(f,Y0,X,(1.0,))
plt.plot(X,Y[:,0],'r-')
plt.title("Une fonction de Bessel")

# trace les axes
xx,XX=-.25,4.5
yy,YY=-1,1
plt.plot([0,0],[yy,YY],'k-', [xx,XX],[0,0],'k-')


# repère orthonormé
plt.axes().set_aspect('equal')


plt.grid()
plt.show()
