# Robot Workspace

ROS2 workspace containing robot packages.

## Packages

- `robot_bringup` - Bringup and launch files
- `robot_description` - Robot Description (URDF/SDF)
- `robot_sensors` - Sensor drivers and interfaces
- `robot_control` - Control pipelines

## Setup

```bash
# Source ROS2
source /opt/ros/humble/setup.bash

# Build workspace
colcon build --symlink-install # for autobuild or use (colcon build)

# Source overlay
source install/setup.bash
```

## Usage

Launch robot:

```bash
ros2 launch robot_bringup robot.launch.py
```
