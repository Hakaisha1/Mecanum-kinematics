import numpy as np
import math

def forward_kinematic(omega, r, L, W):
    """
    Forward kinematics: wheel speeds -> robot velocity
    omega: [omega1, omega2, omega3, omega4] (rad/s)
    Returns: [vx, vy, omega_z] (m/s, m/s, rad/s)
    """
    M = (r/4) * np.array([
        [1, 1, 1, 1],                                    # vx
        [-1, 1, 1, -1],                                  # vy
        [-1/(L + W), 1/(L + W), -1/(L + W), 1/(L + W)]   # omega_z
    ])
    return M @ omega
