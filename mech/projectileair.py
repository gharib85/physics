from vpython.graph import *

"""
Solve for projectile motion with air resistance and
find the frictionless case analytically.
"""

v0 = 22
angle = 34
g = 9.8
kf = 0.9
N = 25
v0x = v0*cos(angle*pi/180)
v0y = v0*sin(angle*pi/180)
T = 2*v0y/g
H = v0y*voy/(2*g)
R = 2*v0x*v0y/g


graph1 = gdisplay(title="Projectile width (red)/without (yellow) Air Resistance",
                xtitle ="x", ytitle="y", xmax=R, xmin=-R/20, ymax=8, ymin=-6.0)

funct
