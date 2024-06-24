## About

This is a Python script that captures video from a camera or a video file using the OpenCV library. It provides a `VideoCapture` class that can be used to capture video frames and display them in a window. The video capture can be stopped by pressing any of the stop keys defined when creating a `VideoCapture` object.

---

#### Prerequisites
Clone the repository to your local machine:

>```bash
>git clone https://github.com/kotdanissimo/OBS-Video-Capture
>```

Additionally, ensure you have the required dependencies installed using one of the following commands:

>```bash
>pip install -r requirements.txt
>```
>
>  or
>
>```bash
>pip install opencv-python
>```

---

#### Usage
Create a `VideoCapture` object and start capturing video frames or displaying the video stream:

>```python
>from main import VideoCapture
>
># Create a VideoCapture object and start displaying the video stream
>video_capture = VideoCapture(height=720, width=1280, stop_keys=[' '])
>video_capture.show_stream()
>
># Or create a VideoCapture object and start capturing video frames
>video_capture = VideoCapture(height=720, width=1280, stop_keys=[' '])
>for img in video_capture.capture():
>    # Print the shape of each captured frame
>    print(img.shape)
>```

Press any of the stop keys (in this case, space) to stop the video capture.

---

### License
This code and the opencv library are licensed under the Apache License, version 2.0 - see the [LICENSE](LICENSE) file for details.