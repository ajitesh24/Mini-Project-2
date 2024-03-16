from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.vflip = True

camera.start_preview()
time.sleep(2)

camera.start_recording("my_movie.h264")
time.sleep(5)
camera.stop_recording()
