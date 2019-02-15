import serial
import RPi.GPIO as GPIO

led1=17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)



Serial = serial.Serial("/dev/ttyAMA0", baudrate=38400, timeout=2)
data1=""
data=''
while 1:
        data = Serial.read(1)
        data1+=data
        print data
	if data == 'a':
		GPIO.output(led1,False)
		print('BULB on')

	if data == 'b':
		GPIO.output(led1,True)
		print('BULB off')

        Serial.flush();
        data="";
        data1="";
