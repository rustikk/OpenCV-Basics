import argparse
import imutils
import cv2

#construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="tropics.jpg",
help="path to input image")
args = vars(ap.parse_args())

#load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#grab dimensions and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

#in OpenCV, positive degrees specify counterclockwise rotation while
#negative degrees indicate clockwise rotation. 
#rotate image 45 degrees around center
M1 = cv2.getRotationMatrix2D((cY, cX), 45, 1.0)
rotated = cv2.warpAffine(image, M1, (w, h))
cv2.imshow("Rotated by 45 degrees", rotated)

#rotate image -90 degrees around center
M2 = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
roated1 = cv2.warpAffine(image, M2, (w, h))
cv2.imshow("Roatated by -90 degrees", roated1)

#rotate the image around an arbitrary point rather than center
M3 = cv2.getRotationMatrix2D((10, 10), 45, 1.0)
rotated2 = cv2.warpAffine(image, M3, (w, h))
cv2.imshow("Rotated by Arbitrary point", rotated2)


#use imutils library to rotate image with less code
rotated3 = imutils.rotate(image, 180)
cv2.imshow("Rotated 180 degrees", rotated3)

#rotate image by 33 degrees counterclockwise
#ensuring the rotated image still renders within the vieiwing area
rotated4 = imutils.rotate_bound(image, -33)
cv2.imshow("33 degrees Clockwise", image)
cv2.waitKey(0)