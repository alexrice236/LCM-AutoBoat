import time
import lcm
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sqlite3

volt = "VOLT"
curr = "CURR"
power = "POW"

power_db = "/home/pi/LCM-AutoBoat/testScripts/actuation_power.db"

with sqlite3.connect(power_db) as c:
    data_entries = c.execute('''SELECT * FROM actuation_power_data WHERE source = ? ORDER BY rowid DESC;''', ("ACTUATION",)).fetchall()
    voltage_y = []
    current_y = []
    power_y = []
    time_x = []
    for entry in data_entries:
        voltage_y.append(entry[1])
        current_y.append(entry[2])
        power_y.append(entry[3])
        time_x.append(entry[4])
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