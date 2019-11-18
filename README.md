# Teleop-controlled-bot-using-ROS
  This project is intended to be a teaching and learning experience for those who want to get started with ROS. Here,we use master slave concept for controlling the bot; the commands are given from the master system's terminal and the slave(bot) moves accordingly.
 ![alt-text](https://github.com/Rohini-G/Teleop-controlled-bot-using-ROS/blob/master/isometric%20view.jpeg)
 ![alt-text](https://github.com/Rohini-G/Teleop-controlled-bot-using-ROS/blob/master/top%20view.jpeg)
## Components Used
          Odroid XU4 and its shield (Shifter-Shield CON3 Header)
          6V 4.5A Leadacid battery (for odroid - connect it using a jack)
          l298n motor driver
          12V 1.3Ah Leadacid battery (for motor driver)
          Chassis with 12V motors(4)   
          Wifi adapter
          
## Circuit connection
![alt-text](https://github.com/Rohini-G/Teleop-controlled-bot-using-ROS/blob/master/circuit.jpg)
### Explanation
  Connect the motors and battery to the driver and then connect the input pins of the driver to the gpio pins of odroid .
  
          IN1 to wiring pi gpio 7
          
          IN2 to wiring pi gpio 0
          
          IN3 to wiring pi gpio 9
          
          IN4 to wiring pi gpio 8
          
          Ground of driver to gpio 39 (ground)
   
         
## Folder organisation
For Publisher (in master)
![alt-text](https://github.com/Rohini-G/Teleop-controlled-bot-using-ROS/blob/master/publisher.jpg)
For Subscriber(in slave)

![alt-text](https://github.com/Rohini-G/Teleop-controlled-bot-using-ROS/blob/master/subcriber.jpg)

## Configuring Master and Slave
   Install ROS and create catkin_ws and install dependensies of our ros version. For this use http://wiki.ros.org/ROS/Installation . You may install either Kinetic or Melodic , here we used melodic for master system and kinetic for odroid.
          
   First choose a PC or laptop as the master and odroid is our slave (Both master and the slave should have ROS installed in it).
          In the master system, open the terminal, create a teleop_twist_keyboard package and then git clone the publisher code in it . To do so,run the following commands in the terminal
```sh
cd catkin_ws
. ~/catkin_ws/devel/setup.bash
catkin_make
```
The above commands are for sourcing our environment
```sh
cd src
ROS_CREATE_PACKAGE teleop_twist_keyboard
```
The above commands will create a package named teleop_twist_keyboard in the src folder.This package will contain a package.xml file and a Cmakelist.txt file in it.
Now, git clone the publisher code in the teleop_twist_keyboard package
```sh
cd teleop_twist_keyboard
git clone https://github.com/Rohini-G/Teleop-controlled-bot-using-ROS/tree/master/teleop_twist_keyboard
```
While cloning, a tab may appear asking for replacement of package.xml file and Cmakelist.txt file; click on replace option.
Now the publisher code - teleop_twist_keyboard.py would be inside the teleop_twist_keyboard package.Now again source and build the environment by running the following commands
```sh
cd catkin_ws
. ~/catkin_ws/devel/setup.bash
catkin_make
```
This time teleop_twist_keyboard must be recognized as a package and built while running catkin_make command.
Now, the publisher code is ready in the master, its time for us to setup our subscriber code in the slave.
In the slave (odroid), git clone the subscriber code in the src folder using the following commands
```sh
cd catkin_ws/src
git clone https://github.com/Rohini-G/Teleop-controlled-bot-using-ROS/blob/master/subscriberorg.py
cd catkin_ws
. ~/catkin_ws/devel/setup.bash
catkin_make
```
Now the slave is also ready.Its time for us to connect master and slave; for this,connect both master and slave in the same wifi network and then in the master terminal ,run
```sh
ifconfig
```
This will give us information about the network interface; in this, the number following "inet addr:  " is the IP address.

Now,do the same in slave and find the slave's IP address.
In master terminal,run
```sh
cd
nano .bashrc
```
You will find the following lines in the bashrc file
```sh
export ROS_MASTER_URI=http://X.X.X.X:1131
export ROS_HOSTAGE_NAME=X.X.X.X
export ROS_IP=Y.Y.Y.Y
```
edit it such that both X.X.X.X and Y.Y.Y.Y is master's IP ,then save and exit.
Now in terminal,run
```sh
roscore
```
In another terminal,run
```
cd catkin_ws/src
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
If there is any problem in running the rosrun command,it means that teleop_twist_keyboard is not recognised as a package.

In slave,run
```sh
nano .bashrc
```
You will find the following lines in the bashrc file
```sh
export ROS_MASTER_URI=http://X.X.X.X:1131
export ROS_HOSTAGE_NAME=Y.Y.Y.Y
export ROS_IP=Y.Y.Y.Y
```
edit the above lines such that X.X.X.X is master's IP and Y.Y.Y.Y is slave's IP

Now,run
```
cd catkin_ws/src
python subscriber.py
```
Now you can control the bot by teleop commands from master.

NOTE: while giving commands in the master, the cursor should be placed in the terminal in which rosrun teleop_twist_keyboard teleop_twist_keyboard.py is running.






         
          
          
          
          
