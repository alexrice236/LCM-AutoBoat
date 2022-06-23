import keyboard
import RPi.GPIO as GPIO
import time
import lcm

from modata import motion_data

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.output(6, GPIO.LOW)
pwm = GPIO.PWM(12, 1000)

def my_handler(channel, data):
    msg = motion_data.decode(data)
    if msg.linear_speed > 0.5:
        pwm.start(70)
    else:
        pwm.stop()

lc = lcm.LCM()
subscription = lc.subscribe("MOTION", my_handler)

while True:
    lc.handle()