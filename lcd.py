import os
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from time import sleep
import sys

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(40,GPIO.OUT)

# lcd config
lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e = 16,pin_backlight=40, pins_data=[21,22, 23, 24],
              numbering_mode=GPIO.BOARD,charmap='A00',
              cols=16,rows=2,auto_linebreaks=False,
              backlight_mode='active_high')

def scroling_text(s):
        lcd.cursor_mode='hide'                                       
        for i in range(16):
                lcd.cursor_pos=(0,0) 
                lcd.write_string('hello {}'.format(sys.version[:7]))
                lcd.cursor_pos =(1,i)
                lcd.write_string(s)
                sleep(.5)
                lcd.clear()
                
                
l = ['SZYMON','IZA','SEBASTIAN']

for loop in l:        
        scroling_text('{}'.format(loop))
        
'''lcd.cursor_mode='blink'
lcd.cursor_pos=(0,0)
sleep(2)
lcd.cursor_pos=(1,0)
sleep(2)'''
'''
ver = sys.version[:7]
sleep(2)
lcd.write_string(ver)
sleep(5)
lcd.clear()
lcd.write_string('GO AWAY')
sleep(2)
lcd.clear()'''
GPIO.cleanup()
