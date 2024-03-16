import RPi.GPIO as GPIO
import time

# Set the GPIO pins for the ultrasonic sensors    
SENSOR_1_TRIGGER_PIN = 17
SENSOR_1_ECHO_PIN = 18
SENSOR_2_TRIGGER_PIN = 27
SENSOR_2_ECHO_PIN = 22
print('Sensor setup')
# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SENSOR_1_TRIGGER_PIN, GPIO.OUT)
GPIO.setup(SENSOR_1_ECHO_PIN, GPIO.IN)
GPIO.setup(SENSOR_2_TRIGGER_PIN, GPIO.OUT)
GPIO.setup(SENSOR_2_ECHO_PIN, GPIO.IN)

# Function to measure distance from an ultrasonic sensor
def distance(trig_pin, echo_pin):
    # Send a 10us pulse to trigger the sensor
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)

    # Measure the time it takes for the echo pulse to return
    pulse_start = time.time()
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()
    pulse_end = time.time()
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    # Calculate the distance based on the time and the speed of sound
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance

# Initialize the counters
counter_1 = 0
counter_2 = 0

try:
    while True:
        # Measure the distance from each sensor
        distance_1 = distance(SENSOR_1_TRIGGER_PIN, SENSOR_1_ECHO_PIN)
        distance_2 = distance(SENSOR_2_TRIGGER_PIN, SENSOR_2_ECHO_PIN)
        print(distance_1)
        print(distance_2)

        # If an object is detected by sensor 1, increment counter 1
        if distance_1 < 30:
            counter_1 += 1
            print("Counter 1: ", counter_1)

        # If an object is detected by sensor 2, increment counter 2
        if distance_2 < 30:
            counter_2 += 1
            print("Counter 2: ", counter_2)

        # Pause for 0.1 seconds before checking again
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up the GPIO pins on exit
    GPIO.cleanup()
