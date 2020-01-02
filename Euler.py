def Euler(f,y0,T):
   """résolution de y'=f(y,t)
      y0 valeur initiale à l'instant T[0]      
      T tableau des abscisses à évaluer"""       
   Y=[y0]
   for i in range(0,len(T)-1):
       t,h=T[i],T[i+1]-T[i]
       y0=y0+f(y0,t) * h
       Y.append(y0)
   return Y



    
