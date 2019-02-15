import time
import urllib
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
while True:
	url = "http://knowledgeshelf.in/test.php"
	response = urllib.urlopen(url).read()
	print(response)
	print(type(response))
	if int(response) == 1 :
		GPIO.output(17,True)
		print('on')
	else:
		GPIO.output(17,False)
