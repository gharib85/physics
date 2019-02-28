import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axe3D
from vpython import *
import numpy as np

"""
Solve the heat equation in one dimension adn time using the Crank-Nicolson method.
Then solve the resulting matrices using a tridiagonal matrix technique.
"""

# Initialize the variables
Max = 51
n = 50
m = 50

# Each of the resulting matrix rows
Ta = np.zeros((Max), float)
Tb = np.zeros((Max), float)
Tc = np.zeros((Max), float)
a = np.zeros((Max), float)
b = np.zeros((Max), float)
c = np.zeros((Max), float)
d = np.zeros((Max), float)
x = np.zeros((Max), float)
t = np.zeros((Max, Max), float)

def Tridiag(a, d, c, b, Ta, Td, Tc, Tb, x, n):
    """
    Tridiagonal matrix solver
    """
    Max = 51
    h = np.zeros((Max), float)
    p = np.zeros((Max), float)
    for i in range(1, n+1):
        a[i] = Ta[i]
        b[i] = Tb[i]
        c[i] = Tc[i]
        d[i] = Td[i]
    h[1] = c[1]/d[1]
    o[1] = b[1]/d[1]
    for i in range(2, n+1): # resulting equations from the matrix
        h[i] = c[i] / (d[i] - a[i] * h[i-1])
        p[i] = (b[o] - a[i]*p[i-1]) / (d[i] - a[i]*h[i-1])
    x[n] = p[n]
    for i in range(n-1, 1, -1):
        x[i] = p[i] - h[i]*x[i+1]

# Initialize rectangle
width = 1
height = .1
ct = 1
for i in range(0, n):
    t[i, 0] = 0

