import cv2

# Read the image
image = cv2.imread('cristiano.webp')

# ======================================================================
# Outlines Effect
#converting in grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#for reducing noise and to smoothens image
gray = cv2.medianBlur(gray, 5)

# for creating binary image with black and white pixels
outlines = cv2.adaptiveThreshold(gray, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 7, 9)

# ======================================================================
# Cartoon Effect
# make cartoon of your image
color = cv2.bilateralFilter(image, 11, 300, 250)
cartoon = cv2.bitwise_and(color, color, mask=outlines)


# Artistic Effect
# ======================================================================
# Apply artistic stylization effect
artistic_effect = cv2.stylization(image, sigma_s=60, sigma_r=1)


# ======================================================================
# Display the results

cv2.imshow('Original Image', image)
cv2.imshow('Artistic Effect', artistic_effect)
cv2.imshow("outline ", outlines)
cv2.imshow('Cartoon Effect', cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()
