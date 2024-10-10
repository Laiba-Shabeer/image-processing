import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read and resize the image
bacteria_image = cv2.imread("cookie3.jpeg")

# Resizing image
bacteria_image = cv2.resize(bacteria_image, (300, 300))


bacteria_image_rgb = cv2.cvtColor(bacteria_image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray_bacteria = cv2.cvtColor(bacteria_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_bacteria, (5, 5), 1.0)

# Create a histogram
histogram = cv2.calcHist([blurred_image], [0], None, [256], [0, 256])

# Create a binary mask where pixel value < 50
_, mask = cv2.threshold(blurred_image, 50, 255, cv2.THRESH_BINARY_INV)

# Detect connected components (colonies)
num_labels, labels = cv2.connectedComponents(mask)

# Map the connected components to colors
label_hue = np.uint8(179 * labels / np.max(labels))
blank_channel = 255 * np.ones_like(label_hue)
colored_label_image = cv2.merge([label_hue, blank_channel, blank_channel])
colored_label_image = cv2.cvtColor(colored_label_image, cv2.COLOR_HSV2RGB)
colored_label_image[label_hue == 0] = 0  # Set the background to black

# Overlay the colored colonies onto the original image
overlay_image = bacteria_image_rgb.copy()
overlay_image[mask == 255] = colored_label_image[mask == 255]

# Display all images side by side using matplotlib
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

axes[0, 0].imshow(bacteria_image_rgb)
axes[0, 0].set_title("Original Image")
axes[0, 0].axis("off")

axes[0, 1].imshow(gray_bacteria, cmap="gray")
axes[0, 1].set_title("Grayscale Image")
axes[0, 1].axis("off")

axes[0, 2].imshow(blurred_image, cmap="gray")
axes[0, 2].set_title("Blurred Image")
axes[0, 2].axis("off")

axes[1, 0].plot(histogram)
axes[1, 0].set_title("Graylevel Histogram")
axes[1, 0].set_xlim([0, 256])
axes[1, 0].set_xlabel("Pixel Value")
axes[1, 0].set_ylabel("Frequency")

axes[1, 1].imshow(mask, cmap="gray")
axes[1, 1].set_title("Binary Mask")
axes[1, 1].axis("off")

axes[1, 2].imshow(overlay_image)
axes[1, 2].set_title("Colored Colonies")
axes[1, 2].axis("off")

plt.tight_layout()
plt.show()

# (Optional) Wait for key press if running in a standalone script
cv2.waitKey(0)
cv2.destroyAllWindows()
