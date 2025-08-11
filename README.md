
# Mecanum Kinematics

Program for calculating the kinematics of a 4-wheel mecanum robot, including forward kinematics and inverse kinematics


## Installation

Clone the repository to use

```python
  git clone https://github.com/Hakaisha1/Mecanum-kinematics.git
```

Install all the dependencies

```python
  pip install -r requirements.txt
```


    
## Example Variables
This is an example of the variables used in this program. (Change these variables according to your needs)
```python
  r = 0.1 # wheel radius
  L = 0.5 # length of the robot
  W = 0.3 # width of the robot
  omega = np.array([1.0, 0.5, -0.5, 0.2]) # angular velocities for each wheel
  omega_z = 0.3 # angular velocities for robot
```


## Usage/Examples
Change all example variables to the numbers you use

### Forward Kinematics

```python
  def forward_kinematic(omega, r, L, W):
    M = (r/4) * np.array([
        [1, 1, 1, 1],                                    # vx
        [-1, 1, 1, -1],                                  # vy
        [-1/(L + W), 1/(L + W), -1/(L + W), 1/(L + W)]   # omega_z
    ])
    return M @ omega
```
### Inverse Kinematics

```python
def inverse_kinematic(vx, vy, omega_z, r, L, W):
    M_inv = (1/r) * np.array([
        [1, -1, -(L + W)],    # omega1 (front-left)
        [1, 1, (L + W)],      # omega2 (front-right) 
        [1, 1, -(L + W)],     # omega3 (back-left)
        [1, -1, (L + W)]      # omega4 (back-right)
    ])
    return M_inv @ np.array([vx, vy, omega_z])
```
### Run 

```bash
python main.py
```
