import cv2

def capture_frame(video_capture):
    # Captures a frame from the video .
    ret, frame = video_capture.read()
    if ret:
        return frame
    return None

def display_frame(window_name, frame):
    # Displays a frame in a specified window.
    cv2.imshow(window_name, frame)

def convert_to_greyscale(frame):
    # Converts a frame to grayscale.
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def apply_canny_edge(grey_image, threshold1=50, threshold2=150, aperture_size=7):
    return cv2.Canny(grey_image, threshold1, threshold2, apertureSize=aperture_size, L2gradient=True)

def apply_gaussian_blur(image, kernel_size=(3, 3)):
   return cv2.GaussianBlur(image, kernel_size, 0)

def main():
    # Main function to capture, process, and display video frames.
    cap = cv2.VideoCapture(0)

    while True:
        frame = capture_frame(cap)

        if frame is not None:
            # Display original frame
            display_frame("Frame", frame)

            # Convert to grayscale
            grey_image = convert_to_greyscale(frame)

            # Apply Canny Edge Detection
            canny_edge = apply_canny_edge(grey_image)
            display_frame("Canny Edge", canny_edge)

            # Optionally apply Gaussian Blur and display
            Gaussian_Blur = apply_gaussian_blur(canny_edge)
            display_frame("Gaussian Blur", Gaussian_Blur)

            # Exit loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
