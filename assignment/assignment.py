import os
import random
import numpy as np
from skimage import io
from skimage.feature import local_binary_pattern
from skimage.color import rgb2gray
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

# Define classes
categories = {
    'group1': 'fruit',
    'group2': 'flower',
    'group3': 'nature'
}

#  load a specific image from classes
def get_image_by_name(category, file_name):
    file_path = os.path.join(categories[category], file_name)
    image = io.imread(file_path)
    return image, file_path

#  load a random image from classes
def random_image(category):
    image_list = os.listdir(categories[category])
    selected_file = random.choice(image_list)
    img_path = os.path.join(categories[category], selected_file)
    img = io.imread(img_path)
    return img, img_path

# Extract LBP features
def compute_lbp_features(img, points=8, radius=1):
    gray_image = rgb2gray(img)
    normalized_image = (gray_image * 255).astype(np.uint8)
    lbp_image = local_binary_pattern(normalized_image, points, radius, method='uniform')
    histogram, _ = np.histogram(lbp_image.ravel(), bins=np.arange(0, points + 3), range=(0, points + 2))
    histogram = histogram.astype("float")
    histogram /= histogram.sum()
    return histogram, lbp_image

#  first image
first_group = 'group2'  # Flower category
first_file = 'flower22.jfif'  # Specific image
img1, img1_path = get_image_by_name(first_group, first_file)
hist1, lbp1 = compute_lbp_features(img1)

# Load a random image
other_groups = list(set(categories.keys()) - {first_group})
second_group = random.choice(other_groups)
img2, img2_path = random_image(second_group)
hist2, lbp2 = compute_lbp_features(img2)

# Calculate  distance
similarity = euclidean(hist1, hist2)

# Output the results
print(f"LBP Histogram of the first image from '{first_group}': {hist1}")
print(f"LBP Histogram of the second image from '{second_group}': {hist2}")
print(f"Distance between the two images: {similarity:.4f}")

# Compare the images
if similarity < 0.1:
    result = "similar"
else:
    result = "different"

# Plot the images
plt.figure(figsize=(15, 9))

plt.subplot(2, 2, 1)
plt.imshow(img1)
plt.title(f'First Image from {first_group}')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(img2)
plt.title(f'Random Image from {second_group}')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(lbp1, cmap='gray')
plt.title('LBP Image of First Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(lbp2, cmap='gray')
plt.title('LBP Image of Second Image')
plt.axis('off')

plt.suptitle(f'Result: The images are {result}. Distance: {similarity:.4f}')
plt.tight_layout()
plt.show()
