import rospy
from geometry_msgs.msg import Twist
import odroid_wiringpi as gpio
import time
cmd_vel = Twist()

updated_val=None

import random

def callback(twist):
   global cmd_vel
   global updated_val
   cmd_vel = twist
   updated_val=twist
   
    
    

def init():
    gpio.wiringPiSetup()
    gpio.pinMode(8,1)
    gpio.pinMode(9,1)
    gpio.pinMode(7,1)
    gpio.pinMode(0,1)
    
def forward():
    init()
    gpio.digitalWrite(8,1)
    gpio.digitalWrite(9,0)
    gpio.digitalWrite(7,1)  	
    gpio.digitalWrite(0,0)
    print("forward")
   


def izquierda():
    init()
    gpio.digitalWrite(8,1)
    gpio.digitalWrite(9,0)
    gpio.digitalWrite(7,0)
    gpio.digitalWrite(0,0)
    print("right")
    
    


def stop():
    init()
    gpio.digitalWrite(8,0)
    gpio.digitalWrite(9,0)
    gpio.digitalWrite(7,0)
    gpio.digitalWrite(0,0)
    print("stop")


def derecha():
    init()
    gpio.digitalWrite(8,0)
    gpio.digitalWrite(9,0)
    gpio.digitalWrite(7,1)
    gpio.digitalWrite(0,0)
    print("left")
  
    


def backward():
    init()
    gpio.digitalWrite(8,0)
    gpio.digitalWrite(9,1)
    gpio.digitalWrite(7,0)
    gpio.digitalWrite(0,1)
    print("back")
 
    


def roverCallBack(cmd_vel):
  rospy.init_node('rover', anonymous=True)
  while(1):
      rospy.Subscriber('cmd_vel', Twist, callback)
      if(updated_val):
          print("updaded value found")
          cmd_vel=updated_val
      if(cmd_vel.linear.x >= 0.1 and cmd_vel.angular.z == 0):
         forward()

      elif(cmd_vel.linear.x == 0 and cmd_vel.angular.z >= 0.1):
         izquierda()

      elif(cmd_vel.linear.x == 0 and cmd_vel.angular.z == 0):
         izquierda()
      elif(cmd_vel.linear.x == 0 and cmd_vel.angular.z <= 0.1):
         derecha()
      elif(cmd_vel.linear.x <= 0.1 and cmd_vel.angular.z == 0):
         backward()
      else:
         stop()
      time.sleep(1)
     
     


roverCallBack(cmd_vel)  
 
   








     
