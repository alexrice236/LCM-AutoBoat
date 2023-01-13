# from sshkeyboard import listen_keyboard
import lcm

from modata import motion_data

count = 0

def press(key):
    msg = motion_data()
    msg.linear_speed = 0.0
    msg.angle = 0.0

    if key == "w":
        msg.linear_speed = 30
    if key == "a":
        msg.angle = -1
    if key == "d":
        msg.angle = 1

    lc.publish("MOTION", msg.encode())


lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

while True:
    wait(.1)
    if count == 6: count = 0
    msg = motion_data()
    msg.linear_speed = count
    msg.angle = 0.0
    lc.publish("MOTION", msg.encode())
    count += 1
#     listen_keyboard(on_press=press)