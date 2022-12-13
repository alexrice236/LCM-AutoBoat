import time
import lcm

from modata import motion_data



def my_handler(channel, data):
    msg = motion_data.decode(data)
    print(msg.angle)


lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

subscription = lc.subscribe("MOTION", my_handler)

while True:
    lc.handle()
