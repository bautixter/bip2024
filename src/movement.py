from AlphaBot2 import AlphaBot2
from PCA9685 import PCA9685
import RPi.GPIO as GPIO
import time

def right(AB:AlphaBot2):
    AB.right()
    time.sleep(0.2)
    AB.stop()

def left(AB:AlphaBot2):
    AB.left()
    time.sleep(0.2)
    AB.stop()

def forward(AB:AlphaBot2):
    AB.forward()
    time.sleep(0.5)
    AB.stop()

if __name__=='__main__':
    AB = AlphaBot2()
    pwm = PCA9685(0x40,debug=True)
    pwm.setPWMFreq(50)
    try:
        while True:
            for i in range(10):
                #right(AB)
                while not pwm.scanning():
                    time.sleep(0.1)
                #left(AB)
                forward(AB)
            right(AB)
            for i in range(5):
                #right(AB)
                while not pwm.scanning():
                    time.sleep(0.1)
                #left(AB)
                forward(AB)
            right(AB)

    except KeyboardInterrupt:
        GPIO.cleanup()

