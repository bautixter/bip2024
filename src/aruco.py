import numpy as np
from picamera2 import Picamera2, Preview
import cv2
import time

class ArucoDetector:

    def __init__(self):
        picam2 = Picamera2()
        camera_config = picam2.create_preview_configuration()
        picam2.configure(camera_config)
        picam2.start()
        time.sleep(2)

        self.picam2 = picam2
        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    def processFrame(self,value):
        # Capture frame-by-frame
        self.picam2.capture_file("test.jpg")
        time.sleep(value)
        image = cv2.imread("test.jpg")

        # Our operations on the frame come here
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        res  = cv2.aruco.detectMarkers(gray, self.dictionary)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return -1

        # Return if there is or not a marker in the image
        if len(res[0]) > 0:
            cv2.aruco.drawDetectedMarkers(gray,res[0],res[1])
            return 1
        else:
            return 0


    def close():
        # When everything done, release the capture
        cv2.destroyAllWindows()
