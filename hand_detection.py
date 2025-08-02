import cv2
import mediapipe as mp 
import numpy as np


# left/Right Dectecting Function
def get_label(index, hand, results, image_width, image_height):
    output = None

    for idx, classification in enumerate(results.multi_handedness):
        if classification.classification[0].index == index:
            label = classification.classification[0].label
            score = classification.classification[0].score
            text = f'{label} {round(score, 2)}'

            # Convert normalized to pixel coordinates
            x = int(hand.landmark[mp_hands.HandLandmark.WRIST].x * image_width)
            y = int(hand.landmark[mp_hands.HandLandmark.WRIST].y * image_height)

            # Adjust x if text would go off-screen
            (text_width, _), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
            if x + text_width > image_width:
                x = image_width - text_width - 10

            output = text, (x, y)

    return output








mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands



stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("Stream not started")
    exit()



with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
    while(True):
        ret,frame = stream.read()
        if not ret:
            print("No more stream :(")
            break
        
        frame = cv2.flip(frame,1)
        
        
        # BGR 2 RGB
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        # Set flag to False
        image.flags.writeable = False
        
        # Detection
        results = hands.process(image)
        
        # Set flag to True
        image.flags.writeable = True
        
        # RGB 2 BGR
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        
        # Results
        # print(results)
        
        
        # Rendering Results
        if results.multi_hand_landmarks:
            height, width, _ = image.shape

            for num,hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121,22,76),thickness=2,circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(121,44,250),thickness=2,circle_radius=2),
                                          )
        
                # Render left or right Detection
                label_info = get_label(num, hand, results, width, height)
                if label_info:
                    text, coord = label_info
                    cv2.putText(image, text, coord, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

        
        cv2.imshow("Hand_detection",image)
        if cv2.waitKey(1)==ord('q'):
            break
        
        
        
stream.release()
cv2.destroyAllWindows()