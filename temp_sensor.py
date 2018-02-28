import re
from time import sleep
import os
import sys
print('lib imported: {}'.format(re.__name__))



def sensor_id_as_dict(names=['a','b','c']):
# shown in dict conndected sensor in circuit
# names - how to we want names a chosen sensor
    try:    
        soup = os.listdir('/sys/devices/w1_bus_master1/')
        sensors = ['/sys/bus/w1/devices/{}/w1_slave'.format(p) for p in soup if
                   re.search(r'\d+[-]\d+',p)]            
        d = {names:sensors for names,sensors in zip(names,sensors)}
    except:
        print('err')        
        return False    
    else:
        if not d:
            print('sensor not detected')
            sys.exit()
        return d


def sensor_path():
# sensors paths in list
    try:
        soup = os.listdir('/sys/devices/w1_bus_master1/')
        sensors = ['/sys/bus/w1/devices/{}/w1_slave'.format(p) for p in soup if
                   re.search(r'\d+[-]\d+',p)]
    except:
        print('err')
        return False
    
    else:
        if not sensors:
            print('any snensor not detected')
            sys.exit()        
        return sensors    


def read_temp(path='',name=''):    
#Reading temp in Celsius degree, return temp in float   
    if not path:
        print('sensor not detected')
        return False
    
    with open(path,'r') as file:        
            lista = file.readlines()
            temp = lista[1].strip().split()[-1]
            temp = round(float(re.search(r'\d+',temp).group())/1000,2)
            print('Temperatura {} C - {}'.format(temp,name))
            
    return temp

#main
if __name__ == '__main__':
    #print(read_temp(sensor_path()[2]))
    sensors = sensor_id_as_dict(['duzy pokoj','balkon','duzy pokoj 2'])
    print(sensors)
    while 1:
            for name in sensors:      
                print(read_temp(sensors[name],name))
            sleep(1)
        
        
        

