## About

This is a simple Python script that captures video from OBS Studio using the OpenCV library. It displays the video in a window and allows you to quit the application by pressing <kbd>Q</kbd>.

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

Make sure you have OBS Studio installed and the obs-virtualcam plugin enabled to use OBS as a virtual camera.

---

#### Usage
Run the script [capture.py](capture.py):

>```bash
>python capture.py
>```

Ensure that the OBS Studio virtual camera is activated.

Press 'q' to exit the application.

---

### License
This code and the opencv library are licensed under the Apache License, version 2.0 - see the [LICENSE](LICENSE) file for details.
