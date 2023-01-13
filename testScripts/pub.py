import keyboard
import lcm

from modata import motion_data

# def press(key):
#     msg = motion_data()
#     msg.linear_speed = 0.0
#     msg.angle = 0.0

#     if key == "w":
#         msg.linear_speed = 40
#     if key == "a":
#         msg.angle = 10
#     if key == "s":
#         msg.angle = 6
#     if key == "d":
#         msg.angle = 2

#     lc.publish("MOTION", msg.encode())


lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")


while True:
    msg = motion_data()
    msg.linear_speed = 0.0
    msg.angle = 0.0

    if keyboard.read_key() == "w":
        msg.linear_speed = 40
    if keyboard.read_key() == "a":
        msg.angle = 10
    if keyboard.read_key() == "s":
        msg.angle = 6
    if keyboard.read_key() == "d":
        msg.angle = 2

    lc.publish("MOTION", msg.encode())