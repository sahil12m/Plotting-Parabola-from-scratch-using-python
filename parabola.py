import sympy as sym
import numpy as np
import math
import matplotlib.pyplot as plt

D = 4000.0    #Diameter of the parabola
d = 250.0     #Depth of the parabola
s = 50.0      # Cord length
f = (D**2) / (16*d) # focus of parabola

x = sym.Symbol('x')
y = sym.Symbol('y')

lst = []

p0 = [0.0,0.0]  #Starting point
p1 = p0

lst.append(p1)

while p1[0] <= d:
    x1 = p1[0]
    y1 = p1[1]
    
    x = (y**2) / (4*f)
    eqn = (x - x1)**2 + (y - y1)**2 - s**2
    eqn = sym.expand(eqn)
    eqn = sym.simplify(eqn)
    
    roots = sym.solve(eqn, y)
    
    for i in roots:
        if i.is_real == True:
            if i >= y1:
                y2 = i
                break

    x2 = (y2**2)/(4*f)
    
    p2 = [x2,y2]
    lst.append(p2)
    p1 = p2

def rotate2D(x, y, angled):
      angle = math.radians(angled)
      xd = x*math.cos(angle) - y*math.sin(angle)
      yd = x*math.sin(angle) + y*math.cos(angle)
      return xd, yd
    
def plot_graph(lst, angle):
   size = len(lst)
   x = np.zeros(size, dtype=float)
   y = np.zeros(size, dtype=float)
   for i in range(size):
       x[i],y[i] = rotate2D(lst[i][0],lst[i][1],angle)
       
   u = np.zeros(2, dtype=float)
   v = np.zeros(2, dtype=float)
   
   u[0] = lst[0][0]
   v[0] = lst[0][1]
   u[1], v[1] = rotate2D(lst[size-1][0],lst[0][1],angle)
   
   limit = 2200
   if limit != 0:
       plt.gca().set_ylim({-limit, limit})
       plt.gca().set_xlim({-limit, limit})

   # plot upper half of parabola
   plt.plot(x, y,color='Blue', linestyle='-',marker='o', markersize=3)
   
   # plot the axis of parabola
   plt.plot(u, v,color='Red', linestyle='-',marker='o', markersize=3)
     
   for i in range(size):
       x[i],y[i] = rotate2D(lst[i][0],-lst[i][1], angle)
   
   #plot lower half of parabola    
   plt.plot(x, y, color='Blue', linestyle='-',marker='o', markersize=3) 
   
   plt.title("Generated parabola: {} chords.".format(size*2))
   plt.xlabel("x axis")
   plt.ylabel("y axis")
   plt.grid(True)
   plt.show()
    
plot_graph(lst, 0.0)
    