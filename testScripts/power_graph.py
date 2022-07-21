import time
import lcm
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from podata import power_data

voltage_y = []
current_y = []
power_y = []
time_x = []

def my_handler(channel, data):
    msg = power_data.decode(data)
    voltage_y.append(msg.voltage)
    current_y.append(msg.current)
    power_y.append(msg.power)
    time_x.append(time.time())

lc = lcm.LCM()
subscription = lc.subscribe("POWER", my_handler)

while True:
    try:
        plt.savefig("/home/pi/LCM-AutoBoat/testScripts/graph.png")
        lc.handle()
    except KeyboardInterrupt:
        plt.subplot(3,1,1)
        plt.plot(np.array(time_x), np.array(voltage_y))
        plt.title("Voltage (V)")
        plt.subplot(3,1,2)
        plt.plot(np.array(time_x), np.array(current_y))
        plt.title("Current (mA)")
        plt.subplot(3,1,3)
        plt.plot(np.array(time_x), np.array(power_y))
        plt.title("Power (W)")
        plt.xlabel("Time (s)")
        plt.savefig("/home/pi/LCM-AutoBoat/testScripts/graph.png")
        quit()

