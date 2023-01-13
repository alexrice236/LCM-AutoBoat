import time
import lcm
import random
import numpy as np
import cv2

from imagedata import image_t

lc = lcm.LCM()
counter = 0

start = time.time()

try:
    while True:
        print(counter)
        msg = image_t()
        frame = cv2.imread('img.jpg')
        #frame = cv2.resize(frame, (1280, 720))
        image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        msg.width = frame.shape[1]
        msg.height = frame.shape[0]
        msg.row_stride = frame.shape[1]
        msg.size = len(image_bytes)
        msg.data = image_bytes
        msg.bigendian = False
        msg.pixel_format = 2
        msg.channel_type = 1
        msg.compression_method = 2
        lc.publish("IMAGE", msg.encode())
        counter += 1
except KeyboardInterrupt:
    end = time.time()
    print('Total Time: ' + str(end-start))