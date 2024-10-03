import numpy as np
import cv2

#input image
input = cv2.imread("anime-naruto-naruto-uzumaki-ninja-wallpaper-preview.jpg")

# get input size
height, width = input.shape[:2]

#desired "pixelated" size
w, h = (20, 20)

# resize input into "pixelated" size
temp = cv2.resize(input, (w,h), interpolation=cv2.INTER_LINEAR)

# initialize output image
output = cv2.resize(temp, (width,height), interpolation=cv2.INTER_NEAREST)

cv2.imshow("input", input)
cv2.imshow("output", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
