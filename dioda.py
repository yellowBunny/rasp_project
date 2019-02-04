import RPi.GPIO as GPIO
from time import sleep


def set_pin(pin, signal):
    '''Set pin on rpi controler'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, signal)
    
    

