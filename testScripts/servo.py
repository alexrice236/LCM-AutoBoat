import keyboard
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
servo = GPIO.PWM(13, 50)
servo.start(0)

time.sleep(1)

servo.ChangeDutyCycle(7)

time.sleep(1)

servo.stop()
GPIO.cleanup()