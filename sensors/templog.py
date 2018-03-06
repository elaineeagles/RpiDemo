import os
from threading import Thread
import Adafruit_DHT
import requests
import random
import time

#add sensor reading code here
def readSensor(sval):
	print("reading sensor ...")
	time.sleep(5)
	print(sval)
	#myurl = "http://localhost/RPi/sensors/add_data.php?snum=1&sval="+str(sval)
	#urllib3.urlopen(myurl).read()
	sval = str(sval)
	sval = sval.rstrip('%')
	r = requests.post('http://localhost/RPi/sensors/add_temp.php', data={'snum':1, 'sval':sval})
	print(r.text)
	
# function to send data read from sensor to WebAPI
def sendDataToServer(pmode):
	if pmode == 1:
		sensor = Adafruit_DHT.DHT11
		gpio=27 
		while True:
			if pmode == 1:
				humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
				if humidity is not None and temperature is not None:
					print ('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
				else:
					print ('Failed to get reading, try again!')
			if temperature:
				readSensor(humidity) 
			else:
				readSensor(random.randint(1, 10))

#main part of program
pmode=1
sendDataToServer(pmode)
