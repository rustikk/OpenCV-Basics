#import the dependencies
import argparse
import imutils
import cv2

#construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="tropics.jpg",
help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#150px wide divided by number of columns
ratio = 150.0 / image.shape[1]
#150 for x value, int(image.shape[0] * ratio) for y value
#image.shape[0] is the number of rows * 
dim = (150, int(image.shape[0] * ratio))

#perform the resizing of the image
#interpolation= is the algorithm working behind the scenes to resize the img
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized by width", resized)

#using the imutils library to automatically calculate the aspect ratio
resized1 = imutils.resize(image, width=350)
cv2.imshow("imutils resize", resized1)

resized2 = imutils.resize(image, height=150)
cv2.imshow("imutils resized by height", resized2)
cv2.waitKey(0)

#construct the list of interpolation methods in OpenCV
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANZOS4", cv2.INTER_LANCZOS4)
]

#loop over interpolation methods
for (name, method) in methods:
    #increase size of img by 3x using current interpolation method
    print("INFO {}".format(name))
    resized3 = imutils.resize(image, width=image.shape[1] * 3,
    inter=method)
    cv2.imshow(f"Method: {name}", resized)
    cv2.waitKey(0)