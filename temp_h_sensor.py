import Adafruit_DHT
from datetime import datetime 


def start(pin):
    # set date
    date = datetime.now().strftime('%d-%m-%Y, %X')
    # set gpio BCM pin pin  is inpoted arg in func
    
    # set sensor DHT11
    sensor = Adafruit_DHT.DHT11
    # set temp and humanidity
    humanidity, temp = Adafruit_DHT.read_retry(sensor, pin)
    print('date: {}\ntemp: {} C\nhumanidity: {} %'.format(date,temp, humanidity))    
    return temp, humanidity, date

if __name__ =='__main__':
    print(start(16))