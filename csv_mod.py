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
        self.fields_names = ['field1', 'field2']
        self.main()       
    
    def write(self, path, data):
        '''Write file to .csv file '''
        try:
            with open(path, 'r') as f:
                c = 1
        except:
            c = 0
            
        with open(self.path, 'a') as file:                       
            csv_write = csv.DictWriter(file, fieldnames=self.fields_names)
            if not c:
                csv_write.writeheader()
            d = {key: val for key, val in zip(self.fields_names, self.data)}
            csv_write.writerow(d)
            print('data was writer')
            
    def main(self):        
        if len(self.fields_names) < 2:
            print('append header to filed_names')
        else:
            if self.path and self.data:
                print(self.write(self.path, self.data))
            else:
                print('set path and data')
                        
##if __name__ == '__main__':
##    pass
##path = '/home/pi/Desktop/czesc.csv'
##data = ['131245123', 'cokolwiek']
##start = Csv_mod(path, data)
