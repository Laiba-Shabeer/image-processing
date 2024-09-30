import cv2
import numpy as np

# Creating a blank black image
blank_image = np.ones((512, 512, 3), dtype=np.uint8)

# Set the background colors
background_color = (255, 250, 0)
color=(25,80,0)


blank_image[:250] = background_color
blank_image[250:] = color

# Define points for the mountains
t1 = np.array([[50, 250], [150, 100], [250, 250]], np.int32)
t2 = np.array([[200, 250], [300, 150], [400, 250]], np.int32)
t3 = np.array([[350, 250], [450, 120], [512, 250]], np.int32)

# Draw the mountains on the blue area
cv2.fillPoly(blank_image, [t1, t2, t3], (150, 70, 0))



# Display the image
cv2.imshow("Mountain Scene", blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
