import numpy as np
from kinematics.forward import forward_kinematic
from kinematics.inverse import inverse_kinematic

r = 0.1  # wheel radius
L = 0.5  # length of the robot
W = 0.3  # width of the robot
omega = np.array([1.0, 0.5, -0.5, 0.2])  # angular velocities for each wheel

# Forward kinematics
v = forward_kinematic(omega, r, L, W)
print("Forward Kinematics Result:")
print(f"vx: {v[0]:.3f} m/s")
print(f"vy: {v[1]:.3f} m/s") 
print(f"omega_z: {v[2]:.3f} rad/s")

# inverse kinematics
vx, vy, omega_z = 0.1, 0.2, 0.3  # example linear and angular velocities
wheel_speeds = inverse_kinematic(vx, vy, omega_z, r, L, W)
print("\nInverse Kinematics Result:")
print(f"Wheel speeds: {wheel_speeds}")

# verification
v_verify = forward_kinematic(wheel_speeds, r, L, W)
print(f"\nVerification - Original: [{vx}, {vy}, {omega_z}]")
print(f"Verification - Computed: {v_verify}")