from picamera import PiCamera
import time
import RPi.GPIO as GPIO

TRIG1=18
ECHO1=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)

record = False

def recording(x,y):
    
    camera = PiCamera()
    camera.resolution = (1920,1080)
    camera.vflip = True
    camera_record = False
    
    if (x == True):
        camera.start_preview()
        time.sleep(6)
        camera.start_recording("record.h264")
        time.sleep(6)
        camera_record = True
    elif (x == False):
        if (y == True):  
            camera.stop_preview      
            camera.stop_recording()
            camera_record = False
    return camera_record


def Distance(TRIG, ECHO):
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
    return distance

try:
    while True:
        dist1 = Distance(TRIG1,ECHO1)

        if dist1 < 20:
            x = True
            
        else:
            x = False
        record = recording(x,y=record)
            

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()


        

    
    

