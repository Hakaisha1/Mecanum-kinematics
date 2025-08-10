import numpy as np
import math

def inverse_kinematic(vx, vy, omega_z, r, L, W):
    M_inv = (1/r) * np.array([
        [1, -1, -(L + W)],    # omega1 (front-left)
        [1, 1, (L + W)],      # omega2 (front-right) 
        [1, 1, -(L + W)],     # omega3 (back-left)
        [1, -1, (L + W)]      # omega4 (back-right)
    ])
    return M_inv @ np.array([vx, vy, omega_z])
    
