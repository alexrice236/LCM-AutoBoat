import keyboard
import RPi.GPIO as GPIO
import time
from gpiozero import Servo

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
servo = GPIO.PWM(13, 50)
servo.start(7.5)

for i in range(2, 13):
    servo.ChangeDutyCycle(i)
    time.sleep(1)

servo.stop()
GPIO.cleanup()