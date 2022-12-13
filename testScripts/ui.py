from sshkeyboard import listen_keyboard
import lcm

from modata import motion_data

def press(key):
    msg = motion_data()
    msg.linear_speed = 0.0
    msg.angle = 0.0

    if key == "w":
        msg.linear_speed = 40
    if key == "a":
        msg.angle = -1
    if key == "d":
        msg.angle = 1

    lc.publish("MOTION", msg.encode())


lc = lcm.LCM()
lcm_create("udpm://239.255.76.67:7667?ttl=1")

while True:
    listen_keyboard(on_press=press)