import time
import lcm
import sqlite3
from podata import power_data

volt = "VOLT"
curr = "CURR"
power = "POW"

power_db = "/home/pi/LCM-AutoBoat/testScripts/actuation_power.db"
with sqlite3.connect(power_db) as c:
    c.execute("""DROP TABLE actuation_power_data;""")
    c.execute("""CREATE TABLE IF NOT EXISTS actuation_power_data (source text, voltage decimal, current decimal, power decimal, time int);""")

def my_handler(channel, data):
    msg = power_data.decode(data)
    try:
        with sqlite3.connect(power_db) as c:
            c.execute('''INSERT into actuation_power_data VALUES (?,?,?,?,?);''',("ACTUATION",msg.voltage,msg.current,msg.power,time.time()))
    except:
        print("database does not exist")
    return

lc = lcm.LCM()
subscription = lc.subscribe("POWER", my_handler)

while True:
    lc.handle()