from glob import glob
import os
from setuptools import setup

package_name = 'mini_dog'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'ros2_control'), glob('ros2_control/*.xacro')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.stl')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='project contributors',
    maintainer_email='noreply@example.invalid',
    description='Quadruped robot description and Gazebo simulation package (reconstructed candidate)',
    license='License not specified; source permissions require confirmation',
    entry_points={'console_scripts': []},
)
