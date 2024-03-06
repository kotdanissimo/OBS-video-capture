# This code and the opencv library are licensed under the Apache License, version 2.0.
# More details can be found in the LICENSE file or at http://www.apache.org/licenses/
import cv2


def main():
    """
    Main function to capture video from OBS and display it.

        Create a VideoCapture object
        Argument can be either the device index or the name of a video file.
        Device index is just the number to specify which camera.
        Normally one camera will be connected, so we pass 0.
        You can select the second camera by passing 1 and so on.
    """

    cap = cv2.VideoCapture(1)

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video stream from OBS.")
        exit()

    # Set video frame height and width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

    # Infinite loop until video capture is stopped
    while True:
        # Capture frame-by-frame
        # ret is a boolean indicating if it was successful.
        # frame is the current frame being read.
        ret, frame = cap.read()
        print(frame.shape)

        # If frame is read correctly ret is True
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Display the resulting frame
        cv2.imshow("OBS Stream", frame)

        # Wait for user to press 'q' key to stop the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Execute main function
    main()
