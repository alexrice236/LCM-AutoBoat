import keyboard
import RPi.GPIO as GPIO
import time
import lcm
from modata import motion_data

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
servo = GPIO.PWM(13, 50)


def my_handler(channel, data):
    msg = motion_data.decode(data)
    servo.ChangeDutyCycle(msg.angle)

lc = lcm.LCM()
subscription = lc.subscribe("MOTION", my_handler)

while True:
    servo.start(0)
    lc.handle()
    servo.stop()

GPIO.cleanup()