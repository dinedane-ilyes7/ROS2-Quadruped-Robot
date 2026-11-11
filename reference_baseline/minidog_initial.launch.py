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


    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        rviz_node,
        
    ])