import tkinter as tk
import datetime
from dioda import set_pin as pin
import random
import temp_sensor as temp_ds, temp_h_sensor as temp_dht

class MyListBox(tk.Listbox):
    def __init__(self, window, n, width, height):
        tk.Listbox.__init__(self, master=window, width=width, height=height)
        for i in range(n):
            self.insert(i,i)
            

class MyOptionMenu(tk.OptionMenu):
    def __init__(self, window, title, n, font, flag=0, color='alice blue'):
        self.var = tk.StringVar()
        self.var.set(title)
        if flag:
            content = (num for num in range(n) if not num % 5)
        else:
            content = self.is_tuple(n)
        tk.OptionMenu.__init__(self, window, self.var, *content)
        self.config(font=font, bg=color)
        self['menu'].config(font=font, bg=color)
        
    def get_data(self):
        return self.var.get()

    def is_tuple(self, n):
        if type(n) is tuple:
            start, stop = n
            # print('tuple')
            return range(start, stop)
        else:
            # print('not tuple')
            return range(n)

        
class MyButtons(tk.Button):
    def __init__(self, window, title, command):
        pass

class MyApp:
    '''DESCRYPTION
\t\tWindow steering for turn 'ON' and turn 'OFF' any kind of devices'''
    root = tk.Tk()
    root.geometry('600x400')
    root.title('Home Steering')
    ###FRAMES###
    frame_time = tk.Frame(master=root)
    frame_time.grid(row=0,column=2, stick='N')
    frame_other = tk.Frame(master=root)
    frame_other.grid(row=0)
    PIN_SOCKETS = 14
    ###TEMP PINS###
    PIN_OUTSIDE = 4 #0
    PIN_SALON = 7   #1
    PIN_POKOJ1 = 12 #2
    PIN_KUCHNIA = 16 #3
    PIN_POKOJ2 = 20  #4     
    PIN_WC = 8 #5
    ###HETERS PINS###
    PIN_HEATER1 = 13
    PIN_HEATER2 = 19
    PIN_HEATER3 = 26
    ###COLORS###
    HOT = 'tomato'
    COLD = 'light sky blue'
    ###KEEP CURENT TEMPERATURE IN ROOMS where look abowe###
    temp_container = [0,0,0,0,0,0]
    
    def __init__(self):
        self.main()
        
    def wigets(self):
        fonts = [('Arial', 10),('Arial', 8)]
        ###LABELS###
        lb1 = tk.Label(master=self.frame_other, text='Godziny')
        lb1.grid(row=0, column = 0)
        lb2 = tk.Label(master=self.frame_other, text='Minuty')
        lb2.grid(row=0,column=1)
        self.lb_show_time = tk.Label(master=self.frame_time, text='time', font=('Arial',18), fg='blue2')
        self.lb_show_time.grid(row=0, column=0, stick='W')
        self.lb_show_date = tk.Label(master=self.frame_time, text='date', font=('Arial',18), fg='purple3')
        self.lb_show_date.grid(row=1, column=0, stick='W')
        self.lb_show_status = tk.Label(master=self.frame_other, text = 'status')
        self.lb_show_status.grid(row=5, column=0,columnspan=2, stick='W')
        ###TEMP LABELS###
        ##view rooms##
        self.view_room1 = tk.Label(master=self.frame_other, text='Na zewnatrz: ', font=('Arial',10,'bold'))
        self.view_room1.grid(row=1, column=3)
        self.view_room2 = tk.Label(master=self.frame_other, text='Salon: ', font=('Arial',10,'bold'))
        self.view_room2.grid(row=2, column=3)
        self.view_room3 = tk.Label(master=self.frame_other, text='Pokoj 1: ', font=('Arial',10,'bold'))
        self.view_room3.grid(row=3, column=3)
        self.view_room4 = tk.Label(master=self.frame_other, text='Kuchnia: ', font=('Arial',10,'bold'))
        self.view_room4.grid(row=4, column=3)
        self.view_room5 = tk.Label(master=self.frame_other, text='Pokoj 2 ', font=('Arial',10,'bold'))
        self.view_room5.grid(row=5, column=3)
        self.view_room6 = tk.Label(master=self.frame_other, text='Łazienka: ', font=('Arial',10,'bold'))
        self.view_room6.grid(row=6, column=3)
        ##view temp in rooms##
        self.view_temp1 = tk.Label(master=self.frame_other, text='temp1')
        self.view_temp1.grid(row=1, column=4)
        self.view_temp2 = tk.Label(master=self.frame_other, text='temp2')
        self.view_temp2.grid(row=2, column=4)
        self.view_temp3 = tk.Label(master=self.frame_other, text='temp3')
        self.view_temp3.grid(row=3, column=4)
        self.view_temp4 = tk.Label(master=self.frame_other, text='temp4')
        self.view_temp4.grid(row=4, column=4)
        self.view_temp5 = tk.Label(master=self.frame_other, text='temp5')
        self.view_temp5.grid(row=5, column=4)
        self.view_temp6 = tk.Label(master=self.frame_other, text='None')
        self.view_temp6.grid(row=6, column=4)
        ##view seted temperature in each room##
        self.view_seted_temp = tk.Label(master=self.frame_time,
                                        text='Ustawienie\nSalon: {}\nPokój1: {}\nKuchnia: {}'.format('n/a','n/a','n/a'), font= fonts[0])
        self.view_seted_temp.grid(row=3, column=0, stick='W')
        
        
        ####OPTIONMENU####
        ##choose time to switch on/off sockets##
        self.opt_men1 = MyOptionMenu(window=self.frame_other, title='godzina', n=24, font=fonts[0])
        self.opt_men1.grid(row=1,column=0)
        self.opt_men2 = MyOptionMenu(window=self.frame_other, title='minuta', n=60, font=fonts[1], flag=1)
        self.opt_men2.grid(row=1, column=1)
        self.opt_men3 = MyOptionMenu(window=self.frame_other, title='godzina', n=24, font=fonts[0])
        self.opt_men3.grid(row=2,column=0)
        self.opt_men4 = MyOptionMenu(window=self.frame_other, title='minuta', n=60, font=fonts[1], flag=1)
        self.opt_men4.grid(row=2,column=1)
        ##choose temperature when heaters valve turn on or turn off
        temp_range = (19,30)
        self.opt_heater1 = MyOptionMenu(window=self.frame_other, title='salon', n=temp_range, font=fonts[1])
        self.opt_heater1.grid(row=2, column=5)
        self.opt_heater2 = MyOptionMenu(window=self.frame_other, title='Pokój1', n=temp_range, font=fonts[1])
        self.opt_heater2.grid(row=3,column=5)
        self.opt_heater3 = MyOptionMenu(window=self.frame_other,
                                        title='Kuchnia', n=temp_range, font=fonts[1])
        self.opt_heater3.grid(row=4, column=5)

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
            self.lb_show_status.config(text='Gniazda:\nOFF {}\nON {}'.format(time1, time2), font=('Arial', 12), fg='green')            
        except ValueError:            
            self.lb_show_status.config(text='Ustaw czas!', fg='red', font=('Arial', 14))
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
##                print(status)
                #pin(self.PIN_SOCKETS,status)
                return True
            else:
                status = 0
##                print(status)
                #pin(self.PIN_SOCKETS,status)
                return False
        except TypeError:
            # print('ustaw poprawnie czas')
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
        #reads temp and update temp_container
        self.insert_to_temp_container(time)
        #reads seted temp from optionmenus
        self.get_temp_from_bars(self.opt_heater1, self.opt_heater2, self.opt_heater3)
        ###Update root window delay 1s###
        self.root.after(1000, self.update_time)
        
    def outside_ds18b20(self):
        'to read temp from module'
        print('ds18b20 here')
        instance = temp_ds.DS18b20()        
        return instance.grab_temp()[0] # brackets is responsible for sensor applay to pin gpio 4

    def outside_DHT11(self, pin):
        print('DHT11 here is pin{}'.format(pin))
        instance = temp_dht.DHT11()        
        return instance.grab_temp(pin) #when we  have brackets here method grab_temp return only temp. In other case return tuple with temperature na humanidity
    
    def sensor_n_c_func(self, pin):
        print('pin {} is not connected to sensor'.format(pin))
        return 'N/C'

    def insert_to_temp_container(self, time):
        '''this function insert readed temperature for sensor to list called temp_container.
        after time is updated every 10 second temperature is readed by two functions:
        func to read ds18b20 sensor - two first cells in list [:2]
        func to read dht11 sensor -  other cells [2:]'''
        print(time.second)
        pins = [self.PIN_OUTSIDE, self.PIN_SALON, self.PIN_POKOJ1, self.PIN_KUCHNIA, self.PIN_POKOJ2, self.PIN_WC]
        f = lambda t: int(t * .1) if t * .1 % 1 == 0 else -1
        is_tenth = f(time.second)
        if is_tenth == 0:            
            ds18b20 = self.outside_ds18b20()
            self.temp_container[is_tenth] = ds18b20
            # print(self.temp_container)
        elif 0 < is_tenth < 4:            
            dht11 = self.outside_DHT11(pins[is_tenth])
            self.temp_container[is_tenth] = dht11
            # print(self.temp_container)        
        elif 4 <= is_tenth < 6:            
            n_c = self.sensor_n_c_func(pins[is_tenth])
            self.temp_container[is_tenth] = n_c
            
        self.update_labels_with_temp(self.view_temp1, self.view_temp2, self.view_temp3,
                                     self.view_temp4, self.view_temp5, self.view_temp6)

            
    def update_labels_with_temp(self,*labels):        
        for arr, lb in zip(self.temp_container, labels):
            if type(arr) != tuple:
                lb.config(text='{} {}C'.format(arr, chr(186))) #chr(186) - stopni (degrees)
            else:
                temp, humanidity = arr                
                lb.config(text='{} {}C {} %'.format(temp, chr(186), humanidity))

    def get_temp_from_bars(self, *arg):
        '''This function reads seted temp form optmenus and return list with int temperature.
        Second step this finction is config label wiget responslible for viwe seted temp'''
        try:
            container = [int(opt.get_data()) for opt in arg]
            salon, room1, kitchen = container
            self.view_seted_temp.config(
                text='Ustawienie\nSalon: {}\nPokój1: {}\nKuchnia: {}'.format(salon,room1,kitchen), fg='green')
            self.compare_two_temps(container, ['pin1','pin2','pin3'],
                                   self.opt_heater1, self.opt_heater2, self.opt_heater3)
        except ValueError as err:
            # print('ustaw temperature', err)
            self.view_seted_temp.config(
                text='Ustaw temperature!', fg='red', font=('Arial', 14))
        else:
            return container

    def compare_two_temps(self, seted_temps, pin_list, *optmenus):
        '''This function compare readed temperature form sensor nad seted temperature from optmenus.
        Next turn turn on or off relay to "TERMOSTAT" in heater.
        In next step config optmenus bars e.g change bg clor'''
        #temperature form main container#
        temp_from_sensors = self.temp_container[1:4]
        heaters_pins = [self.PIN_HEATER1, self.PIN_HEATER2, self.PIN_HEATER3]
        for sensor_temp, seted_temp, s_pin, heat_pin, opt_m in zip(temp_from_sensors, seted_temps, pin_list, heaters_pins,optmenus):
            if type(sensor_temp) != tuple:
                try:                    
                    if sensor_temp <= seted_temp:
                        status = 1
##                        print('for {} status {}'.format(s_pin, status))
                        opt_m.config(bg=self.HOT)
                    else:
                        status = 0
##                        print('for {} status {}'.format(s_pin, status))
                        opt_m.config(bg=self.COLD)
                        
                except TypeError as err:
                    print(err,'temperatura nie została podana jako int')
            else:
                if sensor_temp[0] <= seted_temp:
                    status = 1
##                    print('for {} status {}'.format(s_pin, status))
                    opt_m.config(bg=self.HOT)
##                    print(heat_pin)
                    pin(heat_pin, status)
                else:
                    status = 0
##                    print('for {} status {}'.format(s_pin, status))
                    opt_m.config(bg=self.COLD)
##                    print(heat_pin)
                    pin(heat_pin, status)
            
                    
        
    def main(self):
        self.wigets()
        self.update_time()
    
        
if __name__ == '__main__':
    start = MyApp()
    start.root.mainloop()
    