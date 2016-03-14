robotics_class
===========

Starting code for various labs. See the [wiki] (https://github.com/irwineffect/ta_robotics/wiki) for information about various labs

#Getting Started
Run the following commands to get set up with everything.

To clone this repo:
```
git clone --recursive https://github.com/irwineffect/robotics_class.git
```

Install dependencies:
```
cd robotics_class
rosdep install --from-paths src --ignore-src --rosdistro indigo -y
sudo apt-get install ros-indigo-joystick-drivers
rosdep install joy
```

Build the project:
```
catkin_make
```

Add sourcing the environment to your *.bashrc*:
```
echo "source `pwd`/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
