import cv2

cap = cv2.VideoCapture(0)
while True:
    # read frames
    ret , frame = cap.read()

# check if frame is captured successfully
    if ret:
      # display frame
      cv2.imshow("frame" , frame)

      # read image in grey form
      grey_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

      # Gaussian blur
      # gaussian_blur = cv2.GaussianBlur(grey_frame, (3,3), 0)
      # cv2.imshow("gaussian blur", gaussian_blur)

      # canny edges
      canny_edges = cv2.Canny(grey_frame, 100, 200)
      cv2.imshow("Canny edge", canny_edges)

      # Gaussian Blur
      gaussian_blur = cv2.GaussianBlur(canny_edges, (3, 3), 0)
      cv2.imshow("Canny Edges", canny_edges)

      # canny parameters
      canny = cv2.Canny(grey_frame, threshold1=100, threshold2=200  ,apertureSize=5, L2gradient=False)
      cv2.imshow("canny", canny)

    # exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release capture object and close
cap.release()
cv2.destroyAllWindows()



