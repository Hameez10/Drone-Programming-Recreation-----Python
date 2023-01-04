"""
Names: Hameez Iqbal, Benjamin Ouellet, Admir Halilovic, Rafay Khan
Date: Thursday, June 2, 2022
Drone: EE5214
Drone: EE529A

Connect to drone through wifi
"""

#Import Statements
from djitellopy import tello
from time import sleep #delay between commands

#Create tello object
me = tello.Tello()
me.connect()

#Print Statements
print(me.get_battery())#print battery percentage


#Commands
me.send_rc_control(0, 0, 0, 0) #set zero
"""
Velocity: left-right, forward-backward, up-down, 
yaw
-100 to 100
"""
me.send_rc_control(0, 50, 0, 0) #Edit this command
sleep(2)
me.send_rc_control(0, 0, 0, 0) #Prevent it fromg going forward when landing
me.land()