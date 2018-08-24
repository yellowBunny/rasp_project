import unittest, sys, time
sys.path.append('/home/pi/Desktop/examples/')
import rfid_module
import RPi.GPIO as GPIO
GPIO.cleanup()
class RFID_testing(unittest.TestCase):
    
    rfid = rfid_module.Rfid()
    
    def test_read_card(self):
        '''testing reade_card method if return correctly value and quantity/amount value'''
        self.rfid.set_pins()
        func = self.rfid.read_card()
        # testing if read_card method return two value
        self.assertEqual(len(func), 2, 'should be {} is {}'.format(2, len(func)))
        
        # testing first value in func. value should be int calss
        self.assertIs(type(func[0]), int, 'should be int is {}'.format(type(func[0])))
        
        # testing first value in func. value should be str calss
        self.assertIs(type(func[1]), str, 'should be int is {}'.format(type(func[1])))
        GPIO.cleanup()
    
    def test_open_lock(self):
        '''testing open_lock method.'''
        self.rfid.set_pins()
        name = 'seba'        
        f = self.rfid.open_lock(name)
        self.assertFalse(f, 'should be False')
        GPIO.cleanup()
    
    def test_warning(self):
        '''testing warning method.'''        
        self.rfid.set_pins()
        id = 12314
        name = 'Waclaw'
        c = 2
        f = self.rfid.warning(id, name, c)
        self.assertTrue(f, 'Should be True')
        GPIO.cleanup()
    
    def test_let_in(self):
        self.rfid.set_pins()
        name = 'seba'
        id = 12345
        c = 3
        f = self.rfid.let_in(name, id, c)
        self.assertFalse(f, 'should be False is True')
        name = 'unknown'
        f = self.rfid.let_in(name, id, c)
        self.assertEqual(f, c + 1, 'should be {} is {}'.format(c + 1, f))
        GPIO.cleanup()    
    
    
                
unittest.main(exit=False)


        
        
