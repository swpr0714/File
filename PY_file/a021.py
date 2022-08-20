from vpython import *
import random
#const
r=0.2
dt=1/120


scene = canvas(width=1600, height=1000, x=0, y=0, center=vec(0,0,0))

ball=[5]
x=0
for i in range(0,2,1):
    ball[i] = sphere(radius=0.2, pos=vec(x,0,0), color=vec(1,0,0))
    x+=1

