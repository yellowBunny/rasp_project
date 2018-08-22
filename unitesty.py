import unittest 
from csv_mod import Csv_mod
import os
import csv

class Sensor_tests(unittest.TestCase):
    
    def test_simple_csv_test_write_func(self):
        sample_path = '/home/pi/Desktop/test.csv'
        data = ['third', 'fourth']
        headers = Csv_mod().headers
        func = Csv_mod().write(sample_path, data, headers)        
        dict_with_saved_data = {key : val for key, val in zip(headers, data)}
        
        file_localization = '/'.join(s for s in sample_path.split('/')[:-1])
        self.assertIn(func, os.listdir(file_localization))
        
        with open(sample_path, 'r') as file:
            csv_read = csv.DictReader(file)
            for line in csv_read:
                print(dict_with_saved_data)
                print(line)
                self.assertEqual(line, dict_with_saved_data, 'should be {} is {}'.format(dict_with_saved_data, line))
                if line == dict_with_saved_data:
                    print('ok')
                else:
                    print('wrong')
                    
unittest.main()
    

