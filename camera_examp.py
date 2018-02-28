from picamera import PiCamera
from time import sleep

cam = PiCamera()

def rec(file_name):
    cam.resolution = (640, 480)
    cam.start_recording('/home/pi/Desktop/rec/{}.h264'.format(file_name))
    cam.wait_recording(3)
    cam.stop_recording()

def photo(file_name):
    cam.resolution = (1024,720)
    cam.vflip = True
    cam.start_preview()
    sleep(2)
    cam.capture('/home/pi/Desktop/rec/{}.jpg'.format(file_name))



photo('foto1')
