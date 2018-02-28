import RPi.GPIO as GPIO
from time import sleep
pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)
try:
    while 1:
        
        if not GPIO.input(pin):
            print('alarm ktoś wszedł')
        else:
            print('clean')
        
        sleep(.1)
except KeyboardInterrupt:
    print('exit form app')
    


