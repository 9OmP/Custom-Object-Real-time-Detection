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
MAILJET_API_KEY = '#################'
MAILJET_SECRET_KEY = '###############'
FROM_EMAIL_ADDRESS = '##################'
TO_EMAIL_ADDRESS = '#############'
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
