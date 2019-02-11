import Adafruit_DHT
from datetime import datetime 

class PinConectionError(Exception):
    def __ini__(self,mgs):
        Exception.__init__(self,mgs)
        
class DHT11:    
    def grab_temp(self, pin=0):
        if pin:                
            # set sensor DHT11        
            sensor = Adafruit_DHT.DHT11
            # set temp and humanidity
            humanidity, temp = Adafruit_DHT.read_retry(sensor, pin)
            print('temp: {} C\nhumanidity: {} %'.format(temp, humanidity))
            return temp, humanidity        
        else:
            print('Set Pin!!')
            raise PinConectionError('Check GPIO pin connection and try again')
            
            

if __name__ =='__main__':
    instance = DHT11()
    instance.grab_temp(1)
##    instance.grab_temp(16)
##    instance.grab_temp(12)