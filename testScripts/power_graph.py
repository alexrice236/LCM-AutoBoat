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
    voltages = c.execute('''SELECT * FROM actuation_power_data WHERE type = ? ORDER BY rowid DESC;''', (volt,)).fetchall()
    currents = c.execute('''SELECT * FROM actuation_power_data WHERE type = ? ORDER BY rowid DESC;''', (curr,)).fetchall()
    powers = c.execute('''SELECT * FROM actuation_power_data WHERE type = ? ORDER BY rowid DESC;''', (power,)).fetchall()
    times = c.execute('''SELECT * FROM actuation_power_data WHERE type = ? ORDER BY rowid DESC;''', ("TIME",)).fetchall()
    voltage_y = [entry[1] for entry in voltages]
    current_y = [entry[1] for entry in currents]
    power_y = [entry[1] for entry in powers]
    time_x = [entry[1] for entry in times]
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


