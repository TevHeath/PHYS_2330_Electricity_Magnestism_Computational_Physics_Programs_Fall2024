
# Computational Exercise 1 for PHYS*2330 - Fall 2024
# ------------------------------------------------------------------------------


"""
# PART A
# """

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
    Four_pi = (4 * np.pi)
    K = 1 / (Four_pi * epsilon_0)
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
    Four_pi = (4 * np.pi)
    K = 1 / (Four_pi * epsilon_0)

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
Pt_chrg_q1 = -3
Pt_chrg_q2 = -1
Pt_chrg_q3 = +2
Pt_chrg_q4 = +6

# Positions (assisted using hand-Calculations)
x1, y1 = 1 / np.sqrt(2), 3 / np.sqrt(2)
x2, y2 = -1 / np.sqrt(2), 3 / np.sqrt(2)
x3, y3 = -1, 3.5
x4, y4 = 1 / np.sqrt(2), 0.5 - 3 / np.sqrt(2)

# Electric Potential Calculation
V_potential = electric_potential(Pt_chrg_q1, [x1, y1], X, Y)
V_potential += electric_potential(Pt_chrg_q2, [x2, y2], X, Y)
V_potential += electric_potential(Pt_chrg_q3, [x3, y3], X, Y)
V_potential += electric_potential(Pt_chrg_q4, [x4, y4], X, Y)

# Electric Field Calculation (using 2D grid X and Y)
EField_x1, EField_y1 = electric_field(Pt_chrg_q1, [x1, y1], X, Y)
EField_x2, EField_y2 = electric_field(Pt_chrg_q2, [x2, y2], X, Y)
EField_x3, EField_y3 = electric_field(Pt_chrg_q3, [x3, y3], X, Y)
EField_x4, EField_y4 = electric_field(Pt_chrg_q4, [x4, y4], X, Y)

# Sum the Electric Field components
Ex = EField_x1 + EField_x2 + EField_x3 + EField_x4
Ey = EField_y1 + EField_y2 + EField_y3 + EField_y4


""" Section 4:  Plotting the Contour Plots, Elec Potential & Elec Field
#---------------------------------------------------------------------------"""
fig = plt.figure(figsize=(20, 20))

# Top left plot: Electric Potential
ax1 = fig.add_subplot(221)  # 2 rows, 2 columns, position 1
ax1.set_title("Electric Potential", fontsize=20)

# Electric potential plot (using coolwarm colour scheme)
im1 = ax1.imshow(V_potential, cmap='coolwarm', extent=(-6, 6, -5, 5), origin="lower")
plt.colorbar(im1, ax=ax1)

# Contour plot for electric potential
VpLines = 10 ** np.linspace(6, 12, 5)
VpLines = sorted(list(-VpLines) + list(VpLines))
ax1.contour(X, Y, V_potential, colors='red', linewidths=0.5, levels=VpLines)

# Top right plot: Y Meshgrid
ax2 = fig.add_subplot(222)  # 2 rows, 2 columns, position 2
ax2.set_title("Y Meshgrid", fontsize=20)

# Meshgrid plot (using coolwarm colour scheme)
im2 = ax2.imshow(Y, cmap='coolwarm', extent=(-6, 6, -5, 5), origin="lower")
plt.colorbar(im2, ax=ax2)

# Bottom plot: Electric Field
ax3 = fig.add_subplot(212)  # 2 rows, 1 column, position 3 (spans both columns)
ax3.set_title("Electric Field and Equipotential Lines", fontsize=16)

# Streamplot for the electric field (Ex, Ey)
ax3.streamplot(X, Y, Ex, Ey, color='blue', cmap='coolwarm', density=1.0)

# Contour plot for electric potential on the electric field plot
ax3.contour(X, Y, V_potential, colors='red', linewidths=0.5, levels=VpLines)

# Color-filled contour plot for electric potential on the electric field plot
filled_contour = ax3.contourf(X, Y, V_potential, levels=15, cmap='coolwarm')

# Labels for the bottom plot
ax3.set_xlabel("x (m)", fontsize=14)
ax3.set_ylabel("y (m)", fontsize=14)

# Colorbar for the potential field
plt.colorbar(filled_contour, ax=ax3, label="Electric Potential (V)")


# Save the figure
plt.savefig('fieldPlot2.png', dpi=300)



# '''
# PART B
# In the following section, simply uncomment below and comment PART A starting from line 170 upwards
# Run the program once it is uncommented, then it will provide the necessary my estimation of the charges and location.
# In PART B, I used the same structure from PART A to help with experimenting the design.
# '''



# """ Section 1:  Start by importing relevant libraries
# #---------------------------------------------------------------------------"""
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.constants import epsilon_0

# """ Section 2:  Define functions for the script
# #---------------------------------------------------------------------------"""

# def electric_potential(q, rq, X, Y):
#     e_o = epsilon_0
#     Fr_pi = (4 * np.pi)
#     K = 1 / (Fr_pi * e_o)
#     r = np.sqrt((rq[0] - X) ** 2 + (rq[1] - Y) ** 2)  # Distance between the position
#     V = K * q / r
#     return V

# def electric_field(q, rq, X, Y):
#     e_o = epsilon_0
#     Fr_pi = (4 * np.pi)
#     K = 1 / (Fr_pi * e_o)

#     # Distance between charge and observation points
#     r = np.sqrt((X - rq[0]) ** 2 + (Y - rq[1]) ** 2)

#     # Angle calculation
#     theta = np.arctan2((Y - rq[1]), (X - rq[0]))

#     # Electric field components using r-squared and theta
#     Efield_comp_x = K * q / (r ** 2) * np.cos(theta)  # x direction
#     Efield_comp_y = K * q / (r ** 2) * np.sin(theta)  # y direction

#     return Efield_comp_x, Efield_comp_y

# """ Section 3:  Main body of code
# #---------------------------------------------------------------------------"""
# # Create a 2D grid of x, y points using numpy meshgrid function

# nx, ny = 100, 100
# x = np.linspace(-5, 5, nx)
# y = np.linspace(-5, 5, ny)
# X, Y = np.meshgrid(x, y)




# # Charges using (trial and error although I determine the charges were small)
# q1 = -0.4
# q2 = 0.6
# q3 = -0.55
# q4 = 0.6

# # Positions (trial and error)
# x1, y1 = 2.2, -2
# x2, y2 = -1.5, -3.15
# x3, y3 = -3,3
# x4, y4 = 0,1

# # Electric Potential Calculation
# V_potential = electric_potential(q1, [x1, y1], X, Y)
# V_potential += electric_potential(q2, [x2, y2], X, Y)
# V_potential += electric_potential(q3, [x3, y3], X, Y)
# V_potential += electric_potential(q4, [x4, y4], X, Y)

# # Electric Field Calculation (using 2D grid X and Y)
# EField_x1, EField_y1 = electric_field(q1, [x1, y1], X, Y)
# EField_x2, EField_y2 = electric_field(q2, [x2, y2], X, Y)
# EField_x3, EField_y3 = electric_field(q3, [x3, y3], X, Y)
# EField_x4, EField_y4 = electric_field(q4, [x4, y4], X, Y)

# # Sum the electric field components
# Ex = EField_x1 + EField_x2 + EField_x3 + EField_x4
# Ey = EField_y1 + EField_y2 + EField_y3 + EField_y4
# #
# # """ Section 4:  Plot your results as a contour plot
# # #---------------------------------------------------------------------------"""

# fig = plt.figure(figsize=(14, 14))

# # Top left plot: Electric Potential
# ax1 = fig.add_subplot(221)  # 2 rows, 2 columns, position 1
# ax1.set_title("Electric Potential", fontsize=20)

# # Electric potential plot (using coolwarm colour scheme)
# im1 = ax1.imshow(V_potential, cmap='coolwarm', extent=(-6, 6, -5, 5), origin="lower")
# plt.colorbar(im1, ax=ax1)

# # Contour plot for electric potential
# VpLines = 15.5 ** np.linspace(6, 21, 10)
# VpLines = sorted(list(-VpLines) + list(VpLines))
# ax1.contour(X, Y, V_potential, colors='red', linewidths=0.5, levels=VpLines)

# # Top right plot: Y Meshgrid
# ax2 = fig.add_subplot(222)  # 2 rows, 2 columns, position 2
# ax2.set_title("Y Meshgrid", fontsize=20)

# # Meshgrid plot (using coolwarm colour scheme)
# im2 = ax2.imshow(Y, cmap='coolwarm', extent=(-6, 6, -5, 5), origin="lower")
# plt.colorbar(im2, ax=ax2)

# # Bottom plot: Electric Field
# ax3 = fig.add_subplot(212)  # 2 rows, 1 column, position 3 (spans both columns)
# ax3.set_title("Electric Field and Equipotential Lines", fontsize=16)

# # Streamplot for the electric field (Ex, Ey)
# ax3.streamplot(X, Y, Ex, Ey, color='blue', cmap='coolwarm', density=1.0)

# # Contour plot for electric potential on the electric field plot
# ax3.contour(X, Y, V_potential, colors='red', linewidths=0.5, levels=VpLines)

# # Color-filled contour plot for electric potential on the electric field plot
# filled_contour = ax3.contourf(X, Y, V_potential, levels=15, cmap='coolwarm')

# # Labels for the bottom plot
# ax3.set_xlabel("x (m)", fontsize=14)
# ax3.set_ylabel("y (m)", fontsize=14)

# # Colorbar for the potential field
# plt.colorbar(filled_contour, ax=ax3, label="Electric Potential (V)")

# # Adjust layout to avoid overlap
# plt.tight_layout()

# # Save the figure
# plt.savefig('fieldPlot.png', dpi=300)







