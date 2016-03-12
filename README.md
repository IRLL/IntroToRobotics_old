ta_robotics
===========

Starting code for various labs

#Getting Started
Run the following commands to get setup

To clone this repo:
```
git clone https://github.com/irwineffect/ta_robotics.git
```

Install dependencies:
```
cd ta_robotics
rosdep install --from-paths src --ignore-src --rosdistro indigo -y
sudo apt-get install ros-indigo-joystick-drivers
rosdep install joy
```

Build the project:
```
catkin_make
```

Source the environment:
```
source devel/setup.bash
```
