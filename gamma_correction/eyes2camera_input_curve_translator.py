from __future__ import print_function
from matplotlib.pyplot import table
import numpy as np
import argparse
import cv2

def adjust_gamma(image, gamma=1.0):
    #build a lookup table mapping the pixel values [0, 255] to their adjusted
    #gamma values
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

    #apply gamma correction using the lookup table
    return cv2.LUT(image, table)

#define argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, type=str, help="path to input image")
args = vars(ap.parse_args())

#load the original
original = cv2.imread(args["image"])

for gamma in np.arange(0.0, 3.5, 0.5):
    #ignore when gamma is 1 as there will be no change to the image
    if gamma == 1:
        continue

    #apply the gamma correction
    gamma = gamma if gamma > 0 else 0.1
    #change 2nd value to change gamma correction value
    adjusted = adjust_gamma(original, 2.0)
    cv2.putText(adjusted, f"g={gamma}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Images", np.hstack([original, adjusted]))
    cv2.waitKey(0)
