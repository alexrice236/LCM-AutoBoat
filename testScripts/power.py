import RPi.GPIO as GPIO
import time
import lcm
from ina219 import INA219
from podata import power_data

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 0.6

lc = lcm.LCM()
ina = INA219(SHUNT_OHMS)
ina.configure()

while True:
    msg = power_data()
    msg.voltage = ina.voltage()
    msg.current = ina.current()
    msg.power = ina.power()
    lc.publish("POWER", msg.encode())
    time.sleep(1)