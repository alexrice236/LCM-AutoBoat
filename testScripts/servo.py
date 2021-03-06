import keyboard
import RPi.GPIO as GPIO
import time
import lcm

from modata import motion_data

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
servo = GPIO.PWM(13, 50)
servo.start(0)
time.sleep(1)

def set_servo(duty):
    GPIO.output(13, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(.5)
    GPIO.output(13, False)
    servo.ChangeDutyCycle(0)


def my_handler(channel, data):
    msg = motion_data.decode(data)
    set_servo(msg.angle)


lc = lcm.LCM()
subscription = lc.subscribe("MOTION", my_handler)

while True:
    lc.handle()

servo.stop()
GPIO.cleanup()