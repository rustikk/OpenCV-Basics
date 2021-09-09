#adding these 2 matrices
#pretend lines connect
#|9 3 2| + |0 9 4| = |9+0 3+9 2+4|
#|4 1 4| + |7 9 4| = |4+7 1+9 4+4|

#if a value that was added to a r,g or b channel exceeded 255
#numpy would apply modulus arithmetic and "wrap around"
#opencv will perform clipping and ensure pixel values never fall outside 
#the range(0, 255)


#uses of image arithmetic

#adjusting brightness and contrast 
#working with alpha blending and transparency 
#creating instagram like filters

import numpy as np
import argparse
import cv2

#construct argumentparser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="grand_canyon.png",
help="path to input image")
args = vars(ap.parse_args())

#images are NumPy arrays stored as unsigned 8-bit integers (unit8)
#with values in the range [0, 255]; when using the add/subtract
#functions in OpenCV, these values will be *clipped* to this range,
#even if they fall outside the range [0, 255] after applying the operation

#assign 2 numpy arrays that are 8-bit unsigned integers each with one element
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print(f"max of 255: {added}")
print(f"min of 0: {subtracted}")

#using NumPy arithmetic operations (rather than OpenCV operations)
#will result in a modulo ("wrap around") instead of being clipped
#to the range [0, 255]

#once 255 is reached numpy wraps around to zero and starts counting up again
#until 100 steps have been reached
added1 = np.uint8([200]) + np.uint8([100])
subtracted1 = np.uint8([50]) - np.uint8([100])
print(f'wrap around: {added1}')
print(f'wrap around: {subtracted1}')

#load and display original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#increasing the pixel intensities in the input image is accomplished by
#constructing a numpy array with the same dimensions, filling it with
#1's and multiplying the values by 100 then adding the input image
#and matrix together
M = np.ones(image.shape, dtype="uint8") * 100
added2 = cv2.add(image, M)
cv2.imshow("Lighter", added2)

#we can also make the image darker by subtracting 50 from all pixel's
#rbg values.
M1 = np.ones(image.shape, dtype="uint8") * 50
subtracted2 = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted2)
cv2.waitKey(0)

