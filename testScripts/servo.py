import keyboard
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 1000)

while True:
    if keyboard.read_key() == 'a':
        pwm.start(70)
    elif keyboard.read_key() == 'd':
        pwm.start(30)
    continue