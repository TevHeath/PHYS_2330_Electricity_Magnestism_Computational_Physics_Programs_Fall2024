# Computational Exercise 1 for PHYS*2330 - Fall 2024
# dipolePlot.py - scaffold code
# MVM
#------------------------------------------------------------------------------


""" Section 1:  Start by importing relevant libraries
#---------------------------------------------------------------------------"""
import numpy as np
import matplotlib.pyplot as plt

""" Section 2:  Define functions for the script
#---------------------------------------------------------------------------"""
# Return the electric potential, V, due to a charge "q" located at position 
# rq = (xq,yq).  Evaluate V at the given position (x,y)
def potential(q, rq, x, y):

    return 


""" Section 3:  Main body of code
#---------------------------------------------------------------------------"""
# Create a 2D grid of x, y points using numpy's meshgrid function
nx, ny = 100,100
x = np.linspace(-5, 5, nx)
y = np.linspace(-5, 5, ny)
X, Y = np.meshgrid(x, y)

# Define the charges (charge & position) that make up the electric dipole



# For each gridpoint in X, Y, we will need to calculate the electric potential
# using our function potential().  The total potential is the sum of contributions
# from each charge.


# Read in the files "vFieldX.csv" and "vFieldY.csv", which contains a 2D array 
# representing a 2D vector field
#vX = np.loadtxt('vFieldX.csv',delimiter=',')
#vY = np.loadtxt('vFieldY.csv',delimiter=',')


""" Section 4:  Plot your results as a contour plot
#---------------------------------------------------------------------------"""
# The following line creates 'handles' fig and ax, which allow us to direct 
# formatting commands to the figure and the axes within the figure, respectively.
# [This is useful when creating multiple plots, but also works for a single plot]
fig = plt.figure( figsize = (20,10) )
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set_title("X meshgrid", fontsize=20)
ax2.set_title("Y meshgrid", fontsize=20)

im1 = ax1.imshow(X, cmap='inferno')
im2 = ax2.imshow(Y, cmap='inferno')
plt.colorbar(im2)

# Contour plots set equipotential lines that are equally spaced in values of V
# We can specify the values of the contour lines

#VpLines = 10**np.linspace(8,12,5)
#VpLines = sorted(list(-VpLines) + list(VpLines))

#ax1.contour(X, Y, V, colors='k', linewidths=1)


# Save your plot
plt.savefig('fieldPlot.png', dpi=300)
