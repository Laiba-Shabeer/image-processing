import cv2
import numpy as np

# Read the image
img = cv2.imread('anime-naruto-naruto-uzumaki-ninja-wallpaper-preview.jpg')


# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
gaussian_blur = cv2.GaussianBlur(gray_img, (7,7), 0)

# Perform Canny edge detection
canny_edge = cv2.Canny(gaussian_blur, (100 , 200))

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Canny Edge Detection', canny_edge)


# Wait until a key is pressed
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()
