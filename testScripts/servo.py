import keyboard
import RPi.GPIO as GPIO
import time
import lcm

from modata import motion_data

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
servo = GPIO.PWM(13, 50)
servo.start(0)
old_angle = 0

def get_old_angle():
    return old_angle

def set_old_angle(angle):
    global old_angle
    old_angle = angle

def my_handler(channel, data):
    msg = motion_data.decode(data)
    print(get_old_angle())
    if msg.angle == get_old_angle():
        return
    print("starting pwm")
    servo.start(msg.angle)
    time.sleep(.1)
    servo.stop()
    set_old_angle(msg.angle)

lc = lcm.LCM()
subscription = lc.subscribe("MOTION", my_handler)

while True:
    lc.handle()

servo.stop()
GPIO.cleanup()