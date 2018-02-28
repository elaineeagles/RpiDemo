import os
from threading import Thread
import urllib2
import random
import time

#add sensor reading code here
def readSensor():
        sval = 0
	print("Sensing...")
	sval = random.randint(1,5)
        #time.sleep(5)
	print(sval)
	myurl = "http://localhost/RPi/sensors/add_data.php?snum=1&sval="+str(sval)
	urllib2.urlopen(myurl).read()
	
# function to send data read from sensor to WebAPI
def sendDataToServer():
        for i in range (10):
	 	t = Thread(target=readSensor, args=())	
                t.start()

#main part of program
sendDataToServer()
