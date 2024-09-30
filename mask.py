import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image
image = cv2.imread('anime-naruto-naruto-uzumaki-ninja-wallpaper-preview.jpg')

# Check if the image was successfully loaded
assert image is not None, "Image not found or failed to load."

# Create a mask the same size as the image
mask = np.zeros(image.shape[:2], dtype=np.uint8)

mask[100:500, 100:400] = 255
masked_img = cv2.bitwise_and(image, image, mask=mask)

#hiistogram without mask
hist_without_mask = cv2.calcHist([image], [0], None, [256], [0, 256])

#histogram with mask
hist_with_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])

plt.figure(figsize=(10, 6))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(222)
plt.imshow(cv2.cvtColor(masked_img, cv2.COLOR_BGR2RGB))
plt.title('Masked Image')
plt.subplot(223)
plt.plot(hist_without_mask)
plt.title('Histogram Without Mask')
plt.subplot(224)
plt.plot(hist_with_mask, color="green")
plt.title('Histogram With Mask')

plt.tight_layout()
plt.show()