import RPi.GPIO as GPIO
import time
TRIG1=18
ECHO1=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
while True:
    print("distance measurement in progress")
    GPIO.output(TRIG1,False)
  
    
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG1,True)
    time.sleep(0.00001)
    GPIO.output(TRIG1,False)
    while GPIO.input(ECHO1)==0:
        pulse_start1=time.time()
    
    while GPIO.input(ECHO1)==1:
        pulse_end1=time.time()
    
    pulse_duration1=pulse_end1-pulse_start1
    
    distance=pulse_duration1*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    time.sleep(0.5)
