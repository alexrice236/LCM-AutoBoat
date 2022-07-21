import RPi.GPIO as GPIO
import time
import lcm
import board
import busio
import adafruit_ina219
from podata import power_data

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 0.6

lc = lcm.LCM()
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ina219.INA219(i2c)

while True:
    msg = power_data()
    msg.voltage = sensor.bus_voltage
    msg.current = sensor.current
    msg.power = sensor.power
    lc.publish("POWER", msg.encode())
    time.sleep(1)