import keyboard
import RPi.GPIO as GPIO
import time
from gpiozero import Servo

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 1000)

for i in range(2, 13):
    pwm.changeDutyCycle(i)
    time.sleep(1)