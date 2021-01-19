from numpy import *
import matplotlib.pyplot as plt
import math
r=4
t=linspace(0,2*pi)
plt.axis("equal")
x=r*cos(t);
y=r*sin(t);
plt.plot(x,y)
r=6
t=linspace(0,2*pi)
plt.axis("equal")
x=r*cos(t);
y=r*sin(t);
#let the tangent is drawn from point A(a,b) which is located on circle of radius 6 and lie on Yaxis and touches smaller circle at point B(c,d)
a=0
b=6
plt.plot([0,0],[0,6])
#taking right angled traingle AOB let the angle between OA and OB is M
M=math.acos(4/6)
#let the angle between X axis and OB is W
W=pi/2-M
#using W in right angled traingle
c=4*cos(W)
d=4*sin(W)
plt.plot([0,c],[0,d])
plt.plot([c,a],[d,b])
plt.plot(x,y)
plt.show()

