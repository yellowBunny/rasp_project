import RPi.GPIO as GPIO
import sys
#sys.path.append('/home/pi/Desktop/examples/sensor_libs/MFRC522-python')
sys.path.append('/home/pi/Desktop/exp/MFRC522-python')
sys.path.append('/home/pi/Desktop/rasp_project')
import SimpleMFRC522
from time import sleep
from datetime import datetime
from csv_mod import Csv_mod

class Rfid():    
    reader = SimpleMFRC522.SimpleMFRC522()
    to_csv = Csv_mod()
    allarm_pin = 21
    door_pin = 20
    allow_to = {'seba': []}
    notallow_to = {}
    
    def __init__(self):
        self.set_pins()
        self.csv_configure()        
    
    def set_pins(self):        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.allarm_pin, GPIO.OUT)
        GPIO.setup(self.door_pin, GPIO.OUT)
        return 'Pin was set'
    
    def csv_configure(self,):        
        self.to_csv.path ='/home/pi/Desktop/entry_data_base.csv'
        self.to_csv.headers = ['id/name', 'date/time']
        return 'path and headets was set'
        

    def entries_time_data(self):
        '''grab time and date when someone will apply the card
            to rfid reader'''
        return datetime.now().strftime('%d-%m-%Y, %X')

    def read_card(self):
        '''card reader
            id - unique card id
            name - text writed in card maybe name/number/surname
            must be str type'''
        id, name = self.reader.read()
        if name:
            name = name.split()[-1]        
        print(id, '--->', name)
        print(type(id), type(name))
        return id, name

    def open_lock(self, name):
        '''open door/ lock when user in data base'''        
        self.to_csv.data = [name, self.entries_time_data()]
        self.to_csv.main()
        print('Otwarte')        
        GPIO.output(self.door_pin, 1)       
        sleep(3)
        GPIO.output(self.door_pin, 0)        
        return 0

    def warning(self, id, name, c):
        '''dont's allow to etry not difined person. When n/d person try
            five times'''
        self.to_csv.data = [str(id), self.entries_time_data()]
        self.to_csv.main()
        print(c)    
        print('Nieautoryzowane wejscie!!')
        GPIO.output(self.allarm_pin, 1)        
        if c >= 5:            
            print('ALLARM!!')
            sleep(5)
        sleep(.5)
        GPIO.output(self.allarm_pin, 0)    
        return 1            
    
    def let_in(self, name, id, c):
        if name in self.allow_to:
            self.open_lock(name)
            return 0
        else:
            self.warning(id, name, c)
            c += 1
            return c    
    
    def main(self):
        c = 0        
        try:        
            while True:
                print('Read mode')
                id, name = self.read_card()
                c = self.let_in(name, id, c)
                if c >5:
                    c = 0
                sleep(.5)
                
        except KeyboardInterrupt:
            GPIO.cleanup()        
            print('quit from program')
            
if __name__ == '__main__':
    start = Rfid()
    start.main()
