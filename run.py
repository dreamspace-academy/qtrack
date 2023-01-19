import cv2
import random
import pyttsx3
from datetime import datetime
import time

# impotant variable 
camera_id = 0
delay = 1
window_name = 'qTrack'
qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)
qr_counter = 0


# Create voice object
def initialize_pyttsx3():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
   
    return engine
# Variable for pyttsx3
engine_say = initialize_pyttsx3()


# Current time return function
def get_current_time_data():
    current_date_and_time = datetime.now()
    current_time = current_date_and_time.strftime("%H:%M:%S")
    current_date = current_date_and_time.strftime("%Y-%m-%d")
    current_hour = current_date_and_time.strftime("%H")

    return [current_time, current_date, current_hour]

# Current time return function
def get_date_month_year_only():
    current_date_and_time = datetime.now()
    year_only = current_date_and_time.strftime("%Y")
    month_only = current_date_and_time.strftime("%m")
    date_only = current_date_and_time.strftime("%d")
   
    return [year_only,month_only, date_only]

# qr scanner function 
def qr_scanner():
    while True:
        ret, frame = cap.read()

        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for QrValue, point in zip(decoded_info, points):
                    if QrValue:
                    
                        time_now, date_now, hour_now = get_current_time_data()
                        print(time_now)
                        print(date_now)
                        print(hour_now)

                        print(QrValue)
                        # time.sleep(2)
                        color = (0, 255, 0)

                            
                        
                    else:
                        color = (0, 0, 255)
                    frame = cv2.polylines(frame, [point.astype(int)], True, color, 8)
            cv2.imshow(window_name, frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

qr_scanner()
cv2.destroyWindow(window_name)

