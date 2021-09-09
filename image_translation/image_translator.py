"""
Negative values for the t_{x} value will shift the image to the left
Positive values for  t_{x} shifts the image to the right
Negative values for  t_{y} shifts the image up
Positive values for  t_{y} will shift the image down
"""
import numpy as np
import argparse
import imutils
import cv2

#construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="tropics.jpg")
args = vars(ap.parse_args())

#load the image and display it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#shift image 25px right and 50px down
M1 = np.float32([
    [1, 0, 25],
    [0, 1, 50]
])
shifted_img = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted_img)

#shift image 50px left and 90px up by using negative values
M2 = np.float32([
    [1, 0, -50],
    [0, 1, -90]
])
shifted_img_neg = cv2.warpAffine(image, M2, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted_img_neg)

#use the imutils library to translate in less lines of code
shifted_imutils = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted_imutils)
cv2.waitKey(0)







































"""
#shift an image 25px to right and 50px down
Mt = np.float32([
    [1, 0, 25],
    [0, 1, 50]
])

#shift an image 7px to left and 23px up
M1 = np.float32([
    [1, 0, -7],
    [0, 1, -23]
])

#shift an image 30px left and 13px down
M2 = np.float32([
    [1, 0, -30],
    [0, 1, 12]
])

shifted = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))
"""