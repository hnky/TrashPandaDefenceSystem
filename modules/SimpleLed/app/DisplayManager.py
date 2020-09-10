from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO
import time

class DisplayManager(object):
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(8, GPIO.OUT)
        GPIO.setwarnings(False)

        # Flash the LED logo at initialization
        print("Init")

    def DisplayLED(self, strImage):

        print("Displaying " + strImage)
        if 'bit' in strImage.lower():
             GPIO.output(8, True)
             print("On")
        else:
            GPIO.output(8, False)
            print("Off")  