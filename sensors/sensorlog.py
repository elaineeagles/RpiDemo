import os
from threading import Thread
import urllib2
import random
import time
import RPi.GPIO as GPIO

#add sensor reading code here
def readSensor(sval):
	print("reading sensor ...")
        time.sleep(5)
	print(sval)
	myurl = "http://localhost/RPi/sensors/add_data.php?snum=1&sval="+str(sval)
	urllib2.urlopen(myurl).read()
	
# function to send data read from sensor to WebAPI
def sendDataToServer(pmode):
	if pmode == 1:
		GPIO.setmode(GPIO.BCM)
		INPUT_PIN = 27 
		GPIO.setup(INPUT_PIN, GPIO.IN)
        while True:
		if pmode == 1:
                	val=GPIO.input(INPUT_PIN)
			if val:
				readSensor(val) 
		else:
			readSensor(random.randint(1, 10))

#main part of program
pmode=1
sendDataToServer(pmode)
