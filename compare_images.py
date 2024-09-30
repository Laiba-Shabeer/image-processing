import cv2
import numpy as np
import matplotlib.pyplot as plt

# FOR IMAGE 1

# Load the image (make sure the file path and name are correct)
image1 = cv2.imread('images1.jfif')

# Check if the image was loaded successfully
if image1 is None:
    print("Error: Image not loaded. Check the file path and extension.")
else:
    # Print the dimensions of the image to verify the size
    height, width, channels = image1.shape
    print(f"Image dimensions: Width={width}, Height={height}")


    # Define the coordinates for the region of interest (ROI)
    x1, y1 = 131, 51
    x2, y2 = 295, 140

    # Extract the region of interest (ROI)
    roi1 = image1[y1:y2, x1:x2]

    # Display the ROI
    cv2.imshow("Region of Interest image 1", roi1)

    # Display the original image
    # cv2.imshow("Image 1", image1)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# For image 2
# Load the image (make sure the file path and name are correct)
image2 = cv2.imread('images2.jfif')

# Check if the image was loaded successfully
if image1 is None:
    print("Error: Image not loaded. Check the file path and extension.")
else:
    # Print the dimensions of the image to verify the size
    height, width, channels = image2.shape
    print(f"Image dimensions: Width={width}, Height={height}")


    # Define the coordinates for the region of interest (ROI)
    x1, y1 = 131, 51
    x2, y2 = 295, 140

    # Extract the region of interest (ROI)
    roi2 = image2[y1:y2, x1:x2]

    # Display the ROI
    cv2.imshow("Region of Interest image 2", roi2)

    # Display the original image
    # cv2.imshow("Image 2", image2)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Calculate histograms for both images
    hist1 = cv2.calcHist([roi1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([roi2], [0], None, [256], [0, 256])

    # Set up the figure and subplots
    plt.figure(figsize=(10, 8))

    # Subplot 1: ROI Image 1
    plt.subplot(221)
    plt.imshow(cv2.cvtColor(roi1, cv2.COLOR_BGR2RGB))
    plt.title('ROI Image 1')
    plt.axis('off')  # Hide axis

    # Subplot 2: Histogram for Image 1
    plt.subplot(222)
    plt.plot(hist1, color='blue')
    plt.title('Histogram for Image 1')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    #setting limit for x-axis
    plt.xlim([0, 256])

    # Subplot 3: ROI Image 2
    plt.subplot(223)
    plt.imshow(cv2.cvtColor(roi2, cv2.COLOR_BGR2RGB))
    plt.title('ROI Image 2')
    plt.axis('off')  # Hide axis

    # Subplot 4: Histogram for Image 2
    plt.subplot(224)
    plt.plot(hist2, color='orange')
    plt.title('Histogram for Image 2')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.show()


# Normalize the histograms for reducing 2D matrix into 1D array
hist1 = cv2.normalize(hist1, hist1).flatten()
hist2 = cv2.normalize(hist2, hist2).flatten()

# Create a new figure to plot both histograms
plt.figure(figsize=(10, 6))

# Plot histogram 1
plt.plot(hist1, color='blue', label='Histogram 1')

# Plot histogram 2 on the same plot
plt.plot(hist2, color='orange', label='Histogram 2')

# Adding titles and labels
plt.title('Comparison of Two Histograms')
plt.xlabel('Pixel Value')
plt.ylabel('Normalized Frequency')
plt.legend(loc='upper right')
plt.xlim([0, 256])  # Set x-axis limit

# Display the plot
plt.show()

#compare histogram
correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
print(f"Correlation: {correlation}")

