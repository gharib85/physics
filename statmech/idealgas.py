from pylab import *
import matplotlib.plot as plt
import numpy as np
from numpy import zeros

"""
We can also use the molecular dynamics simulations to learn about the ideal gas. We can, for example,
determine how the pressure in the gas depends on other properties of the system?

The pressure is a property we can measure in the gas and which may vary or at least fluctuate with time — just as we have
seen the number of particles in the left half to vary. The volume and the total energy on the other hand, are values we
determine when we start the simulations, and we typically do not allow them to vary throughout the simulation: Total energy
is conserved when the particles move in conservative force fields, and we keep the size of the box, and hence the volume, constant.

If the gas is very dilute, all the particles are far away from each other most of the time, and the interaction energies from the interatomic
potentials will be very small (since it decays rapidly with the distance between atoms). We may therefore approximate the
total energy by the kinetic energy of the atoms instead. We will come back later to how to
measure the pressure in a molecular dynamics simulation, but let us here assume that it is measured from the average force on the walls of the system.
We introduce reflective walls in both the x and the y direction to contain the system.
We can set up a two-dimensional simulation of a dilute gas, just as we did before, and measure the volume V = Lx · Ly , the pressure P , as measured by the
 simulation program, and the total kinetic energy.
 
 K=summation from i=1 to N of (1/2)m(v_x^2 +v_y^2).

"""

data = dump("gasstat01.lammpstrj") # Read output states t = data.time()
nt = size(t)
nleft = zeros(nt,float) # Store number of particles
# Get information about simulation box tmp_time,box,atoms,bonds,tris,lines = data.viz(0)
# halfsize = 0.5*box[3]
# Box size in x-dir
for it in range(nt):
   xit = np.array(data.vecs(it,"x"))
   jj = find(xit<halfsize)
   numx = size(jj)
   nleft[it] = numx
plt(t,nleft, xlabel="t" ylabel="n")
plt.show()
np.savetxt("ndata.d",(t, nleft))
