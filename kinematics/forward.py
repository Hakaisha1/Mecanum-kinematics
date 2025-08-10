import numpy as np
import math

def forward_kinematic(omega, r, L, W):
    M = (r/4) * np.array([
        [1, 1, 1, 1],                                    # vx
        [-1, 1, 1, -1],                                  # vy
        [-1/(L + W), 1/(L + W), -1/(L + W), 1/(L + W)]   # omega_z
    ])
    return M @ omega
