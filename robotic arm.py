import time
from adafruit_servokit import ServoKit

# Initialize servo controller
kit = ServoKit(channels=16)

# Define servo angles
base_angle = 90
shoulder_angle = 90
elbow_angle = 90
wrist_angle = 90
gripper_angle = 90

# Function to move robotic arm
def move_arm(base, shoulder, elbow, wrist, gripper):
    kit.servo[0].angle = base
    kit.servo[1].angle = shoulder
    kit.servo[2].angle = elbow
    kit.servo[3].angle = wrist
    kit.servo[4].angle = gripper

# Move robotic arm to initial position
move_arm(base_angle, shoulder_angle, elbow_angle, wrist_angle, gripper_angle)

# Example: Move arm to a new position
new_base_angle = 120
new_shoulder_angle = 60
new_elbow_angle = 30
new_wrist_angle = 45
new_gripper_angle = 60

move_arm(new_base_angle, new_shoulder_angle, new_elbow_angle, new_wrist_angle, new_gripper_angle)
