import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import xacro

def generate_launch_description():
    # Define package and URDF file names
    package_name = 'mini_dog'
    urdf_file_name = 'LatestFullRobot.urdf'

    # Paths
    urdf_file = os.path.join(get_package_share_directory(package_name), 'urdf', urdf_file_name)

    # Robot State Publisher
    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{'use_sim_time': True}],
        arguments=[urdf_file],
        output='screen',
    )

    # Gazebo Launch (Optional)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    )

    # Spawn Robot in Gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'mini_dog'],
        output='screen',
    )

    # Controller Spawners
    joint_trajectory_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_trajectory_controller"],
        output="screen",
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    # RViz2 Node 
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
    )


    # Return Launch Description
    return LaunchDescription([
        rsp,
        #gazebo,  # Comment this out if not simulating in Gazebo
        spawn_entity,
        joint_trajectory_spawner,
        joint_state_broadcaster_spawner,
        rviz_node,
    ])
