"""
Import Module
"""
from vpython import *
import matplotlib.pyplot as plt
"""
Var Setup
"""
L = 15                                  # Length of Water
m, r = 1, 1                             # Mess of stone, Radius of stone
theta=pi/180*(5)                     # Angle of V0
V=12                                    # Magnitude of V0
v0=vec(V*cos(theta),V*sin(theta),0)     # Vector of V0 
t, dt=0, 0.001                                # dt
rho, g = 1, -9.8                         
ya, yb = 1, 1                           # Variable to determine if a stone falls into the water
pos,x, zero, ground=[], [], [], []
"""
Scene Setup
"""
canva = canvas(width=2000,height=1200,z=0,y=0,center=vec(0,0,0),forward=vec(0,-1,-5))
water = box(size=vec(2*L,5,1),pos=vec(0,-2.5,0),color=color.blue)
land = box(size=vec(5,6,5),pos=vec(-L-2.5,-2,0),color=color.green)
stone = cylinder(radius=r,axis=vec(0,0.5,0),pos=vec(-L,1,0),color=vec(0.5,0.5,0.5),make_trail=True)
stone.rotate(angle=theta,axis=vec(0,0,1),origin=vec(stone.pos))
point = sphere(radius=0.2,pos=land.pos-vec(0,1,0),color=color.red)      # Points to mark where the stone contact the water
"""
Sub
"""
def get_B (rho,r,h):        # A sub function to calculate Buoyancy
    B = rho*r*r*pi*h
    return B
def plot_history(pos,zero,ground,plt_title,legends=None):
    plt.title(plt_title)
    plt.plot(x,zero, c='b')
    plt.plot(x,pos, c='#A4A4A4')
    plt.plot(x,ground, c='k')
    if legends :
        plt.legend(legends)
    plt.show()
"""
Main
"""
sleep(1)
while (stone.pos.y>-5):
    rate(1000)
    ya=stone.pos.y
    v0.y+=g*dt
    stone.pos+=v0*dt
    yb=stone.pos.y
    if (stone.pos.y<0):
        h = stone.pos.y
        if (stone.pos.y>0.5):
            h=0.5
        B = get_B(rho,r,-h) 
    if (stone.pos.y<0 and ya*yb<0 and v0.x>5):
        v0.x*=0.8
        v0.y*=-0.8
        a=point.clone(pos=stone.pos)
    elif (stone.pos.y<0 and ya*yb<0):
        a=point.clone(pos=stone.pos)
    t+=dt
    x.append(stone.pos.x+L)
    pos.append(stone.pos.y)
    zero.append(0)
    ground.append(-5)
stone.rotate(angle=-theta,axis=vec(0,0,1),origin=vec(stone.pos))

plot_history(pos,zero,ground,"position point")