import os
import threading
import urllib2
import random

#add sensor reading code here
def readSensor():
	global sval 
	sval = random.randint(0,5)
	
# function to send data read from sensor to WebAPI
def sendDataToServer():
	global sval

	threading.Timer(600,sendDataToServer).start()
	print("Sensing...")
	readSensor()
	print(sval)
	myurl = "http://localhost/RPi/sensors/add_data.php?snum=1&sval="+str(sval)
	urllib2.urlopen(myurl).read()

#main part of program
sendDataToServer()
