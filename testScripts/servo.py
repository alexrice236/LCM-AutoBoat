import keyboard
import RPi.GPIO as GPIO
import time
import lcm

from modata import motion_data

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
servo = GPIO.PWM(13, 100)
servo.start(0)

def set_servo(duty):
    #if duty < 1:
    #    return
    #GPIO.output(13, True)
    servo.ChangeDutyCycle(duty)
    #time.sleep(1)
    #GPIO.output(13, False)


def my_handler(channel, data):
    msg = motion_data.decode(data)
    #set_servo(msg.angle)
    servo.ChangeDutyCycle(msg.angle)


lc = lcm.LCM()
subscription = lc.subscribe("MOTION", my_handler)

servo.ChangeDutyCycle(6)
time.sleep(1)
servo.ChangeDutyCycle(8)
time.sleep(1)
servo.ChangeDutyCycle(10)
time.sleep(1)


#while True:
#    lc.handle()

servo.stop()
GPIO.cleanup()