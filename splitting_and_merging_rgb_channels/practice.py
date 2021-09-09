#practice maing the argument parser
import argparse
import cv2

#construct the argument parser
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









































cv2.waitKey(0)