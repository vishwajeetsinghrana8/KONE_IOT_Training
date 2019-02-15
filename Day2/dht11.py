import sys
import RPi.GPIO as GPIO
import os
import Adafruit_DHT
import urllib2
import smbus
import time
from ctypes import c_short

DHTpin = 17
key="T6EHZUTD1T96H80G"       # Enter your Write API key from ThingSpeak
GPIO.setmode(GPIO.BCM)
# Define GPIO to LCD mapping


def readDHT():
    humi, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
    return (str(int(humi)), str(int(temp)))

    
# main() function
def main():
    
    print 'System Ready...'
    URL = 'https://api.thingspeak.com/update?api_key=%s' % key
    print "Wait...."
    while True:
            (humi, temp)= readDHT()
            
            finalURL = URL +"&field1=%s&field2=%s"%(humi, temp)
            print finalURL
            s=urllib2.urlopen(finalURL);
            print  humi+ " " + temp + " "
            s.close()
            time.sleep(10)
            
     
if __name__=="__main__":
   main()
