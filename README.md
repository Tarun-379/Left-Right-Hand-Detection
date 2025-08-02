# Left-Right-Hand-Detection
Detecting right and left hand using python mediapipe,openCV,numpy liberaries at an accuracy of 95-99 percent.  




# 🖐️ Real-Time Hand Detection and Classification using MediaPipe & OpenCV

This project uses [MediaPipe](https://google.github.io/mediapipe/) and [OpenCV](https://opencv.org/) to detect and track hands in real-time through a webcam feed. It classifies each detected hand as either **Left** or **Right**, displays the result on screen, and adapts the label's position to prevent it from going off the screen edge.

---

## ✨ Features

- 📹 Real-time webcam capture using OpenCV
- 🖐️ Hand landmark detection with MediaPipe
- 🧠 Left/Right hand classification
- ✏️ Smart label positioning to avoid clipping on screen
- 🔁 Flips camera view to create a mirror effect
- ⚠️ Handles multiple hands simultaneously

---

## 📦 Requirements

Install the required libraries using `pip`:

```bash
pip install -r requirements.txt
Or install manually:
pip install opencv-python mediapipe numpy

▶️ How to Run
python hand_detection.py
The camera window will open and start detecting hands.
Press q to quit.

📁 Project Structure
hand-tracking-mediapipe/
│
├── hand_detection.py      # Main script
├── requirements.txt       # Required dependencies
├── README.md              # Project documentation
└── .gitignore             # Files to ignore in Git

🧠 How It Works
Captures video from your default webcam.
Processes each frame with MediaPipe’s Hands solution.
Identifies key hand landmarks (like wrist, fingertips).
Classifies each hand as "Left" or "Right".
Calculates wrist position and dynamically adjusts text placement so labels don’t run off-screen.
Displays labeled results in real-time with OpenCV.

⚠️ Known Limitations
Classification may flip when showing the back of the hand or if hands enter the frame abruptly.
Works best with palm facing the camera.
Currently assumes a fixed camera resolution (640x480) unless adjusted dynamically.

🔧 Possible Improvements
Add gesture recognition (e.g. thumbs up, fist, etc.)
Save hand positions for data logging
Export as a module or integrate into a GUI
Display palm orientation (facing camera vs back)


🙋‍♂️ Author
Tarun

Feel free to reach out or fork and contribute!
