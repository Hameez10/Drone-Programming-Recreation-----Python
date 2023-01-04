"""
Names: Hameez Iqbal, Benjamin Ouellet, Admir Halilovic, Rafay Khan
Date: Sunday, June 5, 2022
Drone: EE5214

Connect to drone through wifi
"""

#Import Statements
from djitellopy import Tello
from time import sleep #delay between commands

#Create tello object
me = tello.Tello()
me.connect()
print(me.get_battery())

#Commands
me.streamon()

while True:
	img = me.get_frame_read().frame 
	#img = cv2.resize(img.(360, 240))
	ev2.imshow("image", img) #Dsiplay
	cv2.waitKey(1) #Otherwise it wil close