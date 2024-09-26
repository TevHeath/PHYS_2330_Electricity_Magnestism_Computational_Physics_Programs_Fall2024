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
from IPython.core.pylabtools import figsize

""" Section 1:  Start by importing relevant libraries
#---------------------------------------------------------------------------"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0

""" Section 2:  Define functions for the script
#---------------------------------------------------------------------------"""

# Return the electric potential, V, due to a charge "q" located at position
# rq = (xq,yq).  Evaluate V at the given position (x,y)

def electric_potential(q, rq, x, y):
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

#Charges

q1 = -3
q2 = -1
q3 = +2         #the plus + is not needed, but useful for clarity
q4 = +6

#Positions (after the comment)
'''
Note the following:
1. Position of the charges on the vertices of a square of side length d = 3m
2. Center the square position is at x = -1 and y =0.5
*This is import to keep in mind especially as it relates understanding Part B
*I will need to complete my hand calculation to determine these locations
'''

#Charge Position #1: -3
x1 = 1/(np.sqrt(2))
y1 = 3/(np.sqrt(2))

#Charge Position #1: -1
x2 = -1/(np.sqrt(2))
y2 = 3/(np.sqrt(2))

#Charge Position #1: +2
x3 =-1
y3 = 3.5

#Charge Position #1: +6
x4 = 1/(np.sqrt(2))
y4 = 0.5 + 3

Vfunzies = electric_potential(q1, [x1,y1], X,Y)
Vfunzies += electric_potential(q2, [x2,y2], X,Y)
Vfunzies += electric_potential(q3, [x3,y3], X,Y)
Vfunzies += electric_potential(q4, [x4,y4], X,Y)

#Note I haven't added the electrical field component yet.
#This is because I would like to review the position currently

""" Section 4:  Plot your results as a contour plot (re-created from Tutorial, Dr. Massa)
#---------------------------------------------------------------------------"""
fig = plt.figure(figsize(20,10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set_title("X meshgrid", fontsize = 20) #Adds title to the X axis
ax2.set_title("Y meshgrid", fontsize = 20) #Adds title to the Y axis

im1 = ax1.imshow(Vfunzies, cmap = 'coolwarm', extent = (-6, 6, 6, 6), origin = "lower")
im2 = ax2.imshow(Y, cmap='coolwarm')
plt.colorbar(im2)

# Contour plots set equipotential lines that are equally spaced in values of V
# We can specify the values of the contour lines

VpLines = 10 ** np.linspace(6,12,5)
VpLines = sorted(list(-VpLines) + list(VpLines))

ax1.contour(X,Y,Vfunzies, color='r', linewidths=1, levels=VpLines)
#Notice that the Vplines within the contours is connected to the line 129
#To make adjustments change within 129

# Save you plot
plt.savefig('fieldPlot2.png', dpi=300)


""" 
PART B
"""
