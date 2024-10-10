import cv2
import numpy as np
import imageio.v3 as iio
import skimage.color
import skimage.filters
import skimage.measure
import matplotlib.pyplot as plt

# Read the image
bacteria_image = iio.imread(uri="cookie3.jpeg")

# Display the original image
fig, ax = plt.subplots()
plt.imshow(bacteria_image)
plt.title("Original Image")
plt.show()

# Convert the image to grayscale
gray_bacteria = skimage.color.rgb2gray(bacteria_image)

# Display the grayscale image
fig, ax = plt.subplots()
plt.imshow(gray_bacteria, cmap="gray")
plt.title("Grayscale Image")
plt.show()

# Blur the grayscale image using a Gaussian filter
blurred_image = skimage.filters.gaussian(gray_bacteria, sigma=1.0)

# Create a histogram of the blurred image
histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))

# Plot the histogram
fig, ax = plt.subplots()
plt.plot(bin_edges[0: -1], histogram)
plt.title("Graylevel Histogram")
plt.xlabel("Gray Value")
plt.ylabel("Pixel Count")
plt.xlim(0, 1.0)
plt.show()

# Create a binary mask where the image is dark (value < 0.2)
mask = blurred_image < 0.2

# Display the binary mask
fig, ax = plt.subplots()
plt.imshow(mask, cmap="gray")
plt.title("Binary Mask")
plt.show()

# Analyze the image to detect colonies (connected components)
labeled_image, count = skimage.measure.label(mask, return_num=True)
print(f"Number of colonies detected: {count}")

# Color each of the detected colonies differently
colored_label_image = skimage.color.label2rgb(labeled_image, bg_label=0)

# Convert the grayscale image back to RGB for display purposes
summary_image = skimage.color.gray2rgb(gray_bacteria)

# Overlay the colored colonies onto the grayscale image
summary_image[mask] = colored_label_image[mask]

# Display the summary image with colored colonies
fig, ax = plt.subplots()
plt.imshow(summary_image)
plt.title("Color colony")
plt.show()



# (Optional) Wait for key press if running in a standalone script
cv2.waitKey(0)
cv2.destroyAllWindows()