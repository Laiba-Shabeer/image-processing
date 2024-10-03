import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Reading the image
image = cv2.imread('anime-naruto-naruto-uzumaki-ninja-wallpaper-preview.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image using matplotlib
plt.imshow(image_rgb)
plt.axis('off')  # Hide axes
plt.show()

image_rgb.shape

image_rgb.size

height, width, _ = image_rgb.shape

crop_width = width // 2
crop_height = height // 2

start_x = (width - crop_width) // 2
start_y = (height - crop_height) // 2
end_x = start_x + crop_width
end_y = start_y + crop_height

cropped_image = image_rgb[start_y:end_y, start_x:end_x]

plt.imshow(cropped_image)
# plt.axis('off')  # Hide axes
plt.show()

