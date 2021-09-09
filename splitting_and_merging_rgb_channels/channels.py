import numpy as np
import argparse
import cv2

#argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="drake_and_I.jpg",
help="path to input image")
args = vars(ap.parse_args())

#load the image and grab each rgb value
#in openCV represents images as numpy arrarys with the channels in
#Blue, Green, Red order instead of Red, Green, Blue
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

#show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

#merge the image back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

#channels in color instead of grayscale
zeros = np.zeros(image.shape[:2], dtype="uint8")
#0 value for blue and green in pixels
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
#0 value for red and blue in pixels
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
#0 value for green and red in pixels
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))









































cv2.waitKey(0)
cv2.destroyAllWindows()