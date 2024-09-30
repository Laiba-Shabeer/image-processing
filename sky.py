import cv2
import numpy as np

# Create a blank image with sky-blue background
image = np.full((600, 800, 3), (255, 255, 255), dtype=np.uint8)

# Set the sky color
image[:] = (255, 250, 0)  # Sky blue

# Draw the sun
sun_center = (700, 100)
sun_radius = 50
sun_color = (0, 255, 255)  # Yellow color
cv2.circle(image, sun_center, sun_radius, sun_color, -1)

# Draw sun rays
for angle in range(0, 360, 30):
    x = int(sun_center[0] + sun_radius * 1.5 * np.cos(np.radians(angle)))
    y = int(sun_center[1] + sun_radius * 1.5 * np.sin(np.radians(angle)))
    cv2.line(image, sun_center, (x, y), sun_color, 2)



# Display the image
cv2.imshow('Sun', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
