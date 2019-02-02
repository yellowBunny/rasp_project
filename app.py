import tkinter as tk
import datetime

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
    root = tk.Tk()
    root.geometry('600x400')
    root.title('home ster')
    ###FRAMES###
    frame_time = tk.Frame(master=root)
    frame_time.grid(row=0,column=2, stick='N')
    frame_other = tk.Frame(master=root)
    frame_other.grid(row=0)
    ### CURRENT TIME###
    CURRENT_TIME = datetime.datetime.now().time()
    ###CURRENT DATE###
    CURRENT_DATE = datetime.datetime.now().date()
    
    
    def __init__(self):
        self.wigets()
        self.update_time()
        
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
        ####OptionMenu####
        opt_men1 = MyOptionMenu(window=self.frame_other, title='godzina', n=24, font=fonts[0])
        opt_men1.grid(row=1,column=0)
        opt_men2 = MyOptionMenu(window=self.frame_other, title='minuta', n=60, font=fonts[1], flag=1)
        opt_men2.grid(row=1, column=1)
        opt_men3 = MyOptionMenu(window=self.frame_other, title='godzina', n=24, font=fonts[0])
        opt_men3.grid(row=2,column=0)
        opt_men4 = MyOptionMenu(window=self.frame_other, title='minuta', n=60, font=fonts[1], flag=1)
        opt_men4.grid(row=2,column=1)
        ###BUTTONS###
        b_set_time = tk.Button(self.frame_other, text='ustaw czas',
                               command=lambda: self.set_time(opt_men1, opt_men2, opt_men3, opt_men4))
        b_set_time.grid()
        
    def set_time(self, *arg):
        try:
            func = lambda arr: [int(obj.get_data()) for obj in arr]
            s_off_h, s_off_m, s_on_h, s_on_m= func(arg)
            time1= datetime.time(hour=s_off_h, minute=s_off_m)
            time2 = datetime.time(hour=s_on_h, minute=s_on_m)
        except ValueError:
            print('set all cells')
##        except:
##            print('other err')
        else:
            print(time1, time2)
            return time1, time2
         
        
    
    def update_time(self):
        time = datetime.datetime.now().time().strftime('%X')
        date = datetime.datetime.now().date().strftime('{}/{}/{}'.format('%d','%m','%y'))
        self.lb_show_date.config(text=date)     
        self.lb_show_time.config(text=time)
        self.root.after(1000, self.update_time)
    
start = MyApp()
start.root.mainloop()
    