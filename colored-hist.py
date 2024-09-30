import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# reading image
img = cv2.imread('anime-naruto-naruto-uzumaki-ninja-wallpaper-preview.jpg')
assert img is not None, "Image not found"
cv2.imshow('Original Image', img)

#define color for channel
colors = ['b', 'g', 'r']

# Create a figure and axis
plt.figure(figsize=(10, 5))
plt.title('Color Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')

# Calculate and plot the histogram for each color channel
for i, color in zip(range(len(colors)), colors):
    #(0 'b')
    #(1, 'g'),
    #(2, 'r')

    # Calculate histogram for each channel
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    # Plot the histogram w
    plt.plot(hist, color=color)

# Set x-axis limit
plt.xlim([0, 256])
plt.show()

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()