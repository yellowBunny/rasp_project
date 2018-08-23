import csv

class Csv_mod():
    ''' Discription:
        This class is for append data to .csv file'''
    
    def __init__(self):
        '''before you start append to csv file first set:
           - path,
           - data (list of str)
           - fields_names (default set value are field1 field2)'''        
        
        self.path = ''
        self.data = ''        
        self.headers = ['field1','field2']              
    
    def write(self, path, data, headers):
        '''Write file to .csv file '''        
        try:
            with open(path, 'r') as f:
                c = 1
        except:
            c = 0
            
        with open(path, 'a') as file:                       
            csv_write = csv.DictWriter(file, fieldnames=headers)
            if not c:
                csv_write.writeheader()
            d = {key: val for key, val in zip(self.headers, data)}
            csv_write.writerow(d)
            print('data was writer')            
        return path.split('/')[-1]
    
    def raise_errors(self,):
        if len(self.headers) < 2:            
            raise ValueError('varible headers must be grater or equal 2')                     
        if not self.path:
            raise FileNotFoundError('path are not set')
        if not self.data:
            raise FileExistsError('data are not set')        
            
    def main(self):
        self.raise_errors()           
        print(self.write(self.path, self.data, self.headers))
        
        
                        
if __name__ == '__main__':
    start = Csv_mod()
    start.main()
