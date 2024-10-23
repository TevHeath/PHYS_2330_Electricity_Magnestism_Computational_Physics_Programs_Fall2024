# Computational Exercise 3 for PHYS*2330 - Fall 2023
# chargeIntegration.py - scaffold code
# MVM
# ------------------------------------------------------------------------------


""" Section 1:  Start by importing relevant libraries
#---------------------------------------------------------------------------"""
import numpy as np

""" Section 2:  Define functions for the script
#---------------------------------------------------------------------------"""


# This produces arrays of (x,y) positions for a line
# segment, from position ri to rf, divided into N equally spaced intervals
def lineSegment(ri, rf, N):
    # ri: Initial point of the line segment (as a tuple/list of x and y coordinates).
    # rf: Final point of the line segment (as a tuple/list of x and y coordinates).
    # N: Number of points to divide the line segment into.

    x = np.linspace(ri[0], rf[0], N)
    # Creates an array of N equally spaced points along the x-axis between the initial x-coordinate (ri[0]) and the final x-coordinate (rf[0]).

    y = np.linspace(ri[1], rf[1], N)
    # Creates an array of N equally spaced points along the y-axis between the initial y-coordinate (ri[1]) and the final y-coordinate (rf[1]).

    dL = np.sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)
    # Calculates the distance between two consecutive points along the line segment using the Euclidean distance formula.
    # This represents the length of each segment between points.

    return x, y, dL
    # Returns the arrays of x and y coordinates, and the length of each small segment along the line.


# Return the electric field, E, due to a charge "q" located at position (xq,yq).
# Evaluate V at the given position (x,y).
# This can be taken and modified from exercise 1.
def eField(q, xq, yq, x, y):
    # q: Charge of the point source.
    # xq, yq: Coordinates of the charge (location of the source charge).
    # x, y: Coordinates of the observation point (where we want to calculate the electric field).

    k = 9.0e9
    # k is the Coulomb constant, approximately 9.0 × 10^9 N·m²/C² (in SI units).

    denom = ((x - xq) ** 2 + (y - yq) ** 2) ** 1.5
    # denom represents the denominator of the electric field formula.
    # It calculates the distance between the source charge and the observation point raised to the power of 3/2.
    # (x - xq)² + (y - yq)² is the squared distance between the two points.

    dEx = k * q * (x - xq) / denom
    # dEx is the x-component of the electric field at point (x, y).
    # It is calculated using Coulomb's law, where the field decreases with the square of the distance and depends on the difference in x-coordinates.

    dEy = k * q * (y - yq) / denom
    # dEy is the y-component of the electric field at point (x, y).
    # It is calculated similarly, but for the y-component, using the difference in y-coordinates.

    return dEx, dEy
    # Returns the electric field components in the x-direction (dEx) and y-direction (dEy).


# Create a function that will integrate, using Trapezoid Rule
# Inputs should be A function f, and a segment length dL (associated with dQ)
def trapz(f, dL):
    area = 0.0

    for i in range(f.size - 1):  # 1
        # area += dL * (f[i]+ f[i+1])/2 #2
        area = dL * np.sum(f[1:] + f[:-1]) / 2  # 3

        """ 
        #1 - We need to take one less for the trapzoid hence range(f.size - 1), this makes the area for each trapzoid, this might need to be considered for simpson's rule
        #2 - We added the += because we want to add the area as we go hence the area+= dl...
        #3 - Here we are using slicing, 1: means start from index 1 to the end, and :-1 mean everything except the last one
        #4 - The output we want to know is the y value not necessarily the x value since it will be about 0 anyways only be interested in the y value
        """

    return area  # 4


""" Section 3:  Main body of code
#---------------------------------------------------------------------------"""
# Define characteristics of the uniformly charged line segment
Ri = np.array([-5, 0])  # 10 meters long so -5m
Rf = np.array([5, 0])  # 10 meters long so 5m
Nsegments = 100
Qtot = 3.0
Length = np.sqrt(np.sum((Rf - Ri) ** 2))
# dL =


# linear charge density (charge per unit length)
lamb = Qtot / Length

# position at which electric field is calculated
# Ro = np.array([0,5]) #Changed only use y-values
Ro = np.array([10, 0])  # Changed only use x-values

# compute dEx, dEy at position Ro due to each segment along the
# charged line segment.
# NOTE:  the *Ro - assigns Ro values to appropriate variables, in order of how
#        they are defined in function


X, Y, dL = lineSegment(Ri, Rf, Nsegments + 1)  # We need to add the +1 to ensure that we use 101 instead of 100

"""
Consider making it from polar ot cartesian to same time
"""

# Notice that we input 'lamb' instead of dQ here?
dEx, dEy = eField(lamb, X, Y, *Ro)

# Apply trapz function to integrate all contributions dEx, dEy to computer the
# total electric field at position Ro
Ex = trapz(dEx, dL)
Ey = trapz(dEy, dL)

print(Ex, Ey)
