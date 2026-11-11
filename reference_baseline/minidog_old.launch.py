#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    xacro_file_name = 'LatestFullRobot.urdf.xacro'
    urdf_file_name = 'LatestFullRobot.urdf'

    package_name = 'mini_dog'

    urdf_file = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        urdf_file_name)
    
    xacro_file = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        xacro_file_name)
    doc = xacro.process_file(xacro_file)
    robot_desc = doc.toprettyxml(indent='    ')
    f = open(urdf_file, 'w+')
    f.write(robot_desc)
    f.close()

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        arguments=[urdf_file],
    )
    
    joint_state_publisher = Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
    )
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
    )

    joint_broad_spawner = Node(
        package='controller_manager',
        executable='spawner.py',
        arguments=['joint_broad'],
        output='screen',
    )

    leg_trajectory_spawner = Node(
        package='controller_manager',
        executable='spawner.py',
        arguments=['leg_trajectory_controller'],
        output='screen',
    )

    teleop_twist_keyboard = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard.py',
        name='teleop_twist_keyboard',
        output='screen',
        remappings=[('/cmd_vel', '/minidog/cmd_vel')]  # Adjust the topic name as necessary
    )


    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        rviz_node,
        joint_broad_spawner,
        leg_trajectory_spawner,
#        teleop_twist_keyboard,          
    ])