from sshkeyboard import listen_keyboard
#import keyboard
import lcm

from modata import motion_data
from podata import power_data

lc = lcm.LCM()

subscription = lc.subscribe("POWER", my_handler)

def press(key):
    msg = motion_data()
    msg.linear_speed = 0.0
    msg.angle = 0.0

    if key == "w":
        msg.linear_speed = 60
    if key == "a":
        msg.angle = 10
    if key == "s":
        msg.angle = 6
    if key == "d":
        msg.angle = 2

    lc.publish("MOTION", msg.encode())

def my_handler(channel, data):
    msg = power_data.decode(data)
    print("-----------")
    print("Voltage: " + str(msg.voltage))
    print("Current: " + str(msg.current))
    print("Power: " + str(msg.power))

while True:
    listen_keyboard(on_press=press)
    lc.handle()