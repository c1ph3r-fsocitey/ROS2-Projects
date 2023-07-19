from setuptools import setup

package_name = 'my_python_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='c1ph3r',
    maintainer_email='c1ph3r@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_python_package.my_first_node:main",
            "py_node_oop = my_python_package.my_first_node_oop:main",
            "robot_news_station = my_python_package.robot_news_station:main",
            "smartphone = my_python_package.smartphone:main", 
            "number_publisher = my_python_package.number_publisher:main", 
            "number_counter = my_python_package.number_counter:main", 
            "add_two_ints_server = my_python_package.add_two_ints_server:main",
            "add_two_ints_client = my_python_package.add_two_ints_client:main", 
            "add_two_ints_client_oops = my_python_package.add_two_ints_client_oops:main",
            "hardware_status_publisher = my_python_package.hardware_status_publisher:main", 
            "basic_sub = my_python_package.basic_sub:main", 
            "basic_pub = my_python_package.basic_pub:main",
            "LED_panel = my_python_package.LED_panel:main", 
            "battery_status = my_python_package.battery_status:main"
        ],
    },
)
