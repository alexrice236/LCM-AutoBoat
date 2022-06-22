import RPi.GPIO as GPIO
import time
import keyboard

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.output(6, GPIO.LOW)
pwm = GPIO.PWM(12, 1000)

while True:
    if keyboard.read_key() == "w":
        pwm.start(50)
    else:
        pwm.stop()
