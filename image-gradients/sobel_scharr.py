#USAGE
#-s 1 uses the scharr function, the sobel function is used by default
#python3 sobel_scharr.py -i image_path -s 1
import argparse
import cv2

#argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="path to input img")
ap.add_argument("-s", "--scharr", type=int, default=0)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Gray", gray)

#set the kernel size
ksize = -1 if args["scharr"] > 0 else 3
#compute x-axis 
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

#convert floating point data to unsigned 8 bit integer
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

#combine the gradients into one image
combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

#show outputs
cv2.imshow("Sobel/Scharr X", gX)
cv2.imshow("Sobel/Scharr Y", gY)
cv2.imshow("Sobel/Scharr Combined", combined)
cv2.waitKey(0)
