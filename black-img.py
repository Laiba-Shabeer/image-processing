import cv2
import numpy as np
import matplotlib.pyplot as plt

# creating a blank black image
blank_image  = np.ones((512, 512,3), dtype=np.uint8)

# Set the background color
background_color = (255, 250, 0)

blank_image[:] = background_color

#draw a line on black image
# we will use the cv line func
line1_image = cv2.line(blank_image,(100,0), (100,350) , (17,255,121) , 10)
cv2.circle(line1_image,[100,350],40,[0,55,88],-1)

line2_image = cv2.line(blank_image,(200,0),(200,210),(25,250,70),10)
cv2.circle(line2_image,[200,220],40,[0,55,88],-1)

line3_image = cv2.line(blank_image,(300,0),(300,150),(25,250,70),10)
cv2.circle(line3_image,(300,130),40,[0,55,88], -1)

line4_image = cv2.line(blank_image,(400,0),(400,75),(25,250,70),10)
cv2.circle(line4_image,(400,60),40,[0,55,88], -1)


## Draw triangle

# points = np.array([[200, 400], [300, 200], [400, 200]], np.int32)
# points = points.reshape((-1, 1, 2))
#
# # Draw the triangle
# cv2.polylines(blank_image, [points], isClosed=True, color=(0, 255, 0), thickness=3)
# cv2.fillPoly(blank_image, [points], color=(0, 255, 230))
#
# point2 = np.array([[100,300],[200,350,],[420,350]], np.int32)
# point2 = point2.reshape(-1,1,2)
# cv2.polylines(blank_image, [point2], isClosed=True, color=(0, 255, 0), thickness=3)
# cv2.fillPoly(blank_image, [point2], color=(250, 255, 230))


# display image
cv2.imshow("black image", blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()