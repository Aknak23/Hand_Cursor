
import cv2 as cv
import sys
import numpy as np

#img = cv.imread(cv.samples.findFile("starry_night.png"))

#if img is None:
#    sys.exit("Could not read the image.")

#cv.imshow("Display window", img)
#k = cv.waitKey(0)

#if k == ord("s"):
#    cv.imwrite("starry_night.png", img)
M = np.zeros((2,2,3), dtype=np.uint8)
M[:] = (0,0,255)  # BGR (Red)

print("M = \n", M)
print("Shape:", M.shape)
print("Rows:", M.shape[0])
print("Columns:", M.shape[1])
print("Channels:", M.shape[2])