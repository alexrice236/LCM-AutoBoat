import RPi.GPIO as GPIO
import time
import lcm

from modata import motion_data

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, GPIO.LOW)
pwm = GPIO.PWM(6, 100)

def my_handler(channel, data):
    msg = motion_data.decode(data)
    pwm.start(msg.linear_speed)

lc = lcm.LCM()
subscription = lc.subscribe("MOTION", my_handler)

while True:
    lc.handle()