
#cropping with numpy
import numpy as np
# arnage() creates a 1D array
I = np.arange(0, 25)
print(I)

#reshape into a 2d matrix
I = I.reshape((5, 5))
print(I)

#extract pixels starting at y=0, x=0 and ending at x=2, y=3
#subscription notation
#y before x becauase its an array
#extracts 3 rows and 2 columns
print(I[0:3, 0:2])

#extract the pixels starting at x=1, y=3 and ending at x=5 and y=5
print(I[3:5, 1:5])
