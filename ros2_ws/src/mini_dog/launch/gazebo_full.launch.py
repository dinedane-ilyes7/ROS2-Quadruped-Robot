"""Reconstructed Gazebo Harmonic launch candidate based on the 2026 integration notes.

NOT tested on the author's current ROS 2 installation; replace with latest known-working
local gazebo_full.launch.py if it differs.
"""
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro


def generate_launch_description():
    pkg_dir = get_package_share_directory('mini_dog')
    description = xacro.process_file(os.path.join(pkg_dir, 'urdf', 'LatestFullRobot.urdf.xacro')).toxml()
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ), launch_arguments={'gz_args': '-r empty.sdf'}.items()
    )
    publisher = Node(
        package='robot_state_publisher', executable='robot_state_publisher',
        parameters=[{'robot_description': description, 'use_sim_time': True}],
        output='screen'
    )
    spawn = Node(
        package='ros_gz_sim', executable='create',
        arguments=['-topic', 'robot_description', '-name', 'mini_dog', '-z', '0.25'],
        output='screen'
    )
    spawners = TimerAction(period=7.0, actions=[
        Node(package='controller_manager', executable='spawner',
             arguments=['joint_state_broadcaster'], output='screen'),
        Node(package='controller_manager', executable='spawner',
             arguments=['leg_trajectory_controller'], output='screen'),
    ])
    return LaunchDescription([gazebo, publisher, spawn, spawners])
