from numpy import *
import matplotlib.pyplot as plt
r=3
t=linspace(0,2*pi)
plt.axis("equal")
x=r*cos(t);
y=r*sin(t);
plt.plot(x,y)
r=3
t=linspace(0,2*pi)
plt.axis("equal")
x=3+r*cos(t);
y=r*sin(t);
plt.plot(x,y)
plt.plot([0,3],[0,0])
#let the two points of intersection between the circles are A(a,b)and B(p,q)
#By symmetry a and p will be same
a=p=1.5
#for calculating b,q we will apply PGT in the respective rt angled traingles
b=math.sqrt(-a**2+r**2)
qm=math.sqrt(-a**2+r**2)
q=-qm
plt.plot([a,p],[b,q])
#the lines will be perpendicular as line joining the centers bisects the chord

plt.show()
