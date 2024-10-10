import cv2

# Load the image
path = "shape.jfif"
image = cv2.imread(path)

# Crop a portion of the image
crop = image[80:150, 80:170]

# Display the cropped and original images
cv2.imshow("crop", crop)
cv2.imshow("original image", image)

# Convert the original and cropped images to grayscale
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original gray", img_gray)

crop_gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
cv2.imshow("crop gray", crop_gray)

# Apply template matching
result = cv2.matchTemplate(image, crop, method=cv2.TM_CCORR_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Setting coordinates for the rectangle
top_left = max_loc
print(f"Shape of the cropped image (height, width): {crop_gray.shape[0]}, {crop_gray.shape[1]}")

# Define the bottom-right corner based on the top-left corner and crop size
bottom_right = (top_left[0] + crop_gray.shape[1], top_left[1] + crop_gray.shape[0])

# Draw a rectangle on the original image where the match is found
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# Show the image with the rectangle
cv2.imshow("Detected Area", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
