import cv2
import mediapipe as mp
import pyautogui

# Initialize video capture and MediaPipe Face Mesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        
        # Control mouse movement using left eye (landmarks 474 to 477)
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))  # Draw circle on left eye landmarks
            
            if id == 1:  # Use the second landmark for mouse movement
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)

        # Control left click using left eye blink (landmarks 145 and 159)
        left_eye = [landmarks[145], landmarks[159]]
        for landmark in left_eye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))  # Draw circle on left eye landmarks

        if abs(left_eye[0].y - left_eye[1].y) < 0.004:  # Blink detection for left click
            pyautogui.click()
            pyautogui.sleep(1)

        # Control right click using right eye blink (landmarks 386 and 374)
        right_eye = [landmarks[386], landmarks[374]]
        for landmark in right_eye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (255, 0, 255))  # Draw circle on right eye landmarks

        if abs(right_eye[0].y - right_eye[1].y) < 0.004:  # Blink detection for right click
            pyautogui.click(button='right')  # Perform right click
            pyautogui.sleep(1)

    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()