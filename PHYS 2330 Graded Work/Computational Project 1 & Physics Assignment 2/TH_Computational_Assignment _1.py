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
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0

""" Section 2:  Define functions for the script
#---------------------------------------------------------------------------"""

def electric_potential(q, rq, X, Y):
    """
     Calculate electric potential at each point in a 2D grid.

     Parameters:
     - q: Charge magnitude
     - rq: Charge position [x, y]
     - X, Y: Grid coordinates (2D arrays)

     Returns:
     - V: Electric potential at each grid point (2D array)
     """
    Fr_pi = (4 * np.pi)
    K = 1 / (Fr_pi * epsilon_0)
    r = np.sqrt((rq[0] - X) ** 2 + (rq[1] - Y) ** 2)  # Distance between the position
    V = K * q / r
    return V

def electric_field(q, rq, X, Y):
    """
     Calculate electric field components (Ex, Ey) at each point in a 2D grid.

     Parameters:
     - q: Charge magnitude
     - rq: Charge position [x, y]
     - X, Y: Grid coordinates (2D arrays)

     Returns:
     - Efield_comp_x: X-component of electric field (2D array)
     - Efield_comp_y: Y-component of electric field (2D array)
     """
    Fr_pi = (4 * np.pi)
    K = 1 / (Fr_pi * epsilon_0)

    # Distance between charge and observation points
    r = np.sqrt((X - rq[0]) ** 2 + (Y - rq[1]) ** 2)

    # Angle calculation
    theta = np.arctan2((Y - rq[1]), (X - rq[0]))

    # Electric field components using r-squared and theta
    Efield_comp_x = K * q / (r ** 2) * np.cos(theta)  # x direction
    Efield_comp_y = K * q / (r ** 2) * np.sin(theta)  # y direction

    return Efield_comp_x, Efield_comp_y

""" Section 3:  Main body of code 
#---------------------------------------------------------------------------"""
# Create a 2D grid of x, y points using numpy meshgrid function

nx, ny = 100, 100
x = np.linspace(-5, 5, nx)
y = np.linspace(-5, 5, ny)
X, Y = np.meshgrid(x, y)

# Charges
q1 = -3
q2 = -1
q3 = +2
q4 = +6

# Positions (assisted using Hand-Calculations)
x1, y1 = 1 / np.sqrt(2), 3 / np.sqrt(2)
x2, y2 = -1 / np.sqrt(2), 3 / np.sqrt(2)
x3, y3 = -1, 3.5
x4, y4 = 1 / np.sqrt(2), 0.5 - 3 / np.sqrt(2)

# Electric Potential Calculation
V_potential = electric_potential(q1, [x1, y1], X, Y)
V_potential += electric_potential(q2, [x2, y2], X, Y)
V_potential += electric_potential(q3, [x3, y3], X, Y)
V_potential += electric_potential(q4, [x4, y4], X, Y)

# Electric Field Calculation (using 2D grid X and Y)
EField_x1, EField_y1 = electric_field(q1, [x1, y1], X, Y)
EField_x2, EField_y2 = electric_field(q2, [x2, y2], X, Y)
EField_x3, EField_y3 = electric_field(q3, [x3, y3], X, Y)
EField_x4, EField_y4 = electric_field(q4, [x4, y4], X, Y)

# Sum the electric field components
Ex = EField_x1 + EField_x2 + EField_x3 + EField_x4
Ey = EField_y1 + EField_y2 + EField_y3 + EField_y4

""" Section 4:  Plot your results as a contour plot
#---------------------------------------------------------------------------"""
fig = plt.figure(figsize=(21, 7))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set_title("Electric Potential", fontsize=20)
ax2.set_title("Electric Field (Y meshgrid)", fontsize=20)

# Electric potential plot
im1 = ax1.imshow(V_potential, cmap='coolwarm', extent=(-6, 6, -5, 5), origin="lower")
plt.colorbar(im1, ax=ax1)

# Y meshgrid plot
im2 = ax2.imshow(Y, cmap='coolwarm')
plt.colorbar(im2, ax=ax2)

# Contour plot for electric potential
VpLines = 10 ** np.linspace(6, 12, 5)
VpLines = sorted(list(-VpLines) + list(VpLines))
ax1.contour(X, Y, V_potential, colors='r', linewidths=0.5, levels=np.linspace(np.min(V_potential), np.max(V_potential), 50))

""" Section 5: Vector plot (Electric Field)
#---------------------------------------------------------------------------"""
fig2 = plt.figure(figsize=(21, 7))
ax3 = fig2.add_subplot(131)
# Streamplot for the electric field (vX, vY as Ex, Ey)
ax3.streamplot(X, Y, Ex, Ey, color='blue', cmap='coolwarm', density=1.0)

# Contour plot for electric potential
ax3.contour(X, Y, V_potential, colors='red', linewidths=0.5, levels=np.linspace(np.min(V_potential), np.max(V_potential), 50))
#ax3.contour(X, Y, V_potential, colors='red', linewidths=1, levels=VpLines)
# Color-filled contour plot
filled_contour = ax3.contourf(X, Y, V_potential, levels=50, cmap='coolwarm')

# Title and labels
ax3.set_title("Electric Field and Equipotential Lines", fontsize=16)
ax3.set_xlabel("x (m)", fontsize=14)
ax3.set_ylabel("y (m)", fontsize=14)

# Colorbar for the potential field
plt.colorbar(filled_contour, ax=ax3, label="Electric Potential (V)")

# Show the plot
plt.savefig('fieldPlot.png', dpi=300)


""" 
PART B
"""

#Assuming PART A is correct, I will attempt to trial and error the following
#First it is clear that the larger the charges
#Often indicates that they will be a larger value
#Second, we can also see that the type (i.e., positive or negative) will impact also

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:21:19 2024

@author: tevin
"""

'''
PART B
'''

# Computational Exercise 1 for PHYS*2330 - Fall 2024
# ------------------------------------------------------------------------------
## For this assignment, I need two utilize two functions, one given and the other created
# First, a potential function that was created during tutorial
# Second, design electric field function utilizing the Electric Field equation from Class
# Third I will need to plot both of these function on a plot by highlight key components
    #These components are the following, position, charge, density, potential contour, and directional field
#Fourth/Finally, Save your plot(s) as a single image file, “fieldPlot.png”. And name it accordingly.
#Part B requires that I attempt to locate the area that the charges are placed and their charge


# """
# PART B - Uncomment the below code for my estimate on the charges and positions
# """
#
# """ Section 1:  Start by importing relevant libraries
# #---------------------------------------------------------------------------"""
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.constants import epsilon_0
#
# """ Section 2:  Define functions for the script
# #---------------------------------------------------------------------------"""
#
# def electric_potential(q, rq, X, Y):
#     e_o = epsilon_0
#     Fr_pi = (4 * np.pi)
#     K = 1 / (Fr_pi * e_o)
#     r = np.sqrt((rq[0] - X) ** 2 + (rq[1] - Y) ** 2)  # Distance between the position
#     V = K * q / r
#     return V
#
# def electric_field(q, rq, X, Y):
#     e_o = epsilon_0
#     Fr_pi = (4 * np.pi)
#     K = 1 / (Fr_pi * e_o)
#
#     # Distance between charge and observation points
#     r = np.sqrt((X - rq[0]) ** 2 + (Y - rq[1]) ** 2)
#
#     # Angle calculation
#     theta = np.arctan2((Y - rq[1]), (X - rq[0]))
#
#     # Electric field components using r-squared and theta
#     Efield_comp_x = K * q / (r ** 2) * np.cos(theta)  # x direction
#     Efield_comp_y = K * q / (r ** 2) * np.sin(theta)  # y direction
#
#     return Efield_comp_x, Efield_comp_y
#
# """ Section 3:  Main body of code
# #---------------------------------------------------------------------------"""
# # Create a 2D grid of x, y points using numpy meshgrid function
#
# nx, ny = 100, 100
# x = np.linspace(-5, 5, nx)
# y = np.linspace(-5, 5, ny)
# X, Y = np.meshgrid(x, y)
#
#
#
#
# # Charges for trial and error
# q1 = -0.4
# q2 = 0.6
# q3 = -0.55
# q4 = 0.6
# # Positions
# x1, y1 = 2.2, -2
# x2, y2 = -1.5, -3.15
# x3, y3 = -3,3
# x4, y4 = 0,1
#
# # Electric Potential Calculation
# V_potential = electric_potential(q1, [x1, y1], X, Y)
# V_potential += electric_potential(q2, [x2, y2], X, Y)
# V_potential += electric_potential(q3, [x3, y3], X, Y)
# V_potential += electric_potential(q4, [x4, y4], X, Y)
#
# # Electric Field Calculation (using 2D grid X and Y)
# EField_x1, EField_y1 = electric_field(q1, [x1, y1], X, Y)
# EField_x2, EField_y2 = electric_field(q2, [x2, y2], X, Y)
# EField_x3, EField_y3 = electric_field(q3, [x3, y3], X, Y)
# EField_x4, EField_y4 = electric_field(q4, [x4, y4], X, Y)
#
# # Sum the electric field components
# Ex = EField_x1 + EField_x2 + EField_x3 + EField_x4
# Ey = EField_y1 + EField_y2 + EField_y3 + EField_y4
#
# """ Section 4:  Plot your results as a contour plot
# #---------------------------------------------------------------------------"""
# fig = plt.figure(figsize=(21, 7))
# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)
#
# ax1.set_title("Electric Potential", fontsize=20)
# ax2.set_title("Electric Field (Y meshgrid)", fontsize=20)
#
# # Electric potential plot
# im1 = ax1.imshow(V_potential, cmap='coolwarm', extent=(-6, 6, -5, 5), origin="lower")
# plt.colorbar(im1, ax=ax1)
#
# # Y meshgrid plot
# im2 = ax2.imshow(Y, cmap='coolwarm')
# plt.colorbar(im2, ax=ax2)
#
# # Contour plot for electric potential
# VpLines = 15.5 ** np.linspace(6, 21, 10)
# VpLines = sorted(list(-VpLines) + list(VpLines))
# # ax1.contour(X, Y, V_potential, colors='r', linewidths=0.5, levels=np.linspace(np.min(V_potential), np.max(V_potential), 50))
# ax1.contour(X, Y, V_potential, colors='red', linewidths=1, levels=VpLines)
# """ Section 5: Vector plot (Electric Field)
# #---------------------------------------------------------------------------"""
# fig2 = plt.figure(figsize=(21, 7))
# ax3 = fig2.add_subplot(131)
# # Streamplot for the electric field (vX, vY as Ex, Ey)
# ax3.streamplot(X, Y, Ex, Ey, color='blue', cmap='coolwarm', density=0.9)
#
# # Contour plot for electric potential
# # ax3.contour(X, Y, V_potential, colors='red', linewidths=0.5, levels=np.linspace(np.min(V_potential), np.max(V_potential), 50))
# ax3.contour(X, Y, V_potential, colors='red', linewidths=0.5, levels=VpLines)
#
# # Color-filled contour plot
# filled_contour = ax3.contourf(X, Y, V_potential, levels= 40, cmap='coolwarm')
#
# # Title and labels
# ax3.set_title("Electric Field and Equipotential Lines", fontsize=16)
# ax3.set_xlabel("x (m)", fontsize=14)
# ax3.set_ylabel("y (m)", fontsize=14)
#
# # Colorbar for the potential field
# plt.colorbar(filled_contour, ax=ax3, label="Electric Potential (V)")
#
# # Show the plot
# plt.savefig('fieldPlot_PartB.png', dpi=300)






