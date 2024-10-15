
# Eye Controlled Mouse Using Mediapipe and OpenCV

This project implements an eye-controlled mouse using a webcam, OpenCV, Mediapipe, and PyAutoGUI. It tracks facial landmarks, specifically eye landmarks, to control the mouse pointer's movement and trigger mouse clicks based on eye blinks.




## Features

- Mouse Movement Control: The cursor moves according to the position of the left eye.
- Left Click: Blink of the left eye triggers a left-click event.
- Right Click: Blink of the right eye triggers a right-click event.
- Real-Time Detection: Utilizes Mediapipe's Face Mesh solution to track facial landmarks in real time.




## Installation

To run this project, you'll need the following Python libraries:

- OpenCV: pip install opencv-python
- Mediapipe: pip install mediapipe
- PyAutoGUI: pip install pyautogui

## How It Works

- Face Mesh Detection: Mediapipe’s Face Mesh detects facial landmarks from the webcam feed.
- Mouse Movement: The left eye's landmarks are tracked (landmarks 474 to 477), and the mouse pointer moves based on the position of one of these landmarks.
- Left Click Detection: When the vertical distance between two specific landmarks on the left eye (145 and 159) becomes small (indicating a blink), a left-click is triggered.
- Right Click Detection: Similarly, a blink in the right eye is detected using landmarks 386 and 374 to trigger a right-click.

## Method

- Move Cursor: Move your head and eyes, and the mouse pointer will follow the movement of your left eye.
- Left Click: Blink your left eye to perform a left click.
- Right Click: Blink your right eye to perform a right click.

## Exiting the Application

Press the 'q' key to exit the program.

