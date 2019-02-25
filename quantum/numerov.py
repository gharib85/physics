from vpython import *

"""
Use the Numerov method to solve the 1-D time-independent Schrodinger equation
for bound-state energies.
"""

psigr = display(x=0, y=0, width=600, height=300, title="R and L Wave Functions")
psi = curve(x=list(range(0, 1000)), display=psigr, color=color.yellow)
psi2gr = display(x=0, y=300, width=600, height=300, title="Wave func^2")
psio = curve(x=list(range(0, 1000)), color=color.magenta, display=psi2gr)
energr = display(x=0, y=500, width=600, height=200, title="Potential and E")
poten = curve(x=list(range(0, 1000)), color=color.cyan, display=energr)
autoen = curve(x=list(range0, 1000)), display=energr)

dl = 1e-6 # interval to stop bisection
ul = zeros([1501], float) # u value for left side
ur = zeros([1501], float) # and the right side
k2l = zeros([1501], float) # k**2 Schrodinger equation left wavefunction
k2r = zeros([1501], float) # k**2 S. E. right wavefunction
n = 1501
m = 5 # plot every 5 points
imax = 100 # number of iterations
xl0 = -1000
xr0 = 1000
h = (1*(xr0-xl0)/(n-1)) # h constant
amin = -.001
amax = -.00085
e = amin
de = .01
ul[0] = 0
ul[1] = .00001
ur[0] = 0
ur[1] = .00001
im = 500
nl = im + 2 # match point left and right wavefunction
nr = n - im + 1
istep = 0

def V(x): # Finite square well from particle-in-a-box
    if abs(x) <= 500:
        v = -.001
    else:
        v = 0
    return v

def setk2():
    for i in range(0, n):
        xl = xl0 + i*h
        xr = xr0 - i*h
        k2l[i] = e-V(xl)
        k2r[i] = e-V(xr)

def numerov(n, h, k2, u): # Numerov algorithm for left and right wavefunctions
    b = (h**2)/12.0
    for i in range(1, n-1): # shown from integration of both sides
        u[i+1] = (2*u[i]*(1-5*b*k2[i])-(1+b*k2[i-1])*u[i-1])/(1+b*k2[i+1])

setk2()
numerov(nl, h, k2l, ul)
numerov(nr, h, k2r, ur)
fact = ur[nr-2]/ul[im]
for i in range(0, nl):
    ul[i] = fact*ul[i]
f0 = (ur[nr-1]+ul[nl-1]-ur[nr-3]-ul[nl-3])/(s*h*ur[nr-2]) # log derivative

