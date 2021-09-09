#basic kernel/matrice
#    [1 1 1]
#K = [1 1 1]
#    [1 1 1]

#3 x 3 square kernel
#kernels must have an odd width and height to ensure it has a center pixel

#a convolution requires 3 components:

#1). An input image

#2). A kernel matrix to apply to the input image

#3). an output image to store the output of the inoput image convolved

#steps to convolve an image

#1). Select an (x, y)-coordinate from the original image.
#)2. Place the center of the kernel at this (x, y)-coordinate.
#)3. Take the element-wise multiplication of the input image region and the kernel, then sum up the values of these multiplication operations into a single value. The sum of these multiplications is called the kernel output.
#)4. Use the same (x, y)-coordinates from Step #1, but this time, store the kernel output in the same (x, y)-location as the output image.

from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

def convolve(image, kernel):
    #spatial dimensions of img
    iH, iW = image.shape[:2]
    #spatial dimensions of kernel
    kH, kW = image.shape[:2]

    #allocate memory for outpout image, padding borders so no size is lost
    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")

    #loop over the input image, "sliding" the kernel across each (x, y)-coordinate 
    #from left-to-right and top to bottom
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            #extract the ROI of the image by extracting the
			#*center* region of the current (x, y)-coordinates dimensions
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

            #perform the actual convolution by taking the #element-wise 
			#multiplicate between the ROI and the kernel, then summing the matrix
            k = (roi * kernel).sum()

            #store the convolved value in the output (x,y)- coordinate of the
            #output image
            output[y - pad, x - pad] = k
			
			#rescale the image to be in the range [0, 255]
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

    return output

#argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

#construct average blurring kernels used to smooth an image
small_blur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
large_blur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

#build a sharpening filter
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")

#construct the Laplacian kernel to detect edge-like regions of an image
laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")

sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

#construct the kernel bank, a list of kernels we're going to apply using both
#our custom `convole` function and OpenCV's `filter2D` function

kernel_bank = (
    ("small_blur", small_blur),
    ("large_blur", large_blur),
    ("sharpen", sharpen),
    ("laplacian", laplacian),
    ("sobel_x", sobelX),
    ("sobel_y", sobelY)
)

#load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for (kernel_name, kernel) in kernel_bank:
    print(f"[INFO] applying {kernel_name} kernel")
    convole_output = convolve(gray, kernel)
    opencv_ouput = cv2.filter2D(gray, -1, kernel)

    #show the output images
    cv2.imshow("original-gray", gray)
    cv2.imshow(f"{kernel_name} - convole", convole_output)
    cv2.imshow(f"{kernel_name} - opencv", opencv_ouput)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

