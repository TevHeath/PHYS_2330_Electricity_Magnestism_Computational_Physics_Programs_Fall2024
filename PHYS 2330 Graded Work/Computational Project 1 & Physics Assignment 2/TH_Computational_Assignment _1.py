# -*- coding: utf-8 -*-

# Computational Exercise 1 for PHYS*2330 - Fall 2024
# ------------------------------------------------------------------------------
## For this assignment, I need two utilize two functions, one given and the other created
# First, a potential function that was created during tutorial
# Second, design electric field function utilizing the Electric Field equation from Class
# Third I will need to plot both of these function on a plot by highlight key components
    #These components are the following, position, charge, density, potential contour, and directional field
#Fourth/Finally, Save your plot(s) as a single image file, “fieldPlot.png”. And name it accordingly.
#Part B requires that I attempt to locate the area that the charges are placed and their charge


"""
PART A
"""

""" Section 1:  Start by importing relevant libraries
#---------------------------------------------------------------------------"""
import numpy as np
# import matplotlib.pyplot as plt

""" Section 2:  Define functions for the script
#---------------------------------------------------------------------------"""

# Return the electric potential, V, due to a charge "q" located at position
# rq = (xq,yq).  Evaluate V at the given position (x,y)

def e_potential(q, rq, x, y):
    k = 8.99e9 #Colombs Constant
    r = np.sqrt((rq[0] - x) ** 2 + (rq[1] - y) **2) #Distance between the position
    V = k * q / r #Note electrical potential has been written as U also
    return V #This return allows for the output to be calculated

#print(V) #I will need values to provide in order to determine the necessary values



""" 
PART B
"""
