from sshkeyboard import listen_keyboard
#import keyboard
import lcm

from modata import motion_data

lc = lcm.LCM()

def press(key):
    msg = motion_data()
    msg.linear_speed = 0.0
    msg.angle = 0.0

    if key == "w":
        msg.linear_speed = 1
    if key == "a":
        msg.angle = 10
    elif key == "s":
        msg.angle = 8
    elif key == "d":
        msg.angle = 6

    lc.publish("MOTION", msg.encode())

while True:
    listen_keyboard(on_press=press)