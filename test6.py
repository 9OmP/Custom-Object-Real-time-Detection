from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import os
import requests
from requests.auth import HTTPBasicAuth
import numpy as np

# Set your Mailjet API credentials
MAILJET_API_KEY = '88fed663b7c741a97516e01fc4c5b5fe'
MAILJET_SECRET_KEY = 'a9b79ba4ca707a6e5d8def3e05474d19'
FROM_EMAIL_ADDRESS = 'ompatil16022002@gmail.com'
TO_EMAIL_ADDRESS = '<ompatil16022002@gmail.com'
EMAIL_SUBJECT = 'Security Alert'
# Compose the email
email_body = f'Number of persons detected:2'
response = requests.post(
    'https://api.mailjet.com/v3.1/send',
    auth=(MAILJET_API_KEY, MAILJET_SECRET_KEY),
    data={
        'FromEmail': FROM_EMAIL_ADDRESS,
        'FromName': 'Security System',
        'Subject': EMAIL_SUBJECT,
        'Text-part': email_body,
        'Recipients': [{'Email': TO_EMAIL_ADDRESS}]
    }
)
print("Mail sent")
