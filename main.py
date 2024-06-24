import cv2


class VideoCapture:
    """
    A class used to capture video from a camera or a video file.

    Attributes
    ----------
    height : int
        the height of the video frame
    width : int
        the width of the video frame
    stop_keys : list
        the keys that will stop the video capture

    Methods
    -------
    capture():
        Captures video frames and yields them one by one.
    show_stream():
        Displays the video stream in a window.
    """

    def __init__(self, height=720, width=1280, stop_keys=None):
        """
        Constructs all the necessary attributes for the VideoCapture object.

        Parameters
        ----------
            height : int
                the height of the video frame
            width : int
                the width of the video frame
            stop_keys : list
                the keys that will stop the video capture
        """

        self.height = height
        self.width = width

        if stop_keys is None:
            self.stop_keys = ['q', 'Q']
        else:
            self.stop_keys = stop_keys

    def capture(self):
        """
        Captures video frames and yields them one by one.

        Yields
        ------
        numpy.ndarray
            a frame captured from the video
        """

        # Create a VideoCapture object
        try:
            cap = cv2.VideoCapture(1)
        except Exception as e:
            print("Error" + str(e))
            return

        # Set video frame height and width
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)

        # Infinite loop until video capture is stopped
        while True:
            # ret is a boolean indicating if it was successful.
            # frame is the current frame being read.
            try:
                ret, frame = cap.read()

                yield frame

            except Exception as e:
                print("Error" + str(e))
                continue

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    def show_stream(self):
        """
        Displays the video stream in a window.

        The video stream is displayed in a window until one of the stop keys is pressed.
        """

        for frame in self.capture():
            # Display the resulting image
            cv2.imshow("OBS Stream", frame)

            # Wait for user to press stop keys to stop the program
            key = chr(cv2.waitKey(1) & 0xFF)
            if key in self.stop_keys:
                break


if __name__ == "__main__":
    # Create a VideoCapture object and start displaying the video stream
    video_capture = VideoCapture(height=720, width=1280, stop_keys=[' '])
    video_capture.show_stream()

    # Create a VideoCapture object and start capturing video frames
    video_capture = VideoCapture(stop_keys=[' '])
    for img in video_capture.capture():
        # Print the shape of each captured frame
        print(img)
