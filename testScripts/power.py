import RPi.GPIO as GPIO
import time
import lcm
import board
import busio
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219
from podata import power_data

lc = lcm.LCM()
i2c = busio.I2C(board.SCL, board.SDA)
sensor = INA219(i2c)
sensor.bus_adc_resolution = ADCResolution.ADCRES_12BIT_16S
sensor.bus_voltage_range = BusVoltageRange.RANGE_16V

while True:
    msg = power_data()
    msg.voltage = 0
    msg.current = 0
    msg.power = 0
    msg.voltage = sensor.bus_voltage
    msg.current = sensor.current
    msg.power = sensor.power
    lc.publish("POWER", msg.encode())
    time.sleep(.1)