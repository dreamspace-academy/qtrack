import cv2
import random
import pyttsx3
from datetime import datetime

# impotant variable 
camera_id = 0
delay = 1
window_name = 'qTrack'
qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)


# qr scanner function 
def qr_scanner():
    while True:
        ret, frame = cap.read()

        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for QrValue, point in zip(decoded_info, points):
                    if QrValue:
                        print(QrValue)
                        color = (0, 255, 0)
                    else:
                        color = (0, 0, 255)
                    frame = cv2.polylines(frame, [point.astype(int)], True, color, 8)
            cv2.imshow(window_name, frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

cv2.destroyWindow(window_name)