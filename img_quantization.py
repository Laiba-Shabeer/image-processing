import cv2
import numpy as np

# Number of clusters
k = 10

# Load the image
img = cv2.imread('cristiano.webp')

# Reshape the image to a 2D array of pixels
z = img.reshape((-1, 3))

# Convert to np.float32 for k-means
z = np.float32(z)

# Define the criteria and apply k-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

# Save the image
cv2.imwrite("output.jpg", res2)

# Display the result
cv2.imshow('Original Image', img)
cv2.imshow('K-means Image', res2)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
