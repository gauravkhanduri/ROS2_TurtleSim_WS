from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtle_stimulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='ros@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'driving_node_=py_pubsub.driving_node:main',
            'go_to_goal_=py_pubsub.go_to_goal:main',
            'Go_to_goal_ = py_pubsub.class_go_to_goal:main'

        ],
    },
)
