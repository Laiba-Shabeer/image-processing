import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# reading image
img = cv2.imread('anime-naruto-naruto-uzumaki-ninja-wallpaper-preview.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

assert img is not None, "image not found"

# displaying histrogram
plt.hist(img.ravel(), bins=256, range=[0,256])
cv2.imshow(gray_img,img,plt.show())



