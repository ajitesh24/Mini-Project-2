import RPi.GPIO as GPIO
import dis_fun as d


TRIG = 18
ECHO = 17
TRIG1 = 23
ECHO1 = 22
d.setup(TRIG, ECHO)
d.setup(TRIG1, ECHO1)

while True:
	dist1 = d.Distance(TRIG, ECHO)
	dist2 = d.Distance(TRIG1, ECHO1)
	print(dist1)
	print(dist2)
