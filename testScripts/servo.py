import keyboard
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
servo = GPIO.PWM(12, 50)
servo.start(0)

for i in range(2, 13):
    time.sleep(1)
    servo.ChangeDutyCycle(i)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

servo.stop()
GPIO.cleanup()