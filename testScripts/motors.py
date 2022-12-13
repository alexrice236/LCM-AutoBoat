import RPi.GPIO as GPIO
import time
import lcm

from modata import motion_data

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

#switchLeft = 5
#switchRight = 6

GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.LOW)

left = GPIO.PWM(12, 400)
right = GPIO.PWM(13, 400)
left.start(0)
right.start(0)


def my_handler(channel, data):
    msg = motion_data.decode(data)
    if msg.angle == -1:
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
    elif msg.angle == 1:
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
    else:
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
    left.ChangeDutyCycle(msg.linear_speed)
    right.ChangeDutyCycle(msg.linear_speed)

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")
subscription = lc.subscribe("MOTION", my_handler)

while True:
    lc.handle()