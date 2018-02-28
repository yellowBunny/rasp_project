import  RPi.GPIO as GPIO
from time import sleep
# chose pin
pin = 21

GPIO.setmode(GPIO.BCM)
#set pin
GPIO.setup(pin,GPIO.OUT)


# servo moves
def turn2(move):
        GPIO.output(pin,GPIO.HIGH)
        sleep(move)
        GPIO.output(pin,GPIO.LOW)
        
def center():
        for loop in range(10):
                turn2(.0015)
                sleep(.1)
        
        
#times in ms        
t = [.0015,.0028,.0005]

# freez time stop move camera to freez  n second
freez = 3

def constant_moves():
        move = .0023
        try:                
                while 1:                        
                        #print(round(move,4))
                        turn2(round(move,4))
                        sleep(freez)
                        move-=.0002        
                        if move <.0003:
                                for loop in range(10):
                                        #print(round(move,4))
                                        move+=.0002
                                        turn2(round(move,4))
                                        sleep(freez)
        except KeyboardInterrupt:
                pass
                                     
def insert_and_move(x):            
        
        #turn left
        if x == 'a':
                turn2(t[1])
        #turn right                        
        elif x =='d':
                turn2(t[2])
        # center servo                       
        elif x == 'c':
                center()
        else:                
                print('pressed other key other than "a" or "d"')

#main
while 1:
        user = input('Wybierz opcje :\n1-Sam kierujesz\n2-Ruch ciagly\ne-exit\n : ')
        if user == '1':
                while 1:
                        x = input('Wpisz:\na-lewo\nd-prawo\nc-center\nw-wyjdz\n : ')
                        if x =='a' or x =='d' or x =='c':
                                insert_and_move(x)
                        elif x =='w':
                                break

        elif user =='2':
                constant_moves()
        if user == 'e':
                print('you left from applcation')
                break
       
                
                

                
        
        

                         
                      

        
        
        
