import keyboard
import RPi.GPIO as GPIO
import time
from gpiozero import Servo

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 1000)

while True:
    if keyboard.read_key() == 'a':
        pwm.start(2)
    elif keyboard.read_key() == 'd':
        pwm.start(12)
    continue