from pylab import *

import matplotlib.plot as plt
import numpy as np

"""
Simple method of adjusting distances to achieve equilibrium.
"""

for i in range(1,nstep):
r = rand(1)
if (r<n[i-1]/N):
    n[i] = n[i-1] - 1 # Move atom from left to right else:
    n[i] = n[i-1] + 1 # Move atom from right to left
    plt(range(0,nstep),n/N, xlabel="t", ylabel="n/N")
    plt.show()
