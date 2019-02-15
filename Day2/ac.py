import serial
import RPi.GPIO as GPIO
import os, time
led1=17
#led2=27
#led3=22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
#GPIO.setup(led2, GPIO.OUT)
#GPIO.setup(led3, GPIO.OUT)
GPIO.output(led1 , 1)
#GPIO.output(led2 , 0)
#GPIO.output(led3 , 0)
Serial = serial.Serial("/dev/ttyAMA0", baudrate=38400, timeout=2)
data1=""
data=''
while 1:
  while data != '#':
    data = Serial.read(1)
    data1+=data
  print data1
  if data1.find("light on")>0:
      GPIO.output(led1 , 0)
      print "Light on"
  if data1.find("light off")>0:
      GPIO.output(led1 , 1)
      print "Light Off"
 # if data1.find("red light on")>0:
  #    GPIO.output(led2 , 1)
   #   print "Red Light on"
 # if data1.find("red light off")>0:
  #    GPIO.output(led2 , 0)
   #   print "red Light Off"
 # if data1.find("green light on")>0:
  #    GPIO.output(led3 , 1)
   #   print "Green Light on"
 # if data1.find("green light off")>0:
  #    GPIO.output(led3 , 0)
    #  print "Green Light Off"
 # if data1.find("all lights on")>0:
  #    GPIO.output(led1 , 1)
   #   GPIO.output(led2 , 1)
    #  GPIO.output(led3 , 1)
     # print "All Lights on"
  #if data1.find("all lights off")>0:
   #   GPIO.output(led1 , 0)
    #  GPIO.output(led2 , 0)
     # GPIO.output(led3 , 0)
     # print "All Light Off"
  if data1.find("blink")>0:
      for k in range (100):
        GPIO.output(led1 , 1)
  #      GPIO.output(led2 , 1)
   #     GPIO.output(led3 , 1)
        time.sleep(0.1)
        GPIO.output(led1 , 0)
    #    GPIO.output(led2 , 0)
     #   GPIO.output(led3 , 0)
 # if data1.find("all lights on")>0:
  #    GPIO.output(led1 , 1)
   #   GPIO.output(led2 , 1)
    #  GPIO.output(led3 , 1)
     # print "All Lights on"
  #if data1.find("all lights off")>0:
   #   GPIO.output(led1 , 0)
    #  GPIO.output(led2 , 0)
     # GPIO.output(led3 , 0)
     # print "All Light Off"
  if data1.find("blink")>0:
      for k in range (100):
        GPIO.output(led1 , 1)
  #      GPIO.output(led2 , 1)
   #     GPIO.output(led3 , 1)
        time.sleep(0.1)
        GPIO.output(led1 , 0)
    #    GPIO.output(led2 , 0)
     #   GPIO.output(led3 , 0)
        time.sleep(0.1)

  Serial.flush();
  data="";
  data1="";


