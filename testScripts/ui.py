import keyboard
import lcm

from modata import motion_data

lc = lcm.LCM()

while True:
    msg = motion_data()
    msg.linear_speed = 0.0
    msg.angle = 0.0

    if keyboard.read_key() == "w":
        msg.linear_speed = 1
    if keyboard.read_key() == "a":
        msg.angle = -1
    elif keyboard.read_key() == "d":
        msg.angle = 1

    lc.publish("MOTION", msg.encode())
