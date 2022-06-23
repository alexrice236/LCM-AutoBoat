import keyboard
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.output(6, GPIO.LOW)
#GPIO.output(12, GPIO.HIGH)
pwm = GPIO.PWM(12, 1000)

#for i in range(75):
#    pwm.start(i)
#    time.sleep(.5)

while True:
    if keyboard.read_key() == "w":
        pwm.start(70)
    else:
        pwm.stop()