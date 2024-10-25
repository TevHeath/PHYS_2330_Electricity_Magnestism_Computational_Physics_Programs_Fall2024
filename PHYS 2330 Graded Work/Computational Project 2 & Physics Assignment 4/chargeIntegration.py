
""" Section 1: Start by importing relevant libraries """
import numpy as np

""" Section 2: Define functions for the script """

# This produces arrays of (x,y) positions for a line
# segment, from position ri to rf, divided into N equally spaced intervals
def lineSegment(ri, rf, N):
    x = np.linspace(ri[0], rf[0], N)
    y = np.linspace(ri[1], rf[1], N)
    dL = np.sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)
    return x, y, dL

# Return the electric field, E, due to a charge "q" located at position (xq, yq).
def eField(q, xq, yq, x, y):
    k = 9.0e9  # Coulomb constant
    denom = ((x - xq) ** 2 + (y - yq) ** 2) ** 1.5
    dEx = k * q * (x - xq) / denom
    dEy = k * q * (y - yq) / denom
    return dEx, dEy

# Create a function that will integrate using Trapezoid Rule
def trapz(f, dL):
    area = 0.0
    for i in range(f.size - 1):  # 1
        # area += dL * (f[i]+ f[i+1])/2 #2
        area = dL * np.sum(f[1:] + f[:-1]) / 2  # 3
    return area

# Create a function that will integrate using Simpson's Rule
def simpson(f, dL):
    """
    Simpson's rule approximates the integral of a function by fitting parabolas through groups of three points.
    It requires an even number of intervals (odd number of points).
    """
    if f.size % 2 == 0:
        raise ValueError("Simpson's rule requires an odd number of points.")

    n = f.size - 1  # Number of intervals
    area = f[0] + f[-1]  # Initialize with first and last terms of f(x)

    # Apply Simpson's rule coefficients:
    # 4 for odd-indexed terms, 2 for even-indexed terms
    area += 4 * np.sum(f[1:n:2])  # Sum of odd-indexed terms
    area += 2 * np.sum(f[2:n - 1:2])  # Sum of even-indexed terms

    # Multiply by the interval size divided by 3 (Simpson's factor)
    area *= dL / 3

    return area

# Function to calculate the electric field for a semi-circle
def semiCircle(radius, Qtot, Nsegments, Ro_cir):
    theta = np.linspace(-np.pi / 2, np.pi / 2, Nsegments)  # Angle from -π/2 to π/2
    dtheta = np.pi / Nsegments  # Angular width of each segment
    dL = radius * dtheta  # Length of each segment
    lamb = Qtot / (np.pi * radius)  # Linear charge density

    X = radius * np.cos(theta)  # x-coordinates
    Y = radius * np.sin(theta)  # y-coordinates

    Ex_total, Ey_total = 0.0, 0.0

    # Electric field contribution from each segment
    for i in range(Nsegments):
        r_charge = np.array([X[i], Y[i]])  # Position of charge element
        r = Ro_cir - r_charge  # Distance vector from charge to observation point
        r_mag = np.linalg.norm(r)

        dq = lamb * dL  # Charge of each element
        dE = (1 / (4 * np.pi * 8.854e-12)) * (dq / r_mag**2) * (r / r_mag)

        Ex_total += dE[0]
        Ey_total += dE[1]

    return Ex_total, Ey_total

""" Section 3: Main body of code """
"""PART A"""
# Line Segment Electric Field
Ri = np.array([-5, 0])  # Start of the line segment
Rf = np.array([5, 0])  # End of the line segment
Qtot = 3.0  # Total charge
Ro_x = np.array([10, 0])  # Observation point for line segement
Ro_y = np.array([0, 5])  # Observation point for line segement
Ro_cir = np.array([0, 0]) #Observation point for circle segement centre-point

# Calculate for line segment (Trapzoid -> above the line [0,5])
Nsegments_trap = 100
Xt, Yt, dL_t = lineSegment(Ri, Rf, Nsegments_trap + 1)
lamb = Qtot / np.sqrt(np.sum((Rf - Ri) ** 2))  # Linear charge density
dEx_t_abv, dEy_t_abv = eField(lamb, Xt, Yt, * Ro_y)
Ex_line_abv = trapz(dEx_t_abv, dL_t)
Ey_line_abv = trapz(dEy_t_abv, dL_t)

# Calculate the line segment (Simpson -> above the line [0,5])
Nsegments_simp = 60
Xs, Ys, dL_s = lineSegment(Ri, Rf, Nsegments_simp + 1)
lamb = Qtot / np.sqrt(np.sum((Rf - Ri) ** 2))  # Linear charge density
dEx_s_abv, dEy_s_abv = eField(lamb, Xs, Ys, * Ro_y)
Ex_S_line_abv = simpson(dEx_s_abv,dL_s)
Ey_S_line_abv = simpson(dEy_s_abv, dL_s)

# Calculate for line segment (Trapzoid -> along the line [10,0])
Nsegments_trap = 100
Xt, Yt, dL_t = lineSegment(Ri, Rf, Nsegments_trap + 1)
lamb = Qtot / np.sqrt(np.sum((Rf - Ri) ** 2))  # Linear charge density
dEx_t_acrs, dEy_t_acrs = eField(lamb, Xt, Yt, * Ro_x)
Ex_line_acrs = trapz(dEx_t_acrs, dL_t)
Ey_line_acrs = trapz(dEy_t_acrs, dL_t)

# Calculate the line segment (Simpson -> along the line [10,0])
Nsegments_simp = 60
Xs, Ys, dL_s = lineSegment(Ri, Rf, Nsegments_simp + 1)
lamb = Qtot / np.sqrt(np.sum((Rf - Ri) ** 2))  # Linear charge density
dEx_s_acrs, dEy_s_acrs = eField(lamb, Xs, Ys, * Ro_x)
Ex_S_line_acrs = simpson(dEx_s_acrs,dL_s)
Ey_S_line_acrs = simpson(dEy_s_acrs, dL_s)


# Print electric field for line segment across the line [10,0]
print(f"Line Segment Electric Field at Ro = {Ro_x}:")
print(f"Trapezoid Rule: Ex = {Ex_line_acrs} N/C, Ey = {Ey_line_acrs} N/C")
print(f"Simpson's Rule: Ex = {Ex_S_line_acrs} N/C, Ey = {Ey_S_line_acrs} N/C")


# Print electric field for line segment above the line [0,5]
print(f"Line Segment Electric Field at Ro = {Ro_y}:")
print(f"Trapezoid Rule: Ex = {Ex_line_abv} N/C, Ey = {Ey_line_abv} N/C")
print(f"Simpson's Rule: Ex = {Ex_S_line_abv} N/C, Ey = {Ey_S_line_abv} N/C")


# int(f"Line Segment Electric Field Simpson at Ro = {Ro}:")
# print(f"Ex = {Ex_S_line} N/C, Ey = {Ey_S_line} N/C")

# # Semi-Circle Electric Field for Centre Point
# radius = 5.0  # Radius of the semicircle
# Ro_cir = np.array([0, 0]) #Observation point for circle segment centre-point
# Ex_semi_centre, Ey_semi_centre = semiCircle(radius, Qtot, Nsegments, Ro_cir)
#
# #Semi-Circle Electric Field for Outside
# Ex_semi_out, Ey_semi_out = semiCircle(radius, Qtot, Nsegments, Ro)
#
#
#
# # Print electric field for semi-circle at centre-point
# print(f"Semi-Circle Electric Field at Ro_circle centre point = {Ro_cir}:")
# print(f"Ex = {Ex_semi_centre} N/C, Ey = {Ey_semi_centre} N/C")
#
# # Print electric field for semi-circle at 5 meter from radius
# print(f"Semi-Circle Electric Field at Ro_circle outside point = {Ro}:")
# print(f"Ex = {Ex_semi_out} N/C, Ey = {Ey_semi_out} N/C")

"""PART B"""




"""PART C"""
