from vpython import *
#Web VPython 3.2

# This code draws the bounding grid *************
sidelength=0.08
canvas(center=vector(sidelength/sqrt(2),0,0))
curve(pos=[vector(0,0,0),vector(sidelength/sqrt(2),sidelength/sqrt(2),0)], color=color.white)
curve(pos=[vector(sidelength/sqrt(2),sidelength/sqrt(2),0),vector(sqrt(2)*sidelength,0,0)], color=color.white)
curve(pos=[vector(0,0,0),vector(sidelength/sqrt(2),-sidelength/sqrt(2),0)], color=color.white)
curve(pos=[vector(sidelength/sqrt(2),-sidelength/sqrt(2),0),vector(sqrt(2)*sidelength,0,0)], color=color.white)

bigticklength = 0.004
smallticklength = 0.002
tickspacing = 0.002
blanklength = 0.01
# draw ticks along bottom diagonal
xstart = sidelength*sqrt(2)-(blanklength/sqrt(2))
ystart = 0-(blanklength/sqrt(2))
count = 0
while count <= 30:
    if count/5==round(count/5):
        curve(pos=[vector(xstart-count*tickspacing/sqrt(2),ystart-count*tickspacing/sqrt(2),0),vector(xstart-count*tickspacing/sqrt(2)+bigticklength/sqrt(2),ystart-count*tickspacing/sqrt(2)-bigticklength/sqrt(2),0)],color=color.white)
    else:
        curve(pos=[vector(xstart-count*tickspacing/sqrt(2),ystart-count*tickspacing/sqrt(2),0),vector(xstart-count*tickspacing/sqrt(2)+smallticklength/sqrt(2),ystart-count*tickspacing/sqrt(2)-smallticklength/sqrt(2),0)],color=color.white)
    count=count+1
    
# draw ticks along top diagonal
xstart = sidelength*sqrt(2)-(blanklength/sqrt(2))
ystart = 0+(blanklength/sqrt(2))
count = 0
while count <= 30:
    if count/5==round(count/5):
        curve(pos=[vector(xstart-count*tickspacing/sqrt(2),ystart+count*tickspacing/sqrt(2),0),vector(xstart-count*tickspacing/sqrt(2)+bigticklength/sqrt(2),ystart+count*tickspacing/sqrt(2)+bigticklength/sqrt(2),0)],color=color.white)
    else:
        curve(pos=[vector(xstart-count*tickspacing/sqrt(2),ystart+count*tickspacing/sqrt(2),0),vector(xstart-count*tickspacing/sqrt(2)+smallticklength/sqrt(2),ystart+count*tickspacing/sqrt(2)+smallticklength/sqrt(2),0)],color=color.white)
    count=count+1
    
# draw deflecting plates
dzlength = 0.012
platelength = 0.09
spacing = 0.008
curve(pos=[vector(dzlength,spacing/2,0),vector(dzlength+platelength,spacing/2,0)],color=color.white)
curve(pos=[vector(dzlength,-spacing/2,0),vector(dzlength+platelength,-spacing/2,0)],color=color.white)



# OBJECTS AND INITIAL CONDITIONS ##*******************************************
particle = sphere(pos=vector(0, 0, 0), radius=0.002, color=color.cyan, make_trail=True)

#------------My Alterations from here onwards------------

#Above 1: Attempted conversion for initial velocity from initial voltage - for use in initial velocity vector
#vi = sqrt(2((1.602e-19)(5000))/(9.11e-19)) = 4193455.8

#Above 2: Attempted calculation of electric field between plates - for use in determining downwards velocity vector
#E = (350)/(8e-3) = 43750

#Electron properties
particle.mass = 9.11e-31
particle.charge = 1.602e-19

#Apparatus Properties
Vstarter = 2000
Vdeflection = 200
separation = 8e-3
distance = 0.01

#Initial velocity from initial leftwards voltage
#Velocity as placeholder until Above 1 can be entered
particle.vel = vector((sqrt(2*((particle.charge)*(Vstarter))/(particle.mass))),0,0)
particle.acceleration = vector(0,-(((particle.charge)*(Vdeflection))/(particle.mass*separation)),0)

dt = 1e-10
t = 0

while (particle.pos.x < distance):
    rate(17)
    particle.pos = particle.pos + particle.vel*dt

while (-separation/2 < particle.pos.y < separation/2):
    rate(17)
    particle.pos = particle.pos + particle.vel*dt
    particle.vel = particle.vel+particle.acceleration*dt
    
while (particle.pos.x < 0.12):
    rate(17)
    particle.pos = particle.pos + particle.vel*dt

