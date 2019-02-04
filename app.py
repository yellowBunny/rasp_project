import tkinter as tk
import datetime
from dioda import set_pin as pin
import random

class MyListBox(tk.Listbox):
    def __init__(self, window, n, width, height):
        tk.Listbox.__init(self, master=window, width=width, height=height)
        for i in range(n):
            self.insert(i,i)
            

class MyOptionMenu(tk.OptionMenu):
    def __init__(self, window, title, n, font, flag=0):
        self.var = tk.StringVar()
        self.var.set(title)
        if flag:
            content = (num for num in range(n) if not num % 5)
        else:
            content = range(n)
        tk.OptionMenu.__init__(self, window, self.var, *content)
        self.config(font=font)
        self['menu'].config(font=font)
        
    def get_data(self):
        return self.var.get()
        
class MyButtons(tk.Button):
    def __init__(self, window, title, command):
        pass

class MyApp:
    '''DESCRYPTION
\t\tWindow steering for turn 'ON' and turn 'OFF' any kind of devices'''
    root = tk.Tk()
    root.geometry('600x400')
    root.title('home ster')
    ###FRAMES###
    frame_time = tk.Frame(master=root)
    frame_time.grid(row=0,column=2, stick='N')
    frame_other = tk.Frame(master=root)
    frame_other.grid(row=0)
    PIN_SOCKETS = 21
    ###TEMP PINS###
    PIN_OUTSIDE = 12
    PIN_SALON = 26
    PIN_POKOJ1 = 20
    temp_container = [0,0]
    
    def __init__(self):
        self.main()
        
        
    def wigets(self):
        fonts = [('Arial', 10),('Arial', 8)]
        ###LABELS###
        lb1 = tk.Label(master=self.frame_other, text='Ustaw godzine')
        lb1.grid(row=0, column = 0)
        lb2 = tk.Label(master=self.frame_other, text='Ustaw minute')
        lb2.grid(row=0,column=1)
        self.lb_show_time = tk.Label(master=self.frame_time, text='time', font=('Arial',18), fg='blue')
        self.lb_show_time.grid(row=0, column=2, stick='E')
        self.lb_show_date = tk.Label(master=self.frame_time, text='date', font=('Arial',18), fg='green')
        self.lb_show_date.grid(row=1, column=2, stick='E')
        self.lb_show_status = tk.Label(master=self.frame_other, text = 'status')
        self.lb_show_status.grid(row=5, column=0)
        ###TEMP LABELS###
        ##view rooms##
        self.view_room1 = tk.Label(master=self.frame_other, text='Na zewnatrz: ')
        self.view_room1.grid(row=1, column=3)
        self.view_room2 = tk.Label(master=self.frame_other, text='Salon: ')
        self.view_room2.grid(row=2, column=3)
        self.view_room3 = tk.Label(master=self.frame_other, text='Pokoj 1: ')
        self.view_room3.grid(row=3, column=3)
        self.view_room4 = tk.Label(master=self.frame_other, text='Pokoj 2: ')
        self.view_room4.grid(row=4, column=3)
        self.view_room5 = tk.Label(master=self.frame_other, text='Kuchnia: ')
        self.view_room5.grid(row=5, column=3)
        self.view_room6 = tk.Label(master=self.frame_other, text='Łazienka: ')
        self.view_room6.grid(row=6, column=3)
        ##view temp in rooms##
        self.view_temp1 = tk.Label(master=self.frame_other, text='temp1')
        self.view_temp1.grid(row=1, column=4)
        self.view_temp2 = tk.Label(master=self.frame_other, text='temp2 ')
        self.view_temp2.grid(row=2, column=4)
        self.view_temp3 = tk.Label(master=self.frame_other, text='temp3 ')
        self.view_temp3.grid(row=3, column=4)
        self.view_temp4 = tk.Label(master=self.frame_other, text='temp4 ')
        self.view_temp4.grid(row=4, column=4)
        self.view_temp5 = tk.Label(master=self.frame_other, text='temp5 ')
        self.view_temp5.grid(row=5, column=4)
        self.view_temp6 = tk.Label(master=self.frame_other, text='temp6 ')
        self.view_temp6.grid(row=6, column=4)   
        
        
        ####OptionMenu####
        self.opt_men1 = MyOptionMenu(window=self.frame_other, title='godzina', n=24, font=fonts[0])
        self.opt_men1.grid(row=1,column=0)
        self.opt_men2 = MyOptionMenu(window=self.frame_other, title='minuta', n=60, font=fonts[1], flag=1)
        self.opt_men2.grid(row=1, column=1)
        self.opt_men3 = MyOptionMenu(window=self.frame_other, title='godzina', n=24, font=fonts[0])
        self.opt_men3.grid(row=2,column=0)
        self.opt_men4 = MyOptionMenu(window=self.frame_other, title='minuta', n=60, font=fonts[1], flag=1)
        self.opt_men4.grid(row=2,column=1)
        ###BUTTONS###
##        b_set_time = tk.Button(self.frame_other, text='Ustaw czas',
##                               command=lambda: self.set_time(self.opt_men1, self.opt_men2, self.opt_men3, self.opt_men4))
##        b_set_time.grid(row=4,column=0)   
   
        
    def set_time(self, *arg):
        '''Arguments this function are four OptionMenus with selected data hours ON, OFF relay and minutes ON, OFF relay.
            This fnction convert input data as int to two datetime.time class in tuple'''
        try:
            func = lambda arr: [int(obj.get_data()) for obj in arr]
            s_off_h, s_off_m, s_on_h, s_on_m= func(arg)
            time1= datetime.time(hour=s_off_h, minute=s_off_m)
            time2 = datetime.time(hour=s_on_h, minute=s_on_m)
            self.lb_show_status.config(text='Gniazda OFF {}\nGniazda ON {}'.format(time1, time2), font=('Arial', 12), fg='green')            
        except ValueError:            
            self.lb_show_status.config(text='uzupełnij pola', fg='red')
            return 0,0
        except:
            print('Other err in set_time!!')
            pass
        else:            
            return time1, time2        
        
    def time_swith_func(self, current_time, shut_down, swith_on):
        '''this function swith releay to on and off depends on given arg.
            shut_down - given time in hours e.g 1:00 to open circuit
            swith_on - given time in hours e.g. 7:00 to close circuit
            (open circuit - sockets in room are without current otherwise sockets are on voltage)'''
##        print(current_time, shut_down, swith_on)        
        try:
            if shut_down <= current_time <= swith_on:
                status = 1
                print(status)
                pin(self.PIN_SOCKETS,status)
                return True
            else:
                status = 0
                print(status)
                pin(self.PIN_SOCKETS,status)
                return False
        except TypeError:
            print('ustaw poprawnie czas')
            pass
        except Exception as err:
            print('other err in:\n{}==> {}'.format(self.time_swith_func.__name__, err))           
      
    
    def update_time(self):
        '''This function update root window with content'''
        ###Curent time in datetime class###
        time = datetime.datetime.now().time()
        ###Current date in str###
        date = datetime.datetime.now().date().strftime('{}/{}/{}'.format('%d','%m','%Y'))
        ###config time labels###
        self.lb_show_date.config(text=date)     
        self.lb_show_time.config(text=time.strftime('%X'))
        ##confg socket switches##
        time_off, time_on = self.set_time(self.opt_men1, self.opt_men2, self.opt_men3, self.opt_men4)        
        self.time_swith_func(time, time_off, time_on)
        #try read temp
        self.insert_to_temp_container(time)
        ###Update root window delay 1s###
        self.root.after(1000, self.update_time)
        
    def outside_func(self):
        'to read temp from module'
        return random.randint(0,100)
    
    def insert_to_temp_container(self,time):
        '''This function insert to container reded temperature with deleay between temp sensors'''
        print(time.strftime('%X'))
        if time.second == 0:
            print(time.second,'ds18b20')
            ds18b20 = self.outside_func()
            print('zapisano {}'.format(ds18b20))
            self.temp_container[0] = ds18b20
            print(self.temp_container)
        elif time.second == 5:
            print(time.second,'dth11')
            dht11 = self.outside_func()
            print('zapisano {}'.format(dht11))
            self.temp_container[1] = dht11            
            print(self.temp_container)
        self.f(self.view_temp1, self.view_temp2)
            
    def f(self,*labels):
        #print(labels)
        for temp, lb in zip(self.temp_container, labels):
            lb.config(text='{} C'.format(temp))
            
        
        
    
        
    def main(self):
        self.wigets()
        self.update_time()
    
        
        
start = MyApp()
start.root.mainloop()
    