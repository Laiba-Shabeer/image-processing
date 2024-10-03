import cv2
import cv2
import numpy as np

# Load a grayscale image
# image = cv2.imread('cristiano.webp', cv2.IMREAD_GRAYSCALE)
image = cv2.imread('cristiano.webp')

# Apply a color map (e.g., COLORMAP_JET)
colormap_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)

# Display the original grayscale and color-mapped images
cv2.imshow('Original Grayscale Image', image)
cv2.imshow('Color Map Image', colormap_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
