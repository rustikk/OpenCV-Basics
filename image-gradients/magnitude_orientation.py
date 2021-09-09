import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#gradients for x and y-axis
gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

#magnitude is the sq root  of the squared gradients in both x and y directions
#added together
magnitude = np.sqrt((gX ** 2) + (gY ** 2))
#the gradient orientation is the arc-tangent of the gradients
orientation = np.arctan2(gX, gY) * (180 / np.pi) % 180

#intitalize a figure to display grayscale image and the gradient magnitude and
#orientation
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))

#plot the images
axs[0].imshow(gray, cmap="gray")
axs[1].imshow(magnitude, cmap="jet")
axs[2].imshow(orientation, cmap="jet")

axs[0].set_title("Grayscale")
axs[1].set_title("Gradient Magnitude")
axs[2].set_title("Gradient Orientation [0, 180]")

for i in range(0, 3):
    axs[i].get_xaxis().set_ticks([])
    axs[i].get_yaxis().set_ticks([])

#show plots
plt.tight_layout()
plt.show()
