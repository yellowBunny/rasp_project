import Adafruit_DHT
from datetime import datetime 

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
            raise ValueError
            
            

if __name__ =='__main__':
    instance = DHT11()
    instance.grab_temp(20)