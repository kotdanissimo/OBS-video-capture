# This code and the opencv library are licensed under the Apache License, version 2.0.
# More details can be found in the LICENSE file or at http://www.apache.org/licenses/
import cv2


def main():
    # Open a video stream from OBS (change the index if needed)
    cap = cv2.VideoCapture(1)

    # Check if the video stream is successfully opened
    if not cap.isOpened():
        print("Error: Unable to open video stream from OBS.")
        exit()

    # Set the frame height and width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()
        print(frame.shape)

        # Check if the frame is successfully read
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Display the frame
        cv2.imshow("OBS Stream", frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video stream and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Call the main function if the script is executed
    main()
