import time
import lcm
from podata import power_data

lc = lcm.LCM()

count = 0

while True:
    msg = power_data()
    msg.voltage = 0
    msg.current = 0
    msg.power = count
    lc.publish("POWER", msg.encode())

    count += 1
    if count == 6:
        count = 0

    time.sleep(.05)