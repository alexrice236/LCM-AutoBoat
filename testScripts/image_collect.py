import lcm
import numpy as np
import cv2
from imagedata import image_t

counter = 0

def my_handler(channel, data):
    msg = image_t.decode(data)
    nparr = np.fromstring(msg.data, np.uint8)
    receieved = cv2.imdecode(nparr, flags=1)
    cv2.imwrite('../../received.jpeg', receieved)
    return

lc = lcm.LCM()
subscription = lc.subscribe("IMAGE", my_handler)

while True:
    lc.handle()
    print(counter)
    counter += 1