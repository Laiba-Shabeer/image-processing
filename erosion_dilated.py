import cv2
import numpy as np

# Read the image
image = cv2.imread('anime-naruto-naruto-uzumaki-ninja-wallpaper-preview.jpg')

# Create a kernel for the erosion operation
kernel = np.ones((3, 3), np.uint8)

# Apply the erosion operation with 3 iterations
eroded_image = cv2.erode(image, kernel, iterations=3)

dilate_image = cv2.dilate(image,(3,3))
cv2.imshow("dilate_image",dilate_image)


# Show the eroded image
cv2.imshow("Eroded Image", eroded_image)

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()