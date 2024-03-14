import RPi.GPIO as GPIO
import time
import random

# GPIO pin numbers (change these according to your setup)
servo1_pin = 18
servo2_pin = 19

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)

# Set PWM frequency
pwm_freq = 50  # Hz
servo1_pwm = GPIO.PWM(servo1_pin, pwm_freq)
servo2_pwm = GPIO.PWM(servo2_pin, pwm_freq)

# Start PWM
servo1_pwm.start(0)
servo2_pwm.start(0)

def set_angle(pwm, angle):
    duty = angle / 18 + 2
    GPIO.output(pwm, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(pwm, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Generate random angles (between 0 and 180) for the servos
        angle1 = random.randint(0, 180)
        angle2 = random.randint(0, 180)
        
        # Move the servos to the random angles
        set_angle(servo1_pwm, angle1)
        set_angle(servo2_pwm, angle2)
        
        # Delay before moving again
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    servo1_pwm.stop()
    servo2_pwm.stop()
    GPIO.cleanup()
