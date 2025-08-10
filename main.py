import numpy as np
from kinematics.forward import forward_kinematic
from kinematics.inverse import inverse_kinematic

r = 0.1  # Wheel radius
L = 0.5  # Length of the robot
W = 0.3  # Width of the robot
omega = np.array([1.0, 0.5, -0.5, 0.2])  # Angular velocities for each wheel

# Forward kinematics
v = forward_kinematic(omega, r, L, W)
print("Forward Kinematics Result:")
print(f"vx: {v[0]:.3f} m/s")
print(f"vy: {v[1]:.3f} m/s") 
print(f"omega_z: {v[2]:.3f} rad/s")

# Inverse kinematics
vx, vy, omega_z = 0.1, 0.2, 0.3  # Example linear and angular velocities
wheel_speeds = inverse_kinematic(vx, vy, omega_z, r, L, W)
print("\nInverse Kinematics Result:")
print(f"Wheel speeds: {wheel_speeds}")

# Verification (should get back original velocities)
v_verify = forward_kinematic(wheel_speeds, r, L, W)
print(f"\nVerification - Original: [{vx}, {vy}, {omega_z}]")
print(f"Verification - Computed: {v_verify}")