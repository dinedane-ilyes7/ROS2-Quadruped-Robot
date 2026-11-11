# Latest recorded progress (November 2026)

## Implemented or verified in earlier local tests

- ROS 2 **Jazzy** on Ubuntu **24.04**, with Gazebo **Harmonic**, `gz_ros2_control`, RViz.
- Local `mini_dog` package displayed the robot and had **12 joint position command interfaces**.
- `joint_state_broadcaster` and `leg_trajectory_controller` were active; joint motion to ~0.6 rad observed in simulation.
- Physical robot: **Teensy 3.2**, PCA9685, 12 servos. `STAND` and `MOVE` serial commands were observed in a local hardware testing conversation, but **the final source file for those commands is not in this archive**.
- Standing calibration: FL (CH0 1800, CH1 1200, CH2 1100), RL (CH4/5/6 1500), FR (CH8 1500, CH9 1700, CH10 1300), RR (CH12 1400, CH13 1500, CH14 1100), all in microseconds.
- CH12 rear-right hip roll: increasing PWM moves inward; safe tested 1000–1800 µs; standing reference 1400 µs. Servo-horn mechanical re-indexing was discussed and adjusted during testing.
- One-leg numerical forward/inverse kinematic consistency check recorded (see `KINEMATICS_CHECK.md`).

## Reconstructed here, **not** retested

- The current `LatestFullRobot.urdf.xacro` starts with the old supplied SolidWorks geometry, renames the twelve joints to `*_joint`, makes them revolute with simulation-only ±1 rad limits, and includes a separate `ros2_control` Xacro.
- The ROS 2 setup, Gazebo Harmonic `gazebo_full.launch.py`, controller YAML, and plugin Xacro are reconstructed from prior configuration notes rather than copied from the most recent local workspace.
- No verification of actual Gazebo startup, controller activation, STL contact behavior or physical hardware compatibility was performed on this package.

## Not included or not yet completed

- The user's latest original **Teensy `main.cpp`** containing `STAND`/`MOVE`, actual up-to-date ROS 2 launch scripts and RViz config were not available as original files.
- Full walking gait / stance-swing generation / body stabilization not yet verified.
- ROS 2 to Teensy UART/Jetson hardware bridge not yet integrated.
- NVIDIA Isaac Lab RL training files and policy **not yet provided**; they will be added as a separate part when available.

## Do not confuse

The old third-party package uses Gazebo Classic / legacy joint names and has fixed or zero-range joints. It should not be advertised as a fully operational Jazzy/Gazebo Harmonic controller without the later changes.
