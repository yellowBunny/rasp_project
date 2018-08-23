import unittest, sys
sys.path.append('/home/pi/Desktop/examples/')
import rfid_module
import RPi.GPIO as GPIO
GPIO.cleanup()
class RFID_testing(unittest.TestCase):
    
    rfid = rfid_module.Rfid()
    
    def test_read_card(self):
        f = self.rfid.read_card()
        self.assertEqual(len(f), 2, 'should be {} is {}'.format(2, len(f)))
        GPIO.cleanup()
        
        
unittest.main()