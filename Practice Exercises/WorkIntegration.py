import numpy as np
from scipy.integrate import quad


def extField(r, charges, positions):
    """
    Calculate the electric field at a point due to a distribution of point charges.

    Parameters:
    - r: Position vector where we calculate the field (numpy array)
    - charges: List of charge magnitudes (in Coulombs)
    - positions: List of position vectors of charges (each a numpy array)

    Returns:
    - E: Electric field vector at point r (numpy array)
    """
    k_e = 8.99e9  # Coulomb constant in Nm^2/C^2
    E = np.array([0.0, 0.0])

    for q, pos in zip(charges, positions):
        r_vec = r - pos  # Vector from charge position to point
        r_mag = np.linalg.norm(r_vec)  # Distance from charge to point
        if r_mag != 0:  # Avoid division by zero
            E += (k_e * q / r_mag ** 3) * r_vec

    return E


def path_func(t, r_initial, r_final):
    """
    Parameterize the path between initial and final points.

    Parameters:
    - t: Parameter (0 <= t <= 1)
    - r_initial: Initial position vector
    - r_final: Final position vector

    Returns:
    - Position along the path at time t
    """
    return r_initial + t * (r_final - r_initial)


def integrand(t, r_initial, r_final, charge, charges, positions):
    """
    Calculate the dot product of the electric field and the tangent vector along the path.

    Parameters:
    - t: Parameter (0 <= t <= 1)
    - r_initial: Initial position vector
    - r_final: Final position vector
    - charge: Charge of the particle moving along the path (in Coulombs)
    - charges: List of charge magnitudes (in Coulombs)
    - positions: List of position vectors of charges (each a numpy array)

    Returns:
    - Dot product of E and dr/dt at time t
    """
    r = path_func(t, r_initial, r_final)
    E = extField(r, charges, positions)
    dr_dt = (r_final - r_initial)  # Constant derivative for a straight-line path
    return np.dot(E, dr_dt) * charge / np.linalg.norm(r_final - r_initial)


def workDone_integral(r_initial, r_final, charge, charges, positions):
    """
    Calculate the work done on a charge moving from r_initial to r_final using line integral.

    Parameters:
    - r_initial: Initial position vector (numpy array)
    - r_final: Final position vector (numpy array)
    - charge: Charge that is being moved (in Coulombs)
    - charges: List of point charge magnitudes (in Coulombs)
    - positions: List of position vectors of charges (each a numpy array)

    Returns:
    - work: Work done on the charge (in Joules)
    """
    result, _ = quad(integrand, 0, 1, args=(r_initial, r_final, charge, charges, positions))
    return result


# Example usage
# Define the positions and magnitudes of point charges
charges = [1e-6, -2e-6]  # Charges in Coulombs
positions = [np.array([0, 0]), np.array([1, 0])]  # Charge positions in meters

# Define initial and final positions
r_initial = np.array([-4.0, -3.0])  # Initial position in meters
r_final = np.array([3.0, 2.0])  # Final position in meters

# Define the charge moving along the path
moving_charge = 4.0  # Charge in Coulombs

# Calculate work done
work = workDone_integral(r_initial, r_final, moving_charge, charges, positions)
print(work)
