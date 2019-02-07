import re
from time import sleep
import os
import sys

class DS18b20:        
    def sensor_id_and_directory(self):
        '''This  method finds id's sensors saved as directory.
            Each sensor with his directory is saved in list if is exist, otherwise method return False'''        
        try:    
            file_list = os.listdir('/sys/devices/w1_bus_master1/')            
            sensors_list = ['/sys/bus/w1/devices/{}/w1_slave'.format(p) for p in file_list if
                       re.search(r'[1-9]+[-]\d+',p)]          
        except Exception as err:
            print('Some err in {} {}'.function('sensor_id_and_directory', err))
            return False    
        else:
            if sensors_list:
                #nedded sort data
##                print(sensors_list)
                return sensors_list                
            else:
                print('sensor not detected')
                return False   

    def read_temp(self, path='',name=''):    
        '''Reading temp in Celsius degree, return temp in float'''
        with open(path,'r') as file:        
                lista = file.readlines()
                temp = lista[1].strip().split()[-1]
                temp = round(float(re.search(r'\d+',temp).group())/1000,1)
##                print('Temperatura {} C'.format(temp))                
        return temp    
    
    def grab_temp(self):        
        directory_container = self.sensor_id_and_directory()
##        print(directory_container)
        return [self.read_temp(sensor_dir) for sensor_dir in directory_container]

    
#main
if __name__ == '__main__':
    #print(read_temp(sensor_path()[2]))
    read = DS18b20()
    
        
        
        

