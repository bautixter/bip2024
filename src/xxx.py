from AlphaBot2 import AlphaBot2
from PCA9685 import PCA9685
import RPi.GPIO as GPIO
import time
import random
import aruco


DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

def right(AB:AlphaBot2,value):
    AB.right()
    time.sleep(value)
    AB.stop()

def left(AB:AlphaBot2):
    AB.left()
    time.sleep()
    AB.stop()

def forward(AB:AlphaBot2,value):
    AB.forward()
    for elem in range(10):
        DR_status = GPIO.input(DR)
        DL_status = GPIO.input(DL)
        time.sleep(0.05)
        if ((DL_status == 0) or (DR_status == 0)):
            AB.stop()
            return True
    AB.stop()
    return False
        

if __name__=='__main__':
    arucoo = aruco.ArucoDetector()
    AB = AlphaBot2()
    pwm = PCA9685(0x40,debug=False)
    pwm.setPWMFreq(50)
    try:
        while True:
            if forward(AB,0.5):
                value = random.uniform(0,0.6)
                right(AB,value) 
            else:
                while not pwm.scanning(arucoo):
                    time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()









