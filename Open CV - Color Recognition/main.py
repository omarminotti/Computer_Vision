# import cv2

# img = cv2.imread("oranges_fruit.jpg") # Lettura

# print(img) # Print colori BGR

# cv2.imshow("Img", img) # Display
# cv2.waitKey(4000) # Chiusura da tasto o da tempo in ms

# -----------------

import cv2

cap = cv2.VideoCapture(0) # Webcam

# HD camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# # Single frame:
# _, frame = cap.read() 
# cv2.imshow("Frame", frame)
# cv2.waitKey(0)

# Video:
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Da BGR a HSV
    # Pointer:
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value:
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(frame, color, (10, 70), 0, 1.5, (b, g, r), 2)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
 
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()