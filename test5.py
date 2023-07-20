from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import os
import requests
from mailjet_rest import Client
import mailjet_rest
from requests.auth import HTTPBasicAuth
import numpy as np

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
#cap = cv2.VideoCapture("rtsp://admin:abcd@123@192.168.1.207:554", cv2.CAP_FFMPEG)
cap = cv2.VideoCapture(0)  # For Webcam
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO("../Yolo-Weights/yolov8m.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
myColor = (0, 0, 255)
last_alert_time = 0
person_count = 0

# Set your Mailjet API credentials
MAILJET_API_KEY = '############'
MAILJET_SECRET_KEY = '###########'
FROM_EMAIL_ADDRESS = '#############'
TO_EMAIL_ADDRESS = '<######################
EMAIL_SUBJECT = 'Security Alert'


while True:
    success, img = cap.read()
    results = model(img, stream=True)
    persons_count = 0 # initialize persons count
    detected_items = [] # initialize detected items list
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass in ['scissors', 'fork', 'knife']:
                    # tIME for Email alert
                    current_time = time.time()
                    if current_time - last_alert_time >= 60:
                        last_alert_time = current_time

                        # Capture a screenshot
                        # timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
                        # screenshot_path = f'screenshot_{timestamp}.png'
                        # cv2.imwrite(screenshot_path, img)

                        # Compose the email
                        mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_SECRET_KEY), version='v3.1')
                        data = {
                            'Messages': [
                                {
                                    "From": {
                                        "Email": "##################",
                                        "Name": "Weaapon Detection App"
                                    },
                                    "To": [
                                        {
                                            "Email": "############",
                                            "Name": "Om Patil"
                                        }
                                    ],
                                    "Subject": "Security Alert",
                                    "HTMLPart": "A harmful object has been detected with "+str(persons_count)+" person "
                                                                                                         "around.",
                                    "CustomID": "AppGettingStartedTest"
                                }
                            ]
                        }
                        result = mailjet.send.create(data=data)


                    # Add detected item to list
                    detected_items.append(currentClass)
                    # Draw bounding box and label on image
                    cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                                       scale=1, thickness=1, colorB=myColor, colorT=(255, 255, 255),
                                       colorR=myColor, offset=5)
                    cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)



                # Check if detected item is a person
            elif currentClass == 'person':
                    # Increment persons count
                    persons_count += 1

    # Draw persons count on image
    cvzone.putTextRect(img, f'Persons: {persons_count}', (10, 10), scale=1, thickness=1,
                       colorB=myColor, colorT=(255, 255, 255), colorR=myColor, offset=5)

    # If at least one fork, scissors, or knife is detected, print detected items list
    if detected_items:
        print(f'Detected items: {detected_items}')

    cv2.imshow("Image", img)
    cv2.waitKey(1)
