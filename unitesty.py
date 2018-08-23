import unittest 
from csv_mod import Csv_mod
import os
import csv

class Sensor_tests(unittest.TestCase):
    mod = Csv_mod()
    
    def test_simple_csv_test_write_func(self):
        '''write function test
            in first part we westing inherence file at desktop
            second part code check what is in file and compare writed data '''
        print(self.mod.__dict__)
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
    
    def test_all_raise_errors(self):
        errors = [FileNotFoundError, FileExistsError, ValueError]        
        for i, error in enumerate(errors):
            if i == 0:
                with self.assertRaises(error):
                    self.mod.raise_errors()
                    
            elif i == 1:
                self.mod.path = '/home/pi/Desktop/test.csv'
                with self.assertRaises(error):
                    self.mod.raise_errors()
                    
            elif i == 2:
                print('pierwszy')
                self.mod.headers = ['f1']
                with self.assertRaises(error):
                    self.mod.raise_errors()       
        
        
unittest.main()
    

