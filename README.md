# Quadruped Robot — ROS 2 Jazzy, Gazebo and Teensy Servo Calibration

> **Status:** organized development snapshot. The ROS 2 package is a **reconstructed candidate**, not a byte-for-byte copy of the final working local installation.

This repository brings together a historical `mini_dog` robot model (SolidWorks URDF, meshes, ROS 2 package) and subsequent work recorded during development in November 2026: ros2_control, Gazebo Harmonic integration, servo mapping, standing calibration and one-leg kinematic verification. The last locally verified firmware and full current launch files were **not provided as original source files**, so they are not claimed as validated here.

## Technical stack

- Ubuntu 24.04 / ROS 2 Jazzy
- Gazebo Harmonic, RViz and `gz_ros2_control`
- 4 legs × 3 commanded joints = 12 joint targets
- Teensy 3.2 with PCA9685 (50 Hz) and 12 hobby servos
- Planned Jetson high-level execution and future Isaac Lab reinforcement learning

## Directory guide

| Path | Description |
| --- | --- |
| [`ros2_ws/src/mini_dog/`](ros2_ws/src/mini_dog/) | Reconstructed ROS 2 robot-description and Gazebo integration candidate with original STL meshes |
| [`hardware/servo_calibration.csv`](hardware/servo_calibration.csv) | Latest recorded 12 servo standing PWM targets and conservative tested bounds |
| [`hardware/platformio.ini`](hardware/platformio.ini) | Reported Teensy 3.2 PlatformIO settings (firmware source not yet recovered) |
| [`docs/PROJECT_PROGRESS.md`](docs/PROJECT_PROGRESS.md) | Verified achievements versus unverified/reconstructed aspects |
| [`docs/CONNECTIONS.md`](docs/CONNECTIONS.md) | Wiring and signal architecture |
| [`docs/KINEMATICS_CHECK.md`](docs/KINEMATICS_CHECK.md) | Previously verified one-leg FK/IK example |
| [`docs/ORIGIN_AND_PERMISSIONS.md`](docs/ORIGIN_AND_PERMISSIONS.md) | Legacy source attribution and publication limits |
| [`reference_baseline/`](reference_baseline/) | Old URDF and launch scripts kept as history; **not** active Jazzy configuration |

## What had been verified in the development conversation

- Gazebo Harmonic simulation and RViz visualisation on the development computer.
- `joint_state_broadcaster` and `leg_trajectory_controller` running; 12 position command interfaces, joint-target tracking.
- Physical servo neutral/standing calibration for channels 0,1,2,4,5,6,8,9,10,12,13,14.
- Simple leg-1 FK/IK check for a 5 mm Cartesian displacement.

Those outcomes refer to the **previous local configuration**, not a run of this reconstructed ZIP. No full gait or robot-learning controller is included.

## Build and test (candidate; requires an installed Jazzy/Gazebo environment)

```bash
source /opt/ros/jazzy/setup.bash
mkdir -p ~/quadruped_ws/src
cp -a ros2_ws/src/mini_dog ~/quadruped_ws/src/
cd ~/quadruped_ws
colcon build --symlink-install --packages-select mini_dog
source install/setup.bash
ros2 launch mini_dog gazebo_full.launch.py
```

The launch and modified URDF here are a **best-effort reconstruction**, so review them against the latest known-working files from `~/quadruped_ws/src/mini_dog` before replacing your local setup.

## Important safety and authorship notes

The original `mini_dog` source was provided in a historical archive containing material from other collaborators. **Do not publicly republish their meshes or model without permission.** Keep this repository private pending rights review. Servo limits are experimental bounds and do not certify a safe physical robot. Jetson integration, gait generation, and Isaac Lab RL remain future work.

See the [project-progress notes](docs/PROJECT_PROGRESS.md) for exact status.
