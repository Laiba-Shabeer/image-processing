import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Reading the image
image = cv2.imread('anime-naruto-naruto-uzumaki-ninja-wallpaper-preview.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


