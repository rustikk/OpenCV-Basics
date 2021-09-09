import argparse
import cv2

#argparser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="fish_items.jpg",
help="path to input image")
args = vars(ap.parse_args())

#load original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

octupus = image[0:105, 0:132]
cv2.imshow("Octopus", octupus)

dolphin = image[0:105, 132:265]
cv2.imshow("Dolphin", dolphin)

jellyfish = image[0:105, 256:367]
cv2.imshow("JellyPhysh", jellyfish)

lobster = image[100:220, 150:250]
cv2.imshow("Lobster", lobster)
cv2.waitKey(0)