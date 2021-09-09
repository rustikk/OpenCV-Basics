import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, 
default="/home/t-dawg/Documents/python/py_image_search/image_flipping/input_01.png",
help="path to the input image")
args = vars(ap.parse_args())

# load the original input image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#flip image horizontally
print("flipping the img horizontally")
#with cv2.flip() 1 is a horizontal flip around the y-axis, 0 is vertical flip
#around the x-axis, using a -1 flip its both horizontally and vetically
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

#flip image vertically
flipped = cv2.flip(image, 0)
print("[INFO] flipping image vertically...")
cv2.imshow("Flipped Vertically", image)

#flip image vertically and horizontally
flipped = cv2.flip(image, -1)
print("[INFO] flipping image horizontally and vertically")
cv2.imshow("flipped on both axis", flipped)
cv2.waitKey(0)