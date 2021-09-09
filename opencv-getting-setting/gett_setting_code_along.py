import argparse
import cv2

#construct the argument parser
ap = argparse.ArgumentParser()
#if no argument is passed, "adrian.png" is used
ap.add_argument("-i", "--image", type=str, default="adrian.png", 
help="path to input image")
#vars stores the arguments in a dictionary
args = vars(ap.parse_args())
#load the image, grab it spacial dimensions (width and height),
#and then display the original image to our screen

#reads the image from the argument passed at the command line,
#the input path to the image being manipulated
image = cv2.imread(args["image"])
#grabs the width and height
(h, w) = image.shape[:2]
#shows the image with a title of Original
cv2.imshow("Original", image)
#keeps the image open til a key is pressed, then it closes
#cv2.waitKey(0)

#rgb values at (0, 0)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue {}".format(r, g, b))

# access the pixel located at x=50, y=20
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# update the pixel at (50, 20) and set it to red
image[20, 50] = (0, 0, 255)
#y values first then x values as images are numpy arrays
#and you access rows before columns in numpy arrays
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# compute the center of the image, which is simply the width and height
# divided by two
cX, cY = (w // 2, h // 2)

# since we are using NumPy arrays, we can apply array slicing to grab
# large chunks/regions of interest from the image -- here we grab the
# top-left corner of the image
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Left Corner", tl)
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-left Corner", bl)
#set the top left corner of the original image to be green
image[0:cY, 0:cX] = (255, 0, 255)
#show updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)