import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    # read frames
    ret , frame = cap.read()

# check if frame is captured successfully
    if ret:
      # display frame
      cv2.imshow("frame" , frame)

      # Define a kernel for morphological operations
      kernel = np.ones((5, 5), np.uint8)

      # Apply erosion
      eroded = cv2.erode(frame, kernel, iterations=1)
      cv2.imshow('Eroded Image', eroded)

      # Apply dilation
      dilated = cv2.dilate(frame, kernel, iterations=1)
      cv2.imshow('Dilated Image', dilated)

    # exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release capture object and close
cap.release()
cv2.destroyAllWindows()



