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
from scipy.constants import epsilon_0
# import matplotlib.pyplot as plt

""" Section 2:  Define functions for the script
#---------------------------------------------------------------------------"""

# Return the electric potential, V, due to a charge "q" located at position
# rq = (xq,yq).  Evaluate V at the given position (x,y)

def e_potential(q, rq, x, y):
    #k = 8.99e9  # Coulombs Constant - I could also use another
    e_o = epsilon_0
    Fr_pi = (4*np.pi)
    K = 1 / (Fr_pi * e_o)
    r = np.sqrt((rq[0] - x) ** 2 + (rq[1] - y) **2) #Distance between the position
    V = K * q / r #Note electrical potential has been written as U also
    return V #This return allows for the output to be calculated

#print(V) #I will need values to provide in order to determine the necessary values



def electric_field(q, rq, x,y):
    e_o = epsilon_0
    Fr_pi = (4*np.pi)
    K = 1 / (Fr_pi * e_o)

    #Calculation of the distance between charge and the observation point
    r = np.sqrt((x - rq[0]) ** 2 + (y - rq[1]) ** 2)

    #Calculation of the angle
    theta = np.arctan(y - rq[1], x -rq[0])

    #Electric field components using r-squared and theta
    Efield_comp_x = K * q / (r ** 2) * np.cos(theta) #np.cos represents x direction
    Efield_comp_y = K * q / (r ** 2) * np.sin(theta) #np.cos represents x direction

    return Efield_comp_x, Efield_comp_y

#Now that all the function are created
#We can verify using print command and testing

""" Section 3:  Main body of code
#---------------------------------------------------------------------------"""
# Create a 2D grid of x, y points using numpy meshgrid function

nx, ny = 100, 100
x = np.linspace(-5,5,nx)
y = np.linspace(-5,5,ny)
X,Y = np.meshgrid(x,y)





""" 
PART B
"""
